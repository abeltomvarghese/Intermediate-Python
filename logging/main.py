import logging
import helperLogger
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %H:%M:%S')

if __name__ == '__main__':
	logging.debug("This is a debug message")
	logging.info("This is a info message")
	logging.warning("This is a warning message")
	logging.error("This is a error message")
	logging.critical("This is a critical message")