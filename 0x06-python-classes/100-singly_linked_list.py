#!/usr/bin/python3
"""Definition of a singly-linked list."""


class Node:
    """Representation of a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new node.

        Args:
            data (int): The data of the new node.
            next_node (Node): The next node of the new node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get or set the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the node.

        Args:
            value (int): The new data of the node.

        Raises:
            TypeError: If data is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("Data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get or set the next node of the current node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node of the current node.

        Args:
            value (Node): The new next node.

        Raises:
            TypeError: If next_node is not a Node object.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("Next node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Representation of a singly-linked list."""

    def __init__(self):
        """Initialize an empty singly-linked list."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new node into the singly-linked list.

        The node is inserted into the list at the correct
        ordered numerical position.

        Args:
            value (Node): The new node to insert.
        """
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new_node.next_node = tmp.next_node
            tmp.next_node = new_node

    def __str__(self):
        """Define the string representation of a singly-linked list."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return '\n'.join(values)
