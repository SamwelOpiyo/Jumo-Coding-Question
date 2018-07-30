import logging.config


def get_logging_configuration(config_object):
    DEFAULT_LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "verbose": {
                "format": "%(levelname)s %(asctime)s %(name)s %(module)s "
                "%(process)d %(thread)d %(message)s"
            }
        },
        "handlers": {
            "console": {
                "level": "DEBUG",
                "class": "logging.StreamHandler",
                "formatter": "verbose",
            },
            "file": {
                "level": "ERROR",
                "class": "logging.FileHandler",
                "filename": config_object.LOGS_DIRECTORY + "/error_logs",
                "formatter": "verbose",
            },
        },
        "loggers": {
            "error_logging": {
                "level": "ERROR",
                "handlers": ["file"],
                "propagate": True,
            },
            "debug_logging": {
                "level": "DEBUG",
                "handlers": ["console"],
                "propagate": True,
            },
        },
    }
    return DEFAULT_LOGGING
