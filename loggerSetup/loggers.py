import logging.config

from loggerSetup.logging_config import dict_config

logging.config.dictConfig(dict_config)
root = logging.getLogger("root")
commandCalculate = logging.getLogger("commandCalculate")
utils = logging.getLogger("utils")
