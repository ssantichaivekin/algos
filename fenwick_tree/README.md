A Fenwick Tree.

```python
>>> testarr = [1,2,3,4,5]
>>> tree = FenwickTree(testarr)
>>> tree.rangesum(1, 5)
15
>>> tree.rangesum(1, 1)
1
>>> tree.rangesum(3, 5)
12
```