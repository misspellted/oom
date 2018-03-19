from models import Model, DynamicModel
from views import View

# Define the Controller interface that connects a model to a vew.
class Controller:
    def __init__(this):
        this.__statics = dict()
        this.__dynamics = dict()

    def addModelAndView(this, identifier, model, view):
        if not identifier is None and isinstance(view, View):
            if isinstance(model, DynamicModel):
                this.__dynamics[identifier] = (model, view)
            elif isinstance(model, Model):
                this.__statics[identifer] = (model, view)

        return (model, view)

    def getModelAndView(this, identifier, dynamic):
        mvPair = None

        if dynamic:
            if identifier in this.__dynamics:
                mvPair = this.__dynamics[identifier]
        else:
            if identifier in this.__statics:
                mvPair = this.__statics

        return mvPair

    def nixModelAndView(this, identifer, dynamic):
        mvPair = None

        if dynamic:
            if identifier in this.__dynamics:
                mvPair = this.__dynamics.pop(identifier, None)
        else:
            if identifier in this.__statics:
                mvPair = this.__statics.pop(idenifier, None)

        return mvPair

    def start(this):
        ## TODO: Check to see if there are any actual uses of this method, and see if we can delete it.
        pass

    def update(this):
#        print "Controller.update()"
        for identifier in this.__dynamics:
            mvPair = this.__dynamics[identifier]
            mvPair[0].update()

class RenderingController(Controller):
    def __init__(this):
        Controller.__init__(this)

    def renderTo(this, rendering, renderer):
        return NotImplemented

    def onMouseButtonPressed(this, button, currentWorldPosition):
        return NotImplemented

    def onMouseButtonReleased(this, button, currentWorldPosition):
        return NotImplemented
