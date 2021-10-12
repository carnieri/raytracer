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
from raytracer.util import equal
from raytracer.matrices import Matrix, I


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

def test_multiplying_a_matrix_by_the_identity_matrix():
    A = Matrix(
        [[0,1,2,4],
         [1,2,4,8],
         [2,4,8,16],
         [4,8,16,32]]
    )
    assert A * I == A

def test_multiplying_the_identity_matrix_by_a_tuple():
    a = tuple(1, 2, 3, 4)
    assert I * a == a

def test_transposing_a_matrix():
    A = Matrix(
        [[0,9,3,0],
         [9,8,0,8],
         [1,8,5,3],
         [0,0,5,8]]
    )
    assert A.transpose() == Matrix(
        [[0,9,1,0],
         [9,8,8,0],
         [3,0,5,5],
         [0,8,3,8]]
    )

def test_transposing_the_identity_matrix():
    A = I.transpose()
    assert A == I

def test_caculating_the_determinant_of_a_2x2_matrix():
    A = Matrix(
        [[1,5],
         [-3,2]]
    )
    assert equal(A.determinant(), 17)

def test_a_submatrix_of_a_3x3_matrix_is_a_2x2_matrix():
    A = Matrix(
        [[1,5,0],
         [-3,2,7],
         [0,6,-3]]
    )
    assert A.submatrix(0, 2) == Matrix(
        [[-3,2],
         [0,6]]
    )

def test_a_submatrix_of_a_4x4_matrix_is_a_3x3_matrix():
    A = Matrix(
        [[-6,1,1,6],
         [-8,5,8,6],
         [-1,0,8,2],
         [-7,1,-1,1]]
    )
    assert A.submatrix(2, 1) == Matrix(
        [[-6,1,6],
         [-8,8,6],
         [-7,-1,1]]
    )

def test_calculating_a_minor_of_a_3x3_matrix():
    A = Matrix(
        [[3,5,0],
         [2,-1,-7],
         [6,-1,5]]
    )
    B = A.submatrix(1, 0)
    assert equal(B.determinant(), 25)
    assert equal(A.minor(1, 0), 25)

def test_calculating_a_cofactor_of_a_3x3_matrix():
    A = Matrix(
        [[3,5,0],
         [2,-1,-7],
         [6,-1,5]]
    )
    assert equal(A.minor(0, 0),    -12)
    assert equal(A.cofactor(0, 0), -12)
    assert equal(A.minor(1, 0),     25)
    assert equal(A.cofactor(1, 0), -25)

def test_calculating_the_determinant_of_a_3x3_matrix():
    A = Matrix(
        [[1,2,6],
         [-5,8,-4],
         [2,6,4]]
    )
    assert equal(A.cofactor(0, 0), 56)
    assert equal(A.cofactor(0, 1), 12)
    assert equal(A.cofactor(0, 2), -46)
    assert equal(A.determinant(), -196)

def test_calculating_the_determinant_of_a_4x4_matrix():
    A = Matrix(
        [[-2,-8,3,5],
         [-3,1,7,3],
         [1,2,-9,6],
         [-6,7,7,-9]]
    )
    assert equal(A.cofactor(0, 0), 690)
    assert equal(A.cofactor(0, 1), 447)
    assert equal(A.cofactor(0, 2), 210)
    assert equal(A.cofactor(0, 3), 51)
    assert equal(A.determinant(), -4071)

def test_testing_an_invertible_matrix_for_invertibility():
    A = Matrix(
        [[6,4,4,4],
         [5,5,7,6],
         [4,-9,3,-7],
         [9,1,7,-6]]
    )
    assert equal(A.determinant(), -2120)
    assert A.invertible()

def test_testing_a_noninvertible_matrix_for_invertibility():
    A = Matrix(
        [[-4,2,-2,-3],
         [9,6,2,6],
         [0,-5,1,-5],
         [0,0,0,0]]
    )
    assert equal(A.determinant(), 0)
    assert A.invertible() == False

def test_calculating_the_inverse_of_a_matrix():
    A = Matrix(
        [[-5,2,6,-8],
         [1,-5,1,8],
         [7,7,-6,-7],
         [1,-3,7,4]]
    )
    B = A.inverse()
    assert equal(A.determinant(), 532)
    assert equal(A.cofactor(2, 3), -160)
    assert equal(B[3,2], -160.0/532)
    assert equal(A.cofactor(3, 2), 105)
    assert equal(B[2,3], 105.0/532)
    assert B == Matrix(
        [[ 0.21805,  0.45113,  0.24060, -0.04511],
         [-0.80827, -1.45677, -0.44361,  0.52068],
         [-0.07895, -0.22368, -0.05263,  0.19737],
         [-0.52256, -0.81391, -0.30075,  0.30639]]
    )

def test_calculating_the_inverse_of_another_matrix():
    A = Matrix(
        [[8,-5,9,2],
         [7,5,6,1],
         [-6,0,9,6],
         [-3,0,-9,-4]]
    )
    assert A.inverse() == Matrix(
        [[-0.15385, -0.15385, -0.28205, -0.53846],
         [-0.07692,  0.12308,  0.02564,  0.03077],
         [ 0.35897,  0.35897,  0.43590,  0.92308],
         [-0.69231, -0.69231, -0.76923, -1.92308]]
    )

def test_calculating_the_inverse_of_a_third_matrix():
    A = Matrix(
        [[9, 3, 0, 9],
         [-5, -2, -6, -3],
         [-4, 9, 6, 4],
         [-7, 6, 6, 2]]
    )
    assert A.inverse() == Matrix(
        [[-0.04074, -0.07778, 0.14444, -0.22222],
         [-0.07778, 0.03333, 0.36667, -0.33333],
         [-0.02901, -0.14630, -0.10926, 0.12963],
         [0.17778, 0.06667, -0.26667, 0.33333]]
    )

def test_multiplying_a_product_by_its_inverse():
    A = Matrix(
        [[3, -9, 7, 3],
         [3, -8, 2, -9],
         [-4, 4, 4, 1],
         [-6, 5, -1, 1]]
    )
    B = Matrix(
        [[8, 2, 2, 2],
         [3, -1, 7, 0],
         [7, 0, 5, 4],
         [6, -2, 0, 5]]
    )
    C = A @ B
    assert C @ B.inverse() == A