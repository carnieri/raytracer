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
from raytracer.lights import PointLight
from raytracer.util import equal 

def test_a_point_light_has_a_position_and_intensity():
    intensity = Color(1, 1, 1)
    position = point(0, 0, 0)
    light = PointLight(position, intensity)
    assert light.position == position
    assert light.intensity == intensity
