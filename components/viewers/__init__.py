## Define the viewer 'interface'.
class Viewer:
    def initialize(this, dimensions = None):
        return NotImplemented

    def getDimensions(this):
        return NotImplemented

    def toggleFullScreen(this):
        return NotImplemented

    def clear(this):
        return NotImplemented

    def draw(this, item, coordinates):
        return NotImplemented

    def refresh(this):
        return NotImplemented

    def terminate(this):
        return NotImplemented

## Import the available viewers.
from piegame.viewer import PygameViewer

## Define the available viewers.
__viewers = dict()
__viewers["pygame"] = PygameViewer()

## Provide the ability to get the names of available viewers.
def getAvailableViewerNames():
    return __viewers.keys()

## Provides the ability to get an available viewer.
def getViewer(viewerName):
    viewer = None
    if viewerName in __viewers.keys():
        viewer = __viewers[viewerName]
    return viewer
