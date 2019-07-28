import logging, sys
from spider.Config import FILE_LOG, CONSOLE_LOG, LOG_FILENAME


def get_logger():
    myLogger = logging.getLogger('log')
    while myLogger.hasHandlers():
        for i in myLogger.handlers:
            myLogger.removeHandler(i)

    formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
    if FILE_LOG:
        fh = logging.FileHandler(LOG_FILENAME, encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        myLogger.addHandler(fh)
    if CONSOLE_LOG:
        formatter = logging.Formatter('%(message)s')
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)
        myLogger.addHandler(ch)
    return myLogger


logger = get_logger()
