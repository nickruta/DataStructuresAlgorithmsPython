""" Using the PEP 8 Style Guide for Python Code:
https://www.python.org/dev/peps/pep-0008/ and python linters """


def binarySearch(alist, item):
    """This algorithm is a great example of a divide and conquer strategy.
    Divide and conquer means that we divide the problem into smaller pieces,
    solve the smaller pieces in some way, and then reassemble the whole problem
    to get the result. When we perform a binary search of a list, we first
    check the middle item. If the item we are searching for is less than the
    middle item, we can simply perform a binary search of the left half of
    the original list. Likewise, if the item is greater, we can perform a
    binary search of the right half. Either way, this is a recursive call to
    the binary search function passing a smaller list.

    Big-O Complexity:
        When we split the list enough times, we end up with a list that has
        just one item. Either that is the item we are looking for or it is not.
        Either way, we are done. The number of comparisons necessary to get to
        this point is 𝑖 where 𝑛 = 1. Solving for 𝑖 gives us 𝑖 = log 𝑛. The
        maximum 2𝑖 number of comparisons is logarithmic with respect to the
        number of items in the list. Therefore, the binary search
        is 𝑂(log 𝑛).

        One additional analysis issue needs to be addressed. In the recursive
        solution shown below, the recursive call,
        binary_search(a_list[:midpoint],item).
        uses the slice operator to create the left half of the list that is
        then passed to the next invocation (similarly for the right half as
        well). The analysis that we did above assumed that the slice operator
        takes constant time. However, we know that the slice operator in
        Python is actually 𝑂(𝑘). This means that the binary search using slice
        will not perform in strict logarithmic time. Luckily this can be
        remedied by passing the list along with the starting and ending
        indices.

        Args:
            alist (list(int)) : the ordered list to be searched
            item (int) : the item to be searched for

        Returns:
            found (boolean) : True if found, False otherwise.
    """
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binarySearch(alist[:midpoint], item)
            else:
                return binarySearch(alist[midpoint+1:], item)


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))
