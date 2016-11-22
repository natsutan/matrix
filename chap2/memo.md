# 行列プログラマメモ 2章

---
# 2.1 what is vector
定義 2.1.1 実数の4つの組からなるベクターを、4 vector over Rと呼ぶ。
定義 2.1.2 体Fと正数nに対して、Fに所属するn個の組からなるベクターを　n-vector over Fと呼ぶ。F<sup>n></sup>と書く。

# 2.2 Vector and function

# 2.4 Vectorの加算
要素が2のベクターの加算
```python
def add2(v, w):
    return [v[0]+w[0], v[1]+w[1]]

```

要素がnのベクターの加算
```python
def addn(v, w):
    return [x+y for (x,y) in zip(v,w)]
```




