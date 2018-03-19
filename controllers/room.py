from components.events.mouse import *
from controllers import RenderingController
from models.character import DetectiveModel
from models.room import RoomModel
from models.table import TableModel
from views.character import CharacterView
from views.room import RoomView

class RoomController(RenderingController):
    Identifier = "Room"
    TableIdentifier = "Table"

    def __init__(this, tileRows, tileColumns, watchController):
        RenderingController.__init__(this)

        roomModel = RoomModel(tileRows, tileColumns, watchController)

        ## TODO: Temporary testing of responding to user events (toggling door state (OPENED <-> CLOSED)).
        this.__doorModel = roomModel.getDoorModel()

        # An interrogation room is pointless without an interrogation table. It really sets the mood.
        tableModel = TableModel(7, 8)

        roomModel.setTableModel(RoomController.TableIdentifier, tableModel)

        this.addModelAndView(RoomController.Identifier, roomModel, RoomView(roomModel))

        this.__detective = None
        this.__characters = dict()

    def __getCharacterMVIdentifier(this, characterModel):
#        print "RoomController.__getCharacterMVIdentifier()::characterModel =", characterModel
        mvIdentifier = characterModel.getType()

        identifier = characterModel.getIdentifier()
        if not identifier is None:
            mvIdentifier += "-" + str(identifier)

        return mvIdentifier

    def addCharacter(this, characterModel): # may need an identifier..
        # Remember these. They are le useful.
        if isinstance(characterModel, DetectiveModel):
            if this.__detective is None:
                this.__detective = characterModel

        else:
            type = characterModel.getType()
            identifier = characterModel.getIdentifier()

            if not type in this.__characters:
                this.__characters[type] = dict()

            if not identifier in this.__characters[type]:
                this.__characters[type][identifier] = characterModel

#            print "RoomController.addCharacter()::__characters[", type, "][", identifier, "]:", this.__characters[type][identifier]

        # Add it to the growing list of things to be rendered.
        mvIdentifier = this.__getCharacterMVIdentifier(characterModel)

        this.addModelAndView(mvIdentifier, characterModel, CharacterView(characterModel))

    def renderTo(this, rendering, renderer):
        # First, render the background (the interrogation room).
        model, view = this.getModelAndView(RoomController.Identifier, True)

        roomRendering = view.render(renderer)

        # Assumption: The room controller will generate a rendering that will fit exactly into the rendering provided by
        #             the scene controller.
        renderer.renderItemTo(rendering, roomRendering, (0, 0))

        # Then, render all the characters.
        if not this.__detective is None:
            mvIdentifier = this.__getCharacterMVIdentifier(this.__detective)

            model, view = this.getModelAndView(mvIdentifier, True) # Are characters dynamic?

            detectiveRendering = view.render(renderer)

            renderer.renderItemTo(rendering, detectiveRendering, model.getPosition()) ## TODO: getPosition()!

#        print "RoomController.renderTo()::len(this.__characters)", len(this.__characters)
        for type in this.__characters:
#            print "RoomController.renderTo()::type", type
#            print "RoomController.renderTo()::len(this.__characters[", type, "]", len(this.__characters[type])
            for identifier in this.__characters[type]:
#                print "RoomController.renderTo()::identifier", identifier
                mvIdentifier = this.__getCharacterMVIdentifier(this.__characters[type][identifier]) # Sorry, that was total derp.

                model, view = this.getModelAndView(mvIdentifier, True)

                characterRendering = view.render(renderer)

                renderer.renderItemTo(rendering, characterRendering, model.getPosition()) ## TODO: getPosition()!

    def onMouseButtonPressed(this, button, currentWorldPosition):
        if button == BUTTON_LEFT:
            this.__doorModel.open()

    def onMouseButtonReleased(this, button, currentWorldPosition):
        if button == BUTTON_RIGHT:
            this.__doorModel.close()
