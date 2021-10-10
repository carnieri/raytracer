from raytracer.tuple import color


def convert_range(p):
    """Convert a float from 0-1 range to integer 0-255 range."""
    return max(0, min(255, round(255 * p)))


class canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = [[color(0, 0, 0) for x in range(width)] for y in range(height)]

    def pixel_at(self, x, y):
        return self.data[y][x]

    def write_pixel(self, x, y, c):
        self.data[y][x] = c

    def to_ppm(self):
        ppm = f"P3\n{self.width} {self.height}\n255\n"
        line_txts = []
        for y in range(self.height):
            pixel_txts = []
            for x in range(self.width):
                c = self.pixel_at(x, y)
                r = convert_range(c.r)
                g = convert_range(c.g)
                b = convert_range(c.b)
                pixel_txt = f"{r} {g} {b}"
                pixel_txts.append(pixel_txt)
            line_txt = " ".join(pixel_txts)
            line_txts.append(line_txt)
        ppm += "\n".join(line_txts) + "\n"
        # TODO: no line in a PPM file should be more than 70 characters long
        return ppm

    def save(self, filename):
        with open(filename, "wb") as fd:
            fd.write(self.to_ppm().encode())
