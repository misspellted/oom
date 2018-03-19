import assets
from controllers import Controller
from components.events.mouse import BUTTON_LEFT, BUTTON_MIDDLE, BUTTON_RIGHT

class MouseController(Controller):
    def __init__(this, inputComponent, cameraComponent, sceneController):
        # Tracks used components and controllers.
        this.__input = inputComponent
        this.__input.setMouseListener(this)
        this.__camera = cameraComponent
        this.__sceneController = sceneController

        # Tracks mouse positions
        this.__lastFramePosition = None
        this.__currentFramePosition = None
        this.__lastWorldPosition = None
        this.__currentWorldPosition = None

    def start(this):
        pass

    def update(this):
        this.__currentFramePosition = this.__input.getMousePosition()
        this.__currentWorldPosition = this.__camera.screenToWorldPosition(this.__currentFramePosition)

        ## TODO: All the things.

        this.__lastFramePosition = this.__input.getMousePosition()
        this.__lastWorldPosition = this.__camera.screenToWorldPosition(this.__currentFramePosition)

    ## The mouse button referenced was JUST pressed.
    def onMouseButtonPressed(this, button):
        this.__sceneController.onMouseButtonPressed(button, this.__currentWorldPosition)

    ## The mouse button referenced was JUST released.
    def onMouseButtonReleased(this, button):
        this.__sceneController.onMouseButtonReleased(button, this.__currentWorldPosition)
