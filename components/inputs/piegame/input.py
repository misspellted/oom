import pygame
from components.geometry.vectors import Vector2

## For help diagnosing any relative import issues, please see components.loggers.null.logger.
from components.inputs import Input
from ...events.mouse import *

class ButtonState:
    def __init__(this):
        this.__down = False
        this.__pressed = False
        this.__released = False

    def isDown(this):
        return this.__down

    def isUp(this):
        return not this.__down

    def onUpdate(this, buttonDown):
        this.__pressed = not this.__down and buttonDown
        this.__released = this.__down and not buttonDown
        this.__down = buttonDown

    def wasPressed(this):
        wasPressed = this.__pressed
        this.__pressed = False
        return wasPressed

    def wasReleased(this):
        wasReleased = this.__released
        this.__released = False
        return wasReleased

class PygameInput(Input):
    def __init__(this):
        ## Track the last mouse event to occur per button.
        this.__buttons = dict()
        this.__position = None
        this.__mouseListener = None

    def initialize(this, buttonList):
        ## Start off all mouse buttons in the Up state.
        for button in buttonList:
            this.__buttons[button] = ButtonState()

    def __getAgnosticButton(this, mouseEvent):
        button = None
        if mouseEvent.button == 1:
            button = BUTTON_LEFT
        elif mouseEvent.button == 2:
            button = BUTTON_MIDDLE
        elif mouseEvent.button == 3:
            button = BUTTON_RIGHT
        return button

    def __setPosition(this, position):
        this.__position = Vector2()
        x, y = position
        this.__position[0] = x
        this.__position[1] = y

    def refresh(this):
        quitting = False

        pygame.event.pump()

        for event in pygame.event.get():
            quitting = event.type == pygame.QUIT

            if not quitting:
                # Is the button in the down state?
                if event.type == pygame.MOUSEBUTTONDOWN:
                    this.__setPosition(event.pos)

                    button = this.__getAgnosticButton(event)

                    if not button is None:
                        # Attempt to publish events.
                        this.__buttons[button].onUpdate(True)

                        # Publish the event to the listener if one is set.
                        if not this.__mouseListener is None:
                            if this.__buttons[button].wasPressed():
                                this.__mouseListener.onMouseButtonPressed(button)

                # Is the button in the up state?
                elif event.type == pygame.MOUSEBUTTONUP:
                    this.__setPosition(event.pos)

                    button = this.__getAgnosticButton(event)

                    if not button is None:
                        this.__buttons[button].onUpdate(False)

                        # Publish the event to the listener if one is set.
                        if not this.__mouseListener is None:
                            if this.__buttons[button].wasReleased():
                                this.__mouseListener.onMouseButtonReleased(button)

                ## What is the state of the buttons when the mouse moved?
                elif event.type == pygame.MOUSEMOTION:
                    this.__setPosition(event.pos)

                    ## event.buttons is a tuple of (left, middle, right).
                    left, middle, right = event.buttons

                    this.__buttons[BUTTON_LEFT].onUpdate(True if left == 1 else False)
                    this.__buttons[BUTTON_MIDDLE].onUpdate(True if middle == 1 else False)
                    this.__buttons[BUTTON_RIGHT].onUpdate(True if right == 1 else False)

        return quitting

    def getMouseButtonPressed(this, button):
        return this.__buttons[button].wasPressed()

    def getMouseButtonDown(this, button):
        return this.__buttons[button].isDown()

    def getMouseButtonReleased(this, button):
        return this.__buttons[button].wasReleased()

    def getMousePosition(this):
        return this.__position

    def setMouseListener(this, mouseListener):
        this.__mouseListener = mouseListener
