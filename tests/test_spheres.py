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
from raytracer.spheres import Sphere
from raytracer.intersections import Intersection, intersect


def test_a_ray_intersects_a_sphere_at_two_points():
    r = Ray(point(0, 0, -5), vector(0, 0, 1))
    s = Sphere()
    xs = intersect(s, r)
    print(type(xs), xs)
    assert len(xs) == 2
    assert equal(xs[0].t, 4.0)
    assert equal(xs[1].t, 6.0)

def test_a_ray_intersects_a_sphere_at_a_tangent():
    r = Ray(point(0, 1, -5), vector(0, 0, 1))
    s = Sphere()
    xs = intersect(s, r)
    assert len(xs) == 2
    assert equal(xs[0].t, 5.0)
    assert equal(xs[1].t, 5.0)

def test_a_ray_misses_a_sphere():
    r = Ray(point(0, 2, -5), vector(0, 0, 1))
    s = Sphere()
    xs = intersect(s, r)
    assert len(xs) == 0

def test_a_ray_originates_inside_a_sphere():
    r = Ray(point(0, 0, 0), vector(0, 0, 1))
    s = Sphere()
    xs = intersect(s, r)
    assert len(xs) == 2
    assert equal(xs[0].t, -1.0)
    assert equal(xs[1].t, 1.0)

def test_a_sphere_is_behind_a_ray():
    r = Ray(point(0, 0, 5), vector(0, 0, 1))
    s = Sphere()
    xs = intersect(s, r)
    assert len(xs) == 2
    assert equal(xs[0].t, -6.0)
    assert equal(xs[1].t, -4.0)
