## Define the required configuration file (needs to be present in the launching program directory).
CONFIG_FILE = "config.ini"

## Define the configurable component values.
__loggerName = None
__viewerName = None
__loaderName = None
__rendererName = None
__cameraName = None
__inputName = None

## Load any configured component values.
componentsRecordFound = False
with open(CONFIG_FILE, "r") as configFile:
    ## Read the components record.
    for line in configFile:
        ## Strip the line ending.
        line = line.strip("\r\n")
        if not componentsRecordFound and line == "[components]":
            componentsRecordFound = True
            ## GOTO the next line.
            continue
        if componentsRecordFound:
            ## Allow finishing of reading the components record early.
            if len(line) == 0:
                break

            ## Process the component record fields.
            if "logger=" in line:
                __loggerName = line.split("=")[1]
            elif "viewer=" in line:
                __viewerName = line.split("=")[1]
            elif "loader=" in line:
                __loaderName = line.split("=")[1]
            elif "renderer=" in line:
                __rendererName = line.split("=")[1]
            elif "camera=" in line:
                __cameraName = line.split("=")[1]
            elif "input=" in line:
                __inputName = line.split("=")[1]

## Define the configured components.
__logger = None
__viewer = None
__loader = None
__renderer = None
__camera = None
__input = None

## Load the components if the value is configured.
if not __loggerName is None:
    import loggers
    __logger = loggers.getLogger(__loggerName)
    
if not __viewerName is None:
    import viewers
    __viewer = viewers.getViewer(__viewerName)

if not __loaderName is None:
    import loaders
    __loader = loaders.getLoader(__loaderName)

if not __rendererName is None:
    import renderers
    __renderer = renderers.getRenderer(__rendererName)

if not __cameraName is None:
    import cameras
    __camera = cameras.getCamera(__cameraName)

if not __inputName is None:
    import inputs
    __input = inputs.getInput(__inputName)

## Gets the configured logger name.
def getLoggerName():
    return __loggerName

## Gets the configured logger.
def getLogger():
    return __logger

## Gets the configured viewer name.
def getViewerName():
    return __viewerName

## Gets the configured viewer.
def getViewer():
    return __viewer

## Gets the configured loader name.
def getLoaderName():
    return __loaderName

## Gets the configured loader.
def getLoader():
    return __loader

## Gets the configured renderer name.
def getRendererName():
    return __rendererName

## Gets the configured renderer.
def getRenderer():
    return __renderer

## Gets the configured camera name.
def getCameraName():
    return __cameraName

## Gets the configured camera.
def getCamera():
    return __camera

## Gets the configured input name.
def getInputName():
    return __inputName

## Gets the configured input.
def getInput():
    return __input
