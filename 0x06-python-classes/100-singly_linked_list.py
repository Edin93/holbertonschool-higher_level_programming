#!/usr/bin/python3
class Node:
    """Node of singly linked list."""

    def __init__(self, data, next_node=None):
        """Init Node data.
        Parameters:
        data (int): node data.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve node data.
        Returns:
        int: Node data.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Defines node data."""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Retrive node's next node value."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Defines node's next value."""
        if value is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list."""

    def __init__(self):
        """Initialize a linked list."""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node in the correct sorted position in the list."""
        h = self.__head
        new = Node(value)
        if h is None:
            h = Node(value)
        elif new.data <= h.data:
            new.__next_node = h
            h = new
        else:
            while h.next_node:
                h = h.next_node
                if h.data < new.data:
                    new.__next_node = h.next_node
                    h.next_node = new
        print(h.data)
