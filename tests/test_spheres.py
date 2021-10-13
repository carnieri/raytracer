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
from raytracer.spheres import Sphere
from raytracer.intersections import Intersection, intersect
from raytracer.materials import Material


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

def test_a_spheres_default_transformation():
    s = Sphere()
    assert s.transform == I

def test_changing_a_spheres_transformation():
    s = Sphere()
    t = translation(2, 3, 4)
    s.set_transform(t)
    assert s.transform == t

def test_the_normal_on_a_sphere_at_a_point_on_the_x_axis():
    s = Sphere()
    n = s.normal_at(point(1, 0, 0))
    assert n == vector(1, 0, 0)

def test_the_normal_on_a_sphere_at_a_point_on_the_y_axis():
    s = Sphere()
    n = s.normal_at(point(0, 1, 0))
    assert n == vector(0, 1, 0)

def test_the_normal_on_a_sphere_at_a_point_on_the_z_axis():
    s = Sphere()
    n = s.normal_at(point(0, 0, 1))
    assert n == vector(0, 0, 1)

def test_the_normal_on_a_sphere_at_a_nonaxial_point():
    s = Sphere()
    n = s.normal_at(point(sqrt(3)/3, sqrt(3)/3, sqrt(3)/3))
    assert n == vector(sqrt(3)/3, sqrt(3)/3, sqrt(3)/3)

def test_the_normal_is_a_normalized_vector():
    s = Sphere()
    n = s.normal_at(point(sqrt(3)/3, sqrt(3)/3, sqrt(3)/3))
    assert n == normalize(n)

def test_computing_the_normal_on_a_translated_sphere():
    s = Sphere()
    s.set_transform(translation(0, 1, 0))
    n = s.normal_at(point(0, 1.70711, -0.70711))
    assert n == vector(0, 0.70711, -0.70711)

def test_computing_the_normal_on_a_transformed_sphere():
    s = Sphere()
    m = scaling(1, 0.5, 1) * rotation_z(pi / 5)
    s.set_transform(m)
    n = s.normal_at(point(0, sqrt(2)/2, -sqrt(2)/2))
    assert n == vector(0, 0.97014, -0.24254)

def test_a_sphere_has_a_default_material():
    s = Sphere()
    m = s.material
    assert m == Material()

def test_a_sphere_may_be_assigned_a_material():
    s = Sphere()
    m = Material()
    m.ambient = 1
    s.material = m
    assert s.material == m
