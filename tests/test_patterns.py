from raytracer.tuple import (
    tuple,
    point,
    vector,
    magnitude,
    normalize,
    dot,
    cross,
    reflect,
    Color,
)
from raytracer.rays import Ray
from raytracer.spheres import Sphere
from raytracer.intersections import Intersection, intersections, hit, prepare_computations
from raytracer.lights import PointLight
from raytracer.materials import Material, lighting
from raytracer.transformations import (
    translation,
    scaling,
    rotation_x,
    rotation_y,
    rotation_z,
    shearing,
)
from raytracer.util import equal 
from raytracer.world import World, default_world, shade_hit, color_at
from raytracer.stripe_pattern import StripePattern

black = Color(0, 0, 0)
white = Color(1, 1, 1)

def test_creating_a_stripe_pattern():
    pattern = StripePattern(white, black)
    assert pattern.a == white
    assert pattern.b == black

def test_a_stripe_pattern_is_constant_in_y():
    pattern = StripePattern(white, black)
    assert pattern.stripe_at(point(0, 0, 0)) == white
    assert pattern.stripe_at(point(0, 1, 0)) == white
    assert pattern.stripe_at(point(0, 2, 0)) == white

def test_a_stripe_pattern_is_constant_in_b():
    pattern = StripePattern(white, black)
    assert pattern.stripe_at(point(0, 0, 0)) == white
    assert pattern.stripe_at(point(0, 0, 1)) == white
    assert pattern.stripe_at(point(0, 0, 2)) == white

def test_a_stripe_alternates_in_x():
    pattern = StripePattern(white, black)
    assert pattern.stripe_at(point(0.0,  0, 0)) == white
    assert pattern.stripe_at(point(0.9,  0, 0)) == white
    assert pattern.stripe_at(point(1.0,  0, 0)) == black
    assert pattern.stripe_at(point(-0.1, 0, 0)) == black
    assert pattern.stripe_at(point(-1.0, 0, 0)) == black
    assert pattern.stripe_at(point(-1.1, 0, 0)) == white

def test_lighting_with_a_pattern_applied():
    m = Material()
    m.pattern = StripePattern(white, black)
    m.ambient = 1
    m.diffuse = 0
    m.specular = 0
    eyev = vector(0, 0, -1)
    normalv = vector(0, 0, -1)
    light = PointLight(point(0, 0, -10), white)
    object = Sphere()
    c1 = lighting(m, object, light, point(0.9, 0, 0), eyev, normalv, False)
    c2 = lighting(m, object, light, point(1.1, 0, 0), eyev, normalv, False)
    assert c1 == white
    assert c2 == black

def test_stripes_with_an_object_transformation():
    object = Sphere()
    object.set_transform(scaling(2, 2, 2))
    pattern = StripePattern(white, black)
    c = pattern.stripe_at_object(object, point(1.5, 0, 0))
    assert c == white

def test_stripes_with_a_pattern_transformation():
    object = Sphere()
    pattern = StripePattern(white, black)
    pattern.set_pattern_transform(scaling(2, 2, 2))
    c = pattern.stripe_at_object(object, point(1.5, 0, 0))
    assert c == white

def test_stripes_with_both_an_object_and_a_pattern_transformation():
    object = Sphere()
    object.set_transform(scaling(2, 2, 2))
    pattern = StripePattern(white, black)
    pattern.set_pattern_transform(translation(0.5, 0, 0))
    c = pattern.stripe_at_object(object, point(2.5, 0, 0))
    assert c == white
