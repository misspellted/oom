## Define the camera 'interface'.
class Camera:
    def initialize(this, viewer):
        return NotImplemented

    def capture(this, view, renderer):
        return NotImplemented

    def translate(this, delta):
        return NotImplemented

    def terminate(this):
        return NotImplemented

    def screenToWorldPosition(this, screenPosition):
        return NotImplemented

## Import the available cameras.
from piegame.camera import PygameCamera

## Define the available cameras.
__cameras = dict()
__cameras["pygame"] = PygameCamera()

## Provide the ability to get the names of available cameras.
def getAvailableCameraNames():
    return __cameras.keys()

## Provides the ability to get an available camera.
def getCamera(cameraName):
    camera = None
    if cameraName in __cameras.keys():
        camera = __cameras[cameraName]
    return camera
