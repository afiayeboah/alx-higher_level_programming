#!/usr/bin/python3
"""Create a class MyInt that inherits from int."""


class MyInt(int):
    """Body of the MyInt class"""

    def __eq__(self, other_value):
        """Override the == operator with the != behavior."""
        return super().__ne__(other_value)

    def __ne__(self, other_value):
        """Override the != operator with the == behavior."""
        return super().__eq__(other_value)
