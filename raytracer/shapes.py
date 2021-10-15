from math import pi, sqrt
import itertools
from typing import List

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
from raytracer.intersections import Intersection


class Shape:
    def __init__(self):
        self.transform = I
        self.material = Material()

    def set_transform(self, transform):
        self.transform = transform

    def intersect(self, ray: Ray) -> List[Intersection]:
        local_ray = ray.transform(self.transform.inverse())
        return self.local_intersect(local_ray)

    def normal_at(self, world_point):
        local_point = self.transform.inverse() * world_point
        local_normal = self.local_normal_at(local_point)
        world_normal = self.transform.inverse().transpose() * local_normal
        world_normal.w = 0
        return normalize(world_normal)

    def __eq__(self, other):
        return (
            self.transform == other.transform and 
            self.material == other.material
        )


class TestShape(Shape):
    def local_intersect(self, ray):
        self.saved_ray = ray    # for testing
    def local_normal_at(self, local_point):
        # just convert the point to a vector
        return vector(local_point.x, local_point.y, local_point.z)


def test_shape():
    return TestShape()
