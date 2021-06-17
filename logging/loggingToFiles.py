import logging
logging.basicConfig(level=logging.INFO)
if __name__ == "__main__":
	logger = logging.getLogger(__name__)

	#Set the handler
	stream_h = logging.StreamHandler()
	file_h = logging.FileHandler('output.log')

	#Set the Error level
	stream_h.setLevel(logging.INFO)
	file_h.setLevel(logging.ERROR)

	#Set the formatter
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	stream_h.setFormatter(formatter)
	file_h.setFormatter(formatter)

	#Connect up the handlers
	logger.addHandler(stream_h)
	logger.addHandler(file_h)
	logger.propagate = False

	logger.info("This is an information text")
	logger.warning("This is an warning text")
	logger.error("This is an error text")
	logger.critical("This is a critical error text")