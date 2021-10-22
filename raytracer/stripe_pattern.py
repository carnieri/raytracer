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

    def stripe_at(self, point: tuple):
        if floor(point.x) % 2 == 0:
            return self.a
        else:
            return self.b

    def stripe_at_object(self, object: Shape, world_point: tuple) -> Color:
        object_point = object.transform.inverse() * world_point
        pattern_point = self.transform.inverse() * object_point
        return self.stripe_at(pattern_point)
    
    def set_pattern_transform(self, transform: Matrix) -> None:
        self.transform = transform