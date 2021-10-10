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
from raytracer.matrices import Matrix


def test_constructing_and_inspecting_a_4x4_matrix():
    M = Matrix(
        [[1,    2,    3,    4],
         [5.5,  6.5,  7.5,  8.5],
         [9,    10,   11,   12],
         [13.5, 14.5, 15.5, 16.5]]
    )
    assert equal(M[0,0], 1)
    assert equal(M[0,3], 4)
    assert equal(M[1,0], 5.5)
    assert equal(M[1,2], 7.5)
    assert equal(M[2,2], 11)
    assert equal(M[3,0], 13.5)
    assert equal(M[3,2], 15.5)

def test_a_2x2_matrix_ought_to_be_representable():
    M = Matrix(
        [[-3, 5],
         [1, -2]]
    )
    assert equal(M[0,0], -3)
    assert equal(M[0,1], 5)
    assert equal(M[1,0], 1)
    assert equal(M[1,1], -2)

def test_a_3x3_matrix_ought_to_be_representable():
    M = Matrix(
        [[-3, 5, 0],
         [1, -2, -7],
         [0, 1, 1]]
    )
    assert equal(M[0,0], -3)
    assert equal(M[1,1], -2)
    assert equal(M[2,2], 1)

def test_matrix_equality_with_identical_matrices():
    A = Matrix(
        [[1,2,3,4],
         [5,6,7,8],
         [9,8,7,6],
         [5,4,3,2]]
    )
    B = Matrix(
        [[1,2,3,4],
         [5,6,7,8],
         [9,8,7,6],
         [5,4,3,2]]
    )
    assert A == B

def test_matrix_equality_with_different_matrices():
    A = Matrix(
        [[1,2,3,4],
         [5,6,7,8],
         [9,8,7,6],
         [5,4,3,2]]
    )
    B = Matrix(
        [[2,3,4,5],
         [6,7,8,9],
         [8,7,6,5],
         [4,3,2,1]]
    )
    print(A)
    print(B)
    assert A != B

def test_multiplying_two_matrices():
    A = Matrix(
        [[1,2,3,4],
         [5,6,7,8],
         [9,8,7,6],
         [5,4,3,2]]
    )
    B = Matrix(
        [[-2,1,2,3],
         [3,2,1,-1],
         [4,3,6,5],
         [1,2,7,8]]
    )
    assert A @ B == Matrix(
        [[20,22,50,48],
         [44,54,114,108],
         [40,58,110,102],
         [16,26,46,42]]
    )

def test_a_matrix_multiplied_by_a_tuple():
    A = Matrix(
        [[1,2,3,4],
         [2,4,4,2],
         [8,6,4,1],
         [0,0,0,1]]
    )
    b = tuple(1, 2, 3, 1)
    assert A * b == tuple(18, 24, 33, 1)