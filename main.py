class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data: int) -> None:
        """TODO: add node with data to end of list"""
        pass

    def prepend(self, data: int) -> None:
        """TODO: add node with data to start of list"""
        pass

    def delete(self, data: int) -> None:
        """TODO: delete first node with given data"""
        pass

    def to_list(self) -> list[int]:
        """TODO: return all node values as a Python list"""
        pass

    def length(self) -> int:
        """TODO: return number of nodes"""
        pass
