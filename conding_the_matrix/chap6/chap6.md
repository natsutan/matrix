<div id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#sec-1">1. 次元</a>
<ul>
<li><a href="#sec-1-1">1.1. 基底ベクトルの個数</a>
<ul>
<li><a href="#sec-1-1-1">1.1.1. モーフィングの補題とその結果</a></li>
</ul>
</li>
<li><a href="#sec-1-2">1.2. 次元とランク</a></li>
<li><a href="#sec-1-3">1.3. 直和</a></li>
<li><a href="#sec-1-4">1.4. 次元と線形関数</a></li>
</ul>
</li>
</ul>
</div>
</div>

# 次元<a id="sec-1" name="sec-1"></a>

## 基底ベクトルの個数<a id="sec-1-1" name="sec-1-1"></a>

### モーフィングの補題とその結果<a id="sec-1-1-1" name="sec-1-1-1"></a>

νをベクトル空間とする。このとき、νの生成子の集合がもっとも小さくなるのは、その集合がνの基底であるとき、かつ、そのときに限る。

## 次元とランク<a id="sec-1-2" name="sec-1-2"></a>

ベクトル空間の次元を、その基底ベクトルの個数で定義する。ベクトル空間νの次元をdimνと書く。

ベクトルの集合Sのランクを、Span Sの次元と定義する。Sのランクをrank Sと書く

任意の行列に対し、その行ランクと列ランクは等しい

## 直和<a id="sec-1-3" name="sec-1-3"></a>

μとνがゼロベクトルのみを共有するとき、μとνの直和を次の集合

{u+v : u ∈ μ, v ∈ ν}

で定義し、μ⊕νと書く

ゼロでないベクトルを共有しているときは直和は取れない。

## 次元と線形関数<a id="sec-1-4" name="sec-1-4"></a>

<http://study-guide.hatenablog.jp/entry/20150307/p1#L264>

**次元定理**

任意の線形関数 f:ν →W に対し、次がなりたつ

dim Ker f + dim Im f = dim ν

dim Ker f = 0 かつ、dim Im f = dim νのとき, fは可逆
