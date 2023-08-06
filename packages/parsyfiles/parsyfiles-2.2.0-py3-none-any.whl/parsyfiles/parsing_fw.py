import sys
import traceback
from io import StringIO
from logging import getLogger, StreamHandler, Logger
from typing import Type, Dict, Any
from warnings import warn

from parsyfiles.filesystem_mapping import FileMappingConfiguration, WrappedFileMappingConfiguration
from parsyfiles.parsing_core_api import T
from parsyfiles.parsing_registries import ParserRegistryWithConverters
from parsyfiles.plugins_base.support_for_collections import MultifileCollectionParser
from parsyfiles.plugins_base.support_for_objects import MultifileObjectParser
from parsyfiles.type_inspection_tools import get_pretty_type_str
from parsyfiles.var_checker import check_var


def warn_import_error(type_of_obj_support: str, caught: ImportError):
    """
    Utility method to print a warning message about failed import of some modules

    :param type_of_obj_support:
    :param caught:
    :return:
    """
    msg = StringIO()
    msg.writelines('Import Error while trying to add support for ' + type_of_obj_support + '. You may continue but '
                   'the associated parsers and converters wont be available : \n')
    traceback.print_tb(caught.__traceback__, file=msg)
    msg.writelines(str(caught.__class__.__name__) + ' : ' + str(caught) + '\n')
    warn(msg.getvalue())


def create_parser_options(lazy_mfcollection_parsing: bool = False) -> Dict[str, Dict[str, Any]]:
    """
    Utility method to create a default options structure with the lazy parsing inside

    :param lazy_mfcollection_parsing:
    :return: the options structure filled with lazyparsing option (for the MultifileCollectionParser)
    """
    return {MultifileCollectionParser.__name__: {'lazy_parsing': lazy_mfcollection_parsing}}


def add_parser_options(options: Dict[str, Dict[str, Any]], parser_id: str, parser_options: Dict[str, Dict[str, Any]],
                       overwrite: bool = False):
    """
    Utility method to add options for a given parser, to the provided options structure
    :param options:
    :param parser_id:
    :param parser_options:
    :param overwrite: True to silently overwrite. Otherwise an error will be thrown
    :return:
    """
    if parser_id in options.keys() and not overwrite:
        raise ValueError('There are already options in this dictionary for parser id ' + parser_id)
    options[parser_id] = parser_options
    return options


class RootParser(ParserRegistryWithConverters):
    """
    The root parser
    """

    # default logger that prints on stdout
    _default_logger = getLogger('parsyfiles')
    ch = StreamHandler(sys.stdout)
    _default_logger.addHandler(ch)

    def __init__(self, pretty_name: str = None, strict_matching: bool = False,
                 register_default_parsers: bool = True, logger: Logger = _default_logger):
        """
        Constructor. Initializes the dictionary of parsers with the optionally provided initial_parsers, and
        inits the lock that will be used for access in multithreading context.

        :param pretty_name:
        :param strict_matching:
        :param register_default_parsers:
        :param logger:
        """
        super(RootParser, self).__init__(pretty_name or 'parsyfiles defaults', strict_matching)

        # remember if the user registers the default parsers - for future calls to install_basic_multifile_support()
        self.multifile_installed = register_default_parsers

        if register_default_parsers:
            # -------------------- CORE ---------------------------
            try:
                # -- primitive types
                from parsyfiles.plugins_base.support_for_primitive_types import get_default_primitive_parsers, get_default_primitive_converters
                self.register_parsers(get_default_primitive_parsers())
                self.register_converters(get_default_primitive_converters())
            except ImportError as e:
                warn_import_error('primitive types', e)

            try:
                # -- collections
                from parsyfiles.plugins_base.support_for_collections import get_default_collection_parsers, get_default_collection_converters
                self.register_parsers(get_default_collection_parsers(self, self))
                self.register_converters(get_default_collection_converters(self))
            except ImportError as e:
                warn_import_error('dict', e)

            try:
                # -- objects
                from parsyfiles.plugins_base.support_for_objects import get_default_object_parsers, get_default_object_converters
                self.register_parsers(get_default_object_parsers(self, self))
                self.register_converters(get_default_object_converters(self))
            except ImportError as e:
                warn_import_error('objects', e)

            try:
                # -- config
                from parsyfiles.plugins_base.support_for_configparser import get_default_config_parsers, get_default_config_converters
                self.register_parsers(get_default_config_parsers())
                self.register_converters(get_default_config_converters(self))
            except ImportError as e:
                warn_import_error('config', e)

            # ------------------------- OPTIONAL -----------------
            try:
                # -- jprops
                from parsyfiles.plugins_optional.support_for_jprops import get_default_jprops_parsers
                self.register_parsers(get_default_jprops_parsers(self, self))
                # self.register_converters()
            except ImportError as e:
                warn_import_error('DataFrame', e)

            try:
                # -- yaml
                from parsyfiles.plugins_optional.support_for_yaml import get_default_yaml_parsers
                self.register_parsers(get_default_yaml_parsers(self, self))
                # self.register_converters()
            except ImportError as e:
                warn_import_error('DataFrame', e)

            try:
                # -- numpy
                from parsyfiles.plugins_optional.support_for_numpy import get_default_np_parsers, get_default_np_converters
                self.register_parsers(get_default_np_parsers())
                self.register_converters(get_default_np_converters())
            except ImportError as e:
                warn_import_error('numpy', e)

            try:
                # -- pandas
                from parsyfiles.plugins_optional.support_for_pandas import get_default_pandas_parsers, get_default_pandas_converters
                self.register_parsers(get_default_pandas_parsers())
                self.register_converters(get_default_pandas_converters())
            except ImportError as e:
                warn_import_error('DataFrame', e)

        logger = logger or RootParser._default_logger
        check_var(logger, var_types=Logger, var_name='logger')
        self._logger = logger

    def install_basic_multifile_support(self):
        """
        Utility method for users who created a RootParser with register_default_parsers=False, in order to register only
         the multifile support
        :return:
        """
        if not self.multifile_installed:
            self.register_parser(MultifileCollectionParser(self))
            self.register_parser(MultifileObjectParser(self, self))
            self.multifile_installed = True
        else:
            raise Exception('Multifile support has already been installed')

    def parse_collection(self, item_file_prefix: str, base_item_type: Type[T], item_name_for_log: str = None,
                         file_mapping_conf: FileMappingConfiguration = None,
                         options: Dict[str, Dict[str, Any]] = None) -> Dict[str, T]:
        """
        Main method to parse a collection of items of type 'base_item_type'.

        :param item_file_prefix:
        :param base_item_type:
        :param item_name_for_log:
        :param file_mapping_conf:
        :param options:
        :return:
        """
        # -- item_name_for_log
        item_name_for_log = item_name_for_log or ''
        check_var(item_name_for_log, var_types=str, var_name='item_name_for_log')

        # creating the wrapping dictionary type
        collection_type = Dict[str, base_item_type]
        self._logger.info('**** Starting to parse ' + item_name_for_log + ' collection of <'
                          + get_pretty_type_str(base_item_type) + '> at location ' + item_file_prefix +' ****')

        # common steps
        return self._parse__item(collection_type, item_file_prefix, file_mapping_conf, options=options)

    def parse_item(self, location: str, item_type: Type[T], item_name_for_log: str = None,
                   file_mapping_conf: FileMappingConfiguration = None, options: Dict[str, Dict[str, Any]] = None) -> T:
        """
        Main method to parse an item of type item_type

        :param location:
        :param item_type:
        :param item_name_for_log:
        :param file_mapping_conf:
        :param options:
        :return:
        """

        # -- item_name_for_log
        item_name_for_log = item_name_for_log or ''
        check_var(item_name_for_log, var_types=str, var_name='item_name_for_log')

        self._logger.info('**** Starting to parse single object ' + item_name_for_log + ' of type <'
                          + get_pretty_type_str(item_type) + '> at location ' + location + ' ****')

        # common steps
        return self._parse__item(item_type, location, file_mapping_conf, options=options)

    def _parse__item(self, item_type: Type[T], item_file_prefix: str,
                     file_mapping_conf: FileMappingConfiguration = None,
                     options: Dict[str, Dict[str, Any]] = None) -> T:
        """
        Common parsing steps to parse an item

        :param item_type:
        :param item_file_prefix:
        :param file_mapping_conf:
        :param options:
        :return:
        """

        # for consistency : if options is None, default to the default values of create_parser_options
        options = options or create_parser_options()

        # creating the persisted object (this performs required checks)
        file_mapping_conf = file_mapping_conf or WrappedFileMappingConfiguration()
        obj = file_mapping_conf.create_persisted_object(item_file_prefix, logger=self._logger)
        # print('')
        self._logger.info('')

        # create the parsing plan
        pp = self.create_parsing_plan(item_type, obj, logger=self._logger)
        # print('')
        self._logger.info('')

        # parse
        res = pp.execute(logger=self._logger, options=options)
        # print('')
        self._logger.info('')

        return res


def parse_item(location: str, item_type: Type[T], item_name_for_log: str = None,
               file_mapping_conf: FileMappingConfiguration = None,
               logger: Logger = RootParser._default_logger, lazy_mfcollection_parsing: bool = False) -> T:
    """
    Creates a RootParser() and calls its parse_item() method

    :param location:
    :param item_type:
    :param item_name_for_log:
    :param file_mapping_conf:
    :param logger:
    :param lazy_mfcollection_parsing:
    :return:
    """
    rp = RootParser('parsyfiles defaults', logger=logger)
    opts = create_parser_options(lazy_mfcollection_parsing=lazy_mfcollection_parsing)
    return rp.parse_item(location, item_type, item_name_for_log=item_name_for_log, file_mapping_conf=file_mapping_conf,
                         options=opts)


def parse_collection(location: str, base_item_type: Type[T], item_name_for_log: str = None,
                     file_mapping_conf: FileMappingConfiguration = None, logger: Logger = RootParser._default_logger,
                     lazy_mfcollection_parsing: bool = False)\
        -> Dict[str, T]:
    """
    Utility method to create a RootParser() with default configuration and call its parse_collection() method

    :param location:
    :param base_item_type:
    :param item_name_for_log:
    :param file_mapping_conf:
    :param logger:
    :param lazy_mfcollection_parsing:
    :return:
    """
    rp = RootParser('parsyfiles defaults', logger=logger)
    opts = create_parser_options(lazy_mfcollection_parsing=lazy_mfcollection_parsing)
    return rp.parse_collection(location, base_item_type, item_name_for_log=item_name_for_log,
                               file_mapping_conf=file_mapping_conf, options=opts)