""" Using the PEP 8 Style Guide for Python Code:
https://www.python.org/dev/peps/pep-0008/ and python linters """


def merge_sort(a_list):
    """The merge_sort function begins by asking the base
    case question. If the length of the list is less than or equal to one,
    then we already have a sorted list and no more processing is necessary.
    If, on the other hand, the length is greater than one, then we use the
    Python slice operation to extract the left and right halves. It is
    important to note that the list may not have an even number of items. That
    does not matter, as the lengths will differ by at most one.

    Note:
        It is important to notice that the mergeSort function requires extra
        space to hold the two halves as they are extracted with the slicing
        operations. This additional space can be a critical factor if the list
        is large and can make this sort problematic when working on large data
        sets.

    Args:
        a_list (list(int)) : the unordered list to be sorted

    Big-O Complexity:
        In order to analyze the mergeSort function, we need to consider the two
        distinct processes that make up its implementation. First, the list is
         split into halves. We already computed (in a binary search) that we
         can divide a list in half logn times where n is the length of the
         list. The second process is the merge. Each item in the list will
         eventually be processed and placed on the sorted list. So the merge
         operation which results in a list of size n requires n operations. The
         result of this analysis is that logn splits, each of which costs n for
         a total of nlogn operations. A merge sort is an O(nlogn) algorithm.

        Recall that the slicing operator is O(k) where k is the size of the
        slice. In order to guarantee that merge_sort will be O(n log n) we will
        need to remove the slice operator. Again, this is possible if we simply
        pass the starting and ending indices along with the list when we make
        the recursive call.
    """
    print("Splitting ", a_list)
    if len(a_list) > 1:
        mid = len(a_list)//2
        lefthalf = a_list[:mid]
        righthalf = a_list[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                a_list[k] = lefthalf[i]
                i = i+1
            else:
                a_list[k] = righthalf[j]
                j = j+1
            k = k+1

        while i < len(lefthalf):
            a_list[k] = lefthalf[i]
            i = i+1
            k = k+1

        while j < len(righthalf):
            a_list[k] = righthalf[j]
            j = j+1
            k = k+1
    print("Merging ", a_list)


a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
merge_sort(a_list)
print(a_list)
