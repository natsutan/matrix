# coding matrix
# task 1.4.17

import math
from myplot import ploti

S = set()

for x in range(20):
    w = math.e ** (2*math.pi*1j/(x+1))
    S.add(w)

ploti(S, file='task1.4.17.png')