""" Using the PEP 8 Style Guide for Python Code:
https://www.python.org/dev/peps/pep-0008/ and python linters """


def shell_sort(a_list):
    """The shell sort, sometimes called the “diminishing increment sort,”
    improves on the insertion sort by breaking the original list into a number
    of smaller sublists, each of which is sorted using an insertion sort. The
    unique way that these sublists are chosen is the key to the shell sort.
    Instead of breaking the list into sublists of contiguous items, the shell
    sort uses an increment i, sometimes called the gap, to create a sublist by
    choosing all items that are i items apart.

    Note:
        By performing the earlier sublist sorts, we have now reduced the total
        number of shifting operations necessary to put the list in its final
        order. For this case, we need only four more shifts to complete the
        process.

    Args:
        a_list (list(int)) : the unordered list to be sorted

    Big-O Complexity:
        Tends to fall somewhere between 𝑂(𝑛) and 𝑂(𝑛2)
    """
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        print("After increments of size", sublist_count, "The list is", a_list)
        sublist_count = sublist_count // 2


def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
            a_list[position] = current_value


a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shell_sort(a_list)
print(a_list)
