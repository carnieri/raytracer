from math import pi, sqrt

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


def test_creating_and_querying_a_ray():
    origin = point(1, 2, 3)
    direction = vector(4, 5, 6)
    r = Ray(origin, direction)
    assert r.origin == origin
    assert r.direction == direction

def test_computing_a_point_from_a_distance():
    r = Ray(point(2, 3, 4), vector(1, 0, 0))
    assert r.position(0) == point(2, 3, 4)
    assert r.position(1) == point(3, 3, 4)
    assert r.position(-1) == point(1, 3, 4)
    assert r.position(2.5) == point(4.5, 3, 4)

def test_translating_a_ray():
    r = Ray(point(1, 2, 3), vector(0, 1, 0))
    m = translation(3, 4, 5)
    r2 = r.transform(m)
    assert r2.origin == point(4, 6, 8)
    assert r2.direction == vector(0, 1, 0)

def test_scaling_a_ray():
    r = Ray(point(1, 2, 3), vector(0, 1, 0))
    m = scaling(2, 3, 4)
    r2 = r.transform(m)
    assert r2.origin == point(2, 6, 12)
    assert r2.direction == vector(0, 3, 0)
