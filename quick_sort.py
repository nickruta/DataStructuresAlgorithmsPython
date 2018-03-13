""" Using the PEP 8 Style Guide for Python Code:
https://www.python.org/dev/peps/pep-0008/ and python linters """


def quickSort(a_list):
    """The quick sort uses divide and conquer to gain the same advantages as
    the merge sort, while not using additional storage. As a trade-off,
    however, it is possible that the list may not be divided in half. When
    this happens, we will see that performance is diminished.

    A quick sort first selects a value, which is called the pivot value.
    Although there are many different ways to choose the pivot value, we will
    simply use the first item in the list. The role of the pivot value is to
    assist with splitting the list. The actual position where the pivot value
    belongs in the final sorted list, commonly called the split point, will be
    used to divide the list for subsequent calls to the quick sort.

    Args:
        a_list (list(int)) : the unordered list to be sorted

    Big-O Complexity:
        To analyze the quickSort function, note that for a list of length n, if
        the partition always occurs in the middle of the list, there will again
        be logn divisions. In order to find the split point, each of the n
        items needs to be checked against the pivot value. The result is nlogn.
        In addition, there is no need for additional memory as in the merge
        sort process.

        Unfortunately, in the worst case, the split points may not be in the
        middle and can be very skewed to the left or the right, leaving a very
        uneven division. In this case, sorting a list of n items divides into
        sorting a list of 0 items and a list of n−1 items. Then sorting a list
        of n−1 divides into a list of size 0 and a list of size n−2, and so on.
        The result is an O(n2) sort with all of the overhead that recursion
        requires.
    """
    quickSortHelper(alist, 0, len(alist)-1)


def quickSortHelper(alist, first, last):
    if first < last:

        splitpoint = partition(alist, first, last)

        quickSortHelper(alist, first, splitpoint-1)
        quickSortHelper(alist, splitpoint+1, last)


def partition(alist, first, last):
    pivotvalue = alist[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quickSort(alist)
print(alist)
