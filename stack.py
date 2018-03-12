""" Using the PEP 8 Style Guide for Python Code:
https://www.python.org/dev/peps/pep-0008/ and python linters """


class Stack:
    """A stack is structured as an ordered collection of items where items are
    added to and removed from the end called the “top.” Stacks are ordered
    LIFO.

    Big-O Complexity:
        The push() and pop() operations are both constant time 𝑂(1)
    """
    def __init__(self):
        """Creates a new stack that is empty."""
        self.items = []

    def is_empty(self):
        """Tests to see whether the stack is empty. It needs no parameters and
        returns a boolean value.

        Returns:
            boolean : True if empty, False if not empty.
        """
        return self.items == []

    def push(self, item):
        """Adds a new item to the top of the stack. It needs the item and returns
        nothing.

        Args:
            item (type unknown) : The item to be added to the top of the stack.
        """
        self.items.append(item)

    def pop(self):
        """ Removes the top item from the stack. It needs no parameters and returns
        the item. The stack is modified.

        Returns:
            type unkown : The top item.
        """
        return self.items.pop()

    def peek(self):
        """Returns the top item from the stack but does not remove it. It needs no
        parameters. The stack is not modified.

        Returns:
            type unknown : The top item.
        """
        return self.items[len(self.items)-1]

    def size(self):
        """Returns the number of items on the stack. It needs no parameters and
        returns an integer.

        Returns:
            int : the number of items on the stack
        """
        return len(self.items)


s = Stack()
s.push('first')
s.push('second')
print(s.pop())
print(s.peek())
