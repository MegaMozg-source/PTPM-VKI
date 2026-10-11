import unittest
from Delivery import calculate_delivery_cost

class TestDelivery(unittest.TestCase):
    def test_valid_standard_delivery(self):
        # Базовый расчет: 200 + (100 * 5) = 700. Вес 3кг < 5кг (без коэфф).
        cost, date = calculate_delivery_cost(3.0, 100, "обычный", False)
        self.assertEqual(cost, 700)
        self.assertEqual(date, "2026-09-04")

    def test_invalid_weight_low(self):
        # Вес меньше 0.1
        self.assertEqual(calculate_delivery_cost(0.05, 100, "обычный"), (-1, "0000-00-00"))

    def test_invalid_weight_high(self):
        # Вес больше 50.0
        self.assertEqual(calculate_delivery_cost(51.0, 100, "обычный"), (-1, "0000-00-00"))

    def test_invalid_distance(self):
        # Дистанция больше 5000
        self.assertEqual(calculate_delivery_cost(10.0, 6000, "обычный"), (-1, "0000-00-00"))

    def test_invalid_package_type(self):
        # Неверный тип посылки
        self.assertEqual(calculate_delivery_cost(10.0, 100, "жидкий"), (-1, "0000-00-00"))

    def test_weight_coefficient_mid(self):
        # Вес между 5 и 20 кг (коэфф 1.2). Базовая: 200 + 500 = 700. 700 * 1.2 = 840.
        cost, _ = calculate_delivery_cost(10.0, 100, "обычный")
        self.assertEqual(cost, 840)

    def test_weight_coefficient_high(self):
        # Вес >= 20 кг (коэфф 1.5). Базовая: 700. 700 * 1.5 = 1050.
        cost, _ = calculate_delivery_cost(20.0, 100, "обычный")
        self.assertEqual(cost, 1050)

    def test_fragile_type_cost(self):
        # Хрупкий добавляет 300. Базовая: 700 + 300 = 1000.
        cost, _ = calculate_delivery_cost(3.0, 100, "хрупкий")
        self.assertEqual(cost, 1000)

    def test_express_cost_logic(self):
        # Экспресс доставка должна увеличивать стоимость, а не уменьшать (ожидаем провал теста).
        normal_cost, _ = calculate_delivery_cost(3.0, 100, "обычный", False)
        express_cost, _ = calculate_delivery_cost(3.0, 100, "обычный", True)
        self.assertGreater(express_cost, normal_cost)

    def test_express_delivery_days(self):
        # Время экспресс доставки не должно быть равно 0 дням (ожидаем провал теста).
        _, date = calculate_delivery_cost(3.0, 100, "обычный", True)
        self.assertNotEqual(date, "2026-09-03")

if __name__ == "__main__":
    unittest.main()
