from controllers import Controller, RenderingController
from models import Model, DynamicModel

# The scene contains the models of that need to be drawn.
class SceneController(Controller):
    def __init__(this, viewerDimensions):
        Controller.__init__(this)
        this.__controllers = dict()
        this.__dimensions = viewerDimensions

    def addController(this, identifier, controller):
        if isinstance(controller, RenderingController):
            this.__controllers[identifier] = controller

        return controller

    def getController(this, identifier):
        controller = None

        if identifier in this.__controllers:
            controller = this.__controllers[identifier]

        return controller

    def nixController(this, identifier):
        controller = None

        if identifier in this.__controllers:
            controller = this.__controllers.pop(identifier, None)

        return controller

    def update(this):
        for identifier in this.__controllers:
            this.__controllers[identifier].update()

    def render(this, renderer):
        # Step 0: Render a blank scene.
        length, height = this.__dimensions

        rendering = renderer.createRenderTarget(length, height, (0, 0, 0))

        # Step 1: Render all the rendering controllers.
        if not rendering is None:
            for identifier in this.__controllers:
                this.__controllers[identifier].renderTo(rendering, renderer)

        return (this.__dimensions, rendering)

    def onMouseButtonPressed(this, button, currentWorldPosition):
        # Notifiy all rendering controllers, for now.
        for identifier in this.__controllers:
            this.__controllers[identifier].onMouseButtonPressed(button, currentWorldPosition)

    def onMouseButtonReleased(this, button, currentWorldPosition):
        # Notifiy all rendering controllers, for now.
        for identifier in this.__controllers:
            this.__controllers[identifier].onMouseButtonReleased(button, currentWorldPosition)
