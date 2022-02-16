import logging

logging.basicConfig(filename='D:\HW\Python_Vadim_Course\SeleniumLog\Test1.log',
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug('This debug message should go to the log file')
logger.info('This info message should go to the log file')

logger.error('This error message should go to the log file')
logger.warning('This warning message should go to the log file')
logger.critical('This critical message should go to the log file')
