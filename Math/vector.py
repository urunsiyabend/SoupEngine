import math


class Vector2:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"<Vector2f> ({self.x:.2f}, {self.y:.2f})"

    def __add__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x + other.x, self.y + other.y)
        elif isinstance(other, (float, int)):
            return Vector2(self.x + other, self.y + other)

    def __sub__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x - other.x, self.y - other.y)
        elif isinstance(other, (float, int)):
            return Vector2(self.x - other, self.y - other)

    def __mul__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x * other.x, self.y * other.y)
        elif isinstance(other, (float, int)):
            return Vector2(self.x * other, self.y * other)

    def __div__(self, other):
        if isinstance(other, Vector2):
            return Vector2(self.x / other.x, self.y / other.y)
        elif isinstance(other, (float, int)):
            return Vector2(self.x / other, self.y / other)

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    @x.setter
    def x(self, value):
        self._x = value

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def length(self) -> float:
        return (self.x * self.x + self.y * self.y) ** .5

    def dot(self, o):
        return self.x * o.x + self.y * o.y

    def normalize(self):
        return Vector2(self.x / self.length, self.y / self.length)

    def rotate(self, angle: float):
        rad = math.radians(angle)
        cos = math.cos(rad)
        sin = math.sin(rad)

        return Vector2(self.x * cos - self.y * sin, self.x * sin + self.y * cos)


class Vector3:
    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"<Vector3f> ({self.x:.2f}, {self.y:.2f}, {self.z:.2f})"

    def __add__(self, other):
        if isinstance(other, Vector3):
            return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
        elif isinstance(other, (float, int)):
            return Vector3(self.x + other, self.y + other, self.z + other)

    def __sub__(self, other):
        if isinstance(other, Vector3):
            return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
        elif isinstance(other, (float, int)):
            return Vector3(self.x - other, self.y - other, self.z - other)

    def __mul__(self, other):
        if isinstance(other, Vector3):
            return Vector3(self.x * other.x, self.y * other.y, self.z * other.z)
        elif isinstance(other, (float, int)):
            return Vector3(self.x * other, self.y * other, self.z * other)

    def __div__(self, other):
        if isinstance(other, Vector3):
            return Vector3(self.x / other.x, self.y / other.y, self.z / other.z)
        elif isinstance(other, (float, int)):
            return Vector3(self.x / other, self.y / other, self.z / other)

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    @property
    def z(self):
        return self._z

    @x.setter
    def x(self, value):
        self._x = value

    @y.setter
    def y(self, value):
        self._y = value

    @z.setter
    def z(self, value):
        self._z = value

    @property
    def length(self) -> float:
        return (self.x * self.x + self.y * self.y + self.z * self.z) ** .5

    def dot(self, o):
        return self.x * o.x + self.y * o.y + self.z + o.z

    def cross(self, o):
        x_ = self.y * o.z - self.z * o.y
        y_ = self.z * o.x - self.x * o.z
        z_ = self.x * o.y - self.y * o.x

        return Vector3(x_, y_, z_)

    def normalize(self):
        return Vector3(self.x / self.length, self.y / self.length, self.z / self.length)

    def rotate(self, angle: float):
        # TODO: implement 3D rotation
        pass
