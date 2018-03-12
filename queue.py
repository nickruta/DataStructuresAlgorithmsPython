""" Using the PEP 8 Style Guide for Python Code:
https://www.python.org/dev/peps/pep-0008/ and python linters """


class Queue:
    """A queue is structured as an ordered collection of items which are added
    at one end, called the “rear,” and removed from the other end, called the
    “front.” Queues maintain a FIFO ordering property.

    Big-O Complexity:
        enqueue() is linear time 𝑂(𝑛) and dequeue() is constant time 𝑂(1).
    """
    def __init__(self):
        """creates a new queue that is empty. It needs no parameters and
        returns nothing.
        """
        self.items = []

    def is_empty(self):
        """tests to see whether the queue is empty. It needs no parameters
        and returns a boolean value.

        Returns:
            self.items (boolean) : True if empty, False otherwise.
        """
        return self.items == []

    def enqueue(self, item):
        """adds a new item to the rear of the queue. It needs the item and
        returns nothing.

        Args:
            item (type unknown) : The item to be added to the rear of the
            queue.
        """
        self.items.insert(0, item)

    def dequeue(self):
        """removes the front item from the queue. It needs no parameters and
        returns the item. The queue is modified.

        Returns:
            item (type unknown) : The item to be removed from the front of the
            queue.
        """
        return self.items.pop()

    def size(self):
        """returns the number of items in the queue. It needs no parameters
        and returns an integer.

        Returns:
            length (int) : The number of items in the queue.
        """
        return len(self.items)


q = Queue()
q.enqueue('first')
q.enqueue('second')
q.enqueue(3)
print(q.dequeue())
