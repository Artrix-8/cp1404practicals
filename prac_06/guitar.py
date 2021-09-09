
CURRENT_YEAR = 2021
VINTAGE_AGE = 50


class Guitar:
    """Represents a Guitar."""

    def __init__(self, name="", year=0, cost=0):
        """Define variables for Guitar."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Neatly format Guitars variables for display."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Returns the age of the guitar compared to CURRENT_YEAR."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Returns boolean for whether guitar is vintage."""
        return self.get_age() >= VINTAGE_AGE
