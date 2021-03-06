from dataclasses import dataclass, field
from typing import Optional

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
from raytracer.lights import PointLight
from raytracer.patterns import Pattern

@dataclass
class Material:
    color: Color = field(default_factory=lambda: Color(1, 1, 1))
    ambient: float = 0.1
    diffuse: float = 0.9
    specular: float = 0.9
    shininess: float = 200.0
    pattern: Optional[Pattern] = None


black = Color(0, 0, 0)

def lighting(material, object, light: PointLight, point, eyev, normalv, in_shadow):
    if material.pattern is not None:
        color = material.pattern.pattern_at_shape(object, point)
    else:
        color = material.color
    # combine the surface color with the light's color/intensity
    effective_color = color * light.intensity

    # find the direction to the light source
    lightv = normalize(light.position - point)

    # compute the ambient contribution
    ambient = effective_color * material.ambient
    if in_shadow:
        return ambient

    # light_dot_normal: represents the cosine of the angle between the
    # light vector and the normal vector. A negative number means the
    # light is on the other side of the surface.
    light_dot_normal = dot(lightv, normalv)
    if light_dot_normal < 0:
        diffuse = black
        specular = black
    else:
        # compute the diffuse contribution
        diffuse = effective_color * material.diffuse * light_dot_normal

        # reflect_dot_eye represents the cosine of the angle between the
        # reflection vector and the eye vector. A negative number means the
        # light reflects away from the eye.
        reflectv = reflect(-lightv, normalv)
        reflect_dot_eye = dot(reflectv, eyev)
        if reflect_dot_eye <= 0:
            specular = black
        else:
            # compute the specular contribution
            factor = reflect_dot_eye ** material.shininess
            specular = light.intensity * material.specular * factor

    # Add the three contributions together to get the final shading

    return ambient + diffuse + specular
