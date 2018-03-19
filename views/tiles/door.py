from models.tiles.door import DoorState
from views.tile import UpdatingTileView

class DoorTileView(UpdatingTileView):
    def __init__(this, model):
        UpdatingTileView.__init__(this, model)
        ## WARNING: This assumes a DoorTileModel!
        this.__doorModel = model

    def update(this):
        # Check the door state.
        doorState = this.__doorModel.getDoorState()

        if doorState == DoorState.CLOSED:
            this.__doorModel.setLayerContent(1, "door_closed")

            this.__doorModel.open()

        elif doorState == DoorState.SOMEWHAT:
            this.__doorModel.setLayerContent(1, "door_sw_opened")

        elif doorState == DoorState.NEARLY:
            this.__doorModel.setLayerContent(1, "door_nl_opened")

        else:
            this.__doorModel.setLayerContent(1, "door_opened")

            this.__doorModel.close()

        # We already know what tile model is in use.
        this.onTileChanged(None)
