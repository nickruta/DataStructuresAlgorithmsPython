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

        Args:
            alist (list(int)) : the ordered list to be searched
            item (int) : the item to be searched for

        Returns:
            found (boolean) : True if found, False otherwise.
    """
    first = 0
    last = len(alist)-1
    found = False
    while first <= last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1

    return found


testlist = [0, 1, 2, 8, 12, 17, 19, 32, 42]
print(binarySearch(testlist, 4))
print(binarySearch(testlist, 12))
