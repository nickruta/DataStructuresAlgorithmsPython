""" Using the PEP 8 Style Guide for Python Code:
https://www.python.org/dev/peps/pep-0008/ and python linters """

from stack import Stack


def parChecker(symbolString):
    """ This function, parChecker, assumes that a Stack class is available and
    returns a boolean result as to whether the string of parentheses is
    balanced.

    Note: the boolean variable balanced is initialized to True as there is no
    reason to assume otherwise at the start. If the current symbol is (, then
    it is pushed on the stack (lines 9–10). Note also in line 15 that pop
    simply removes a symbol from the stack. The returned value is not used
    since we know it must be an opening symbol seen earlier. At the end
    (lines 19–22), as long as the expression is balanced and the stack has
    been completely cleaned off, the string represents a correctly balanced
    sequence of parentheses.

    Args:
        symbolString (str) : The string of parenthesis to be parsed.

    Returns:
        boolean : True if balanced, False if not.
    """
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                s.pop()

        index = index + 1

    if balanced and s.is_empty():
        return True
    else:
        return False


print(parChecker('((()))'))
print(parChecker('(()'))
