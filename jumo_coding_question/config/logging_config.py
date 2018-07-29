import logging.config
from jumo_coding_question.config import Config

logging.config.dictConfig(
    {
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
                "level": "Error",
                "class": "logging.FileHandler",
                "filename": Config.LOGS_DIRECTORY + "/error_logs",
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
                "handlers": ["cosole"],
                "propagate": True,
            },
        },
    }
)
