from math import pi, sqrt
import itertools

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
from raytracer.rays import Ray


class Sphere:
    id_iter = itertools.count()

    def __init__(self):
        # generate a unique id for this sphere
        self.id = next(self.id_iter)
        self.transform = I

    def set_transform(self, transform):
        self.transform = transform
