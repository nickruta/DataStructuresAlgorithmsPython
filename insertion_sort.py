""" Using the PEP 8 Style Guide for Python Code:
https://www.python.org/dev/peps/pep-0008/ and python linters """


def insertion_sort(a_list):
    """The insertion sort, although still 𝑂(𝑛2), works in a slightly different
    way. It always maintains a sorted sublist in the lower positions of the
    list. Each new item is then “inserted” back into the previous sublist such
    that the sorted sublist is one item larger.

    Note:
        One note about shifting versus exchanging is also important. In
        general, a shift operation requires approximately a third of the
        processing work of an exchange since only one assignment is performed.
        In benchmark studies, insertion sort will show very good performance.

    Args:
        a_list (list(int)) : the unordered list to be sorted

    Big-O Complexity:

        The implementation of insertion_sort shows that there are again 𝑛 − 1
        passes to sort 𝑛 items. The iteration starts at position 1 and moves
        through position 𝑛 − 1, as these are the items that need to be inserted
        back into the sorted sublists. It performs a shift operation that
        moves a value up one position in the list, making room behind it for
        the insertion. Remember that this is not a complete exchange as
        performed in bubble sort.

        The maximum number of comparisons for an insertion sort is the sum of
        the first 𝑛 − 1 integers. Again, this is 𝑂(𝑛2). However, in the best
        case, only one comparison needs to be done on each pass. This would be
        the case for an already sorted list.
    """
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
    a_list[position] = current_value


a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertion_sort(a_list)
print(a_list)
