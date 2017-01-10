# coding matrix
# my library

import matplotlib.pyplot as plt

def ploti(S, size = 1, file = "output.png", xrange = [-5, 5], yrange = [-5, 5]):
    """ plot imarginary"""
    fig = plt.figure()

    ax = fig.add_subplot(1, 1, 1)

    x = []
    y = []
    for i in S:
        x.append(i.real)
        y.append(i.imag)

    ax.scatter(x, y, s=size)

    ax.set_title('complex plane')
    ax.set_xlabel('real axis')
    ax.set_ylabel('imaginary axis')

    xmax = xrange[1]
    xmin = xrange[0]
    ymax = yrange[1]
    ymin = yrange[0]

    plt.xlim(xmin, xmax)
    plt.ylim(ymin, ymax)
    plt.grid(True)
    plt.hlines(0, xmin, xmax)
    plt.vlines(0, ymin, ymax)

    plt.savefig(file)
    plt.show()