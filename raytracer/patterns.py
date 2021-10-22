from raytracer.tuple import Color, tuple
from raytracer.matrices import Matrix, I


class Pattern:
    def set_pattern_transform(self, transform: Matrix) -> None:
        self.transform = transform
    
    def pattern_at_shape(self, object, world_point):
        object_point = object.transform.inverse() * world_point
        pattern_point = self.transform.inverse() * object_point
        return self.pattern_at(pattern_point)
    

class MyTestPattern(Pattern):
    def __init__(self):
        self.set_pattern_transform(I)

    def pattern_at(self, point: tuple) -> Color:
        return Color(point.x, point.y, point.z)
