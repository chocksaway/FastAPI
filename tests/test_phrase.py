from learn.phrase import Phrase


def test_non_palindrome():
    assert not Phrase("apple").is_palindrome()