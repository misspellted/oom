from controllers import Controller
from models import Model, DynamicModel

# The world contains the models of everything in it.
class WorldController(Controller):
    def __init__(this):
        Controller.__init__(this)
        this.__controllers = dict()

    def addController(this, identifier, controller):
        this.__controllers[identifier] = controller

        return controller

    def getController(this, identifier):
        controller = None

        if identifier in this.__controllers:
            controller = this.__controllers[identifier]

        return controller

    def nixController(this, identifier):
        controller = None

        if identifier in this.__controllers:
            controller = this.__controllers.pop(identifier, None)

        return controller

    def update(this):
        for identifier in this.__controllers:
            this.__controllers[identifier].update()
