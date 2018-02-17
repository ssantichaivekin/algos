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

    # normal test cases
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
    from random import randint
    x = set([ randint(0,1000) for i in range(1000) ])
    y = UnionFindSet(x)
    for 
    

