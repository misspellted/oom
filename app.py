import components

class App:
    def __init__(this):
        this.__logger = components.getLogger()
        this.__viewer = components.getViewer()
        this.__loader = components.getLoader()
        this.__renderer = components.getRenderer()
        this.__camera = components.getCamera()
        this.__input = components.getInput()

        # Log the name of the class providing the requested component in config.ini.
        this.logComponentProviders()

        # Inform application whether or not the required components are available.
        if this.hasRequiredComponents():
            this.onRequiredComponentsAvailable()
        else:
            this.onRequiredComponentsNotAvailable()

    def logComponentProviders(this):
        logger = this.getLogger()
        if not logger is None:
            loggerName = logger.__class__.__name__
            logger.debug("Configured logger: " + loggerName)
            viewer = this.getViewer()
            viewerName = "none" if viewer is None else viewer.__class__.__name__
            logger.debug("Configured viewer: " + viewerName)
            loader = this.getLoader()
            loaderName = "none" if loader is None else loader.__class__.__name__
            logger.debug("Configured loader: " + loaderName)
            renderer = this.getRenderer()
            rendererName = "none" if renderer is None else renderer.__class__.__name__
            logger.debug("Configured renderer: " + rendererName)
            camera = this.getCamera()
            cameraName = "none" if camera is None else camera.__class__.__name__
            logger.debug("Configured camera: " + cameraName)
            input = this.getInput()
            inputName = "none" if input is None else input.__class__.__name__
            logger.debug("Configured input: " + inputName)

    def hasRequiredComponents(this):
        return NotImplemented

    def onRequiredComponentsAvailable(this):
        return NotImplemented

    def onRequiredComponentsNotAvailable(this):
        return NotImplemented

    def getLogger(this):
        return this.__logger

    def getViewer(this):
        return this.__viewer

    def getLoader(this):
        return this.__loader

    def getRenderer(this):
        return this.__renderer

    def getCamera(this):
        return this.__camera

    def getInput(this):
        return this.__input
