from math import pi, sqrt

from raytracer.camera import Camera
from raytracer.matrices import Matrix, I
from raytracer.util import equal 
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
from raytracer.transformations import (
    translation,
    scaling,
    rotation_x,
    rotation_y,
    rotation_z,
    shearing,
    view_transform
)
from raytracer.world import World, default_world, shade_hit, color_at


def test_constructing_a_camera():
    hsize = 160
    vsize = 120
    field_of_view = pi/2
    c = Camera(hsize, vsize, field_of_view)
    assert c.hsize == 160
    assert c.vsize == 120
    assert equal(c.field_of_view, pi/2)
    assert c.transform == I

def test_the_pixel_size_for_a_horizontal_canvas():
    c = Camera(200, 125, pi/2)
    assert equal(c.pixel_size, 0.01)

def test_the_pixel_size_for_a_vertical_canvas():
    c = Camera(125, 200, pi/2)
    assert equal(c.pixel_size, 0.01)

def test_constructing_a_ray_through_the_center_of_the_canvas():
    c = Camera(201, 101, pi/2)
    r = c.ray_for_pixel(100, 50)
    assert r.origin == point(0, 0, 0)
    assert r.direction == vector(0, 0, -1)

def test_constructing_a_ray_through_a_corner_of_the_canvas():
    c = Camera(201, 101, pi/2)
    r = c.ray_for_pixel(0, 0)
    assert r.origin == point(0, 0, 0)
    assert r.direction == vector(0.66519, 0.33259, -0.66851)

def test_constructing_a_ray_when_the_camera_is_transformed():
    c = Camera(201, 101, pi/2)
    c.transform = rotation_y(pi/4) @ translation(0, -2, 5)
    r = c.ray_for_pixel(100, 50)
    assert r.origin == point(0, 2, -5)
    assert r.direction == vector(sqrt(2)/2, 0, -sqrt(2)/2)

def test_rendering_a_world_with_a_camera():
    w = default_world()
    c = Camera(11, 11, pi/2)
    from_p = point(0, 0, -5)
    to_p = point(0, 0, 0)
    up = vector(0, 1, 0)
    c.transform = view_transform(from_p, to_p, up)
    image = c.render(w)
    assert image.pixel_at(5, 5) == Color(0.38066, 0.47583, 0.2855)
    