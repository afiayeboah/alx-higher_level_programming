#!/usr/bin/python3
"""
Defines the Base class for handling object  using the turtle module.
"""
import json
import csv
import turtle


class Base:
    """Base class for handling common functionalities."""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes an object with a unique identifier.

        Args:
            id (int): Optional identifier for the object.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    @staticmethod
    def to_json_string(dictionary_list):
        """Converts a list of dictionaries to a JSON-formatted string.

        Args:
            dictionary_list (list): List of dictionaries.

        Returns:
            str: JSON-formatted string.
        """
        if not dictionary_list:
            return "[]"
        return json.dumps(dictionary_list)

    @classmethod
    def save_to_file(cls, object_list):
        """
        Saves a list of objects to a JSON file.

        Args:
            object_list (list): List of objects to be serialized.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as json_file:
            if not object_list:
                json_file.write("[]")
            else:
                dictionary_list = [obj.to_dict() for obj in object_list]
                json_file.write(Base.to_json_string(dictionary_list))

    @staticmethod
    def from_json_string(json_str):
        """
        Deserializes a JSON-formatted string into a list of dictionaries.

        Args:
            json_str (str): JSON-formatted string.

        Returns:
            list: List of dictionaries.
        """
        if not json_str or json_str == "[]":
            return []
        return json.loads(json_str)

    @classmethod
    def create(cls, **attributes):
        """
        Creates an instance of the class from a dictionary of attributes.

        Args:
            attributes (dict): Dictionary of attributes.

        Returns:
            object: Instance of the class.
        """
        if attributes:
            new_instance = cls(1)  # Default values for now
            new_instance.update(**attributes)
            return new_instance

    @classmethod
    def load_from_file(cls):
        """
        Loads a list of objects from a JSON file.

        Returns:
            list: List of objects instantiated from the file.
        """
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, "r") as json_file:
                dict_list = Base.from_json_string(json_file.read())
                return [cls.create(**data) for data in dict_list]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, object_list):
        """
        Writes the CSV serialization of a list of objects to a file.

        Args:
            object_list (list): List of objects to be serialized.
        """
        filename = f"{cls.__name__}.csv"
        with open(filename, "w", newline="") as csv_file:
            if not object_list:
                csv_file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                for obj in object_list:
                    writer.writerow(obj.to_dict())

    @classmethod
    def load_from_file_csv(cls):
        """
        Loads a list of objects from a CSV file.

        Returns:
            list: List of objects instantiated from the file.
        """
        filename = f"{cls.__name__}.csv"
        try:
            with open(filename, "r", newline="") as csv_file:
                fieldnames = cls.get_fieldnames()
                dict_reader = csv.DictReader(csv_file, fieldnames=fieldnames)
                dict_list = [cls.convert_dict_values(data) for data in dict_reader]
                return [cls.create(**data) for data in dict_list]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw_shapes(rectangle_list, square_list):
        """
        Draws rectangles and squares using the turtle module.

        Args:
            rectangle_list (list): List of rectangles.
            square_list (list): List of squares.
        """
        window = turtle.Screen()
        pen = turtle.Pen()
        shapes = rectangle_list + square_list

        for shape in shapes:
            pen.up()
            pen.goto(shape.x, shape.y)
            pen.down()
            pen.forward(shape.width)
            pen.right(90)
            pen.forward(shape.height)
            pen.right(90)
            pen.forward(shape.width)
            pen.right(90)
            pen.forward(shape.height)
            pen.right(90)

        window.exitonclick()
