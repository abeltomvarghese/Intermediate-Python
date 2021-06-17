import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %H:%M:%S')

logger = logging.getLogger(__name__)
#logger.propagate = False
logger.info("SUCCESSFUL IMPORT FROM Helper FILE")