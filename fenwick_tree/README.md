Fenwick Tree or Binary Indexed Tree is the data structure that can compute dynamic range sum. It is often used instead of the segment tree because it is faster and much shorter to write.

```python
>>> testarr = [1,2,3,4,5]
>>> tree = FenwickTree(testarr) # create the fenwick tree with the testarr
>>> tree.rangesum(1, 5)
15 # sum from position 1..5 is 15
>>> tree.rangesum(1, 1)
1 # sum of the position 1 itself is 1.
>>> tree.rangesum(3, 5)
12 # 3+4+5 = 12. You see that we use inclusive range starting with 1 here.
>>> tree.update(1, 5) # add 5 to position 1
>>> tree.rangesum(1, 5)
20
```