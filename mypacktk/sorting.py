def bubble_sort(items):

    '''Return array of items, sorted in ascending order
    Args :
          items is a list or array of strings or int
    Return: a sorted list in an ascending order

    Examples:
        >>> bubble_sort([10,1,5])
        [1,5,10]
        >> bubble_sort([7,19,2])
        [2,7,19]

    '''
    for i in range(len(items)):
        for j in range(len(items)-(1+i)):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
    return items

def linear_merge(list1):
    for a in range(len(list1)):
        for b in range(len(list1)-1-a):
            if list1[b] > list1[b+1]:
                list1[b], list1[b+1] = list1[b+1],list1[b]
    return list1


def quick_sort(items):

    """
     quick sort algorithm takes an unsorted list of numbers.
     returns a list in ascending order.

    Args:
        items : list
        list of unordered numbers

    Returns:
    list
        liist of elements in items in ascending order

    Example :

    Examples:
        >>> bubble_sort([10,1,5])
        [1,5,10]
        >> bubble_sort([7,19,2])
        [2,7,19]
    """
    #index number at which to choose the split value


    index=-1

    if len(items) <= 1:
        return items

    pivot = items[index]
    small = []
    large = []
    dup = []
    for i in items:
        if i < pivot:
            small.append(i)
        elif i > pivot:
            large.append(i)
        elif i == pivot:
            dup.append(i)

    small = quick_sort(small)
    large = quick_sort(large)

    return small + dup + large
