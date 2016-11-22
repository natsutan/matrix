# coding the matrix
# task 2.6.9
from myplot import plot

period = 100

pt1 = [3.5, 3]
pt2 = [0.5, 1]

s = []

for a in range(period):
    alpha = (1.0/period) * a
    beta  = 1.0 - alpha
    x = pt1[0] * alpha + pt2[0] * beta
    y = pt1[1] * alpha + pt2[1] * beta
    s.append((x, y))

plot(s, file='task2.6.9.png')