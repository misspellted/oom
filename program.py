from app import App
import assets
from components.events.mouse import *
import controllers
from controllers.mouse import MouseController
from controllers.room import RoomController
from controllers.scene import SceneController
from controllers.watch import WatchController
from controllers.world import WorldController
from models.character import *
from views.room import FloorTileView

ROOM_ROWS = 20
ROOM_COLUMNS = 20

class LD37(App):
    def hasRequiredComponents(this):
        available = not this.getViewer() is None
        available &= not this.getLoader() is None
        available &= not this.getRenderer() is None
        available &= not this.getCamera() is None
        available &= not this.getInput() is None
        return available

    def onRequiredComponentsAvailable(this):
        # Define the final viewer pixel dimensions.
        viewer = this.getViewer()
        viewerLength = ROOM_COLUMNS * FloorTileView.FloorTileHeight
        viewerHeight = ROOM_ROWS * FloorTileView.FloorTileLength
        viewer.initialize((viewerLength, viewerHeight))

        # Load assets before using them, logging the loading for debugging if necessary.
        assets.loadAssets(this.getLoader(), this.getLogger())

        # Attach the camera to the viewer, and also provide a renderer for displayed snapshots.
        this.getCamera().initialize(viewer, this.getRenderer())

        # Track the 3 main mouse buttons (no exotic MMORPG setups please).
        this.getInput().initialize([BUTTON_LEFT, BUTTON_MIDDLE, BUTTON_RIGHT])

        # Indicate that the game is ready to enter the main game loop.
        this.__ready = True

    def onRequiredComponentsNotAvailable(this):
        this.__ready = False

    def isReady(this):
        return this.__ready

    def play(this):
        if not this.__ready:
            logger = this.getLogger()

            if not logger is None:
                logger.debug("The required components are not available, and thus the game was not ready for playing.")

        else:
            # Get the components used in the game loop.
            viewer = this.getViewer()
            camera = this.getCamera()
            input = this.getInput()
            renderer = this.getRenderer()

            # Create the world.
            world = WorldController()

            # Being on time is relatively useful.
            watch = world.addController("Watch", WatchController())

            # Add a scene.
            scene = world.addController("Scene", SceneController(viewer.getDimensions()))

            # Build the scene.
            room = RoomController(ROOM_ROWS, ROOM_COLUMNS, watch)

            ## TODO: Make this a task, so that the addition or removal of a character activates the door.
#            room.addCharacter(DetectiveModel())
#            room.addCharacter(OfficerModel(1))
#            room.addCharacter(LawyerModel(2))
#            room.addCharacter(AccusedModel(3))
            room.addCharacter(WitnessModel(4))

            scene.addController("InterrogationRoom", room)

            # Attach mouse inputs to the scene.
            mouse = world.addController("Mouse", MouseController(input, camera, scene))

            # Enter and maintain the game loop.
            quitting = False
            while not quitting:
                quitting = input.refresh()

                if not quitting:
                    # Update the world.
                    world.update()

                    # Clear the viewer.
                    viewer.clear()

                    # Capture an image from the scene.
                    camera.capture(scene)

                    # Refresh the viewer.
                    viewer.refresh()

        # Clean up to shut down the game.
        this.getCamera().terminate()
        this.getViewer().terminate()

def main():
    LD37().play()

if __name__ == "__main__":
    main()
