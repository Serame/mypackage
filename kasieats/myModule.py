def getMultiples(x,items):
    """
    Return the multiples of x items in an array, in desc order.

    Args:
        item (array): list or array-like object
        x (int): num of items to return

    Return:
        array: multipes of x sorted in desc order

    Egs:
        >>> getMultiples(5,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
        [5,10,15,20]
    """

    result = list(filter(lambda n:n%x == 0, items))

    return result

