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

    def compare_phrase_from_either_end(self):
        """Compare a phrase.  From either - example racecar"""
        for i in range(0, len(self.content)):
            # if self.content[i] == self.content[len(self.content) - 1 - i]:
            #     print("success %s %s", self.content[i], self.content[len(self.content) - 1 - i])
            print ("%s %s", self.content[i], self.content[len(self.content) - 1 - i])


class TranslatedPhrase(Phrase):
    """A class to represent phrases with translation."""

    def __init__(self, content, translation):
        super().__init__(content)
        self.language = None
        self.translation = translation
        self.find_translation()

    def processed_content(self):
        """Process content for palindrome testing."""
        print("super")
        return self.content.lower()

    def find_translation(self):
        if self.translation == "German":
            self.language = "Deutsch"

def reverse(string):
    """Reverse a string."""
    return "".join(reversed(string))
