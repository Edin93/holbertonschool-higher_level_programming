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
        """Defines node data.
        
