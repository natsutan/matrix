from dicvec import *

def triangular_solve_n(rowlist, b):
    def tri_solve_last(rowlist, b):
        """最後の一行だけ解く"""
        if len(b) == 0:
            return []

        # 一番下の行の計算
        blast = b[-1]
        row = rowlist[-1]
        x = blast / row[-1]

        # 計算結果を元に行列を縮小
        row_new = []
        b_new = []
        for row, b_ori in zip(rowlist[0:-1], b[0:-1]):
            b_sub = row[-1] * x
            row.pop()
            row_new.append(row)
            b_new.append(b_ori - b_sub)

        return [x] + tri_solve_last(row_new, b_new)

    result = tri_solve_last(rowlist, b)
    result.reverse()

    return result


# ここから動作確認
v1 = [[1, 0.5, -2, 4],
     [0,   3,  3,  2],
     [0,   0,  1,  5],
     [0,   0,  0,  2]]

b1 = [-8, 3, -4, 6]

s = triangular_solve_n(v1, b1)
print(s)

v2 = [[2, 3, -4],
      [0, 1, 2],
      [0, 0, 5]]

b2 = [10, 3, 15]

s = triangular_solve_n(v2, b2)
print(s)

v3 = [[1, -3, -2],
      [0, 2, 4],
      [0, 0, -10]]

b3 = [7, 4, 12]

s = triangular_solve_n(v3, b3)
print(s)

