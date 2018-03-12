""" Using the PEP 8 Style Guide for Python Code:
https://www.python.org/dev/peps/pep-0008/ and python linters """


class Deque:
    """A deque is structured as an ordered collection of items where items are
    added and removed from either front or rear.


    Big-O Complexity:
        In this implementation adding and removing items from the front is 𝑂(1)
        whereas adding and removing from the rear is 𝑂(𝑛). This is to be
        expected given the common operations that appear for adding and
        removing items

    """
    def __init__(self):
        """creates a new deque that is empty. It needs no parameters and
        returns nothing.
        """
        self.items = []

    def is_empty(self):
        """tests to see whether the deque is empty. It needs no parameters
        and returns a boolean value.

        Args:
            bool (boolean) : True if empty, False otherwise queue.
        """
        return self.items == []

    def add_front(self, item):
        """adds a new item to the front of the deque. It needs the item
        and returns nothing.

        Args:
            item (type unknown) : The item to be added to the front of the
            queue.
        """
        self.items.append(item)

    def add_rear(self, item):
        """adds a new item to the rear of the deque. It needs the item
        and returns nothing.

        Args:
            item (type unknown) : The item to be added to the rear of the
            queue.
        """
        self.items.insert(0, item)

    def remove_front(self):
        """removes the front item from the deque. It needs no parameters and
        returns the item. The deque is modified.
        """
        return self.items.pop()

    def remove_rear(self):
        """removes the rear item from the deque. It needs no parameters and
        returns the item. The deque is modified.
        """
        return self.items.pop(0)

    def size(self):
        """returns the number of items in the deque. It needs no parameters
        and returns an integer.

        Args:
            integer (int) : the number of items in the deque
            queue.
        """
        return len(self.items)


d = Deque()
d.add_rear('last')
d.add_front('first')
d.add_rear("new last")
print(d.remove_front())
print(d.remove_rear())
