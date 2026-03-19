class Phrase:
    """A class to represent phrases."""

    def __init__(self, content):
        self.content = content

    def is_palindrome(self):
        """Return True for a palindrome, False otherwise."""
        return self.processed_content() == reverse(self.processed_content())

    def processed_content(self):
        """Process content for palindrome testing."""
        return self.content.lower()


class TranslatedPhrase(Phrase):
    """A class to represent phrases with translation."""

    def __init__(self, content, translation):
        super().__init__(content)
        self.translation = translation
        self.find_translation()

    def processed_content(self):
        """Process content for palindrome testing."""
        print("super")
        return self.content.lower()

    def find_translation(self):
        print("find_translation")


def reverse(string):
    """Reverse a string."""
    return "".join(reversed(string))
