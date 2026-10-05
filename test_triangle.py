import math
import unittest

from triangle import get_triangle_info

UNKNOWN = (-2, -2)
ERROR = (-1, -1)


def _dist(p, q):
    return math.hypot(p[0] - q[0], p[1] - q[1])


class TestTriangleInfo(unittest.TestCase):

    def _assert_coords_valid(self, coords):
        self.assertEqual(len(coords), 3)
        for point in coords:
            self.assertIsInstance(point, tuple)
            self.assertEqual(len(point), 2)
            for value in point:
                self.assertIsInstance(value, int)
                self.assertGreaterEqual(value, 0)
                self.assertLessEqual(value, 100)

    def _assert_distances(self, coords, sides):
        scale = 80 / max(sides)
        expected = sorted(side * scale for side in sides)
        distances = sorted([
            _dist(coords[0], coords[1]),
            _dist(coords[1], coords[2]),
            _dist(coords[2], coords[0]),
        ])
        for got, exp in zip(distances, expected):
            self.assertLess(abs(got - exp), 1.5, msg=f"расстояние {got} != {exp}")

    def test_equilateral(self):
        kind, coords = get_triangle_info("5", "5", "5")
        self.assertEqual(kind, "равносторонний")
        self._assert_coords_valid(coords)
        self.assertEqual(len(set(coords)), 3)
        d = {round(_dist(coords[0], coords[1])), round(_dist(coords[1], coords[2])), round(_dist(coords[2], coords[0]))}
        self.assertEqual(len(d), 1, msg="у равностороннего все стороны равны")

    def test_equilateral_decimals(self):
        kind, _ = get_triangle_info("5.5", "5.5", "5.5")
        self.assertEqual(kind, "равносторонний")

    def test_equilateral_float_zero_suffix(self):
        kind, _ = get_triangle_info("5.0", "5", "5.00")
        self.assertEqual(kind, "равносторонний")

    def test_equilateral_scaling_fits_field(self):
        kind, coords = get_triangle_info("1000", "1000", "1000")
        self.assertEqual(kind, "равносторонний")
        self._assert_coords_valid(coords)

    def test_isosceles_1(self):
        kind, coords = get_triangle_info("3", "3", "2")
        self.assertEqual(kind, "равнобедренный")
        self._assert_coords_valid(coords)

    def test_isosceles_2(self):
        kind, _ = get_triangle_info("2", "5", "5")
        self.assertEqual(kind, "равнобедренный")

    def test_isosceles_3(self):
        kind, _ = get_triangle_info("6", "4", "6")
        self.assertEqual(kind, "равнобедренный")

    def test_scalene(self):
        kind, coords = get_triangle_info("3", "4", "5")
        self.assertEqual(kind, "разносторонний")
        self._assert_coords_valid(coords)
        self._assert_distances(coords, (3, 4, 5))

    def test_scalene_distances_scaled(self):
        kind, coords = get_triangle_info("6", "8", "10")
        self.assertEqual(kind, "разносторонний")
        self._assert_distances(coords, (6, 8, 10))

    def test_huge_numbers_fit_in_field(self):
        kind, coords = get_triangle_info("1000", "1500", "2000")
        self.assertEqual(kind, "разносторонний")
        self._assert_coords_valid(coords)

    def test_scientific_notation(self):
        kind, _ = get_triangle_info("1e2", "1e2", "1e2")
        self.assertEqual(kind, "равносторонний")

    def test_whitespace_padded_input(self):
        kind, _ = get_triangle_info(" 5 ", " 5\t", "5")
        self.assertEqual(kind, "равносторонний")

    def test_not_triangle_inequality(self):
        kind, coords = get_triangle_info("1", "1", "3")
        self.assertEqual(kind, "не треугольник")
        self.assertEqual(coords, [ERROR] * 3)

    def test_not_triangle_inequality_equality_boundary(self):
        kind, coords = get_triangle_info("1", "1", "2")
        self.assertEqual(kind, "не треугольник")
        self.assertEqual(coords, [ERROR] * 3)

    def test_not_triangle_zero_side(self):
        kind, coords = get_triangle_info("0", "2", "2")
        self.assertEqual(kind, "не треугольник")
        self.assertEqual(coords, [ERROR] * 3)

    def test_not_triangle_negative_side(self):
        kind, coords = get_triangle_info("-5", "6", "7")
        self.assertEqual(kind, "не треугольник")
        self.assertEqual(coords, [ERROR] * 3)

    def test_non_numeric_all(self):
        kind, coords = get_triangle_info("abc", "def", "ghi")
        self.assertEqual(kind, "")
        self.assertEqual(coords, [UNKNOWN] * 3)

    def test_non_numeric_one(self):
        kind, coords = get_triangle_info("5", "x", "5")
        self.assertEqual(kind, "")
        self.assertEqual(coords, [UNKNOWN] * 3)

    def test_empty_strings(self):
        kind, coords = get_triangle_info("", "5", "5")
        self.assertEqual(kind, "")
        self.assertEqual(coords, [UNKNOWN] * 3)

    def test_none_inputs(self):
        kind, coords = get_triangle_info(None, "5", "5")
        self.assertEqual(kind, "")
        self.assertEqual(coords, [UNKNOWN] * 3)

    def test_numeric_error_coords_differ_from_invalid(self):
        _, bad_number = get_triangle_info("1", "1", "3")
        _, bad_text = get_triangle_info("a", "b", "c")
        self.assertEqual(bad_number, [ERROR] * 3)
        self.assertEqual(bad_text, [UNKNOWN] * 3)
        self.assertNotEqual(bad_number, bad_text)

    def test_coordinates_are_tuples_of_ints(self):
        _, coords = get_triangle_info("4", "5", "6")
        for point in coords:
            self.assertIsInstance(point[0], int)
            self.assertIsInstance(point[1], int)

    def test_three_distinct_vertices(self):
        _, coords = get_triangle_info("4", "5", "6")
        self.assertEqual(len(set(coords)), 3)


if __name__ == "__main__":
    unittest.main()