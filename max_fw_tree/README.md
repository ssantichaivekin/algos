This is a maximum-finding variant of the fenwick tree (binary indexed tree).
It supports finding the maximum from index 1..j in O(log n) (we cannot do i..j 
for a full maximum in range problem, go for a segment tree). The replace is a
little bit slower with complexity O(log^2 n).

```python
>>> x = MaxFenwickTree(9)
>>> x = MaxFenwickTree([1, 3, 2, 2, 9, 4, 5])
>>> x.maxrange(3)
3
>>> x.maxrange(1)
1
>>> x.maxrange(6)
9
>>> x.update(1, 5)
>>> x. maxrange(7)
9
>>> x.update(5, 0)
>>> x.maxrange(7)
5
>>> x.update(1, 0)
>>> x.maxrange(4)
3
```