import numpy as np

# 4bitの最大値
QUANTIZE_BIT = 2
MAX_VALUE = (2 ** QUANTIZE_BIT) - 1


def deQuantize(arr, min, max):
    """量子化を元に戻す"""
    gain = (max - min) / MAX_VALUE
    return arr * gain + min


def Quantize(arr, min, max):
    range = max - min
    range_scale = range / MAX_VALUE
    return (arr - min) / range_scale


def q_add(a_qt, a_min, a_max, b_qt, b_min, b_max):
    gain = (b_max - b_min) / (a_max - a_min)
    min = a_min + b_min
    max = a_max + b_max
    c_qt = b_qt * gain + a_qt
    q_param = (max - min) / MAX_VALUE
    c_qt /= q_param

    return c_qt, min, max


def q_mul(a_qt, a_min, a_max, b_qt, b_min, b_max):
    gain_a = (a_max - a_min) / MAX_VALUE
    gain_b = (b_max - b_min) / MAX_VALUE
    offset_a = a_min
    offset_b = b_min
    p_gagb = gain_a * gain_b
    p_gaob = gain_a * offset_b
    p_gboa = gain_b * offset_a
    p_oaob = offset_a * offset_b
    min = p_oaob
    max = a_max * b_max
    q_param = (max - min) / MAX_VALUE

    # start vector alu
    AB = p_gagb * a_qt * b_qt
    gaob_A = a_qt * p_gaob
    gboa_B = b_qt * p_gboa

    c_qt = AB + gaob_A + gboa_B
    c_qt /= q_param

    return c_qt, min, max

# test
A = np.array([0, 1, 2, 3])
a_max = 3
a_min = 0
A_q = Quantize(A, a_min, a_max)
print(A_q)

B = np.array([4, 6, 8, 10])
b_max = 10
b_min = 4
B_q = Quantize(B, b_min, b_max)
print(B_q)

#add
print("ADD")
C_q, c_min, c_max = q_add(A_q, a_min, a_max, B_q, b_min, b_max)
print(C_q)
print(deQuantize(C_q, c_min, c_max))

#mul
print("MUL")
C_q, c_min, c_max = q_mul(A_q, a_min, a_max, B_q, b_min, b_max)
print(C_q)
print(deQuantize(C_q, c_min, c_max))

# 1/3
D_q = B_q
d_min = b_min / 3.0
d_max = b_max / 3.0
print(deQuantize(D_q, d_min, d_max))
