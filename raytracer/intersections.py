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


@dataclass
class Intersection:
    t: float
    object: Any


def intersections(*args: Intersection) -> List[Intersection]:
    xs = sorted(args, key=lambda x: x.t)
    return xs

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
