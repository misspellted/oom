import traceback

## For help diagnosing any relative import issues, please see components.loggers.null.logger.
from components.loggers import Logger

class Print2xLogger(Logger):
    def __printLeveledMessage(this, level, message):
        print str.format("{0}: {1}", level, message)

    def error(this, error, message = None):
        msg = message if not message is None else str.format("{0}: {1}", error.__class__.__name__, str(error))
        this.__printLeveledMessage("ERROR", msg)
        ## Print stack trace, skipping the error(...) call.
        for frame in traceback.extract_stack()[:-1]:
            ## FileName@LineNumber: FunctionName::SourceText(NoneIfUnavailable)
            fileName, lineNumber, fxName, srcText = frame
            print str.format("\t{0}@{1}: {2}::{3}", fileName, lineNumber, fxName, "<source not available>" if srcText is None else srcText)

    def warn(this, message):
        this.__printLeveledMessage("Warning", message)

    def debug(this, message):
        this.__printLeveledMessage("Debugging", message)

    def info(this, message):
        this.__printLeveledMessage("Informing", message)
