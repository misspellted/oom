from controllers.watch import WatchController
from models import Model, DynamicModel

class TileModel(Model):
    pass

class FloorModel(Model):
    Identifier = "Floor"

    def __init__(this, tileRows, tileColumns):
        this.__tileRows = tileRows
        this.__tileColumns = tileColumns
        this.__tiles = list()

        for row in range(tileRows):
            for column in range(tileColumns):
                this.__tiles.append(TileModel())

    def getTileRows(this):
        return this.__tileRows

    def getTileColumns(this):
        return this.__tileColumns

    def getTile(this, rowIndex, columnIndex):
        tile = None

        # 0-based indices.
        if 0 <= rowIndex < this.__tileRows and 0 <= columnIndex < this.__tileColumns:
            tile = this.__tiles[rowIndex * this.__tileColumns + columnIndex]

        ## TODO: Remove (debugging purposes).
        if tile is None:
            print "There is no tile at row index " + str(rowIndex) + ", column index " + str(columnIndex) + "."

        return tile

class DoorState:
    Opened = 0  # Starting/ending state
    Ajar = 1    # Intermediate state
    Cracked = 2 # Intermediate state
    Closed = 3  # Starting/ending state

class DoorModel(DynamicModel):
    Identifier = "Door"
    StateChangeInterval = 1.0 / 6.0

    def __init__(this, watchController):
        this.__desiredState = DoorState.Closed
        this.__doorState = DoorState.Closed
        ## TODO: Convert into adding a listener for time events.
        this.__watch = watchController
        this.__timeAtLastUpdate = this.__watch.getTime()
        this.__timeSinceLastUpdate = 0

    def getDoorState(this):
        return this.__doorState

    def open(this):
        this.__desiredState = DoorState.Opened

    def close(this):
        this.__desiredState = DoorState.Closed

    def update(this):
        timeAtUpdate = this.__watch.getTime()

        this.__timeSinceLastUpdate += (timeAtUpdate - this.__timeAtLastUpdate)

        this.__timeAtLastUpdate = timeAtUpdate

        updateDoorState = DoorModel.StateChangeInterval <= this.__timeSinceLastUpdate

        if updateDoorState:
            this.__timeSinceLastUpdate -= DoorModel.StateChangeInterval

            # Start or resume opening the door.
            if this.__desiredState < this.__doorState:
                this.__doorState -= 1

            # Start or resume closing the door.
            elif this.__doorState < this.__desiredState:
                this.__doorState += 1

class RoomModel(DynamicModel):
    def __init__(this, tileLength, tileHeight, watchController):
        this.__models = dict()

        this.__models[FloorModel.Identifier] = FloorModel(tileLength, tileHeight)
        this.__models[DoorModel.Identifier] = DoorModel(watchController)
        this.__tableIdentifier = None

    def update(this):
        if DoorModel.Identifier in this.__models:
            this.__models[DoorModel.Identifier].update()

    def getFloorModel(this):
        return this.__models[FloorModel.Identifier]

    def getDoorModel(this):
        return this.__models[DoorModel.Identifier]

    def setTableModel(this, identifier, tableModel):
        this.__models[identifier] = tableModel

        this.__tableIdentifier = identifier

        return tableModel

    def getTableModel(this):
        tableModel = None

        if not this.__tableIdentifier is None:
            tableModel = this.__models[this.__tableIdentifier]

        return tableModel
