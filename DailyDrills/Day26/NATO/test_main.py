import unittest
from main import lookup_values_from_csv  # Import the correct function to test

class TestNATO(unittest.TestCase):
    def test_nato_conversion(self):
        # Test the conversion of a word to NATO phonetic alphabet
        result = lookup_values_from_csv("nato_phonetic_alphabet.csv", "hello")
        expected = ["Hotel", "Echo", "Lima", "Lima", "Oscar"]
        self.assertEqual(result, expected)

    def test_empty_input(self):
        # Test behavior with empty input
        result = lookup_values_from_csv("nato_phonetic_alphabet.csv", "")
        expected = []
        self.assertEqual(result, expected)

    def test_non_alphabetic_input(self):
        # Test behavior with non-alphabetic characters
        result = lookup_values_from_csv("nato_phonetic_alphabet.csv", "123")
        expected = []
        self.assertEqual(result, expected)

    def test_mixed_input(self):
        # Test behavior with mixed alphabetic and non-alphabetic characters
        result = lookup_values_from_csv("nato_phonetic_alphabet.csv", "abc123")
        expected = ["Alfa", "Bravo", "Charlie"]
        self.assertEqual(result, expected)

    def test_special_characters(self):
        # Test behavior with special characters
        result = lookup_values_from_csv("nato_phonetic_alphabet.csv", "@#$%")
        expected = []
        self.assertEqual(result, expected)

    def test_uppercase_input(self):
        # Test behavior with uppercase input
        result = lookup_values_from_csv("nato_phonetic_alphabet.csv", "HELLO")
        expected = ["Hotel", "Echo", "Lima", "Lima", "Oscar"]
        self.assertEqual(result, expected)

    def test_mixed_case_input(self):
        # Test behavior with mixed case input
        result = lookup_values_from_csv("nato_phonetic_alphabet.csv", "HeLLo")
        expected = ["Hotel", "Echo", "Lima", "Lima", "Oscar"]
        self.assertEqual(result, expected)

    def test_whitespace_input(self):
        # Test behavior with input containing whitespace
        result = lookup_values_from_csv("nato_phonetic_alphabet.csv", " hello ")
        expected = ["Hotel", "Echo", "Lima", "Lima", "Oscar"]
        self.assertEqual(result, expected)

    def test_unicode_characters(self):
        # Test behavior with Unicode characters
        result = lookup_values_from_csv("nato_phonetic_alphabet.csv", "héllo")
        expected = ["Hotel", "Echo", "Lima", "Lima", "Oscar"]  # Assuming Unicode normalization
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
