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
from raytracer.matrices import Matrix, I
from raytracer.patterns import MyTestPattern
from raytracer.stripe_pattern import StripePattern

black = Color(0, 0, 0)
white = Color(1, 1, 1)

def test_creating_a_stripe_pattern():
    pattern = StripePattern(white, black)
    assert pattern.a == white
    assert pattern.b == black

def test_a_stripe_pattern_is_constant_in_y():
    pattern = StripePattern(white, black)
    assert pattern.pattern_at(point(0, 0, 0)) == white
    assert pattern.pattern_at(point(0, 1, 0)) == white
    assert pattern.pattern_at(point(0, 2, 0)) == white

def test_a_stripe_pattern_is_constant_in_b():
    pattern = StripePattern(white, black)
    assert pattern.pattern_at(point(0, 0, 0)) == white
    assert pattern.pattern_at(point(0, 0, 1)) == white
    assert pattern.pattern_at(point(0, 0, 2)) == white

def test_a_stripe_alternates_in_x():
    pattern = StripePattern(white, black)
    assert pattern.pattern_at(point(0.0,  0, 0)) == white
    assert pattern.pattern_at(point(0.9,  0, 0)) == white
    assert pattern.pattern_at(point(1.0,  0, 0)) == black
    assert pattern.pattern_at(point(-0.1, 0, 0)) == black
    assert pattern.pattern_at(point(-1.0, 0, 0)) == black
    assert pattern.pattern_at(point(-1.1, 0, 0)) == white

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
    c = pattern.pattern_at_shape(object, point(1.5, 0, 0))
    assert c == white

def test_stripes_with_a_pattern_transformation():
    object = Sphere()
    pattern = StripePattern(white, black)
    pattern.set_pattern_transform(scaling(2, 2, 2))
    c = pattern.pattern_at_shape(object, point(1.5, 0, 0))
    assert c == white

def test_stripes_with_both_an_object_and_a_pattern_transformation():
    object = Sphere()
    object.set_transform(scaling(2, 2, 2))
    pattern = StripePattern(white, black)
    pattern.set_pattern_transform(translation(0.5, 0, 0))
    c = pattern.pattern_at_shape(object, point(2.5, 0, 0))
    assert c == white

def test_the_default_pattern_transformation():
    pattern = MyTestPattern()
    assert pattern.transform == I

def test_assigning_a_transformation():
    pattern = MyTestPattern()
    pattern.set_pattern_transform(translation(1, 2, 3))
    assert pattern.transform == translation(1, 2, 3)

def test_a_pattern_with_an_object_transformation():
    shape = Sphere()
    shape.set_transform(scaling(2, 2, 2))
    pattern = MyTestPattern()
    c = pattern.pattern_at_shape(shape, point(2, 3, 4))
    assert c == Color(1, 1.5, 2)

def test_a_pattern_with_a_pattern_transformation():
    shape = Sphere()
    pattern = MyTestPattern()
    pattern.set_pattern_transform(scaling(2, 2, 2))
    c = pattern.pattern_at_shape(shape, point(2, 3, 4))
    assert c == Color(1, 1.5, 2)

def test_a_pattern_with_both_an_object_and_a_pattern_transformation():
    shape = Sphere()
    shape.set_transform(scaling(2, 2, 2))
    pattern = MyTestPattern()
    pattern.set_pattern_transform(translation(0.5, 1, 1.5))
    c = pattern.pattern_at_shape(shape, point(2.5, 3, 3.5))
    assert c == Color(0.75, 0.5, 0.25)