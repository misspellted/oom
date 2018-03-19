## Define the loader 'interface'.
class Loader:
    def loadImage(this, filePath):
        return NotImplemented

    def loadAudio(this, filePath):
        return NotImplemented

## Import the available loaders.
from piegame.loader import PygameLoader

## Define the available loaders.
__loaders = dict()
__loaders["pygame"] = PygameLoader()

## Gets the names names of all available loaders.
def getAvailableLoaderNames():
    return __loaders.keys()

## Gets the desired loader if available.
def getLoader(loaderName):
    loader = None
    if loaderName in __loaders.keys():
        loader = __loaders[loaderName]
    return loader
