""" Using the PEP 8 Style Guide for Python Code:
https://www.python.org/dev/peps/pep-0008/ and python linters """


def short_bubble_sort(a_list):
    """The short bubble sort makes multiple passes through a list. It compares
    adjacent items and exchanges those that are out of order. Each pass
    through the list places the next largest value in its proper place. In
    essence, each item “bubbles” up to the location where it belongs. It
    modifies a standard bubble sort by stopping short when no exchanges are
    left to be made.

    Note: A bubble sort is often considered the most inefficient sorting method
    since it must exchange items before the final location is known. These
    “wasted” exchange operations are very costly. However, because the bubble
    sort makes passes through the entire unsorted portion of the list, it has
    the capability to do something most sorting algorithms cannot. In
    particular, if during a pass there are no exchanges, then we know that the
    list must be sorted. A bubble sort can be modified to stop early if it f
    inds that the list has become sorted. This means that for lists that
    require just a few passes, a bubble sort may have an advantage in that it
    will recognize the sorted list and stop.

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
    exchanges = True
    pass_num = len(a_list) - 1
    while pass_num > 0 and exchanges:
        exchanges = False
        for i in range(pass_num):
            if a_list[i] > a_list[i + 1]:
                exchanges = True
                temp = a_list[i]
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = temp
    pass_num = pass_num - 1


a_list = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
short_bubble_sort(a_list)
print(a_list)
