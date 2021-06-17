import logging
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler

if __name__ == '__main__':
	logger = logging.getLogger(__name__)
	logger.setLevel(logging.INFO)

	handler = RotatingFileHandler("app.log", maxBytes=2000, backupCount=5)
	logger.addHandler(handler)

	for x in range(1000):
		logger.info("{0} iteration".format(x))

	handler = TimedRotatingFileHandler('timed_test.log', when='m', interval=1, backupCount=5)
	logger.addHandler(handler)

	for _ in range(10000):
		logger.info('Hello World!')