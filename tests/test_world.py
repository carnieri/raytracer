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
from raytracer.world import World, default_world, shade_hit, color_at


def test_creating_a_world():
    w = World()
    assert w.objects == []
    assert w.light is None

def test_the_default_world():
    light = PointLight(point(-10, 10, -10), Color(1, 1, 1))
    s1 = Sphere()
    s1.material.color = Color(0.8, 1.0, 0.6)
    s1.material.diffuse = 0.7
    s1.material.specular = 0.2
    s2 = Sphere()
    s2.transform = scaling(0.5, 0.5, 0.5)
    w = default_world()
    assert w.light == light
    assert s1 in w.objects
    assert s2 in w.objects

def test_intersect_a_world_with_a_ray():
    w = default_world()
    r = Ray(point(0, 0, -5), vector(0, 0, 1))
    xs = w.intersect_world(r)
    assert len(xs) == 4
    assert equal(xs[0].t, 4)
    assert equal(xs[1].t, 4.5)
    assert equal(xs[2].t, 5.5)
    assert equal(xs[3].t, 6)

def test_shading_an_intersection():
    w = default_world()
    r = Ray(point(0, 0, -5), vector(0, 0, 1))
    shape = w.objects[0]
    i = Intersection(4, shape)
    comps = prepare_computations(i, r)
    c = shade_hit(w, comps)
    assert c == Color(0.38066, 0.47583, 0.2855)

def test_shading_an_intersection_from_the_inside():
    w = default_world()
    w.light = PointLight(point(0, 0.25, 0), Color(1, 1, 1))
    r = Ray(point(0, 0, 0), vector(0, 0, 1))
    shape = w.objects[1]
    i = Intersection(0.5, shape)
    comps = prepare_computations(i, r)
    c = shade_hit(w, comps)
    assert c == Color(0.90498, 0.90498, 0.90498)

def test_the_color_when_a_ray_misses():
    w = default_world()
    r = Ray(point(0, 0, -5), vector(0, 1, 0))
    c = color_at(w, r)
    assert c == Color(0, 0, 0)

def test_the_color_when_a_ray_hits():
    w = default_world()
    r = Ray(point(0, 0, -5), vector(0, 0, 1))
    c = color_at(w, r)
    c = Color(0.38066, 0.47583, 0.2855)

def test_the_color_with_an_intersectino_behind_the_ray():
    w = default_world()
    outer = w.objects[0]
    outer.material.ambient = 1
    inner = w.objects[1]
    inner.material.ambient = 1
    r = Ray(point(0, 0, 0.75), vector(0, 0, -1))
    c = color_at(w, r)
    assert c == inner.material.color

def test_there_is_no_shadow_when_nothing_is_collinear_with_point_and_light():
    w = default_world()
    p = point(0, 10, 0)
    assert w.is_shadowed(p) == False

def test_the_shadow_when_an_object_is_between_the_point_and_the_light():
    w = default_world()
    p = point(10, -10, 10)
    assert w.is_shadowed(p)

def test_there_is_no_shadow_when_an_object_is_behind_the_light():
    w = default_world()
    p = point(-20, 20, -20)
    assert w.is_shadowed(p) == False

def test_there_is_no_shadow_when_an_object_is_behind_the_point():
    w = default_world()
    p = point(-2, 2, -2)
    assert w.is_shadowed(p) == False

def test_shade_hit_is_given_an_intersection_in_shadow():
    w = World()
    w.light = PointLight(point(0, 0, -10), Color(1, 1, 1))
    s1 = Sphere()
    w.add_object(s1)
    s2 = Sphere()
    s2.set_transform(translation(0, 0, 10))
    w.add_object(s2)
    r = Ray(point(0, 0, 5), vector(0, 0, 1))
    i = Intersection(4, s2)
    comps = prepare_computations(i, r)
    c = shade_hit(w, comps)
    # only the ambient color of the second sphere should be returned
    assert c == Color(0.1, 0.1, 0.1)
