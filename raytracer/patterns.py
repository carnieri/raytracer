from dataclasses import dataclass, field
from math import floor, sqrt

from raytracer.tuple import Color, tuple
from raytracer.matrices import Matrix, I
from raytracer.util import EPSILON


class Pattern:
    def set_pattern_transform(self, transform: Matrix) -> None:
        self.transform = transform
    
    def pattern_at_shape(self, object, world_point):
        object_point = object.transform.inverse() * world_point
        pattern_point = self.transform.inverse() * object_point
        return self.pattern_at(pattern_point)
    

class DummyPattern(Pattern):
    def __init__(self):
        self.set_pattern_transform(I)

    def pattern_at(self, point: tuple) -> Color:
        return Color(point.x, point.y, point.z)


@dataclass
class StripePattern(Pattern):
    a: Color
    b: Color
    transform: Matrix = I

    def pattern_at(self, point: tuple) -> Color:
        if floor(point.x) % 2 == 0:
            return self.a
        else:
            return self.b


@dataclass
class GradientPattern(Pattern):
    a: Color
    b: Color
    transform: Matrix = I

    def pattern_at(self, point: tuple) -> Color:
        distance = self.b - self.a
        fraction = point.x - floor(point.x)
        return self.a + (distance * fraction)


@dataclass
class RingPattern(Pattern):
    a: Color
    b: Color
    transform: Matrix = I
    
    def pattern_at(self, point: tuple) -> Color:
        r = sqrt((point.x*point.x) + (point.z*point.z))
        if floor(r) % 2 == 0:
            return self.a
        else:
            return self.b


@dataclass
class CheckersPattern(Pattern):
    a: Color
    b: Color
    transform: Matrix = I

    def pattern_at(self, point: tuple) -> Color:
        if (floor(point.x) + floor(point.y) + floor(point.z)) % 2 == 0:
            return self.a
        else:
            return self.b
