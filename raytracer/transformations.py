from math import cos, sin

from raytracer.tuple import normalize, cross
from raytracer.matrices import Matrix

def translation(x, y, z):
    return Matrix(
        [[1, 0, 0, x],
         [0, 1, 0, y],
         [0, 0, 1, z],
         [0, 0, 0, 1]]
    )

def scaling(x, y, z):
    return Matrix(
        [[x, 0, 0, 0],
         [0, y, 0, 0],
         [0, 0, z, 0],
         [0, 0, 0, 1]]
    )

def rotation_x(r):
    return Matrix(
        [[1, 0, 0, 0],
         [0, cos(r), -sin(r), 0],
         [0, sin(r), cos(r), 0],
         [0, 0, 0, 1]]
    )

def rotation_y(r):
    return Matrix(
        [[cos(r), 0, sin(r), 0],
         [0, 1, 0, 0],
         [-sin(r), 0, cos(r), 0],
         [0, 0, 0, 1]]
    )

def rotation_z(r):
    return Matrix(
        [[cos(r), -sin(r), 0, 0],
         [sin(r), cos(r), 0, 0],
         [0, 0, 1, 0],
         [0, 0, 0, 1]]
    )

def shearing(xy, xz, yx, yz, zx, zy):
    return Matrix(
        [[1, xy, xz, 0],
         [yx, 1, yz, 0],
         [zx, zy, 1, 0],
         [0, 0, 0, 1]]
    )

def view_transform(from_p, to_p, up):
    forward = normalize(to_p - from_p)
    upn = normalize(up)
    left = cross(forward, upn)
    true_up = cross(left, forward)
    orientation = Matrix(
        [[left.x, left.y, left.z, 0],
         [true_up.x, true_up.y, true_up.z, 0],
         [-forward.x, -forward.y, -forward.z, 0],
         [0, 0, 0, 1]]
    )
    return orientation @ translation(-from_p.x, -from_p.y, -from_p.z)
