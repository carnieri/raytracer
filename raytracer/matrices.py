from typing import List

from raytracer.tuple import tuple
from raytracer.util import equal


class Matrix:
    def __init__(self, data: List[List]):
        self.data = data

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
                ret = ret and (equal(self[i,j], other[i,j]))
        return ret
    
    def __str__(self):
        lines = []
        for row in self.data:
            line = " | ".join([str(x) for x in row])
            lines.append(line)
        return "\n".join(lines)

    def copy(self):
        """Return a copy of the matrix."""
        new_data = [[self[r,c] for c in range(self.cols())] for r in range(self.rows())]
        M = Matrix(new_data)
        return M

    def __matmul__(self, other):
        A = self
        B = other
        assert A.cols() == B.rows()
        M = A.copy()    # to get a new matrix with correct shape
        for i in range(M.rows()):
            for j in range(M.cols()):
                M[i,j] = 0
                for k in range(A.cols()):
                    M[i,j] += A[i,k] * B[k,j]
        return M

    def __mul__(self, other):
        if isinstance(other, tuple):
            assert self.cols() == 4 # tuples always have length 4
            tuple_vals = other.to_list()
            result_lst = [0 for r in range(self.cols())]
            for i in range(self.rows()):
                for j in range(self.cols()):
                    result_lst[i] += self[i,j] * tuple_vals[j]
            return tuple(*result_lst)
        else:
            raise Exception("case not implemented")