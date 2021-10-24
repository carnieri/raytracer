from typing import List

from raytracer.tuple import tuple
from raytracer.util import equal


class Matrix:
    def __init__(self, data: List[List]):
        self.data = data
        self.cached_inverse = None
        self.cached_transpose = None

    def __getitem__(self, key):
        r, c = key
        return self.data[r][c]

    def __setitem__(self, key, value):
        r, c = key
        self.data[r][c] = value

    def rows(self):
        return len(self.data)

    def cols(self):
        return len(self.data[0])

    def __eq__(self, other):
        if self.rows() != other.rows():
            return False
        if self.cols() != other.cols():
            return False
        ret = True
        for i in range(self.rows()):
            for j in range(self.cols()):
                ret = ret and (equal(self[i, j], other[i, j]))
        return ret

    def __str__(self):
        lines = []
        for row in self.data:
            line = " | ".join([str(x) for x in row])
            lines.append(line)
        return "\n".join(lines)

    def copy(self):
        """Return a copy of the matrix."""
        new_data = [
            [self[r, c] for c in range(self.cols())] for r in range(self.rows())
        ]
        M = Matrix(new_data)
        return M

    def __matmul__(self, other):
        A = self
        B = other
        assert A.cols() == B.rows()
        M = A.copy()  # to get a new matrix with correct shape
        for i in range(M.rows()):
            for j in range(M.cols()):
                M[i, j] = 0
                for k in range(A.cols()):
                    M[i, j] += A[i, k] * B[k, j]
        return M

    def __mul__(self, other):
        if isinstance(other, tuple):
            assert self.cols() == 4  # tuples always have length 4
            tuple_vals = other.to_list()
            result_lst = [0 for r in range(self.cols())]
            for i in range(self.rows()):
                for j in range(self.cols()):
                    result_lst[i] += self[i, j] * tuple_vals[j]
            return tuple(*result_lst)
        elif isinstance(other, Matrix):
            return self @ other
        else:
            raise Exception("case not implemented")

    def clone(self):
        T = self.copy()
        T.cached_inverse = None
        return T

    def transpose(self):
        if self.cached_transpose is not None:
            return self.cached_transpose
        T = self.clone()
        for i in range(self.rows()):
            for j in range(self.cols()):
                T[i, j] = self[j, i]
        self.cached_transpose = T
        return T

    def determinant(self):
        # determinant is only defined for square matrices
        assert self.rows() == self.cols()
        if self.rows() == 2:
            a, b = self[0, 0], self[0, 1]
            c, d = self[1, 0], self[1, 1]
            return a * d - b * c
        else:
            # we arbitrarily pick the first row, but any row would do
            i = 0
            det = 0
            for j in range(self.cols()):
                det += self[i, j] * self.cofactor(i, j)
            return det

    def size(self):
        return self.rows(), self.cols()

    def submatrix(self, i, j):
        S = self.clone()
        # for every row, delete column j
        for r in range(S.rows()):
            del S.data[r][j]
        # delete row i
        del S.data[i]
        return S

    def minor(self, i, j):
        S = self.submatrix(i, j)
        return S.determinant()

    def cofactor(self, i, j):
        if (i + j) % 2 == 0:
            sign = 1
        else:
            sign = -1
        return self.minor(i, j) * sign

    def invertible(self):
        det = self.determinant()
        if det == 0:
            # TODO: maybe for stability the equality test needs to be: equal(det, 0)
            return False
        else:
            return True

    def inverse(self):
        if self.cached_inverse is not None:
            return self.cached_inverse
        # assert self.invertible()
        det = self.determinant()
        assert det != 0
        M2 = self.clone()
        for i in range(self.rows()):
            for j in range(self.cols()):
                c = self.cofactor(i, j)
                M2[j, i] = c / det
        self.cached_inverse = M2
        return M2


def identity(size):
    data = [[0 for col in range(size)] for row in range(size)]
    M = Matrix(data)
    for i in range(size):
        M[i, i] = 1
    return M


I = identity(4)
