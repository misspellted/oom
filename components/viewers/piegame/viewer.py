import pygame

# For help diagnosing any relative import issues, please see components.loggers.null.logger.
from components.viewers import Viewer

class PygameViewer(Viewer):
    def __init__(this):
        # Set values indicating lack of initialization.
        this.__display = None
        this.__fullscreen = None
        this.__dimensions = None

    def initialize(this, dimensions = None):
        # Initialize the PyGame display subsystem.
        pygame.display.init()

        this.__fullscreen = dimensions is None
        this.__dimensions = dimensions

        if this.__fullscreen:
            this.__goFullScreen()
        else:
            this.__goWindowed()

    def __goFullScreen(this):
        # Only setup the fullscreen if not already in use or if just starting out.
        if not this.__fullscreen or this.__display is None:
            # If toggling, remember the old dimensions.
            this.__dimensions = this.__display.get_size()
            this.__display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN | pygame.DOUBLEBUF)
            this.__fullscreen = True
        # Indicate if the switch was completed.
        return this.__fullscreen

    def __goWindowed(this):
        # Only setup the window if not already in use or if just starting out.
        if this.__fullscreen or this.__display is None:
            this.__display = pygame.display.set_mode(this.__dimensions, pygame.DOUBLEBUF)
            this.__fullscreen = False
        # Indicate if the switch was completed.
        return not this.__fullscreen

    def getDimensions(this):
        return this.__display.get_size()

    def toggleFullScreen(this):
        toggled = False
        if not this.__dimensions is None:
            toggled = this.__goWindowed() if this.__fullscreen else this.__goFullScreen()
        return toggled

    def clear(this):
        ## TODO: Evaluate adding the capability to specify the background color.
        this.__display.fill((0, 0, 0))

    def draw(this, item, coordinates):
        if not (item is None or coordinates is None):
            if isinstance(item, pygame.Surface) and isinstance(coordinates, tuple) and len(coordinates) == 2:
                this.__display.blit(item, coordinates)

    def refresh(this):
        pygame.display.flip()

    def terminate(this):
        pygame.display.quit()
        this.__display = None
        this.__fullscreen = None
        this.__dimensions = None
