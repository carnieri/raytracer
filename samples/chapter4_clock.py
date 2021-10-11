from math import pi, sqrt

from raytracer.tuple import (
    tuple,
    point,
    vector,
    magnitude,
    normalize,
    dot,
    cross,
    color,
)
from raytracer.canvas import canvas
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

origin = point(0, 0, 0) # middle of the canvas
twelve = point(0, 0, 1)
angles = [k * pi/6 for k in range(12)]
hours = [rotation_y(r) * twelve for r in angles]

canvas_size = 100
c = canvas(canvas_size, canvas_size)
canvas_x_center = canvas_size // 2
canvas_y_center= canvas_size // 2
clock_radius = 3 * canvas_size / 8
mycolor = color(127, 127, 0)
for hour in hours:
    x = round(hour.x * clock_radius)
    y = round(hour.z * clock_radius)
    x += canvas_x_center
    y += canvas_y_center
    y = canvas_size - y
    c.write_pixel(x, y, mycolor)
c.save("chapter4_clock.ppm")
