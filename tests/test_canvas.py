from raytracer.canvas import canvas
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


def test_creating_a_canvas():
    c = canvas(10, 20)
    assert c.width == 10
    assert c.height == 20
    for y in range(c.height):
        for x in range(c.width):
            assert c.pixel_at(x, y) == Color(0, 0, 0)


def test_writing_pixels_to_a_canvas():
    c = canvas(10, 20)
    red = Color(1, 0, 0)
    c.write_pixel(2, 3, red)
    assert c.pixel_at(2, 3) == red


def test_constructing_the_PPM_header():
    c = canvas(5, 3)
    ppm = c.to_ppm()
    lines = ppm.splitlines()
    assert lines[0] == "P3"
    assert lines[1] == "5 3"
    assert lines[2] == "255"


def test_constructing_the_PPM_pixel_data():
    c = canvas(5, 3)
    c1 = Color(1.5, 0, 0)
    c2 = Color(0, 0.5, 0)
    c3 = Color(-0.5, 0, 1)
    c.write_pixel(0, 0, c1)
    c.write_pixel(2, 1, c2)
    c.write_pixel(4, 2, c3)
    ppm = c.to_ppm()
    lines_4_to_6 = "\n".join(ppm.splitlines()[3:])
    assert (
        lines_4_to_6
        == """255 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 128 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 255"""
    )
