#!/usr/bin/python3
"""
Rectangle module
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.
        """
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter"""
        self._validate_attribute("width", value)
        self.__width = value

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter"""
        self._validate_attribute("height", value)
        self.__height = value

    @property
    def x(self):
        """X getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """X setter"""
        self._validate_attribute("x", value)
        self.__x = value

    @property
    def y(self):
        """Y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """Y setter"""
        self._validate_attribute("y", value)
        self.__y = value

    def area(self):
        """Return area of the rectangle"""
        return self.width * self.height

    def display(self):
        """Print size of rectangle using #"""
        for _ in range(self.y):
            print()

        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def _validate_attribute(self, attribute, value):
        """Generic attribute validation"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(attribute))
        if attribute == "x" or attribute == "y":
            if value < 0:
                raise ValueError("{} must be >= 0".format(attribute))
        elif value <= 0:
            raise ValueError("{} must be > 0".format(attribute))

    def update(self, *args, **kwargs):
        """Assign arguments to attributes based on their positions."""
        if args:
            attributes = ["id", "width", "height", "x", "y"]
            for attr, val in zip(attributes, args):
                setattr(self, attr, val)

        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Represent a dictionary representation of rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)


if __name__ == "__main__":
    pass
