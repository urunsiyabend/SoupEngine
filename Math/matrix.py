from enum import Enum


class MatrixType(Enum):
    IDENTITY = 0
    ZEROS = 1
    ONES = 2


class Matrix4:
    def __init__(self, m_type: MatrixType = None):
        self._m = [[0.0 for i in range(4)] for j in range(4)]
        if m_type == MatrixType.IDENTITY:
            self.m = self.__identity()
        if m_type == MatrixType.ZEROS:
            pass
        if m_type == MatrixType.ONES:
            self.__ones()

    def __mul__(self, other):
        res = Matrix4()

        for i in range(len(self.m)):
            for j in range(len(self.m[0])):
                res.change(i, j,
                           self.at(i, 0) * other.at(0, j) +
                           self.at(i, 1) * other.at(1, j) +
                           self.at(i, 2) * other.at(2, j) +
                           self.at(i, 3) * other.at(3, j))

        return res

    @property
    def shape(self) -> tuple:
        return len(self.m), len(self.m[0])

    @property
    def m(self) -> list:
        return self._m

    @m.setter
    def m(self, value) -> None:
        self._m = value

    def __identity(self):
        res = Matrix4()

        r, c = self.shape
        for i in range(r):
            for j in range(c):
                if i == j:
                    res.change(i, j, 1.0)

        return res.m

    def __ones(self):
        res = Matrix4()
        r, c = self.shape
        for i in range(r):
            for j in range(c):
                res.change(i, j, 1)

        return res

    def at(self, x: int, y: int):
        return self.m[x][y]

    def change(self, x: int, y: int, value: float) -> None:
        self.m[x][y] = value
