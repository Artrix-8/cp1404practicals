"""yep"""


class ProgrammingLanguage:
    """Represents a Programming Language."""

    def __init__(self, name, typing, reflection, year):
        """Define a programming language with inputted values."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return a String of the programming language."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Returns boolean based on reflection."""
        return self.reflection
