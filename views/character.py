import assets
from views import View
from views.room import FloorTileView

class CharacterView(View):
    def __init__(this, characterModel):
        View.__init__(this)
        this.__character = characterModel

    def render(this, renderer):
        # Generate the rendering (currently 32 px^2).
        length = FloorTileView.FloorTileLength
        height = FloorTileView.FloorTileHeight

        rendering = renderer.createRenderTarget(length, height, (0, 0, 0, 0))

        characterType = this.__character.getType()

        if not characterType is None:
            renderer.renderItemTo(rendering, assets.getImage(characterType), (0, 0))

        return rendering
