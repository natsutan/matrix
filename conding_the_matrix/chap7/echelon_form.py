import numpy as np


def calc_rowlist(a):
    r = []
    for row in a:
        try:
            pos = row.nonzero()[0][0]
            r.append(pos)
        except IndexError:
            r.append(-1)
    return r


def conv_echelon_form(a):
    row_list = calc_rowlist(a)
    b = []
    for c in range(len(row_list)):
        first = True
        first_pivot = []
        for v, i in zip(row_list, range(len(row_list))):
            if c == v:
                pivot = a[i]
                if first:
                    # 要素が全て０じゃなければ追加
                    if len(np.where(pivot != 0)[0]) != 0:
                        first_pivot = pivot
                        first = False
                        b.append(pivot)
                else:
                    # ピボット行以外の処理
                    mult = a[i][c] / first_pivot[c]
                    a[i] -= mult * first_pivot
                    row_list = calc_rowlist(a)

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