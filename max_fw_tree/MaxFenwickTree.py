'''
Defines the maximum fenwick tree to find the max/min of range 1..x x <= n.
The fenwick tree is just like a normal fenwick tree except that it maintains
the invariant that keeps the maximum of the range each element covers. (Imagine
a normal fenwick tree, now instead of keeping the sum, we keep the max instad.)
'''

class MaxFenwickTree :

    def __init__(self, l) :
        '''
        Initialize the fenwick tree with 0 * size.
        or initialize the fenwick tree with the list.
        '''
        if type(l) == int :
            size = l
            self.empty_init(size)
        elif type(l) == list :
            size = len(l)
            self.empty_init(size)
            for i, val in zip(range(1, size+1), l) :
                self.update(i, val)
    
    def empty_init(self, size) :
        '''
        Initialize the tree with empty values.
        '''
        self.tree = [0 for i in range(size + 1)]
        self.vals = [0 for i in range(size + 1)]
        self.size = size
    
    def evalmax(self, pos) :
        '''
        Reevaluate the position pos to reflect the maximum
        according to the invariant.
        Return whether the value is changed or not.
        '''
        initial_val = self.tree[pos]
        # Bottom is the scope of the search.
        bottom = pos - (pos & -pos)
        # Of course, the value in that position should be compared.
        maxval = self.vals[pos]
        # start with pos - 1.
        # curr : current
        curr = pos - 1
        while curr > bottom :
            maxval = max(maxval, self.tree[curr])
            curr -= curr & -curr
        # set that position of the tree to maxval.
        self.tree[pos] = maxval

        # If the value is changed, return true.
        return maxval != initial_val


    def update(self, pos, val) :
        '''
        Update (change) a position with a value, and then update
        the tree correspondingly to maintain the invariant.
        '''
        self.vals[pos] = val
        while pos <= self.size :
            is_changed = self.evalmax(pos) # this line changes the tree
            if not is_changed :
                break
            pos += pos & -pos
            
    
    def maxrange(self, pos) :
        '''
        Max of 1..j
        '''
        maxval = self.tree[pos]
        while pos > 0 :
            maxval = max(maxval, self.tree[pos])
            pos -= pos & -pos
        return maxval
    
    def __repr__(self) :
        return str(self.tree)

if __name__ == '__main__' :
    '''
    Tests:
    '''

    from random import randint
    n = 1000
    q = 1000
    testarr = [ randint(1, 10000) for i in range(n) ]
    tree = MaxFenwickTree(testarr)
    testarr = [0] + testarr
    for i in range(q) :
        # we will both update the tree and ask a question
        # update the tree :
        index, newval = randint(1, n), randint(1, 10000)
        testarr[index] = newval
        tree.update(index, newval)

        # ask a question :
        j = randint(1, n)
        correct_ans = max(testarr[1:j+1]) # get max 1..j
        attempt_ans = tree.maxrange(j)

        assert correct_ans == attempt_ans




    

            
