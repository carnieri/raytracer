from dataclasses import dataclass, field
from math import pi, sqrt, tan

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
)
from raytracer.rays import Ray
from raytracer.canvas import canvas
from raytracer.world import World, default_world, shade_hit, color_at


class Camera:
    def __init__(self, hsize, vsize, field_of_view):
        self.hsize = hsize
        self.vsize = vsize
        self.field_of_view = field_of_view
        self.transform = I

        # calculate pixel size
        half_view = tan(self.field_of_view / 2)
        aspect = float(self.hsize) / self.vsize
        if aspect >= 1:
            self.half_width = half_view
            self.half_height = half_view / aspect
        else:
            self.half_width = half_view * aspect
            self.half_height = half_view
        self.pixel_size = (self.half_width * 2) / self.hsize

    def __eq__(self, other):
        return (
            self.hsize == other.hsize and
            self.vsize == other.vsize and
            equal(self.field_of_view, other.field_of_view) and
            self.transform == other.transform
        )

    def ray_for_pixel(self, px, py):
        # the offset from the edge of the canvas to the pixel's center
        xoffset = (px + 0.5) * self.pixel_size
        yoffset = (py + 0.5) * self.pixel_size

        # the untrasformed coordinates of the pixel in world space.
        # (remember that the camera looks toward -z, so +x is to the left.)
        world_x = self.half_width - xoffset
        world_y = self.half_height - yoffset

        # using the camera matrix, transform the canvas point and the origin,
        # and then compute the ray's direction vector.
        # (remember that the canvas is at z=-1)
        pixel = self.transform.inverse() * point(world_x, world_y, -1)
        origin = self.transform.inverse() * point(0, 0, 0)
        direction = normalize(pixel - origin)
        return Ray(origin, direction)

    def render(self, world, verbose=False):
        image = canvas(self.hsize, self.vsize)
        for y in range(self.vsize):
            if verbose and y % 10 == 0:
                print(f'rendering line {y+1} of {self.vsize}')
            for x in range(self.hsize):
                ray = self.ray_for_pixel(x, y)
                color = color_at(world, ray)
                image.write_pixel(x, y, color)
        return image

