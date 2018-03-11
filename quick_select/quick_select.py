'''
Implements quickselect.
'''
from random import randint

def quickselect(arr, i) :
    '''
    Return the ith element of the sorted array.
    Note that 0 <= i < len(arr).
    '''
    pivot = arr[randint(0, len(arr)-1)]
    lower = list(filter(lambda x: x < pivot, arr))
    equal = list(filter(lambda x: x == pivot, arr))
    higher = list(filter(lambda x: x > pivot, arr))
    
    if i < len(lower) :
        # The answer is in the lower arr.
        return quickselect(lower, i)
    elif i < len(lower) + len(equal) :
        # The answer is in the equal arr.
        return equal[0]
    else :
        # The answer is in the higher arr.
        i -= len(lower) + len(equal)
        return quickselect(higher, i)

if __name__ == '___main___' :

    testarr = [0, 1, 2, 3, 4, 5]
    assert quickselect(testarr, 3) == 3
    assert quickselect(testarr, 1) == 1
    assert quickselect(testarr, 5) == 5
    assert quickselect(testarr, 0) == 0

    testarr = [5, 6, 2, 1, 3, 4]
    assert quickselect(testarr, 3) == 4
    assert quickselect(testarr, 1) == 2
    assert quickselect(testarr, 5) == 6
    assert quickselect(testarr, 0) == 1
