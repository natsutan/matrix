# coding the matrix
# task 2.4.3
from myplot import plot

def add2(v, w):
    return [v[0] + w[0], v[1] + w[1]]

L = [[2, 2], [3, 2], [1.75, 1], [2, 1], [2.25, 1], [2.5, 1], [2,75, 1], [3, 1], [3.25, 1]]

plot([add2(v, [1, 2]) for v in L], size=4, file='task2.4.3.png')
