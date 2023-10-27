import logging
from pathlib import Path


def setup_logger(name):  # pragma: no cover
    """Setup of the TaskMe Logger.
    """

    # Logs Directory definition, directory will be created  if not existing
    logs_dir = Path(__file__).resolve().parents[3] / "logs"
    logs_dir.mkdir(exist_ok=True)

    logger = logging.getLogger(name)
    if not logger.hasHandlers():
        # Lowest log capture level
        logger.setLevel(logging.DEBUG)

        # Debug handler Init
        debug_log_file = logs_dir / "debug.log"
        debug_handler = logging.FileHandler(debug_log_file)
        debug_handler.setLevel(logging.DEBUG)
        debug_formatter = logging.Formatter('%(asctime)s - [%(levelname)s]: %(message)s')
        debug_handler.setFormatter(debug_formatter)
        logger.addHandler(debug_handler)

        # Error Handler Init
        error_log_file = logs_dir / "error.log"
        error_handler = logging.FileHandler(error_log_file)
        error_handler.setLevel(logging.ERROR)
        error_formatter = logging.Formatter('%(asctime)s - [%(levelname)s]: %(message)s')
        error_handler.setFormatter(error_formatter)
        logger.addHandler(error_handler)

    return logger
