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
from raytracer.shapes import Shape
from raytracer.rays import Ray
from raytracer.intersections import Intersection
from raytracer.util import EPSILON


class Plane(Shape):
    """Infinite plane in xz."""
    def local_normal_at(self, local_point: tuple) -> tuple:
        return vector(0, 1, 0)

    def local_intersect(self, ray: Ray) -> List[Intersection]:
        if abs(ray.direction.y) < EPSILON:
            # no intersections
            return [] 
        t = -ray.origin.y / ray.direction.y
        return [Intersection(t, self)]
        