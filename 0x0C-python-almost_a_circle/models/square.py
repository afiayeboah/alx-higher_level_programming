#!/usr/bin/python3
"""
Square module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        """
        Set the size of the Square.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the Square.
        """
        if args:
            attributes = ["id", "size", "x", "y"]
            for attr, val in zip(attributes, args):
                setattr(self, attr, val)

        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Return the dictionary representation of the Square.
        """
        square_dict = {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }

        return square_dict

    def __str__(self):
        """
        Return the print() and str() representation of a Square.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)


if __name__ == "__main__":
    pass
