""" Using the PEP 8 Style Guide for Python Code:
https://www.python.org/dev/peps/pep-0008/ and python linters """


class BinaryTree:
    """Simple Binary Tree that uses nodes and references. In this case we will
    define a class that has attributes for the root value, as well as the left
    and right subtrees.

    Big-O Complexity:
       As the name suggests, searching for a value in a binary tree is a
       binary process. Thus search is O(log n).

    """
    def __init__(self, root):
        """ creates a new instance of a binary tree. """
        self.key = root
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        """ creates a new binary tree and installs it as the left child of the
        current node.

        Args:
            new_node (unknown value) : the new node key value
        """
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node):
        """ creates a new binary tree and installs it as the right child of the
        current node.

        Args:
            new_node (unknown value) : the new node key value
        """
        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_right_child(self):
        """ returns the binary tree corresponding to the right child of the
        current node.

        Args:
            self (BinaryTree) : the parent node of which we want the right
            child

        Returns:
            right_child (BinaryTree) : the right child node
        """
        return self.right_child

    def get_left_child(self):
        """ returns the binary tree corresponding to the left child of the
        current node.

        Args:
            self (BinaryTree) : the parent node of which we want the left
            child

        Returns:
            left_child (BinaryTree) : the left child node
        """
        return self.left_child

    def set_root_val(self, obj):
        """ stores the object in parameter val in the current node.

        Args:
            self (BinaryTree) : the parent node of which we want the left
            child
            obj (unknown type) : the object to be used as the key
        """
        self.key = obj

    def get_root_val(self):
        """ returns the object stored in the current node.

        Args:
            self (BinaryTree) : the node of which we want to get the key value

        Returns:
            key (unknown type) : the key value of the self node
        """
        return self.key


"""
Notice that in all three of the traversal functions we are simply changing the
position of the print statement with respect to the two recursive function
calls.
"""


def preorder(tree):
    if tree:
        print(tree.get_root_val())
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())


def postorder(tree):
    if tree is not None:
        postorder(tree.get_left_child())
        postorder(tree.get_right_child())
        print(tree.get_root_val())


def inorder(tree):
    if tree is not None:
        inorder(tree.get_left_child())
        print(tree.get_root_val())
        inorder(tree.get_right_child())


r = BinaryTree('a')
print(r.get_root_val())
print(r.get_left_child())
r.insert_left('b')
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right('c')
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val('hello')
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val('c')

print("\n PREORDER TRAVERSAL")
preorder(r)

print("\n POSTORDER TRAVERSAL")
postorder(r)

print("\n INORDER TRAVERSAL")
inorder(r)
