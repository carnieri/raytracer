from dataclasses import dataclass

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

@dataclass
class PointLight:
    position: tuple
    intensity: Color

