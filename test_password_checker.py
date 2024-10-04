# Unit Testing

import unittest
from password_checker import PasswordChecker


class TestPasswordChecker(unittest.TestCase):

    def test_length(self):
        checker = PasswordChecker("short")
        self.assertIn("Super Weak!", checker.length())

        checker = PasswordChecker("longpassword123")
        self.assertIn("Super Strong!", checker.length())

    def test_lowercase_letters(self):
        checker = PasswordChecker("NOLOWERCASE")
        self.assertIn("Super Weak!", checker.lowercase_letters())

        checker = PasswordChecker("haslowercase")
        self.assertIn("Super Strong!", checker.lowercase_letters())

    def test_uppercase_letters(self):
        checker = PasswordChecker("nouppercase")
        self.assertIn("Super Weak!", checker.uppercase_letters())

        checker = PasswordChecker("HASUPPERCASE")
        self.assertIn("Super Strong!", checker.uppercase_letters())

    def test_numbers(self):
        checker = PasswordChecker("nonumbers")
        self.assertIn("Super Weak!", checker.numbers())

        checker = PasswordChecker("password123")
        self.assertIn("Strong!", checker.numbers())

    def test_special_characters(self):
        checker = PasswordChecker("nospecials")
        self.assertIn("Super Weak!", checker.special_characters())

        checker = PasswordChecker("password@123!")
        self.assertIn("Medium Strength.", checker.special_characters())

    def test_entropy_calculator(self):
        checker = PasswordChecker("abc")
        self.assertIn("Super Weak!", checker.entropy_calculator())

        checker = PasswordChecker("ThisIsAVeryStrongPassword123!@#")
        self.assertIn("Super Strong!", checker.entropy_calculator())

    def test_is_common(self):
        checker = PasswordChecker("password")
        self.assertTrue(checker.is_common())

        checker = PasswordChecker("uniquePassword123")
        self.assertFalse(checker.is_common())


if __name__ == "__main__":
    unittest.main()
