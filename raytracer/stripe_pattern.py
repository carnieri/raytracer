from raytracer.patterns import Pattern
from dataclasses import dataclass, field
from math import floor

from raytracer.tuple import Color, tuple
from raytracer.matrices import Matrix, I
from raytracer.shapes import Shape


@dataclass
class StripePattern(Pattern):
    a: Color
    b: Color
    transform: Matrix = field(default_factory=lambda: I)

    def pattern_at(self, point: tuple):
        if floor(point.x) % 2 == 0:
            return self.a
        else:
            return self.b
    