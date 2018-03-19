## Define the logger 'interface'.
class Logger:
    def error(this, error, message = None):
        return NotImplemented

    def warn(this, message):
        return NotImplemented

    def debug(this, message):
        return NotImplemented

    def info(this, message):
        return NotImplemented

## Import the available loggers.
from null.logger import NullLogger
from print2x.logger import Print2xLogger

## Define the available loggers.
__loggers = dict()
__loggers["null"] = NullLogger()
__loggers["print"] = Print2xLogger()

## Gets the names names of all available loggers.
def getAvailableLoggerNames():
    return __loggers.keys()

## Gets the desired logger if available.
def getLogger(loggerName):
    logger = None
    if loggerName in __loggers.keys():
        logger = __loggers[loggerName]
    return logger
