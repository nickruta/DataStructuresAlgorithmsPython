""" Using the PEP 8 Style Guide for Python Code:
https://www.python.org/dev/peps/pep-0008/ and python linters """


def bubble_sort(a_list):
    """The bubble sort makes multiple passes through a list. It compares
    adjacent items and ex- changes those that are out of order. Each pass
    through the list places the next largest value in its proper place. In
    essence, each item “bubbles” up to the location where it belongs.

    Note: A bubble sort is often considered the most inefficient sorting
    method since it must exchange items before the final location is known.
    These “wasted” exchange operations are very costly.

    Args:
        a_list (list(int)) : the unordered list to be sorted

    Big-O Complexity:
        The total number of comparisons is the sum of the first 𝑛 − 1 integers.
        Recall that the sum of the first 𝑛 integers is 1𝑛2 + 1𝑛. The sum of the
        first 𝑛 − 1 integers is 1/2(𝑛2) + 1/2(𝑛 − 𝑛), which is 1/2(𝑛2 − 1/2𝑛).
        This is still 𝑂(𝑛2) comparisons. In the best case, if the list is
        already ordered, no exchanges will be made. However, in the worst case,
        every comparison will cause an exchange. On average, we exchange half
        of the time.

    """
    for pass_num in range(len(a_list) - 1, 0, -1):
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                temp = a_list[i]
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = temp


a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubble_sort(a_list)
print(a_list)
