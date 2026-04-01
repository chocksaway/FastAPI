from learn.phrase import Phrase, TranslatedPhrase


def test_non_palindrome():
    assert not Phrase("apple").is_palindrome()

def test_literal_palindrome():
    assert Phrase("racecar").is_palindrome()

def test_palindrome_from_either_end():
    phrase = Phrase("racecar")
    phrase.compare_phrase_from_either_end()

def test_translated_phrase_which_is_german():
    translated_phrase = TranslatedPhrase("racecar", "German")
    assert translated_phrase.find_translation() == "Deutsch"

def test_translated_phrase_which_is_german_invalid():
    translated_phrase = TranslatedPhrase("racecar", "german")
    assert translated_phrase.find_translation() is None
