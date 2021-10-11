from math import cos, sin

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