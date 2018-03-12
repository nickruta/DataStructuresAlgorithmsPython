""" Using the PEP 8 Style Guide for Python Code:
https://www.python.org/dev/peps/pep-0008/ and python linters """


class Node:
    """The basic building block for the linked list implementation is the node.
    Each node object must hold at least two pieces of information. First, the
    node must contain the list item itself. We will call this the data field of
    the node. In addition, each node must hold a reference to the next node. To
    make this a "doubly" linked list, we would need to add self.previous.

    """
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class OrderedList:
    """creates a new ordered list that is empty. It needs no parameters and
    returns nothing.

    Big-O Complexity:
        Consider a linked list that has 𝑛 nodes. The isEmpty method is 𝑂(1)
        since it requires one step to check the head reference for None. Size,
        on the other hand, will always require 𝑛 steps since there is no way to
        know how many nodes are in the linked list without traversing from head
        to end. Therefore, length is 𝑂(𝑛). Adding an item to an unordered list
        will always be 𝑂(1) since we simply place the new node at the head of
        the linked list. However, search and remove, as well as add for an
        ordered list, all require the traversal process. Although on average
        they may need to traverse only half of the nodes, these methods are
        all 𝑂(𝑛) since in the worst case each will process every node in
        the list.
    """
    def __init__(self):
        """creates a new ordered list that is empty. It needs no parameters
        and returns nothing.
        """
        self.head = None

    def search(self, item):
        """ searches for the item in the list. It needs the item and returns a
         boolean value.

        Args:
            item (type unkown) : the item to be searched for

        Returns:
            bool (boolean) : True if found, False otherwise.
        """
        current = self.head
        found = False
        stop = False
        while current is not None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()

        return found

    def add(self, item):
        """adds a new item to the list making sure that the order is preserved.
        It needs the item and returns nothing. Assume the item is not already
        in the list.

        Args:
            item (type unknown) : the item to be added
        """
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(item)
        if previous is None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)

    def isEmpty(self):
        """tests to see whether the list is empty. It needs no parameters and
        returns a boolean value.

        Args:
            bool (boolean) : True if empty, False otherwise queue.
        """
        return self.head is None

    def size(self):
        """returns the number of items in the list. It needs no parameters and
         returns an integer.

        Returns:
            integer (int) : the number of items in the list
        """
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.getNext()

        return count


mylist = OrderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.size())
print(mylist.search(93))
print(mylist.search(100))
