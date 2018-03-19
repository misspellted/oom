## Help diagnosing relative package imports.
##print "__package__: " + "None" if __package__ is None else __package__
## -> Prints 'None' when imported.
## -> Prints 'None' when executed.
##print "__name__: " + "None" if __name__ is None else __name__
## -> Prints 'components.loggers.null.logger' when imported.
## -> Prints '__main__' when executed.

from components.loggers import Logger
## -> Works if imported.
## -> 'ValueError: Attempted relative import in non-package'

class NullLogger(Logger):
    def error(this, error, message = None):
        ## Do nothing.
        pass

    def warn(this, message):
        ## Do nothing.
        pass

    def debug(this, message):
        ## Do nothing.
        pass

    def info(this, message):
        ## Do nothing.
        pass
