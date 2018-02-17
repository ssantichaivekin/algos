from queue import Queue

class UnionFindSet :
    '''
    A UnionFindSet is a union find disjoint set object.
    It supports __init__ that assigns each element to
    a unique group, numbered 1..len(elements).
    It supports union of two group ids, find, size of each
    group, and enumerate all groups.
    '''

    def __init__(self, l) :
        '''
        @param l: unique list of elements
        Initialize the union find disjoint set.
        Each element is linked to an id in the normal
        version of union find disjoint set.
        '''
        l = list(l)
        self.list_elem = l
        self.elem_ids = {}
        for i in range(len(l)) :
            self.elem_ids[l[i]] = i
        self.parents = [ i for i in range(len(l)) ]
        self.sizes = [ 1 for i in range(len(l)) ]
        self.children = [ set() for i in range(len(l)) ]
    
    def union(self, elem1, elem2) :
        '''
        Unoin the two elements into the same group.
        The elem2 is merged into the elem1 group.
        '''
        parents = self.parents
        sizes = self.sizes
        children = self.children

        group1 = self.find(elem1)
        group2 = self.find(elem2)

        if group1 != group2 :
            parents[group2] = group1
            sizes[group1] += sizes[group2]
            sizes[group2] = 0
            children[group1].add(group2)

    def find_by_id(self, id1) :
        '''
        Find the id of the set an id of an element belongs to.
        '''
        parents = self.parents
        children = self.children
        while parents[id1] != parents[parents[id1]] :
            children[parents[id1]].remove(id1)
            children[parents[parents[id1]]].add(id1)
            parents[id1] = parents[parents[id1]]
        return parents[id1]
    
    def find(self, elem) :
        '''
        Find the id of the set an element belongs to.
        '''
        elem_ids = self.elem_ids
        if elem in elem_ids :
            id1 = elem_ids[elem]
        else :
            print('No elements in set : ', elem)
            print('elem_ids:', elem_ids)
            return
        return self.find_by_id(id1)

    def group(self, elem) :
        '''
        Same as find.
        '''
        return self.find(elem)
    
    def size_from_id(self, group_id) :
        '''
        Return the size of the group from group id.
        '''
        return self.sizes[group_id]
    
    def size(self, elem) :
        '''
        Return the size of the group from the element
        '''
        return self.size_from_id(self.elem_ids[elem])
    
    def get_set_from_id(self, group_id) :
        '''
        Run a BFS traversal to obtain every elements
        in the set. Returns a list.
        '''
        children = self.children
        visited = set()
        q = Queue()
        q.put(self.find_by_id(group_id))
        while not q.empty() :
            this_id = q.get()
            if not this_id in visited :
                visited.add(this_id)
                for child in children[this_id] :
                    q.put(child)
        
        return [ self.list_elem[group_id] for group_id in visited]
    
    def get_set(self, elem) :
        '''
        Like get_set_from_id but using element.
        '''
        return self.get_set_from_id(self.elem_ids[elem])

if __name__ == '__main__' :
    from random import randint
    import matplotlib.pyplot as plt
    from timeit import timeit
    from numpy import mean
    
    def normal_test_cases() :
        '''
        Easy test cases for the union-find disjoint-set.
        '''
        L = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
        U = UnionFindSet(L)
        U.union('a', 'g')
        U.union('g', 'c')
        U.union('a', 'e')
        assert U.group('a') == U.group('g') == U.group('c')
        assert U.group('f') != U.group('d')
        assert U.group('a') != U.group('d')
        U.union('b', 'g')
        assert set(U.get_set('g')) == set(['a', 'c', 'g', 'b', 'e'])

    # test case generator
    # compare the opeerations with set class provided
    # by standard python library
    def generated_test_cases(test_cases, test_size, query_size) :
        '''
        Generated test cases for the set.
        '''
        for t in range(test_cases) :
            x = UnionFindSet([ i for i in range(test_size) ])
            y = []
            for i in range(query_size) :
                p1 = randint(0, test_size-2)
                p2 = randint(p1, test_size-1)
                x.union(p1, p2)
                print('Union:', p1, p2)
                # union and update y
                lo1 = -1
                lo2 = -1
                for i in range(len(y)) :
                    if p1 in y[i] :
                        lo1 = i
                    if p2 in y[i] :
                        lo2 = i
                if lo1 == -1 and lo2 == -1 :
                    # print(y, '<--', set([p1, p2]))
                    y += [set([p1, p2])]
                if lo1 == -1 and lo2 != -1 :
                    # print(y, y[lo2], '<--', set([p1]))
                    y[lo2] |= set([p1])
                if lo1 != -1 and lo2 == -1 :
                    # print(y, y[lo1], '<--', set([p2]))
                    y[lo1] |= set([p2])
                if lo1 != -1 and lo2 != -1 and lo1 != lo2 :
                    # print(y, y[lo1], '<--', y[lo2], '(removed)')
                    y[lo1] |= y[lo2]
                    y.pop(lo2)
            for i in range(len(y)) :
                print('Sets %d in y:' % (i+1), y[i])
            
            # Now check whether things are in the same
            # set
            for i in range(query_size) :
                p1 = randint(0, test_size-2)
                p2 = randint(p1, test_size-1)
                print('Test %d:' % (i+1), p1, p2, end=' ')
                lo1 = -1
                lo2 = -1

                for i in range(len(y)) :
                    if p1 in y[i] :
                        lo1 = i
                    if p2 in y[i] :
                        lo2 = i
                if p1 == p2 or (lo1 != -1 and lo1 == lo2) :
                    samegroup = True
                    print('samegroup')
                else :
                    samegroup = False
                    print('not samegroup')
                
                assert (x.group(p1) == x.group(p2)) == samegroup    
        
    normal_test_cases()
    generated_test_cases(1, 1000, 600)

    def timing_snippet(test_size, query_size) :
        '''
        Timing snippet fot the timit function.
        '''
        x = UnionFindSet([ i for i in range(test_size) ])
        y = []
        for i in range(query_size) :
            p1 = randint(0, test_size-2)
            p2 = randint(p1, test_size-1)
            x.union(p1, p2)
        for i in range(query_size) :
            p = randint(0, test_size-1)
            x.find(p)

    def plot_ufset() :
        '''
        Plot the runtime of the set.
        '''
        sizes = [ x * 10000 for x in range(1,16) ]
        cmd = 'timing_snippet(%d, %d)'
        values = []
        for s in sizes :
            print('Calculating: n =', s)
            values += [ timeit(cmd % (s, s/2), number=10, globals=globals())/10 ]

        plt.plot(sizes, values)
        plt.xlabel('size, queries = sizes / 2')
        plt.ylabel('runtime (s)')
        plt.show()
    
    plot_ufset()



    

        
        

        
    

