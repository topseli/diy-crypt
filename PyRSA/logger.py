import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)


def info(message):
    logging.info(message)


def warning(message):
    logging.warning(message)


def error(message):
    logging.error(message)
