'''
Binary search for the answer (integer version).
'''

def bsearch_answer(condfunc, start, end) :
    '''
    Find the first integer in the range [start, end) that
    satisfies the condition function condfunc(x).
    Note that confunc(x) is a boolean function.
    Return that integer.
    We assume that there is at least one mumber in the range that
    satisfies the function, and that if x satisfies, then y > x also
    satisfies the function.
    '''
    if end - start == 1 :
        # The range is of length 1. Therefore, by our assumption
        # the number satisfies the function.
        return start
    mid = (start+end-1)//2
    if condfunc(mid) :
        # The mid satisfies the condition. Test mid and things before.
        return bsearch_answer(condfunc, start, mid+1)
    else :
        # The mid DOES NOT satisfies the condition.
        # Test the things strictly after the mid.
        return bsearch_answer(condfunc, mid+1, end)

if __name__ == '__main__' :
    assert bsearch_answer(lambda x: x > 10, 1, 100) == 11
    assert bsearch_answer(lambda x: x > 0, 1, 1000) == 1
    assert bsearch_answer(lambda x: False, 1, 1000) == 999