import assets
from models.room import FloorModel, DoorState
from views import View

class FloorTileView(View):
    FloorTileLength = 32
    FloorTileHeight = 32

    def __init__(this, floorTileModel):
        this.__floorTile = floorTileModel

    def render(this, renderer):
        # Generate the rendering.
        rendering = renderer.createRenderTarget(FloorTileView.FloorTileLength, FloorTileView.FloorTileHeight, (0, 0, 0))

        # Apply the floor tile image.
        renderer.renderItemTo(rendering, assets.getImage("tile_ir_e"), (0, 0))

        return rendering

class FloorView(View):
    def __init__(this, floorModel):
        View.__init__(this)
        this.__floor = floorModel
        this.__floorTileViews = list()

        floorTileRows = floorModel.getTileRows()
        floorTileColumns = floorModel.getTileColumns()

        for rowIndex in range(floorTileRows):
            for columnIndex in range(floorTileColumns):
                this.__floorTileViews.append(FloorTileView(floorModel.getTile(rowIndex, columnIndex)))

    def render(this, renderer):
        floorTileRows = this.__floor.getTileRows()
        floorTileColumns = this.__floor.getTileColumns()

        length = FloorTileView.FloorTileLength * floorTileColumns
        height = FloorTileView.FloorTileHeight * floorTileRows

        # Generate the rendering.
        rendering = renderer.createRenderTarget(length, height, (0, 0, 0))

        for rowIndex in range(floorTileRows):
            floorTileY = FloorTileView.FloorTileHeight * rowIndex

            for columnIndex in range(floorTileColumns):
                floorTileView = this.__floorTileViews[rowIndex * floorTileColumns + columnIndex]

                floorTileRendering = floorTileView.render(renderer)

                floorTileX = FloorTileView.FloorTileLength * columnIndex

                # Copy the tile graphic into the rendering.
                renderer.renderItemTo(rendering, floorTileRendering, (floorTileX, floorTileY))

        return rendering

class WallsView(View):
    def __init__(this, floorModel):
        View.__init__(this)
        this.__floorDimensions = (floorModel.getTileRows(), floorModel.getTileColumns())

    def render(this, renderer):
        floorTileRows, floorTileColumns = this.__floorDimensions

        length = FloorTileView.FloorTileLength * floorTileColumns
        height = FloorTileView.FloorTileHeight * floorTileRows

        # Generate the rendering.
        rendering = renderer.createRenderTarget(length, height, (0, 0, 0, 0))

        # Apply the top-left corner.
        image = assets.getImage("tile_ir_tl")
        renderer.renderItemTo(rendering, image, (0, 0))

        # Apply the top wall.
        image = assets.getImage("tile_ir_t")
        for columnIndex in range(1, floorTileColumns - 1):
            floorTileX = FloorTileView.FloorTileLength * columnIndex
            renderer.renderItemTo(rendering, image, (floorTileX, 0))

        # Apply the top-right corner.
        image = assets.getImage("tile_ir_tr")
        rightWallX = FloorTileView.FloorTileLength * (floorTileColumns - 1)
        renderer.renderItemTo(rendering, image, (rightWallX, 0))

        # Apply the right wall.
        image = assets.getImage("tile_ir_r")
        for rowIndex in range(1, floorTileRows - 1):
            floorTileY = FloorTileView.FloorTileHeight * rowIndex
            renderer.renderItemTo(rendering, image,  (rightWallX, floorTileY))

        # Apply the bottom-right corner.
        image = assets.getImage("tile_ir_br")
        bottomWallY = FloorTileView.FloorTileHeight * (floorTileRows - 1)
        renderer.renderItemTo(rendering, image, (rightWallX, bottomWallY))

        # Apply the bottom wall.
        image = assets.getImage("tile_ir_b")
        for columnIndex in range(1, floorTileColumns - 1):
            floorTileX = FloorTileView.FloorTileLength * columnIndex
            renderer.renderItemTo(rendering, image, (floorTileX, bottomWallY))

        # Apply the bottom-left corner.
        image = assets.getImage("tile_ir_bl")
        renderer.renderItemTo(rendering, image, (0, bottomWallY))

        # Apply the left wall (skipping the door, which lives 2 down from the top and is 2 in size).
        image = assets.getImage("tile_ir_l")
        floorTileY = FloorTileView.FloorTileHeight
        renderer.renderItemTo(rendering, image, (0, floorTileY))
        for rowIndex in range(4, floorTileRows - 1):
            floorTileY = FloorTileView.FloorTileHeight * rowIndex
            renderer.renderItemTo(rendering, image,  (0, floorTileY))

        return rendering

class DoorView(View):
    def __init__(this, doorModel):
        View.__init__(this)
        this.__door = doorModel

    def render(this, renderer):
        # Generate the rendering (2x1 tile overlay).
        length = FloorTileView.FloorTileLength
        height = FloorTileView.FloorTileHeight * 2

        rendering = renderer.createRenderTarget(length, height, (0, 0, 0, 0))

        ## TODO: Remove "smurf" naming: door.getDoorState() -> door.getState().
        doorState = this.__door.getDoorState()

        image = None

        if doorState == DoorState.Closed:
            image = assets.getImage("door_closed")
        elif doorState == DoorState.Cracked:
            image = assets.getImage("door_cracked")
        elif doorState == DoorState.Ajar:
            image = assets.getImage("door_ajar")
        elif doorState == DoorState.Opened:
            image = assets.getImage("door_opened")

        if not image is None:
            # Apply the door image.
            renderer.renderItemTo(rendering, image, (0, 0))

        return rendering

class MirrorView(View):
    def __init__(this, floorModel):
        View.__init__(this)
        this.__floorTileRows = floorModel.getTileRows()

    def render(this, renderer):
        # Generate the rendering (sized to the room with 2 rows from the bottom and 2 from the door).
        ## TODO: Make this not/less hardcoded. 2 bottom-wall-buffer, 1 door-mirror-buffer, 2 door-top-wall-buffer, 2 door-size (future).
        mirrorRows = this.__floorTileRows - (2 + 1 + 2 + 2)

        height = FloorTileView.FloorTileHeight * mirrorRows

        rendering = renderer.createRenderTarget(FloorTileView.FloorTileLength, height, (0, 0, 0, 0))

        # Apply the top of the one-way mirror.
        mirrorTileY = 0
        renderer.renderItemTo(rendering, assets.getImage("owm_t"), (0, mirrorTileY))

        # Apply the center of the one-way mirror.
        image = assets.getImage("owm_c")
        for rowIndex in range(1, mirrorRows - 1):
            mirrorTileY += FloorTileView.FloorTileHeight
            renderer.renderItemTo(rendering, image, (0, mirrorTileY))

        # Apply the bottom of the one-way mirror.
        mirrorTileY += FloorTileView.FloorTileHeight
        renderer.renderItemTo(rendering, assets.getImage("owm_b"), (0, mirrorTileY))

        return rendering

class TableView(View):
    def __init__(this, tableModel):
        View.__init__(this)
        this.__table = tableModel

    def render(this, renderer):
        # Generate the rendering (sized to be centered in the room with 3 rows on either side).
        tableTileRows = this.__table.getTileRows()
        tableTileColumns = this.__table.getTileColumns()

        length = FloorTileView.FloorTileLength * tableTileColumns
        height = FloorTileView.FloorTileHeight * tableTileRows

        rendering = renderer.createRenderTarget(length, height, (0, 0, 0, 0))

        # Apply the top-left corner.
        image = assets.getImage("table_tl")
        renderer.renderItemTo(rendering, image, (0, 0))

        # Apply the top-right corner.
        image = assets.getImage("table_tr")
        maxTableX = FloorTileView.FloorTileLength * (tableTileColumns - 1)
        renderer.renderItemTo(rendering, image, (maxTableX, 0))

        # Apply the bottom-right corner.
        image = assets.getImage("table_br")
        maxTableY = FloorTileView.FloorTileHeight * (tableTileRows - 1)
        renderer.renderItemTo(rendering, image, (maxTableX, maxTableY))

        # Apply the bottom-left corner.
        image = assets.getImage("table_bl")
        renderer.renderItemTo(rendering, image, (0, maxTableY))

        # Apply the rest of the table.
        image = assets.getImage("table_c")

        # Apply the top edge
        for columnIndex in range(1, tableTileColumns - 1):
            tableTileX = FloorTileView.FloorTileLength * columnIndex
            renderer.renderItemTo(rendering, image, (tableTileX, 0))

        # Apply the right edge.
        for rowIndex in range(1, tableTileRows - 1):
            tableTileY = FloorTileView.FloorTileHeight * rowIndex
            renderer.renderItemTo(rendering, image,  (maxTableX, tableTileY))

        # Apply the bottom edge.
        for columnIndex in range(1, tableTileColumns - 1):
            tableTileX = FloorTileView.FloorTileLength * columnIndex
            renderer.renderItemTo(rendering, image, (tableTileX, maxTableY))

        # Apply the left edge.
        for rowIndex in range(1, tableTileRows - 1):
            tableTileY = FloorTileView.FloorTileHeight * rowIndex
            renderer.renderItemTo(rendering, image,  (0, tableTileY))

        # Apply the center.
        for rowIndex in range(1, tableTileRows - 1):
            tableTileY = FloorTileView.FloorTileHeight * rowIndex
            for columnIndex in range(1, tableTileColumns - 1):
                tableTileX = FloorTileView.FloorTileLength * columnIndex
                renderer.renderItemTo(rendering, image, (tableTileX, tableTileY))

        ## TODO: Render any evidence folders if the model indicates that it is in that state.

        return rendering

class ChairView(View):
    FacingBottom = 0
    FacingTop = 1

    def __init__(this, facingDirection):
        View.__init__(this)
        this.__facing = facingDirection

    def render(this, renderer):
        # Generate the rendering (chairs take 2x2 floor tiles).
        chairLength = FloorTileView.FloorTileLength * 2
        chairHeight = FloorTileView.FloorTileHeight * 2

        rendering = renderer.createRenderTarget(chairLength, chairHeight, (0, 0, 0, 0))

        # Pick the image used based on the direction the chair is facing.
        if this.__facing == ChairView.FacingBottom:
            renderer.renderItemTo(rendering, assets.getImage("chair_btt"), (0, 0))
        elif this.__facing == ChairView.FacingTop:
            renderer.renderItemTo(rendering, assets.getImage("chair_btb"), (0, 0))

        return rendering

class RoomView(View):
    def __init__(this, roomModel):
        View.__init__(this)
        this.__room = roomModel
        floorModel = roomModel.getFloorModel()
        this.__floorView = FloorView(floorModel)
        this.__wallsView = WallsView(floorModel)
        this.__doorView = DoorView(roomModel.getDoorModel())
        this.__mirrorView = MirrorView(floorModel)
        this.__tableView = TableView(roomModel.getTableModel())
        this.__chairTLView = ChairView(ChairView.FacingBottom)
        this.__chairTRView = ChairView(ChairView.FacingBottom)
        this.__chairBLView = ChairView(ChairView.FacingTop)
        this.__chairBRView = ChairView(ChairView.FacingTop)

    def render(this, renderer):
        # The floor is going to dictate the complete rendering.
        rendering = this.__floorView.render(renderer)

        # The walls exist .. at the walls.
        renderer.renderItemTo(rendering, this.__wallsView.render(renderer), (0, 0))

        # The door exists near the top-left of the room.
        doorY = FloorTileView.FloorTileHeight * 2
        renderer.renderItemTo(rendering, this.__doorView.render(renderer), (0, doorY))

        # The one-way mirror lives in the left wall, 2 tiles up from the bottom wall.
        mirrorY = FloorTileView.FloorTileHeight * 5
        renderer.renderItemTo(rendering, this.__mirrorView.render(renderer), (0, mirrorY))

        # The table sits in the middle of the room.
        tableX = FloorTileView.FloorTileLength * 6
        tableY = FloorTileView.FloorTileHeight * 8
        renderer.renderItemTo(rendering, this.__tableView.render(renderer), (tableX, tableY))

        # The chairs are facing the table and directly opposing each other.
        chairLX = FloorTileView.FloorTileLength * 7
        chairRX = FloorTileView.FloorTileLength * 11

        # The chairs above the table are placed... above the table.
        chairTY = FloorTileView.FloorTileHeight * 5 #?
        renderer.renderItemTo(rendering, this.__chairTLView.render(renderer), (chairLX, chairTY))
        renderer.renderItemTo(rendering, this.__chairTRView.render(renderer), (chairRX, chairTY))

        # The chairs below the table are placed... above the bottom wall.
        chairBY = FloorTileView.FloorTileHeight * 16 #?
        renderer.renderItemTo(rendering, this.__chairBLView.render(renderer), (chairLX, chairBY))
        renderer.renderItemTo(rendering, this.__chairBRView.render(renderer), (chairRX, chairBY))

        return rendering
