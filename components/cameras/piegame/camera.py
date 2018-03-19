import math
import pygame
from components.geometry.vectors import Vector2

# For help diagnosing any relative import issues, please see components.loggers.null.logger.
from components.cameras import Camera

class PygameCamera(Camera):
    def __init__(this, usePadding=False):
        # Set values indicating lack of initialization.
        this.__viewer = None
        this.__renderer = None
        this.__position = Vector2()
        this.__lastCameraOffset = None
        this.__usePadding = usePadding

    def initialize(this, viewer, renderer):
        this.__viewer = viewer
        this.__renderer = renderer

    def capture(this, view):
        # Get a snapshot of the view using the renderer.
        dimensions, rendering = view.render(this.__renderer)

        ## TODO: Properly handle different dimension mismatches.

        # If a rendering was generated..
        if not rendering is None:

            # Get the viewer dimensions.
            vwr = this.__viewer.getDimensions()

            # If padding the rendering (putting a buffer around the rendering)..
            if this.__usePadding:

                # Create a padded rendering (rendering surrounded by padding relative to camera dimensions).

                ## FIXME: Assume that any dimension tuples are not None.
                rl, rh = dimensions
                vl, vh = vwr

                # Create the padded rendering.
                padded = this.__renderer.createRenderTarget(rl + vl, rh + vh, (0, 0, 0, 0))

                # Calculate the start position of the rendering in the padded rendering.
                rsx, rsy = int(math.floor(vl / 2.0)), int(math.floor(vh / 2.0))

                # Copy the rendering into the padded rendering.
                this.__renderer.renderItemTo(padded, rendering, (rsx, rsy))

                # Delete the rendering (not needed anymore, since now in padded rendering).
                rendering = None

                # Clamp the camera position.
                if rl < this.__position[0]:
                    this.__position[0] = rl
                if rh < this.__position[1]:
                    this.__position[1] = rh

                # Convert the Vector2 into a tuple.
                position = (this.__position[0], this.__position[1])

                # Get the region that should be displayed to the viewer.
                viewable = this.__renderer.copyRegionFrom(padded, position, vwr)

                # Camera offset (for screenToWorldPosition calculations).
                this.__lastCameraOffset = (this.__position[0] - rsx, this.__position[1] - rsy)

                # Delete the padded region (not needed anymore, since the viewable region is captured).
                padded = None

                # Draw the viewable region to the viewer. 
                this.__viewer.draw(viewable, (0, 0))

                # Delete the viewable region (not needed anymore, since now in viewer).
                viewable = None

            # Otherwise, just draw the rendering..
            else:

                # Draw the viewable region to the viewer. 
                this.__viewer.draw(rendering, (0, 0))

        dimensions = None

    def translate(this, delta):
        if isinstance(delta, tuple):
            newPosition = (this.__position[0] + delta[0], this.__position[1] + delta[1])
        else:
            newPosition = this.__position + delta
        if newPosition[0] < 0:
            newPosition[0] = 0
        if newPosition[1] < 0:
            newPosition[1] = 0
        this.__position = newPosition
        newPosition = None

    def terminate(this):
        this.__viewer = None
        this.__renderer = None
        this.__position = None

    def screenToWorldPosition(this, screenPosition):
        worldPosition = None

        if not (this.__lastCameraOffset is None or screenPosition is None):
            lcox, lcoy = this.__lastCameraOffset
            worldPosition = (lcox + screenPosition[0], lcoy + screenPosition[1])

        return worldPosition
