import assets

class TileView:
    # Define the visual dimensions of the tile here (for now).
    TILE_LENGTH = 32
    TILE_HEIGHT = 32

    def __init__(this, model):
        this.__model = model
        this.__rendering = None

        model.registerTileChangedCallback(this.onTileChanged)

        this.onTileChanged(model)

    def onTileChanged(this, tile):
        this.__rendering = None

    def render(this, renderer):
        if this.__rendering is None:

            # Update the rendering.
            this.__rendering = renderer.createRenderTarget(TileView.TILE_LENGTH, TileView.TILE_HEIGHT, (0, 0, 0))

            # Get the layer contents of the tile to get the associated image from the loaded assets.
            contentLayers = this.__model.getLayerContents()

            if len(contentLayers) == 0:
                renderer.renderItemTo(this.__rendering, assets.getImage("tile_error"), (0, 0))

            else:
                for layerId in contentLayers:
                    contentId = contentLayers[layerId]

                    image = assets.getImage(contentId)

                    if not image is None:
    	                # Copy the tile graphic into the rendering.
                	    renderer.renderItemTo(this.__rendering, image, (0, 0))

        return this.__rendering

class UpdatingTileView(TileView):
    def __init__(this, model):
        TileView.__init__(this, model)

    def update(this):
        return NotImplemented
#        this.onTileChanged(None)
