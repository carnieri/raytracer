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
from raytracer.rays import Ray
from raytracer.spheres import Sphere
from raytracer.intersections import Intersection, intersect, intersections, hit, prepare_computations
from raytracer.lights import PointLight
from raytracer.materials import Material, lighting
from raytracer.transformations import (
    translation,
    scaling,
    rotation_x,
    rotation_y,
    rotation_z,
    shearing,
)
from raytracer.util import equal 

class World:
    def __init__(self):
        self.objects = []
        self.light = None

    def add_object(self, obj):
        self.objects.append(obj)

    def intersect_world(self, ray):
        all_intersections = []
        for obj in self.objects:
            xs = intersect(obj, ray)
            all_intersections.extend(xs)
        all_intersections.sort(key=lambda x: x.t)
        return all_intersections

    
def default_world():
    light = PointLight(point(-10, 10, -10), Color(1, 1, 1))
    s1 = Sphere()
    s1.material.color = Color(0.8, 1.0, 0.6)
    s1.material.diffuse = 0.7
    s1.material.specular = 0.2
    s2 = Sphere()
    s2.transform = scaling(0.5, 0.5, 0.5)
    w = World()
    w.light = light
    w.add_object(s1)
    w.add_object(s2)
    return w

def shade_hit(world, comps):
    return lighting(
        comps.object.material,
        world.light,
        comps.point, comps.eyev, comps.normalv
    )

def color_at(world, ray):
    xs = world.intersect_world(ray)
    i = hit(xs)
    if i is None:
        return Color(0, 0, 0) # black
    else:
        comps = prepare_computations(i, ray)
        color = shade_hit(world, comps)
        return color
