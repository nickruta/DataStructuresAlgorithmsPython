""" Using the PEP 8 Style Guide for Python Code:
https://www.python.org/dev/peps/pep-0008/ and python linters """


def selection_sort(a_list):
    """The selection sort improves on the bubble sort by making only one
    exchange for every pass through the list. In order to do this, a selection
    sort looks for the largest value as it makes a pass and, after completing
    the pass, places it in the proper location. As with a bubble sort, after
    the first pass, the largest item is in the correct place. After the second
    pass, the next largest is in place. This process continues and requires
    𝑛 − 1 passes to sort 𝑛 items, since the final item must be in place after
    the (𝑛 − 1)st pass.

    Args:
        a_list (list(int)) : the unordered list to be sorted

    Big-O Complexity:
        You may see that the selection sort makes the same number of
        comparisons as the bubble sort and is therefore also 𝑂(𝑛2). However,
        due to the reduction in the number of exchanges, the selection sort
        typically executes faster in benchmark studies. In fact, for our list,
        the bubble sort makes 20 exchanges, while the selection sort makes only
        8.

    """
    for fill_slot in range(len(a_list) - 1, 0, -1):
        pos_of_max = 0
        for location in range(1, fill_slot + 1):
            if a_list[location] > a_list[pos_of_max]:
                pos_of_max = location
        temp = a_list[fill_slot]
        a_list[fill_slot] = a_list[pos_of_max]
        a_list[pos_of_max] = temp


a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selection_sort(a_list)
print(a_list)
