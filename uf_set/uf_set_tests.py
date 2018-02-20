'''
We use assert to test the functions. If it runs correctly it will not
output anything.
'''

from random import randint
import matplotlib.pyplot as plt
plt.xkcd()
from timeit import timeit
from numpy import mean
from UnionFindSet import UnionFindSet

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

def generated_test_cases(test_cases, test_size, query_size) :
    '''
    Test the uf-set using randomized generated test cases.
    '''
    for t in range(test_cases) :
        x = UnionFindSet([ i for i in range(test_size) ])
        y = []
        for i in range(query_size) :
            p1 = randint(0, test_size-2)
            p2 = randint(p1, test_size-1)
            x.union(p1, p2)
            # print('Union:', p1, p2)
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
        # for i in range(len(y)) :
            # print('Sets %d in y:' % (i+1), y[i])
        
        # Now check whether things are in the same
        # set
        for i in range(query_size) :
            p1 = randint(0, test_size-2)
            p2 = randint(p1, test_size-1)
            # print('Test %d:' % (i+1), p1, p2, end=' ')
            lo1 = -1
            lo2 = -1

            for i in range(len(y)) :
                if p1 in y[i] :
                    lo1 = i
                if p2 in y[i] :
                    lo2 = i
            if p1 == p2 or (lo1 != -1 and lo1 == lo2) :
                samegroup = True
                # print('samegroup')
            else :
                samegroup = False
                # print('not samegroup')
            
            assert (x.group(p1) == x.group(p2)) == samegroup    

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

def plot_ufset(sizes, runs) :
    '''
    Plot the runtime of the set.
    '''
    
    cmd = 'timing_snippet(%d, %d)'
    values = []
    for s in sizes :
        print('Calculating: n =', s)
        values += [ timeit(cmd % (s, s/2), number=runs, globals=globals())/runs]

    plt.plot(sizes, values)
    plt.xlabel('size, queries = sizes / 2')
    plt.ylabel('runtime (s)')
    plt.title('Performance of the union-find disjoint-set (%d runs)' % (runs))
    plt.show()

if __name__ == '__main__' :
    normal_test_cases()
    generated_test_cases(1, 1000, 600)

    runs = 50
    sizes = [ x * 10000 for x in range(1,16) ]
    plot_ufset(sizes, runs)