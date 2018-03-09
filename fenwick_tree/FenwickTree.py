def least_significant_digit(num) :
        '''
        The binary least significant digit of a number.
        For example, 3 = 11 so it has the least significant
        digit of 1. 14 = 1110 so it has the least significant
        digit of 10 = 2.
        '''
        return num & -num

class FenwickTree :
    def __init__(self, l) :
        '''
        Initialize the tree with a list or 0 * n.
        '''
        if type(l) == int :
            size = l
            self.tree = [0 for i in range(size+1)]
            self.size = size
        else :
            size = len(l)
            self.tree = [0 for i in range(size+1)]
            self.size = size
            for pos, x in zip(range(1, len(l)+1), l) :
                self.update(pos, x)

    def update(self, pos, val) :
        '''
        Update the position pos in the tree with
        value +val.
        '''
        while pos <= self.size :
            self.tree[pos] += val
            pos += least_significant_digit(pos)
    
    def sum(self, j) :
        '''
        The sum from position 1..j (inclusive)
        '''
        sum = 0
        pos = j
        while pos > 0 :
            sum += self.tree[pos]
            pos -= least_significant_digit(pos)
        return sum

    def rangesum(self, i, j) :
        '''
        Sum of the range i..j (inclusive)
        '''
        return self.sum(j) - self.sum(i-1)
    
    def __repr__(self) :
        return str(self.tree)

if __name__ == '__main__' :
    '''
    Tests :
    '''
    testarr = [1,2,3,4,5]
    tree = FenwickTree(testarr)
    assert tree.rangesum(1, 5) == 15
    assert tree.rangesum(1, 1) == 1
    assert tree.rangesum(3, 5) == 12

    from random import randint
    n = 5000
    t = 500
    testarr = [randint(1,1000) for i in range(n)]
    tree = FenwickTree(testarr)
    for test in range(t) :
        r1 = randint(1, n)
        r2 = randint(r1, n)
        assert tree.rangesum(r1, r2) == sum(testarr[r1-1:r2])
    
