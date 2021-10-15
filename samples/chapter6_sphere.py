from math import pi, sqrt

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
from raytracer.rays import Ray
from raytracer.spheres import Sphere
from raytracer.intersections import Intersection, intersections, hit
from raytracer.lights import PointLight
from raytracer.materials import Material, lighting


def render(shape):
    canvas_pixels = 400
    ray_origin = point(0, 0, -5)
    wall_z = 10
    wall_size = 7
    pixel_size = wall_size / canvas_pixels
    half = wall_size / 2

    light_position = point(-10, 10, -10)
    light_color = Color(1, 1, 1)
    light = PointLight(light_position, light_color)

    c = canvas(canvas_pixels, canvas_pixels)

    # for each row of pixels in the canvas
    for y in range(canvas_pixels):
        # compute the world y coordinate (top = +half, bottom = -half)
        world_y = half - pixel_size * y
        
        # for each pixel in the row
        for x in range(canvas_pixels):
            # compute the world x coordinate (left = -half, right = half)
            world_x = -half + pixel_size * x

            # describe the point on the wall that the ray will target
            position = point(world_x, world_y, wall_z)
            r = Ray(ray_origin, normalize(position - ray_origin))
            xs = shape.intersect(r)
            myhit = hit(xs)
            if myhit is not None:
                hitpoint = r.position(myhit.t)
                normal = myhit.object.normal_at(hitpoint)
                eye = -r.direction
                in_shadow = False
                color = lighting(myhit.object.material, light, hitpoint, eye, normal, in_shadow)
                c.write_pixel(x, y, color)
    return c

shape = Sphere()
shape.material.color = Color(0.2, 1, 1)
render(shape).save("chapter6_sphere.ppm")

