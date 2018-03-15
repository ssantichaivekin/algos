'''
This implements a brute force solution for the horsemove problem.

Problem statement, given point a denoted (xa, ya) and point b denoted
(xb, yb) in I^2, find the number of minimum move that a horse chess piece
need in order to move from a -> b.
'''

from queue import Queue

directions = [(1, 2), (1, -2), (-1, 2), (-1, -2),
              (2, 1), (2, -1), (-2, 1), (-2, -1)]

def horsemove(a, b) :
    '''
    Return the number of moves that a horse chess piece need in order
    to move from point a to point b.
    '''
    # this is our visited points for the BFS
    visited = set()
    # this is the BFS queue
    q = Queue()
    # The queue must keep the new position and the distance.
    # in the form of (pos, dist)
    q.put((a, 0))
    while True :
        pos, dist = q.get()
        # print(pos)
        if not pos in visited :
            if pos == b :
                return dist
            for direction in directions :
                px, py = pos
                dx, dy = direction
                newpos = px+dx, py+dy
                q.put((newpos, dist+1))






if __name__ == '__main__' :
    a = (0, 0)
    b = (-2, -1)
    assert horsemove(a, b) == 1
    a = (0, 0)
    b = (0, 1)
    assert horsemove(a, b) == 3
    a = (-2, -1)
    b = (0, -1)
    assert horsemove(a, b) == 2
    a = (1, 1)
    b = (3, 3)
    assert horsemove(a, b) == 4





