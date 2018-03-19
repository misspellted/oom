class Color3:
    def __init__(this):
        this.__red = 0
        this.__green = 0
        this.__blue = 0

    def getRed(this):
        return this.__red

    def setRed(this, value):
        this.__red = value

    def getGreen(this):
        return this.__green

    def setGreen(this, value):
        this.__green = value

    def getBlue(this):
        return this.__blue

    def setBlue(this, value):
        this.__blue = value

class Color4(Color3):
    def __init__(this):
        Color3.__init__(this)
        this.__translucency = 0

    def getTranslucency(this):
        return this.__translucency

    def setTranslucency(this, value):
        this.__translucency = value
