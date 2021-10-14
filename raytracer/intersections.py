from math import pi, sqrt
from typing import List, Optional, Any
from dataclasses import dataclass

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
from raytracer.util import equal, EPSILON
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
from raytracer.spheres import Sphere


@dataclass
class Intersection:
    t: float
    object: Sphere


def intersections(*args: Intersection) -> List[Intersection]:
    xs = sorted(args, key=lambda x: x.t)
    return xs

def intersect(s: Sphere, r: Ray) -> List[Intersection]:
    # The vector from the sphere's center to the ray origin
    # Remember: the sphere is centered at the world origin
    r2 = r.transform(s.transform.inverse())
    sphere_to_ray = r2.origin - point(0, 0, 0)
    a = dot(r2.direction, r2.direction)
    b = 2 * dot(r2.direction, sphere_to_ray)
    c = dot(sphere_to_ray, sphere_to_ray) - 1
    discriminant = b*b - 4*a*c
    if discriminant < 0:
        return []
    else:
        t1 = (-b - sqrt(discriminant)) / (2*a)
        t2 = (-b + sqrt(discriminant)) / (2*a)
        return intersections(Intersection(t1, s), Intersection(t2, s))

def hit(xs: List[Intersection]) -> Optional[Intersection]:
    valid_xs = [x for x in xs if x.t >= 0]
    sorted_xs = sorted(valid_xs, key=lambda x: x.t)
    if len(sorted_xs) > 0:
        return sorted_xs[0]
    else:
        return None

@dataclass
class Computations:
    t: float
    object: Any
    point: tuple
    eyev: tuple
    normalv: tuple
    inside: bool

    def __init__(self, t, object, point, eyev, normalv, inside=None):
        self.t = t
        self.object = object
        self.point = point
        self.eyev = eyev
        self.normalv = normalv
        if dot(self.normalv, self.eyev) < 0:
            self.inside = True
            self.normalv = -self.normalv
        else:
            self.inside = False


def prepare_computations(i: Intersection, r: Ray) -> Computations:
    p = r.position(i.t)
    eyev = -r.direction
    normalv = i.object.normal_at(p)
    comps = Computations(i.t, i.object, p, eyev, normalv)
    comps.over_point = comps.point + comps.normalv * EPSILON
    return comps
