# config/config.py
import logging
import sys
from pathlib import Path
from rich.logging import RichHandler
from logging import config
import mlflow

## DIRECTORIES CONFIGURATION
BASE_DIR = Path(__file__).parent.parent.absolute()
LOGS_DIR = Path(BASE_DIR, "logs")
LOGS_DIR.mkdir(parents=True, exist_ok=True)
MODEL_REGISTRY_DIR = Path("experiments")
Path(MODEL_REGISTRY_DIR).mkdir(exist_ok=True)  # create experiments dir
mlflow.set_tracking_uri("file://" + str(MODEL_REGISTRY_DIR.absolute()))


###LOGGING configuration
logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "minimal": {"format": "%(message)s"},
        "detailed": {
            "format": "%(levelname)s %(asctime)s [%(name)s:%(filename)s:%(funcName)s:%(lineno)d]\n%(message)s\n"
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "stream": sys.stdout,
            "formatter": "minimal",
            "level": logging.DEBUG,
        },
        "info": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": Path(LOGS_DIR, "info.log"),
            "maxBytes": 10485760,  # 1 MB
            "backupCount": 10,
            "formatter": "detailed",
            "level": logging.INFO,
        },
        "error": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": Path(LOGS_DIR, "error.log"),
            "maxBytes": 10485760,  # 1 MB
            "backupCount": 10,
            "formatter": "detailed",
            "level": logging.ERROR,
        },
    },
    "root": {
        "handlers": ["console", "info", "error"],
        "level": logging.DEBUG,
        "propagate": True,
    },
}

config.dictConfig(logging_config)
logger = logging.getLogger()
logger.handlers[0] = RichHandler(markup=True)
# logger.debug("Logging is configured.")
logger.info("Logging is configured.")
# logger.error("Logging is configured.")
logger.info("Directories are configured.")
