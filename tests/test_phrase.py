import unittest

from learn.phrase import Phrase


class TestPhrase(unittest.TestCase):
    def test_non_palindrome(self):
        self.assertFalse(Phrase("apple").is_palindrome())
