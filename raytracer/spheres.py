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
    Color,
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
from raytracer.materials import Material

class Sphere:
    id_iter = itertools.count()

    def __init__(self):
        # generate a unique id for this sphere
        self.id = next(self.id_iter)
        self.transform = I
        self.material = Material()

    def set_transform(self, transform):
        self.transform = transform

    def normal_at(self, world_point):
        object_point = self.transform.inverse() * world_point
        object_normal = object_point - point(0, 0, 0)
        world_normal = self.transform.inverse().transpose() * object_normal
        world_normal.w = 0
        return normalize(world_normal)

    def __eq__(self, other):
        return (
            self.transform == other.transform and 
            self.material == other.material
        )