from dataclasses import dataclass

from raytracer.tuple import tuple, point, vector, magnitude, normalize, dot, cross
from raytracer.util import equal 


@dataclass
class Projectile:
    position: tuple # point
    velocity: tuple # vector

@dataclass
class Environment:
    gravity: tuple  # vector
    wind: tuple     # vector

def tick(env, proj):
    position = proj.position + proj.velocity
    velocity = proj.velocity + env.gravity + env.wind
    return Projectile(position, velocity)

# projectile starts one unit above the origin
p = Projectile(point(0, 1, 0), normalize(vector(1, 1, 0)))

# gravity -0.1 unit/tick, and wind is -0.01 unit/tick
e = Environment(vector(0, -0.1, 0), vector(-0.01, 0, 0))

i = 0
while p.position.y > 0:
    p = tick(e, p)
    print(f"iteration {i} {p}")
    i += 1