from dataclasses import dataclass

from raytracer.tuple import (
    tuple,
    point,
    vector,
    normalize,
    color,
)
from raytracer.canvas import canvas


@dataclass
class Projectile:
    position: tuple  # point
    velocity: tuple  # vector


@dataclass
class Environment:
    gravity: tuple  # vector
    wind: tuple  # vector


def tick(env, proj):
    position = proj.position + proj.velocity
    velocity = proj.velocity + env.gravity + env.wind
    return Projectile(position, velocity)


# projectile starts one unit above the origin
start = point(0, 1, 0)
velocity = normalize(vector(1, 1.8, 0)) * 11.25
p = Projectile(start, velocity)

# gravity -0.1 unit/tick, and wind is -0.01 unit/tick
gravity = vector(0, -0.1, 0)
wind = vector(-0.01, 0, 0)
e = Environment(gravity, wind)

c = canvas(900, 550)

i = 0
while p.position.y > 0:
    y = int(c.height - p.position.y)
    x = int(p.position.x)
    if x >= 0 and x < c.width and y >= 0 and y < c.height:
        mycolor = color(127, 0, 0)
        c.write_pixel(x, y, mycolor)
    p = tick(e, p)
    i += 1
c.save("chapter2_projectile.ppm")
