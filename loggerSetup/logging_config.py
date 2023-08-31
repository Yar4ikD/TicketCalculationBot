dict_config = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {
        "default": {
            "format": "%(levelname)s| %(name)s | %(asctime)s| %(lineno)d | %(message)s'",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
            "level": "DEBUG",
        },
        "rotatingHandler": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": "loggerSetup/errors.log",
            "when": "D",
            "interval": 10,
            "backupCount": 1,
            "level": "ERROR",
            "encoding": "utf-8",
            "formatter": "default",
        },
    },
    "loggers": {
        "commandCalculate": {
            "level": "DEBUG",
            "handlers": ["rotatingHandler", "console"],
        },
        "utils": {
            "level": "DEBUG",
            "handlers": ["rotatingHandler", "console"],
        },
    },
    "root": {
        "level": "INFO",
        "handlers": ["rotatingHandler", "console"],
    },
}
