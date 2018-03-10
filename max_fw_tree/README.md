This is a maximum-finding variant of the fenwick tree (binary indexed tree).
It supports finding the maximum from index 1..j in O(log n) (we cannot do i..j 
for a full maximum in range problem, go for a segment tree). The replace is a
little bit slower with complexity O(log^2 n).

