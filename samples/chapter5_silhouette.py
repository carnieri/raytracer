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


def render(shape):
    canvas_pixels = 100
    ray_origin = point(0, 0, -5)
    wall_z = 10
    wall_size = 7
    pixel_size = wall_size / canvas_pixels
    half = wall_size / 2

    c = canvas(canvas_pixels, canvas_pixels)
    color = Color(1, 0, 0)

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
            if hit(xs) is not None:
                c.write_pixel(x, y, color)
    return c

shape = Sphere()
render(shape).save("chapter5_silhouette_1.ppm")

shape.set_transform(scaling(1, 0.5, 1))
render(shape).save("chapter5_silhouette_2.ppm")

shape.set_transform(scaling(0.5, 1, 1))
render(shape).save("chapter5_silhouette_3.ppm")

shape.set_transform(rotation_z(pi / 4) * scaling(0.5, 1, 1))
render(shape).save("chapter5_silhouette_4.ppm")

shape.set_transform(shearing(1,0,0,0,0,0) * scaling(0.5, 1, 1))
render(shape).save("chapter5_silhouette_5.ppm")
