import unittest
from main import LinkedList


class TestLinkedList(unittest.TestCase):

    def test_append_single(self):
        ll = LinkedList()
        ll.append(1)
        self.assertEqual(ll.to_list(), [1])

    def test_append_multiple(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        self.assertEqual(ll.to_list(), [1, 2, 3])

    def test_prepend(self):
        ll = LinkedList()
        ll.append(2)
        ll.prepend(1)
        self.assertEqual(ll.to_list(), [1, 2])

    def test_delete_middle(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        ll.delete(2)
        self.assertEqual(ll.to_list(), [1, 3])

    def test_delete_head(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.delete(1)
        self.assertEqual(ll.to_list(), [2])

    def test_delete_nonexistent(self):
        ll = LinkedList()
        ll.append(1)
        ll.delete(99)
        self.assertEqual(ll.to_list(), [1])

    def test_length(self):
        ll = LinkedList()
        ll.append(10)
        ll.append(20)
        ll.append(30)
        self.assertEqual(ll.length(), 3)

    def test_empty_length(self):
        ll = LinkedList()
        self.assertEqual(ll.length(), 0)

    def test_empty_to_list(self):
        ll = LinkedList()
        self.assertEqual(ll.to_list(), [])


if __name__ == "__main__":
    unittest.main()
