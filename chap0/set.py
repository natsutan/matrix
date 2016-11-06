# set

print({1,1,2,2,3,3})  # {1, 2, 3}
print(len({1,1,2,2,3,3})) # 3
print(sum({1,1,2,2,3,3})) # 6

# 要素のテスト
S = {1, 2, 3}
print(2 in S) # True
print(4 in S) # False

# 和集合、共通部分、差集合
S = {1, 2, 3}
T = {2, 3, 4}

print(S | T) # 和集合  {1, 2, 3, 4}
print(S & T) # 共通部分 {2, 3}
print(S - T) # 差集合 {1}

# 集合の変更
S = {1, 2, 3}
S.add(4)
S.remove(2)
print(S) # {1, 3, 4}

# リスト内包
S = {2 * x for x in {1, 2, 3}}
print(S) # {2, 4, 6}