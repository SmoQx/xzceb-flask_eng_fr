import unittest
from translator import english_to_french, french_to_english

class TestString(unittest.TestCase):

    def test_eng_to_fr(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

    def test_fr_to_eng(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")


if __name__ == "__main__":
    unittest.main()