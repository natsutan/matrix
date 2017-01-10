# coding the matrix
# exercise 2.4.7
# Draw a diagram illustrating [-2, 4] + [1, 2]
import matplotlib.pyplot as plt


def addn(v, w):
    return [x+y for (x,y) in zip(v,w)]

a = [-2, 4]
b = [1, 2]
c = addn(a, b)

plt.figure()

plt.quiver(0, 0, a[0], a[1], angles='xy', scale_units='xy',scale=1)
plt.quiver(a[0], a[1], b[0], b[1], angles='xy', scale_units='xy',scale=1)
plt.quiver(0, 0, c[0], c[1], angles='xy', scale_units='xy',scale=1)


plt.xlim(-5, 5)
plt.ylim(-5, 8)
plt.grid(True)
plt.hlines(0, -5, 5)
plt.vlines(0, -5, 8)

plt.savefig('exer2.4.7.png')

plt.show()