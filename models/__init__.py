# Static models should use this foundation.
class Model:
    pass

class DynamicModel(Model):
    def update(this):
        return NotImplemented

