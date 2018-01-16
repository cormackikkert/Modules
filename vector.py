from numbers import Number

class Vector2d:
    
    def __init__(self, x, y):
        assert isinstance(x, Number), "x value must be a number"
        assert isinstance(y, Number), "y value must be a number"
        self.x = x
        self.y = y

    def normalise(self):
        mag = self.mag
        self.x /= mag
        self.y /= mag

    def __add__(self, other):
        assert isinstance(other, Vector2d), "Only vectors can be added to vectors"
        return Vector2d(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        assert isinstance(other, Vector2d), "Only vectors can be subtracted from vectors"
        return Vector2d(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, Vector2d):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, Number):
            return Vector2d(self.x * other, self.y * other)
        else:
            raise ValueError("Vectors can only be multiplied by a number or another vector")
        
    def __iadd__(self, other):
        assert isinstance(other, Vector2d), "Only vectors can be added to vectors"
        self.x += other.x
        self.y += other.y
        
    def __isub__(self, other):
        assert isinstance(other, Vector2d), "Only vectors can be subtracted from vectors"
        self.x -= other.x
        self.y -= other.y

    def __iter__(self):
        yield self.x
        yield self.y

    @property
    def mag(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    @mag.setter
    def mag(self, value):
        assert isinstance(value, Number), "Magnitude of a vector must be a number"
        self.normalise()
        self *= value

    def __str__(self):
        return f"Vector x:{self.x} y:{self.y}"
        
    
