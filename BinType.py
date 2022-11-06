from enum import Enum

class BinType(Enum):
    """Enumeration of the different types of bins."""
    GARBAGE = 1
    COMPOST = 2
    BLACK_BIN = 3
    BLUE_BIN = 4

    def __str__(self):
        """Return the string representation of the bin type.

        Returns:
            str: The string representation of the bin type.
        """
        return self.name

