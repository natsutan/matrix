import numpy as np


def calc_rowlist(a):
    r = []
    for row in a:
        pos = row.nonzero()[0][0]
        r.append(pos)
    return r


def conv_echelon_form(a):
    row_list = calc_rowlist(a)
    b = []
    for c in range(len(row_list)):
        try:
            idx = row_list.index(c)
            pivot = a[idx]
            b.append(pivot)
        except ValueError:
            continue

    return np.array(b, dtype=np.float32)

alist = [[0, 2, 3, 4, 5],
         [0, 0, 0, 3, 2],
         [1, 2, 3, 4, 5],
         [0, 0, 0, 6, 7],
         [0, 0, 0, 9, 8]]

A = np.array(alist, dtype=np.float32)
B = conv_echelon_form(A)

print(A)
print(B)