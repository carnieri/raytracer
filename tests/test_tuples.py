from raytracer.tuple import tuple, point, vector, magnitude, normalize, dot, cross, Color
from raytracer.util import equal 

def test_tuple_to_list():
    a = tuple(4.3, -4.2, 3.1, 1.0)
    assert a.to_list() == [4.3, -4.2, 3.1, 1.0]

def test_a_tuple_with_w_equal_1_is_a_point():
    a = tuple(4.3, -4.2, 3.1, 1.0)
    assert a.x == 4.3
    assert a.y == -4.2
    assert a.z == 3.1
    assert a.w == 1.0
    assert a.is_point() == True
    assert a.is_vector() == False

def test_a_tuple_with_w_equal_0_is_a_vector():
    a = tuple(4.3, -4.2, 3.1, 0.0)
    assert a.x == 4.3
    assert a.y == -4.2
    assert a.z == 3.1
    assert a.w == 0.0
    assert a.is_point() == False
    assert a.is_vector() == True

def test_point_creates_tuples_with_w_equal_1():
    p = point(4, -4, 3)
    assert p == tuple(4, -4, 3, 1)

def test_vector_creates_tuples_with_w_equal_0():
    v = vector(4, -4, 3)
    assert v == tuple(4, -4, 3, 0)

def test_adding_two_tuples():
    a1 = tuple(3, -2, 5, 1)
    a2 = tuple(-2, 3, 1, 0)
    assert a1 + a2 == tuple(1, 1, 6, 1)

def test_subtracting_two_points():
    p1 = point(3, 2, 1)
    p2 = point(5, 6, 7)
    assert p1 - p2 == vector(-2, -4, -6)

def test_subtracting_two_vectors():
    v1 = vector(3, 2, 1)
    v2 = vector(5, 6, 7)
    assert v1 - v2 == vector(-2, -4, -6)

def test_subtracting_a_vector_from_the_zero_vector():
    zero = vector(0, 0, 0)
    v = vector(1, -2, 3)
    assert zero -v == vector(-1, 2, -3)

def test_negating_a_tuple():
    a = tuple(1, -2, 3, -4)
    assert -a == tuple(-1, 2, -3, 4)

def test_multiplying_a_tuple_by_a_scalar():
    a = tuple(1, -2, 3, -4)
    assert a * 3.5 == tuple(3.5, -7, 10.5, -14)

def test_multiplying_a_tuple_by_a_fraction():
    a = tuple(1, -2, 3, -4)
    assert a * 0.5 == tuple(0.5, -1, 1.5, -2)

def test_dividing_a_tuple_by_a_scalar():
    a = tuple(1, -2, 3, -4)
    assert a / 2 == tuple(0.5, -1, 1.5, -2)

def test_computing_the_magnitude_of_vector_1_0_0():
    v = vector(1, 0, 0)
    assert magnitude(v) == 1

def test_normalizing_vector_4_0_0_gives_1_0_0():
    v = vector(4, 0, 0)
    assert normalize(v) == vector(1, 0, 0)

def test_dot_product_of_two_tuples():
    a = vector(1, 2, 3)
    b = vector(2, 3, 4)
    assert equal(dot(a, b), 20)

def test_cross_product_of_two_vectors():
    a = vector(1, 2, 3)
    b = vector(2, 3, 4)
    assert cross(a, b) == vector(-1, 2, -1)
    assert cross(b, a) == vector(1, -2, 1)

def test_colors_are_red_green_blue_tuples():
    c = Color(-0.5, 0.4, 1.7)
    assert equal(c.r, -0.5)
    assert equal(c.g, 0.4)
    assert equal(c.b, 1.7)

def test_adding_colors():
    c1 = Color(0.9, 0.6, 0.75)
    c2 = Color(0.7, 0.1, 0.25)
    assert c1 + c2 == Color(1.6, 0.7, 1.0)

def test_subtracting_colors():
    c1 = Color(0.9, 0.6, 0.75)
    c2 = Color(0.7, 0.1, 0.25)
    assert c1 - c2 == Color(0.2, 0.5, 0.5)

def test_multiplying_a_color_by_a_scalar():
    c = Color(0.2, 0.3, 0.4)
    assert c * 2 == Color(0.4, 0.6, 0.8)

def test_multiplying_colors():
    c1 = Color(1, 0.2, 0.4)
    c2 = Color(0.9, 1, 0.1)
    assert c1 * c2 == Color(0.9, 0.2, 0.04)
