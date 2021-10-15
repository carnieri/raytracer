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
from raytracer.rays import Ray
from raytracer.planes import Plane
from raytracer.util import equal


def test_the_normal_of_a_plane_is_constante_everywhere():
    p = Plane()
    n1 = p.local_normal_at(point(0, 0, 0))
    n2 = p.local_normal_at(point(10, 0, -10))
    n3 = p.local_normal_at(point(-5, 0, 150))
    assert n1 == vector(0, 1, 0)
    assert n2 == vector(0, 1, 0)
    assert n3 == vector(0, 1, 0)

def test_intersect_with_a_ray_parallel_to_the_plane():
    p = Plane()
    r = Ray(point(0, 10, 0), vector(0, 0, 1))
    xs = p.local_intersect(r)
    assert len(xs) == 0

def test_intersect_with_a_coplanar_ray():
    p = Plane()
    r = Ray(point(0, 0, 0), vector(0, 0, 1))
    xs = p.local_intersect(r)
    assert len(xs) == 0

def test_a_ray_intersecting_a_plane_from_above():
    p = Plane()
    r = Ray(point(0, 1, 0), vector(0, -1, 0))
    xs = p.local_intersect(r)
    assert len(xs) == 1
    assert equal(xs[0].t, 1)
    assert xs[0].object == p


def test_a_ray_intersecting_a_plane_from_below():
    p = Plane()
    r = Ray(point(0, -1, 0), vector(0, 1, 0))
    xs = p.local_intersect(r)
    assert len(xs) == 1
    assert equal(xs[0].t, 1)
    assert xs[0].object == p

