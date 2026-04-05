import pytest
from exercises.easy_exercises import (
    reverse_string,
    fizzbuzz,
    count_vowels,
    find_max,
    is_palindrome,
    sum_of_digits,
    remove_duplicates,
    caesar_cipher,
)


class TestReverseString:
    def test_basic(self):
        output = reverse_string("hello")
        assert output == "olleh"

    def test_single_char(self):
        assert reverse_string("a") == "a"

    def test_empty(self):
        assert reverse_string("") == ""

    def test_palindrome_word(self):
        assert reverse_string("racecar") == "racecar"


class TestFizzBuzz:
    def test_basic(self):
        assert fizzbuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]

    def test_only_one(self):
        assert fizzbuzz(1) == ["1"]

    def test_length(self):
        assert len(fizzbuzz(10)) == 10


class TestCountVowels:
    def test_basic(self):
        assert count_vowels("Hello World") == 3

    def test_case_insensitive(self):
        assert count_vowels("AEIOU") == 5

    def test_no_vowels(self):
        assert count_vowels("rhythm") == 0

    def test_empty(self):
        assert count_vowels("") == 0


class TestFindMax:
    def test_basic(self):
        assert find_max([3, 1, 4, 1, 5, 9, 2, 6]) == 9

    def test_single_element(self):
        assert find_max([42]) == 42

    def test_negatives(self):
        assert find_max([-5, -1, -3]) == -1

    def test_duplicates(self):
        assert find_max([7, 7, 7]) == 7


class TestIsPalindrome:
    def test_simple_palindrome(self):
        assert is_palindrome("racecar") is True

    def test_with_spaces(self):
        assert is_palindrome("A man a plan a canal Panama") is True

    def test_not_palindrome(self):
        assert is_palindrome("hello") is False

    def test_empty(self):
        assert is_palindrome("") is True


class TestSumOfDigits:
    def test_basic(self):
        assert sum_of_digits(1234) == 10

    def test_single_digit(self):
        assert sum_of_digits(7) == 7

    def test_zero(self):
        assert sum_of_digits(0) == 0

    def test_large(self):
        assert sum_of_digits(9999) == 36


class TestRemoveDuplicates:
    def test_basic(self):
        assert remove_duplicates([1, 2, 2, 3, 1, 4]) == [1, 2, 3, 4]

    def test_no_duplicates(self):
        assert remove_duplicates([1, 2, 3]) == [1, 2, 3]

    def test_all_duplicates(self):
        assert remove_duplicates([5, 5, 5]) == [5]

    def test_empty(self):
        assert remove_duplicates([]) == []

    def test_preserves_order(self):
        assert remove_duplicates([4, 3, 2, 1, 2, 3]) == [4, 3, 2, 1]

class TestSimpleCharIncrement:
    def test_basic(self):
        # char = "x"
        # next_char = chr((ord(char) + 3) %26)
        # assert "d" == next_char

        char = "x"
        shifted = chr((ord(char) - ord("a") + 3) % 26 + ord("a"))
        assert "a" == shifted

class TestCaesarCipher:
    def test_hello(self):
        assert caesar_cipher("Hello", 1) == "Ifmmp"

    def test_basic(self):
        assert caesar_cipher("Hello, World!", 3) == "Khoor, Zruog!"

    def test_wrap_around(self):
        assert caesar_cipher("xyz", 3) == "abc"

    def test_preserves_case(self):
        assert caesar_cipher("ABC", 1) == "BCD"

    def test_non_letters_unchanged(self):
        assert caesar_cipher("Hello, 123!", 0) == "Hello, 123!"

    def test_zero_shift(self):
        assert caesar_cipher("Python", 0) == "Python"

