def remove_every_other(lst):
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """

    counter = 0
    new_list = []

    for num in lst:
        if lst.index(num) == counter:
            new_list.append(num)
            counter +=2
    
    return new_list
        