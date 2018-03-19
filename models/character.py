from models import Model, DynamicModel

class CharacterModel(DynamicModel):
    def __init__(this, type, identifier=None):
        this.__type = type
        this.__identifier = identifier
        this.__position = (0, 0) # not a fan, feels like an intrusion of the separation of concerns.

    def getType(this):
        return this.__type

    def getIdentifier(this):
        return this.__identifier

    def getPosition(this):
        return this.__position

class DetectiveModel(CharacterModel):
    def __init__(this):
        CharacterModel.__init__(this, "detective")

class OfficerModel(CharacterModel):
    def __init__(this, identifier):
        CharacterModel.__init__(this, "officer", identifier)

class LawyerModel(CharacterModel):
    def __init__(this, identifier):
        CharacterModel.__init__(this, "lawyer", identifier)

class AccusedModel(CharacterModel):
    def __init__(this, identifier):
        CharacterModel.__init__(this, "accused", identifier)

class WitnessModel(CharacterModel):
    def __init__(this, identifier):
        CharacterModel.__init__(this, "witness", identifier)
