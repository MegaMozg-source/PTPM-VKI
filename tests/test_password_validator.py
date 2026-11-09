import unittest

from src.password_validator import validate_password

class TestPasswordValidator(unittest.TestCase):

    # ---------- True тестирование ----------

    def test_valid_latin_password(self):
        self.assertTrue(validate_password("SecurePass1!"))

    def test_valid_cyrillic_password(self):
        self.assertTrue(validate_password("ПарольТест9#"))

    # ---------- Граничные значения длины  ----------

    def test_boundary_length_7(self):
        self.assertFalse(validate_password("Abcde1!"))

    def test_boundary_length_8(self):
        self.assertTrue(validate_password("Abcdef1!"))

    def test_boundary_length_20(self):
        # 20 символов: верхняя граница
        self.assertTrue(validate_password("Aa1!" + "b" * 16))

    def test_boundary_length_21(self):
        # 21 символ: на 1 больше верхней границы
        self.assertFalse(validate_password("Aa1!" + "b" * 17))

    # ---------- Классы эквивалентности ----------
    def test_missing_uppercase(self):
        self.assertFalse(validate_password("securepass1!"))

    def test_missing_lowercase(self):
        self.assertFalse(validate_password("SECUREPASS1!"))

    def test_missing_digit(self):
        self.assertFalse(validate_password("SecurePassword!"))

    def test_missing_special(self):
        self.assertFalse(validate_password("SecurePassword1"))

    def test_underscore_not_special(self):
        self.assertFalse(validate_password("SecurePass1_"))

    def test_question_mark_not_special(self):
        self.assertFalse(validate_password("SecurePass1?"))

    def test_empty_string(self):
        self.assertFalse(validate_password(""))

    # ---------- ValueError ----------
    def test_space_inside(self):
        with self.assertRaises(ValueError):
            validate_password("Pass 1234!")

    def test_space_at_start(self):
        with self.assertRaises(ValueError):
            validate_password(" Pass1234!")

    def test_space_at_end(self):
        with self.assertRaises(ValueError):
            validate_password("Pass1234! ")

    # ---------- TypeError ----------
    def test_none_raises_type_error(self):
        with self.assertRaises(TypeError):
            validate_password(None)

    def test_int_raises_type_error(self):
        with self.assertRaises(TypeError):
            validate_password(12345678)

    def test_list_raises_type_error(self):
        with self.assertRaises(TypeError):
            validate_password(["P", "a", "s", "s", "1", "!"])


if __name__ == "__main__":
    unittest.main()