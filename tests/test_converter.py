import unittest
from src.converter import Converter


class TestConverter(unittest.TestCase):

    # --- Тесты для x >= 100.7 ---
    def test_upper_boundary(self):
        self.assertEqual(Converter.do(100.7), 1000)  # Включительно

    def test_greater_than_upper(self):
        self.assertEqual(Converter.do(150.2), 1000)

    # --- Тесты для 0 < x < 100.7 ---
    def test_positive_range(self):
        self.assertEqual(Converter.do(65.7), 65)  # int(65.7)
        self.assertEqual(Converter.do(1.5), 1)

    def test_just_below_upper_boundary(self):
        self.assertEqual(Converter.do(100.6), 100)  # Ближайшее возможное значение меньше 100.7

    # --- Тест для x == 0.0 (Исключение) ---
    def test_zero_raises_exception(self):
        with self.assertRaises(ValueError):
            Converter.do(0.0)

    # --- Тесты для -30.4 <= x < 0 ---
    def test_lower_boundary_negative_range(self):
        self.assertEqual(Converter.do(-30.4), -35)  # int(-30.4) = -30; -30 - 5 = -35

    def test_negative_range(self):
        self.assertEqual(Converter.do(-5.5), -10)  # int(-5.5) = -5; -5 - 5 = -10
        self.assertEqual(Converter.do(-0.1), -5)   # int(-0.1) = 0; 0 - 5 = -5
        self.assertEqual(Converter.do(-20.0), -25) # int(-20.0) = -20; -20 - 5 = -25

    # --- Тесты для x <= -30.5 ---
    def test_upper_boundary_very_negative_range(self):
        self.assertEqual(Converter.do(-30.5), -2000)  # Включительно

    def test_very_negative_range(self):
        self.assertEqual(Converter.do(-94.5), -2000)
        self.assertEqual(Converter.do(-1000.0), -2000)

    def test_between_ranges_raises_exception(self):
        with self.assertRaises(ValueError):
            Converter.do(-30.45)


if __name__ == '__main__':
    unittest.main()