import logging


class CustomFormatter(logging.Formatter):
	grey = "\x1b[38;20m"
	yellow = "\x1b[33;20m"
	red = "\x1b[31;20m"
	bold_red = "\x1b[31;1m"
	reset = "\x1b[0m"
	format = "[%(name)s] %(levelname)s %(asctime)s - %(message)s"

	FORMATS = {
		logging.DEBUG: grey + format + reset,
		logging.INFO: grey + format + reset,
		logging.WARNING: yellow + format + reset,
		logging.ERROR: red + format + reset,
		logging.CRITICAL: bold_red + format + reset
	}

	def format(self, record):
		log_fmt = self.FORMATS.get(record.levelno)
		formatter = logging.Formatter(log_fmt, datefmt='%Y-%m-%d %H:%M:%S')
		return formatter.format(record)


class Log:
	_logger: logging.Logger

	def __init__(self, name: str):
		self._logger = logging.getLogger(name)
		self._logger.setLevel(logging.DEBUG)

		# create console handler with a higher log level
		ch = logging.StreamHandler()
		ch.setLevel(logging.DEBUG)
		ch.setFormatter(CustomFormatter())
		self._logger.addHandler(ch)

	def debug(self, msg: str) -> None:
		self._logger.debug(msg)

	def info(self, msg: str) -> None:
		self._logger.info(msg)

	def warning(self, msg: str) -> None:
		self._logger.warning(msg)

	def error(self, msg: str) -> None:
		self._logger.error(msg)

	def critical(self, msg: str) -> None:
		self._logger.critical(msg)
