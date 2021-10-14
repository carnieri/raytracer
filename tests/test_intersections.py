from math import pi, sqrt
from typing import Tuple

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
from raytracer.intersections import (
    Intersection,
    intersect,
    intersections,
    hit,
    Computations,
    prepare_computations,
)


def test_an_intersection_encapsulates_t_and_object():
    s = Sphere()
    i = Intersection(3.5, s)
    assert i.t == 3.5
    assert i.object == s

def test_aggregating_intersections():
    s = Sphere()
    i1 = Intersection(1, s)
    i2 = Intersection(2, s)
    xs = intersections(i1, i2)
    assert xs[0].t == 1
    assert xs[1].t == 2

def test_intersect_sets_the_object_on_the_intersection():
    r = Ray(point(0, 0, -5), vector(0, 0, 1))
    s = Sphere()
    xs = intersect(s, r)
    assert len(xs) == 2
    assert xs[0].object == s
    assert xs[1].object == s

def test_the_hit_when_all_intersections_have_positive_t():
    s = Sphere()
    i1 = Intersection(1, s)
    i2 = Intersection(2, s)
    xs = intersections(i2, i1)
    i = hit(xs)
    assert i == i1

def test_the_hit_when_some_intersections_have_negative_t():
    s = Sphere()
    i1 = Intersection(-1, s)
    i2 = Intersection(1, s)
    xs = intersections(i2, i1)
    i = hit(xs)
    assert i == i2

def test_the_hit_when_all_intersections_have_negative_t():
    s = Sphere()
    i1 = Intersection(-2, s)
    i2 = Intersection(-1, s)
    xs = intersections(i2, i1)
    i = hit(xs)
    assert i is None

def test_the_hit_is_always_the_lowest_nonnegative_intersection():
    s = Sphere()
    i1 = Intersection(5, s)
    i2 = Intersection(7, s)
    i3 = Intersection(-3, s)
    i4 = Intersection(2, s)
    xs = intersections(i1, i2, i3, i4)
    i = hit(xs)
    assert i == i4

def test_intersecting_a_scaled_sphere_with_a_ray():
    r = Ray(point(0, 0, -5), vector(0, 0, 1))
    s = Sphere()
    s.set_transform(scaling(2, 2, 2))
    xs = intersect(s, r)
    assert len(xs) == 2
    assert equal(xs[0].t, 3)
    assert equal(xs[1].t, 7)

def test_intersecting_a_translated_sphere_with_a_ray():
    r = Ray(point(0, 0, -5), vector(0, 0, 1))
    s = Sphere()
    s.set_transform(translation(5, 0, 0))
    xs = intersect(s, r)
    assert len(xs) == 0

def test_precomputing_the_state_of_an_intersection():
    r = Ray(point(0, 0, -5), vector(0, 0, 1))
    shape = Sphere()
    i = Intersection(4, shape)
    comps = prepare_computations(i, r)
    assert comps.t == i.t
    assert comps.object == i.object
    assert comps.point == point(0, 0, -1)
    assert comps.eyev == vector(0, 0, -1)
    assert comps.normalv == vector(0, 0, -1)

def test_the_hit_when_an_intersection_occurs_on_the_outside():
    r = Ray(point(0,0, -5), vector(0, 0, 1))
    shape = Sphere()
    i = Intersection(4, shape)
    comps = prepare_computations(i, r)
    assert comps.inside == False

def test_the_hit_when_an_intersection_occurs_on_the_inside():
    r = Ray(point(0, 0, 0), vector(0, 0, 1))
    shape = Sphere()
    i = Intersection(1, shape)
    comps = prepare_computations(i, r)
    assert comps.point == point(0, 0, 1)
    assert comps.eyev == vector(0, 0, -1)
    assert comps.inside == True
    # normal would have been (0, 0, 1), but is inverted!
    assert comps.normalv == vector(0, 0, -1)

def test_the_hit_should_offset_the_point():
    r = Ray(point(0, 0, -5), vector(0, 0, 1))
    shape = Sphere()
    shape.set_transform(translation(0, 0, 1))
    i = Intersection(5, shape)
    comps = prepare_computations(i, r)
    assert comps.over_point.z < -EPSILON/2
    assert comps.point.z > comps.over_point.z
    