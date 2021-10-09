from raytracer.canvas import canvas
from raytracer.tuple import tuple, point, vector, magnitude, normalize, dot, cross, color
from raytracer.util import equal 


def test_creating_a_canvas():
    c = canvas(10, 20)
    assert c.width == 10
    assert c.height == 20
    for y in range(c.height):
        for x in range(c.width):
            assert c.pixel_at(x, y) == color(0, 0, 0)