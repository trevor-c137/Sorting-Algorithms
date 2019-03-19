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
def linear_merge(list1, list2):
    new_listk = list1+list2 
    for a in range(len(new_listk)):
        for b in range(len(new_listk)-1-a):
            if new_listk[b] > new_listk[b+1]:
                new_listk[b], new_listk[b+1] = new_listk[b+1], new_listk[b] 
    return new_listk
def merge_sort(items):

    dist = len(items)
    if dist == 1:
        return items

    mid_v = int(dist / 2)
    list1 = merge_sort(items[:mid_v])
    list2 = merge_sort(items[mid_v:])

    return linear_merge(list1, list2)


def quick_sort(items,index=-1):

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
