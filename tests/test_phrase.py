from learn.phrase import Phrase


def test_non_palindrome():
    assert not Phrase("apple").is_palindrome()

def test_literal_palindrome():
    assert Phrase("racecar").is_palindrome()

def test_palindrome_from_either_end():
    phrase = Phrase("racecar")
    phrase.compare_phrase_from_either_end()