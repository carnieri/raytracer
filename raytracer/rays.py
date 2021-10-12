from dataclasses import dataclass

from raytracer.tuple import (
    tuple,
    point,
    vector,
    magnitude,
    normalize,
    dot,
    cross,
    color,
)
from raytracer.util import equal
from raytracer.matrices import Matrix, I
from raytracer.transformations import (
    translation,
    scaling,
    rotation_x,
    rotation_y,
    rotation_z,
    shearing,
)

@dataclass
class Ray:
    origin: point
    direction: vector

    def position(self, t):
        return self.origin + self.direction * t

    def transform(self, mat):
        return Ray(mat * self.origin, mat * self.direction)