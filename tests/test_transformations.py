from math import pi, sqrt

from raytracer.tuple import (
    tuple,
    point,
    vector,
    magnitude,
    normalize,
    dot,
    cross,
    color,
)
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

def test_multiplying_by_a_translation_matrix():
    transform = translation(5, -3, 2)
    p = point(-3, 4, 5)
    assert transform * p == point(2, 1, 7)

def test_multiplying_by_the_inverse_of_a_translation_matrix():
    transform = translation(5, -3, 2)
    inv = transform.inverse()
    p = point(-3, 4, 5)
    assert inv * p == point(-8, 7, 3)

def test_translation_does_not_affect_vectors():
    transform = translation(5, -3, 2)
    v = vector(-3, 4, 5)
    assert transform * v == v

def test_a_scaling_matrix_applied_to_a_point():
    transform = scaling(2, 3, 4)
    p = point(-4, 6, 8)
    assert transform * p == point(-8, 18, 32)

def test_reflection_is_scaling_by_a_negative_value():
    transform = scaling(-1, 1, 1)
    p = point(2, 3, 4)
    assert transform * p == point(-2, 3, 4)

def test_rotating_a_point_around_the_x_axis():
    p = point(0, 1, 0)
    half_quarter = rotation_x(pi / 4)
    full_quarter = rotation_x(pi / 2)
    assert half_quarter * p == point(0, sqrt(2)/2, sqrt(2)/2)
    assert full_quarter * p == point(0, 0, 1)

def test_rotating_a_point_around_the_y_axis():
    p = point(0, 0, 1)
    half_quarter = rotation_y(pi / 4)
    full_quarter = rotation_y(pi / 2)
    assert half_quarter * p == point(sqrt(2)/2, 0, sqrt(2)/2)
    assert full_quarter * p == point(1, 0, 0)

def test_rotating_a_point_around_the_z_axis():
    p = point(0, 1, 0)
    half_quarter = rotation_z(pi / 4)
    full_quarter = rotation_z(pi / 2)
    assert half_quarter * p == point(-sqrt(2)/2, sqrt(2)/2, 0)
    assert full_quarter * p == point(-1, 0, 0)

def test_a_shearing_transformation_moves_x_in_proportion_to_y():
    transform = shearing(1, 0, 0, 0, 0, 0)
    p = point(2, 3, 4)
    assert transform * p == point(5, 3, 4)

def test_a_shearing_transformation_moves_x_in_proportion_to_z():
    transform = shearing(0, 1, 0, 0, 0, 0)
    p = point(2, 3, 4)
    assert transform * p == point(6, 3, 4)

def test_a_shearing_transformation_moves_y_in_proportion_to_x():
    transform = shearing(0, 0, 1, 0, 0, 0)
    p = point(2, 3, 4)
    assert transform * p == point(2, 5, 4)

def test_a_shearing_transformation_moves_y_in_proportion_to_z():
    transform = shearing(0, 0, 0, 1, 0, 0)
    p = point(2, 3, 4)
    assert transform * p == point(2, 7, 4)

def test_a_shearing_transformation_moves_z_in_proportion_to_x():
    transform = shearing(0, 0, 0, 0, 1, 0)
    p = point(2, 3, 4)
    assert transform * p == point(2, 3, 6)

def test_a_shearing_transformation_moves_z_in_proportion_to_y():
    transform = shearing(0, 0, 0, 0, 0, 1)
    p = point(2, 3, 4)
    assert transform * p == point(2, 3, 7)

def test_individual_transformations_are_applied_in_sequence():
    p = point(1, 0, 1)
    A = rotation_x(pi / 2)
    B = scaling(5, 5, 5)
    C = translation(10, 5, 7)
    # apply rotation first
    p2 = A * p
    assert p2 == point(1, -1, 0)
    # then apply scaling
    p3 = B * p2
    assert p3 == point(5, -5, 0)
    # then apply translation
    p4 = C * p3
    assert p4 == point(15, 0, 7)

def test_chained_transformations_must_be_applied_in_reverse_order():
    p = point(1, 0, 1)
    A = rotation_x(pi / 2)
    B = scaling(5, 5, 5)
    C = translation(10, 5, 7)
    T = C @ B @ A
    assert T * p == point(15, 0, 7)