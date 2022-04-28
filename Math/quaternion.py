from Math.vector import Vector3


class Quaternion:
    def __init__(self, x: float, y: float, z: float, w: float):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def __mul__(self, other):
        if isinstance(other, Quaternion):
            w_: float = self.w * other.w - self.x * other.x - self.y * other.y - self.z * other.z
            x_: float = self.x * other.w + self.w * other.x + self.y * other.z - self.z * other.y
            y_: float = self.y * other.w + self.w * other.y + self.z * other.x - self.x * other.z
            z_: float = self.z * other.w + self.w * other.z + self.x * other.y - self.y * other.x
        elif isinstance(other, Vector3):
            w_: float = -self.x * other.x - self.y * other.y - self.z * other.z
            x_: float = self.w * other.x + self.y * other.z - self.z * other.y
            y_: float = self.w * other.y + self.z * other.x - self.x * other.z
            z_: float = self.w * other.z + self.x * other.y - self.y * other.x
        else:
            raise TypeError("Invalid multiplier type")

        return Quaternion(x_, y_, z_, w_)

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, value) -> None:
        self._x = value

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, value) -> None:
        self._y = value

    @property
    def z(self) -> float:
        return self._z

    @z.setter
    def z(self, value) -> None:
        self._z = value

    @property
    def w(self) -> float:
        return self._w

    @w.setter
    def w(self, value) -> None:
        self._w = value

    @property
    def length(self):
        return (self.x * self.x +
                self.y * self.y +
                self.z * self.z +
                self.w * self.w) ** .5

    def normalize(self):
        return Quaternion(
            self.x / self.length,
            self.y / self.length,
            self.z / self.length,
            self.w / self.length
        )

    def conjugate(self):
        return Quaternion(-self.x, -self.y, -self.z, self.w)
