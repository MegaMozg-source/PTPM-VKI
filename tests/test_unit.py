import unittest
from unittest.mock import Mock, patch
from src.controller import Controller
from src.database import Database


class TestUnitController(unittest.TestCase):
    @patch('src.calculator.TriangleCalculator.get_triangle_info')
    def test_unit_controller_isolation(self, mock_calc):
        # В этом тесте мы используем ПОЛНУЮ заглушку БД (Mock),
        # поэтому реальное соединение открывать не нужно.
        mock_ui = Mock()
        mock_ui.get_input.return_value = ("5", "5", "5")
        mock_ext = Mock()
        mock_db = Mock(spec=Database)
        mock_db.get_record.return_value = None

        mock_calc.return_value = ("равносторонний", "", [])

        controller = Controller(mock_db, mock_ui, mock_ext)
        controller.run()

        mock_db.get_record.assert_called_once_with("5", "5", "5")
        mock_db.add_record.assert_called_once()
        mock_calc.assert_called_once_with("5", "5", "5")
        mock_ext.send.assert_called_once()


class TestUnitDatabase(unittest.TestCase):
    # SETUP: Выполняется перед каждым тестом в этом классе
    def setUp(self):
        self.db = Database(":memory:")

    # TEARDOWN: Выполняется после каждого теста в этом классе
    def tearDown(self):
        self.db.close()

    def test_unit_db_operations(self):
        # БД уже создана в setUp, просто тестируем методы
        self.db.add_record("1", "1", "1", "равносторонний", "")
        self.assertIsNotNone(self.db.get_record("1", "1", "1"))
        self.db.delete_record("1", "1", "1")
        self.assertIsNone(self.db.get_record("1", "1", "1"))


if __name__ == '__main__':
    unittest.main()