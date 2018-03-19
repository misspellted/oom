from models.tile import UpdatingTileModel

class DoorState:
    # 'Enumerates' the door states.
    CLOSED = 0
    SOMEWHAT = 1
    NEARLY = 2
    OPENED = 3

class DoorTileModel(UpdatingTileModel):
    def __init__(this):
        UpdatingTileModel.__init__(this)
        this.__desiredDoorState = DoorState.CLOSED
        this.__doorState = DoorState.CLOSED

    def getDoorState(this):
        return this.__doorState

    def open(this):
        this.__desiredDoorState = DoorState.OPENED

    def close(this):
        this.__desiredDoorState = DoorState.CLOSED

    def update(this):
        # Start or continue opening the door.
        if this.__desiredDoorState == DoorState.OPENED and this.__doorState < DoorState.OPENED:
            this.__doorState += 1

        # Start or continue closing the door.
        elif this.__desiredDoorState == DoorState.CLOSED and DoorState.CLOSED < this.__doorState:
            this.__doorState -= 1
