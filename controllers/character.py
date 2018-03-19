from controllers import RenderingController
from views.character import CharacterView

class Character(RenderingController):
    def __init__(this, characterModel):
        RenderingController.__init__(this)

        # Create the identifier used to track the mvPair.
        this.__modelViewIdentifier = characterModel.getType()

        characterIdentifier = characterModel.getIdentifier()

        if not characterIdentifier is None:
            this.__modelViewIdentifier += "-" + characterIdetifier

        this.addModelAndView(this.__modelViewIdentifier, characterModel, CharacterView(characterModel))

    def renderTo(this, rendering, renderer):
        model, view = this.getModelAndView(this.__modelViewIdentifier, True) # Are characters dynamic?

        characterRendering = view.render(renderer)

        renderer.renderItemTo(rendering, characterRendering, (0, 0))
