""" Using the PEP 8 Style Guide for Python Code:
https://www.python.org/dev/peps/pep-0008/ and python linters """


from deque import Deque


def palindrome_checker(a_string):
    """ A palindrome is a string that reads the same forward and backward,
    for example, radar, toot, and madam. This function takes input as a string
    of characters and checks whether it is a palindrome.

    Args:
        a_string (str) : The string to be checked.

    Returns:
        boolean : True if a palindrome, False if not.
    """
    char_deque = Deque()
    for ch in a_string:
        char_deque.add_rear(ch)
        still_equal = True
    while char_deque.size() > 1 and still_equal:
        first = char_deque.remove_front()
        last = char_deque.remove_rear()
        if first != last:
            still_equal = False
    return still_equal


print(palindrome_checker("radar"))
print(palindrome_checker("notpalindrome"))
