import numbers

class Vector2:
    def __init__(this):
        this.__elements = [0, 0]

    def __getitem__(this, index):
        return this.__elements[index]

    def __setitem__(this, index, value):
        if isinstance(value, numbers.Number):
            this.__elements[index] = value
        else:
            raise TypeError("Expected numerical value")

    def __add__(this, other):
        if not isinstance(other, Vector2):
            return NotImplemented
        vector = Vector2()
        for index in range(2):
            vector[index] = this.__elements[index] + other[index]
        return vector

    def __sub__(this, other):
        if not isinstance(other, Vector2):
            return NotImplemented
        vector = Vector2()
        for index in range(2):
            vector[index] = this.__elements[index] - other[index]
        return vector
