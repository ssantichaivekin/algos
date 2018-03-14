A mock file system. A directory have a name and a comment.

Haven't tested the comment part yet.

```python
>>> _pwd()
>>> _mkdir('sub1')
>>> _mkdir('sub2')
>>> _mkdir('sub3')
>>> set(_ls())
{'sub1', 'sub2', 'sub3'}
>>> _exec('sub1', _mkdir, 'sub11')
>>> _exec('sub1', _mkdir, 'sub12')
>>> _exec('sub1', _mkdir, 'sub13')
>>> set(_exec('sub1', _ls))
{'sub11', 'sub12', 'sub13'}
>>> _cd('sub1')
>>> _pwd()
'/root/sub1/'

```

In hindsight, we should have created File class and Directory class.