from math import pi, sqrt

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
from raytracer.shapes import Shape, test_shape
from raytracer.intersections import Intersection
from raytracer.materials import Material


def test_the_default_transformation():
    s = test_shape()
    assert s.transform == I

def test_assigning_a_transformation():
    s = test_shape()
    s.set_transform(translation(2, 3, 4))
    assert s.transform == translation(2, 3, 4)

def test_the_default_material():
    s = test_shape()
    m = s.material
    assert m == Material()

def test_assigning_a_material():
    s = test_shape
    m = Material()
    m.ambient = 1
    s.material = m
    assert s.material == m

def test_intersecting_a_scaled_shape_with_a_ray():
    r = Ray(point(0, 0, -5), vector(0, 0, 1))
    s = test_shape()
    s.set_transform(scaling(2, 2, 2))
    xs = s.intersect(r)
    assert s.saved_ray.origin == point(0, 0, -2.5)
    assert s.saved_ray.direction == vector(0, 0, 0.5)

def test_intersecting_a_translated_shape_with_a_ray():
    r = Ray(point(0, 0, -5), vector(0, 0, 1))
    s = test_shape()
    s.set_transform(translation(5, 0, 0))
    xs = s.intersect(r)
    assert s.saved_ray.origin == point(-5, 0, -5)
    assert s.saved_ray.direction == vector(0, 0, 1)

def test_computing_the_normal_on_a_translated_shape():
    s = test_shape()
    s.set_transform(translation(0, 1, 0))
    n = s.normal_at(point(0, 1.70711, -0.70711))
    assert n == vector(0, 0.70711, -0.70711)

def test_computing_the_normal_on_a_transformed_shape():
    s = test_shape()
    m = scaling(1, 0.5, 1) * rotation_z(pi/5)
    s.set_transform(m)
    n =  s.normal_at(point(0, sqrt(2)/2, -sqrt(2)/2))
    assert n == vector(0, 0.97014, -0.24254)
