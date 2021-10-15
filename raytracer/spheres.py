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
from raytracer.shapes import Shape
from raytracer.intersections import Intersection, intersections


class Sphere(Shape):
    def local_intersect(self, ray: Ray) -> List[Intersection]:
        # The vector from the sphere's center to the ray origin
        # Remember: the sphere is centered at the world origin
        # r2 = ray.transform(self.transform.inverse())
        sphere_to_ray = ray.origin - point(0, 0, 0)
        a = dot(ray.direction, ray.direction)
        b = 2 * dot(ray.direction, sphere_to_ray)
        c = dot(sphere_to_ray, sphere_to_ray) - 1
        discriminant = b*b - 4*a*c
        if discriminant < 0:
            return []
        else:
            t1 = (-b - sqrt(discriminant)) / (2*a)
            t2 = (-b + sqrt(discriminant)) / (2*a)
            return intersections(Intersection(t1, self), Intersection(t2, self))

    def local_normal_at(self, local_point):
        # object_point = self.transform.inverse() * world_point
        # world_normal = self.transform.inverse().transpose() * object_normal
        # world_normal.w = 0
        # return normalize(world_normal)
        local_normal = local_point - point(0, 0, 0)
        return local_normal
