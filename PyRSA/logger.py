from logging import basicConfig, info, warning, error, DEBUG

# TODO use existing log format
basicConfig(format='%(asctime)s: %(funcName)s %(levelname)s %(message)s', level=DEBUG)
