import unittest
from unittest.mock import Mock, patch
from src.controller import Controller
from src.database import Database


class TestUnitController(unittest.TestCase):
    @patch('src.calculator.TriangleCalculator.get_triangle_info')
    def test_unit_controller_isolation(self, mock_calc):
        # Заглушки для UI и внешнего сервиса
        mock_ui = Mock()
        mock_ui.get_input.return_value = ("5", "5", "5")
        mock_ext = Mock()
        mock_db = Mock(spec=Database)
        mock_db.get_record.return_value = None

        # Настраиваем имитацию вычислений
        mock_calc.return_value = ("равносторонний", "", [])

        controller = Controller(mock_db, mock_ui, mock_ext)
        controller.run()

        # Проверяем изоляцию: методы вызывались правильно
        mock_db.get_record.assert_called_once_with("5", "5", "5")
        mock_db.add_record.assert_called_once()
        mock_calc.assert_called_once_with("5", "5", "5")
        mock_ext.send.assert_called_once()


class TestUnitDatabase(unittest.TestCase):
    def test_unit_db_operations(self):
        db = Database(":memory:")
        db.add_record("1", "1", "1", "равносторонний", "")
        self.assertIsNotNone(db.get_record("1", "1", "1"))
        db.delete_record("1", "1", "1")
        self.assertIsNone(db.get_record("1", "1", "1"))