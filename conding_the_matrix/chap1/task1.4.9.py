# coding matrix
# task 1.4.8
# rotate by 90 deg and scaled by 1/2, and then shift down 1 and to the right 2.

from myplot import ploti

S = {2+2j, 3+2j, 1.75+1j, 2.25+1j, 2.75+1j, 3+1j, 3.25+1j}
Z_shift = 2-1j

ploti({(z * -1j) * 0.5 + Z_shift for z in S}, size=4, file='task1.4.9.png')
