import unittest
from unittest.mock import Mock
from src.controller import Controller
from src.database import Database


class TestIntegration(unittest.TestCase):
    # SETUP: Выполняется ПЕРЕД каждым тестом
    def setUp(self):
        self.real_db = Database(":memory:")  # Открываем новую чистую БД
        self.mock_ui = Mock()
        self.mock_ext = Mock()
        self.controller = Controller(self.real_db, self.mock_ui, self.mock_ext)

    # TEARDOWN: Выполняется ПОСЛЕ каждого теста
    def tearDown(self):
        self.real_db.close()  # Закрываем БД, чтобы не было утечек

    # ИНТЕГРАЦИОННЫЙ ТЕСТ 1
    def test_integration_new_calculation(self):
        self.mock_ui.get_input.return_value = ("3", "4", "5")
        result = self.controller.run()

        self.assertIn("Вычислено: Тип: разносторонний", result)
        self.assertEqual(self.real_db.get_record("3", "4", "5")[0], "разносторонний")

    # ИНТЕГРАЦИОННЫЙ ТЕСТ 2
    def test_integration_from_cache(self):
        self.real_db.add_record("2", "2", "2", "равносторонний", "")
        self.mock_ui.get_input.return_value = ("2", "2", "2")

        result = self.controller.run()
        self.assertIn("Из БД: Тип: равносторонний", result)

    # ИНТЕГРАЦИОННЫЙ ТЕСТ 3
    def test_integration_error_handling(self):
        self.mock_ui.get_input.return_value = ("1", "1", "10")
        result = self.controller.run()

        self.assertIn("Ошибка: Нарушено неравенство", result)
        record = self.real_db.get_record("1", "1", "10")
        self.assertEqual(record[1], "Нарушено неравенство треугольника")


if __name__ == '__main__':
    unittest.main()