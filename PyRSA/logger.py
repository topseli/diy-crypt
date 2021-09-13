from logging import basicConfig, info, warning, error, DEBUG  # noqa: F401

# TODO use existing log format
basicConfig(format='%(asctime)s: %(funcName)s %(levelname)s %(message)s', level=DEBUG)
