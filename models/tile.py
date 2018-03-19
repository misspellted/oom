from collections import OrderedDict

class TileModel:
    def __init__(this):
        this.__onTileChanged = []
        this.__sortedLayers = []
        this.__layers = OrderedDict()

    def onTileChanged(this):
        for callback in this.__onTileChanged:
            callback(this)

    def registerTileChangedCallback(this, callback):
        this.__onTileChanged.append(callback)

    def setLayerContent(this, tileLayer, tileContent):
        if not tileLayer is None:
            this.__sortedLayers.append(tileLayer)
            this.__sortedLayers = sorted(this.__sortedLayers)
        this.__layers[tileLayer] = tileContent
        this.onTileChanged()

    def getLayerContents(this):
        layers = OrderedDict()
        for layerId in this.__sortedLayers:
            layers[layerId] = this.__layers[layerId]
        return layers

class UpdatingTileModel(TileModel):
    def __init__(this):
        TileModel.__init__(this)

    def update(this):
        return NotImplemented
