import logging
logger = logging.getLogger(__name__)
logging.basicConfig(filename='loginfo.log',encoding='UTF-8', level=logging.DEBUG)
logger.debug('Debug')
logger.warning('warning')
logger.info('info')
logger.error('error')