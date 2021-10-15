from math import pi, sqrt, sin, cos

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
    view_transform
)
from raytracer.rays import Ray
from raytracer.spheres import Sphere
from raytracer.planes import Plane
from raytracer.lights import PointLight
from raytracer.materials import Material, lighting
from raytracer.camera import Camera
from raytracer.world import World, default_world


def render():
    floor = Plane()
    # floor.transform = scaling(10, 0.01, 10)
    # floor.material = Material()
    # floor.material.color = Color(1, 0.9, 0.9)
    # floor.material.specular = 0

    ceiling = Plane()
    ceiling.transform = translation(0, 15, 0)
    ceiling.material = Material()
    ceiling.material.color = Color(0.1, 0.1, 0.5)
    ceiling.material.ambient = 0.9
    ceiling.material.diffuse = 1
    ceiling.material.specular = 0

    left_wall = Plane()
    left_wall.transform = translation(0, 0, 5) @ rotation_y(-pi/4) @ rotation_x(pi/2)
    left_wall.material = Material()
    left_wall.material.color = Color(1.0, 0.2, 0.2)
    left_wall.material.specular = 0
    # right_wall = Sphere()
    # right_wall.transform = translation(0, 0, 5) @ rotation_y(pi/4) @ rotation_x(pi/2) @ scaling(10, 0.01, 10)
    # right_wall.material = floor.material


    # create objects that will be in the scene
    
    middle = Sphere()
    middle.transform = translation(-0.5, 0, 0.5)
    middle.material = Material()
    middle.material.color = Color(0.1, 1, 0.5)
    middle.material.diffuse = 0.7
    middle.material.specular = 0.3

    right = Sphere()
    right.transform = translation(1.5, 0.5, -0.5) @ scaling(0.5, 0.5, 0.5)
    right.material = Material()
    right.material.color = Color(0.5, 1, 0.1)
    right.material.diffuse = 0.7
    right.material.specular = 0.3

    left = Sphere()
    left.transform = translation(-1.5, 0.33, -0.75) @ scaling(0.33, 0.33, 0.33)
    left.material = Material()
    left.material.color = Color(1, 0.8, 0.1)
    left.material.diffuse = 0.7
    left.material.specular = 0.3

    # create world
    world = World()
    world.light = PointLight(point(-10, 10, -10), Color(1, 1, 1))
    world.add_object(floor)
    world.add_object(ceiling)
    # world.add_object(left_wall)
    # world.add_object(right_wall)
    world.add_object(middle)
    world.add_object(right)
    world.add_object(left)

    for i in range(30):
        s = Sphere()
        s.transform = translation(-2.0, cos(i)+0.5, i) @ scaling(0.33, 0.33, 0.33)
        s.material = Material()
        s.material.color = Color(0.7, 0.1, 0.1)
        s.material.diffuse = 0.7
        s.material.specular = 0.3
        world.add_object(s)

    # create camera
    scale = 4
    camera = Camera(100*scale, 50*scale, pi/3)
    camera.transform = view_transform(
        point(0, 1.5, -5),
        point(0, 1, 0),
        vector(0, 1, 0)
    )

    # render
    image = camera.render(world, verbose=True)
    return image

render().save("chapter9_planes.ppm")
