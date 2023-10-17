import logging


def setup_logger(name):
    """ Setup of the TaskMe Logger
    """

    logger = logging.getLogger(name)
    if not logger.hasHandlers():
        # TODO: logging was duplicated had to remove streamHandler
        # TODO: logging appear after the new CLI command msg, to investigate
        logger.setLevel(logging.DEBUG)

        logging.basicConfig(format="\n[%(levelname)s]: %(message)s")

    return logger
