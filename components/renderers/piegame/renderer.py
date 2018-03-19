import pygame

# For help diagnosing any relative import issues, please see components.loggers.null.logger.
from ...coloration.colors import Color3, Color4
from components.renderers import Renderer

class PygameRenderer(Renderer):
    def createRenderTarget(this, length, height, background):
        ## FIXME: Not all parameter validations performed!
        renderTarget = None
        if isinstance(background, Color4):
            renderTarget = pygame.Surface((length, height), flags=pygame.SRCALPHA, depth=32)
            bg = (background.getRed(), background.getGreen(), background.getBlue(), background.getTranslucency())
            renderTarget.fill(bg)

        elif isinstance(background, Color3):
            renderTarget = pygame.Surface((length, height), depth=24)
            bg = (background.getRed(), background.getGreen(), background.getBlue(), background.getTranslucency())
            renderTarget.fill(bg)

        elif isinstance(background, tuple):
            if len(background) == 4:
                renderTarget = pygame.Surface((length, height), flags=pygame.SRCALPHA, depth=32)
                renderTarget.fill(background)

            elif len(background) == 3:
                renderTarget = pygame.Surface((length, height), depth=24)
                renderTarget.fill(background)

        return renderTarget

    def renderItemTo(this, target, item, coordinates):
        ## FIXME: No parameter validations performed!
        target.blit(item, coordinates)

    def copyRegionFrom(this, source, coordinates, dimensions):
        ## FIXME: No parameter validations performed!
        length, height = dimensions
        rect = pygame.Rect(coordinates, dimensions)
        subsurface = source.subsurface(rect)
        rect = None
        copy = this.createRenderTarget(length, height, (0, 0, 0, 255))
        this.renderItemTo(copy, subsurface, (0, 0))
        return copy
