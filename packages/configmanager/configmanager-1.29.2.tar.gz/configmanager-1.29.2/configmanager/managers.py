import collections

from .utils import _get_persistence_adapter_for
from .schema_parser import parse_config_schema
from .meta import ConfigManagerSettings
from .persistence import ConfigPersistenceAdapter, YamlReaderWriter, JsonReaderWriter, ConfigParserReaderWriter
from .sections import Section


class _TrackingContext(object):
    def __init__(self, config):
        self.config = config
        self.hook = None
        self._changes = collections.defaultdict(list)

    def __enter__(self):
        return self.push()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.pop()

    def _value_changed(self, item, old_value, new_value):
        if old_value != new_value:
            self._changes[item].append((old_value, new_value))

    def push(self):
        assert self.hook is None
        self.hook = self.config.hooks.item_value_changed.register_hook(self._value_changed)
        self.config._tracking_contexts.append(self)
        return self

    def pop(self):
        popped = self.config._tracking_contexts.pop()
        assert popped is self
        self.config.hooks.unregister_hook(self.config.hooks.item_value_changed, self._value_changed)
        self.hook = None

    @property
    def changes(self):
        values = {}
        for k, k_changes in self._changes.items():
            if len(k_changes) == 1:
                values[k] = k_changes[0][1]
            elif k_changes[0][0] != k_changes[-1][1]:
                values[k] = k_changes[-1][1]
        return values

    def reset_changes(self, item=None):

        for k, k_changes in self._changes.items():
            if item is None or k is item:
                # TODO This doesn't reset raw_str_value properly ...
                k._value = k_changes[0][0]

        if item is None:
            self._changes.clear()
        else:
            del self._changes[item]


class Config(Section):
    """
    Represents a configuration tree.
    
    .. attribute:: Config(schema=None, **kwargs)
        
        Creates a configuration tree from a schema.

        Args:
            ``schema``: can be a dictionary, a list, a simple class, a module, another :class:`.Config`
            instance, and a combination of these.

        Keyword Args:

            ``config_parser_factory``:

        Examples::

            config = Config([
                ('greeting', 'Hello!'),
                ('uploads', Config({
                    'enabled': True,
                    'tmp_dir': '/tmp',
                })),
                ('db', {
                    'host': 'localhost',
                    'user': 'root',
                    'password': 'secret',
                    'name': 'test',
                }),
                ('api', Config([
                    'host',
                    'port',
                    'default_user',
                    ('enabled', Item(type=bool)),
                ])),
            ])
    
    .. attribute:: <config>[<name_or_path>]
    
        Access item by its name, section by its alias, or either by its path.

        Args:
            ``name`` (str): name of an item or alias of a section

        Args:
            ``path`` (tuple): path of an item or a section
        
        Returns:
            :class:`.Item` or :class:`.Config`

        Examples::

            >>> config['greeting']
            <Item greeting 'Hello!'>

            >>> config['uploads']
            <Config uploads at 4436269600>

            >>> config['uploads', 'enabled'].value
            True
    
    .. attribute:: <config>.<name>
    
        Access an item by its name or a section by its alias.

        For names and aliases that break Python grammar rules, use ``config[name]`` notation instead.
        
        Returns:
            :class:`.Item` or :class:`.Config`

    .. attribute:: <name_or_path> in <Config>

        Returns ``True`` if an item or section with the specified name or path is to be found in this section.

    .. attribute:: len(<Config>)

        Returns the number of items and sections in this section (does not include sections and items in
        sub-sections).

    .. attribute:: __iter__()

        Returns an iterator over all item names and section aliases in this section.

    """

    is_config = True

    def __init__(self, schema=None, **configmanager_settings):
        if 'configmanager_settings' in configmanager_settings:
            if len(configmanager_settings) > 1:
                raise ValueError('Dubious configmanager_settings specification: {}'.format(configmanager_settings))
            configmanager_settings = configmanager_settings['configmanager_settings']

        if not isinstance(configmanager_settings, ConfigManagerSettings):
            self._settings = ConfigManagerSettings(**configmanager_settings)

        super(Config, self).__init__()

        self._tracking_contexts = []

        self._configparser_adapter = None
        self._json_adapter = None
        self._yaml_adapter = None
        self._click_extension = None

        if schema is not None:
            parse_config_schema(schema, root=self)

        if self.settings.auto_load:
            self.load()

    def __repr__(self):
        return '<{cls} {alias} at {id}>'.format(cls=self.__class__.__name__, alias=self.alias, id=id(self))

    @property
    def settings(self):
        return self._settings

    def tracking_context(self):
        """
        Returns:
            _TrackingContext
        """
        return _TrackingContext(self)

    @property
    def configparser(self):
        """
        Adapter to dump/load INI format strings and files using standard library's
        ``ConfigParser`` (or the backported configparser module in Python 2).
        
        Returns:
            ConfigPersistenceAdapter
        """
        if self._configparser_adapter is None:
            self._configparser_adapter = ConfigPersistenceAdapter(
                config=self,
                reader_writer=ConfigParserReaderWriter(
                    config_parser_factory=self.settings.configparser_factory,
                ),
            )
        return self._configparser_adapter

    @property
    def json(self):
        """
        Adapter to dump/load JSON format strings and files.
        
        Returns:
            ConfigPersistenceAdapter
        """
        if self._json_adapter is None:
            self._json_adapter = ConfigPersistenceAdapter(
                config=self,
                reader_writer=JsonReaderWriter(),
            )
        return self._json_adapter

    @property
    def yaml(self):
        """
        Adapter to dump/load YAML format strings and files.
        
        Returns:
            ConfigPersistenceAdapter
        """
        if self._yaml_adapter is None:
            self._yaml_adapter = ConfigPersistenceAdapter(
                config=self,
                reader_writer=YamlReaderWriter(),
            )
        return self._yaml_adapter

    @property
    def click(self):
        """
        click extension

        Returns:
            ClickExtension
        """
        if self._click_extension is None:
            from .click_ext import ClickExtension
            self._click_extension = ClickExtension(
                config=self
            )
        return self._click_extension

    def load(self):
        """
        Load user configuration based on settings.
        """

        # Must reverse because we want the sources assigned to higher-up Config instances
        # to overrides sources assigned to lower Config instances.
        for section in reversed(list(self.iter_sections(recursive=True, key=None))):
            if section.is_config:
                section.load()

        for source in self.settings.load_sources:
            adapter = getattr(self, _get_persistence_adapter_for(source))
            if adapter.store_exists(source):
                adapter.load(source)
