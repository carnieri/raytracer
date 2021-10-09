from dataclasses import dataclass
from math import sqrt

from raytracer import util

@dataclass
class tuple:
    x: float
    y: float
    z: float
    w: float

    def is_point(self):
        return util.equal(self.w, 1.0)

    def is_vector(self):
        return util.equal(self.w, 0.0)

    def __eq__(self, other):
        return (
            util.equal(self.x, other.x)
        and util.equal(self.y, other.y)
        and util.equal(self.z, other.z)
        and util.equal(self.w, other.w)
        ) 

    def __add__(self, other):
        result = tuple(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z,
            self.w + other.w,
        )
        assert result.w == 0.0 or result.w == 1.0
        return result

    def __sub__(self, other):
        result = tuple(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z,
            self.w - other.w,
        )
        assert result.w == 0.0 or result.w == 1.0
        return result

    def __neg__(self):
        return tuple(-self.x, -self.y, -self.z, -self.w)

    def __mul__(self, scalar):
        return tuple(
            self.x * scalar,
            self.y * scalar,
            self.z * scalar,
            self.w * scalar,
        )

    def __truediv__(self, scalar):
        return tuple(
            self.x / scalar,
            self.y / scalar,
            self.z / scalar,
            self.w / scalar,
        )
    
    def magnitude(self):
        return sqrt(
            self.x * self.x +
            self.y * self.y +
            self.z * self.z +
            self.w * self.w
        )

    def normalize(self):
        m = self.magnitude()
        return tuple(
            self.x / m,
            self.y / m,
            self.z / m,
            self.w / m,
        )

    
def point(x, y, z):
    return tuple(x, y, z, 1.0)

def vector(x, y, z):
    return tuple(x, y, z, 0.0)

def magnitude(v):
    return v.magnitude()

def normalize(v):
    return v.normalize()

def dot(a, b):
    """The dot product of two vectors."""
    assert a.is_vector() and b.is_vector()
    return (
        a.x * b.x +
        a.y * b.y +
        a.z * b.z + 
        a.w * b.w
    )

def cross(a, b):
    """The cross product of two vectors."""
    assert a.is_vector() and b.is_vector()
    return vector(
        a.y * b.z - a.z * b.y,
        a.z * b.x - a.x * b.z,
        a.x * b.y - a.y * b.x,
    )

@dataclass
class color:
    r: float
    g: float
    b: float

    def __eq__(self, other):
        return (
            util.equal(self.r, other.r)
        and util.equal(self.g, other.g)
        and util.equal(self.b, other.b)
        )

    def __add__(self, other):
        return color(
            self.r + other.r,
            self.g + other.g,
            self.b + other.b,
        )

    def __sub__(self, other):
        return color(
            self.r - other.r,
            self.g - other.g,
            self.b - other.b,
        )

    def __mul__(self, other):
        if isinstance(other, (float,int)):
            scalar = other
            return color(
                self.r * scalar,
                self.g * scalar,
                self.b * scalar,
            )
        else:
            # Hadamard product
            return color(
                self.r * other.r,
                self.g * other.g,
                self.b * other.b,
            )