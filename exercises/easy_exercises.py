"""
Easy Python Exercises
=====================
Solve each function below by replacing the `pass` statement with your code.
Run the tests with: pytest exercises/test_easy_exercises.py
"""


# Exercise 1: Reverse a String
# Return the reverse of the given string.
# Example: reverse_string("hello") -> "olleh"
def reverse_string(s: str) -> str:
    reverse_str = []
    reverse_str.extend([None] * len(s))
    reverse_counter = len(s) - 1

    for i in range(len(s)):
        reverse_str[i] = s[reverse_counter]
        reverse_counter -= 1

    return "".join(reverse_str)


# Exercise 2: FizzBuzz
# Return a list of strings for numbers 1 through n (inclusive).
# - Multiples of 3 -> "Fizz"
# - Multiples of 5 -> "Buzz"
# - Multiples of both 3 and 5 -> "FizzBuzz"
# - Everything else -> the number as a string
# Example: fizzbuzz(5) -> ["1", "2", "Fizz", "4", "Buzz"]
def fizzbuzz(n: int) -> list[str]:
    output = []
    output.extend([None] * n)
    each = ""
    counter = 0

    for i in range(1, n+1):
        print(i)
        if i % 5 == 0 and i % 3 == 0:
            each = "FizzBuzz"
        elif i % 3 == 0:
            each = "Fizz"
        elif i % 5 == 0:
            each = "Buzz"
        else:
            each = str(i)

        output[counter] = each

        counter += 1

    return output


# Exercise 3: Count Vowels
# Return the number of vowels (a, e, i, o, u) in the string (case-insensitive).
# Example: count_vowels("Hello World") -> 3
def count_vowels(s: str) -> int:
    count = 0
    for char in s:
        if char.lower() in "aeiou":
            count += 1

    return count


# Exercise 4: Find the Maximum
# Return the largest number in a list WITHOUT using the built-in max() function.
# Example: find_max([3, 1, 4, 1, 5, 9, 2, 6]) -> 9
def find_max(numbers: list[int]) -> int:
    previous = 0
    if numbers[0] <= 0:
        previous = numbers[0]

    for each in numbers:
        if each > previous:
            previous = each

    return previous





# Exercise 5: Palindrome Check
# Return True if the string is a palindrome (reads the same forwards and backwards),
# ignoring case and spaces. Return False otherwise.
# Example: is_palindrome("A man a plan a canal Panama") -> True
def is_palindrome(s: str) -> bool:
    parsed_s = s.replace(" ", "")
    parsed_s = parsed_s.lower()
    as_list = list(parsed_s)
    end_marker = len(parsed_s)

    for i in range(0, len(as_list)):
        if as_list[i] != as_list[end_marker-1]:
            return False

        end_marker -= 1

    return True



# Exercise 6: Sum of Digits
# Given a non-negative integer, return the sum of its digits.
# Example: sum_of_digits(1234) -> 10
def sum_of_digits(n: int) -> int:
    total = 0
    for each in str(n):
        print(each)
        total += int(each)
    return total



# Exercise 7: Remove Duplicates
# Return a new list with duplicates removed, preserving the original order.
# Example: remove_duplicates([1, 2, 2, 3, 1, 4]) -> [1, 2, 3, 4]
def remove_duplicates(items: list) -> list:
    duplicates = {}
    unique = []
    for item in items:
        if item not in duplicates:
            duplicates[item] = item
            unique.append(item)

    return unique


# Exercise 8: Caesar Cipher
# Shift each letter in the string forward by `shift` positions in the alphabet.
# Wrap around if needed. Leave non-letter characters unchanged. Preserve case.
# Example: caesar_cipher("Hello, World!", 3) -> "Khoor, Zruog!"
def caesar_cipher(text: str, shift: int) -> str:
    changed = ""

    for each in text:
        start = "a"
        if each.isalpha():
            if each.isupper():
                start  = "A"
            shifted = chr((ord(each) - ord(start) + shift) % 26 + ord(start))
            changed += shifted
        else:
            changed += each

    return changed




