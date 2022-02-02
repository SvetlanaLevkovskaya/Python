import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    filename='D:\HW\Python_Vadim_Course\SeleniumLog\Test.log')
#logging.basicConfig(level=logging.DEBUG)

logging.debug('This debug message should go to the log file')
logging.info('This info message should go to the log file')

logging.error('This error message should go to the log file')
logging.warning('This warning message should go to the log file')
logging.critical('This critical message should go to the log file')

