```python
L = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
U = UnionFindSet(L)
U.union('a', 'g')
U.union('g', 'c')
U.union('a', 'e')
U.group('a') == U.group('g') == U.group('c')
=> True
U.group('f') == U.group('d')
=> False
U.group('a') == U.group('d')
=> False
U.union('b', 'g')
U.get_set('g')
=> ['a', 'c', 'g', 'b', 'e']
```
- Support amortized O(log n) for union and find. We do not implement union by rank.
- Support finding all elements a the set using BFS in amortized(log n + k) where k is the size of the result set.