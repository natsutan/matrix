# coding the matrix
# task 2.5.4

from myplot import plot

def scalar_vector_mult(alpha, v):
    return [alpha*v[i] for i in range(len(v))]

L = [[2, 2], [3, 2], [1.75, 1], [2, 1], [2.25, 1], [2.5, 1], [2,75, 1], [3, 1], [3.25, 1]]

L2 = [scalar_vector_mult(0.5, v) for v in L]
L3 = [scalar_vector_mult(-0.5, v) for v in L2]

L2.extend(L3)

plot(L2, size=4, file='task2.5.4.4.png')

