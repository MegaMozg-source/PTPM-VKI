import logging
import math
import decimal
from decimal import Decimal

FIELD_SIZE = 100
ERROR_NUMBER = (-1, -1)
ERROR_TEXT = (-2, -2)


class TriangleCalculator:
    @staticmethod
    def get_triangle_info(str_a, str_b, str_c):
        try:
            a = Decimal(str_a)
            b = Decimal(str_b)
            c = Decimal(str_c)
        except (TypeError, ValueError, decimal.InvalidOperation):
            logging.warning("Неуспешный запрос: A=%s, B=%s, C=%s - невалидные данные", str_a, str_b, str_c)
            return "ошибка", "Невалидные данные (не числа)", [ERROR_TEXT, ERROR_TEXT, ERROR_TEXT]

        if a <= 0 or b <= 0 or c <= 0:
            logging.warning("Неуспешный запрос: стороны должны быть положительными")
            return "не треугольник", "Стороны должны быть положительными", [ERROR_NUMBER, ERROR_NUMBER, ERROR_NUMBER]

        if a + b <= c or a + c <= b or b + c <= a:
            logging.warning("Неуспешный запрос: нарушено неравенство треугольника")
            return "не треугольник", "Нарушено неравенство треугольника", [ERROR_NUMBER, ERROR_NUMBER, ERROR_NUMBER]

        if a == b == c:
            kind = "равносторонний"
        elif a == b or b == c or a == c:
            kind = "равнобедренный"
        else:
            kind = "разносторонний"

        try:
            coords = TriangleCalculator.calculate_coordinates(float(a), float(b), float(c))
        except Exception:
            logging.exception("Сбой при расчёте координат")
            return "ошибка", "Сбой при расчёте", [ERROR_TEXT, ERROR_TEXT, ERROR_TEXT]

        return kind, "", coords

    @staticmethod
    def calculate_coordinates(a, b, c):
        k = 80 / max(a, b, c)
        a, b, c = a * k, b * k, c * k
        cos_a = (b * b + c * c - a * a) / (2 * b * c)
        cos_a = max(-1.0, min(1.0, cos_a))
        sin_a = math.sqrt(1 - cos_a * cos_a)
        y_bottom = FIELD_SIZE - 10
        return [(10, y_bottom), (int(round(10 + c)), y_bottom),
                (int(round(10 + b * cos_a)), int(round(y_bottom - b * sin_a)))]