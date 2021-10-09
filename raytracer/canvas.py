from raytracer.tuple import color

class canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = [[color(0,0,0) for x in range(width)] for y in range(height)]

    def pixel_at(self, x, y):
        return self.data[y][x]

    def write_pixel(self, x, y, c):
        self.data[y][x] = c
