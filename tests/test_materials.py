from math import sqrt

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
from raytracer.materials import Material, lighting
from raytracer.lights import PointLight
from raytracer.spheres import Sphere


def test_the_default_material():
    m = Material()
    assert m.color == Color(1, 1, 1)
    assert m.ambient == 0.1
    assert m.diffuse == 0.9
    assert m.specular == 0.9
    assert m.shininess == 200.0

def setup():
    m = Material()
    position = point(0, 0, 0)
    return m, position

def test_lighting_with_the_eye_between_the_light_and_the_surface():
    m, position = setup()
    eyev = vector(0, 0, -1)
    normalv = vector(0, 0, -1)
    light = PointLight(point(0, 0, -10), Color(1, 1, 1))
    in_shadow = False
    object = Sphere()
    result = lighting(m, object, light, position, eyev, normalv, in_shadow)
    assert result == Color(1.9, 1.9, 1.9)

def test_lighting_with_the_eye_between_light_and_surface_eye_offset_45_degrees():
    m, position = setup()
    eyev = vector(0, sqrt(2)/2, -sqrt(2)/2)
    normalv = vector(0, 0, -1)
    light = PointLight(point(0, 0, -10), Color(1, 1, 1))
    in_shadow = False
    object = Sphere()
    result = lighting(m, object, light, position, eyev, normalv, in_shadow)
    assert result == Color(1.0, 1.0, 1.0)

def test_lighting_with_eye_opposite_surface_light_offset_45_degrees():
    m, position = setup()
    eyev = vector(0, 0, -1)
    normalv = vector(0, 0, -1)
    light = PointLight(point(0, 10, -10), Color(1, 1, 1))
    in_shadow = False
    object = Sphere()
    result = lighting(m, object, light, position, eyev, normalv, in_shadow)
    assert result == Color(0.7364, 0.7364, 0.7364)

def test_lighting_with_eye_in_the_path_of_the_reflection_vector():
    m, position = setup()
    eyev = vector(0, -sqrt(2)/2, -sqrt(2)/2)
    normalv = vector(0, 0, -1)
    light = PointLight(point(0, 10, -10), Color(1, 1, 1))
    in_shadow = False
    object = Sphere()
    result = lighting(m, object, light, position, eyev, normalv, in_shadow)
    assert result == Color(1.6364, 1.6364, 1.6364)

def test_lighting_with_the_light_behind_the_surface():
    m, position = setup()
    eyev = vector(0, 0, -1)
    normalv = vector(0, 0, -1)
    light = PointLight(point(0, 0, 10), Color(1, 1, 1))
    in_shadow = False
    object = Sphere()
    result = lighting(m, object, light, position, eyev, normalv, in_shadow)
    assert result == Color(0.1, 0.1, 0.1)

def test_lighting_with_the_surface_in_shadow():
    m, position = setup()
    eyev = vector(0, 0, -1)
    normalv = vector(0, 0, -1)
    light = PointLight(point(0, 0, -10), Color(1, 1, 1))
    in_shadow = True
    object = Sphere()
    result = lighting(m, object, light, position, eyev, normalv, in_shadow)
    assert result == Color(0.1, 0.1, 0.1)
    