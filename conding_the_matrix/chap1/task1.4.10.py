# coding matrix
# task 1.4.10
# 画像を読み込んで、輝度が１２０以下の点をプロットする
import itertools
from PIL import Image, ImageOps
from myplot import ploti

input_file = 'twittan.jpeg'
th = 120

# 空集合を作る
S = set()

img = Image.open(input_file)
img_gray = ImageOps.grayscale(img)
max_x, max_y = img.size

for x, y in itertools.product(range(max_x), range(max_y)):
    # 座標変換
    yval = img_gray.getpixel((x, y))
    y = max_y - y
    if yval < th:
        p = x + y * 1j
        S.add(p)

size = max(max_x, max_y)

ploti(S, xrange=[-size, size], yrange=[-size, size], file='task1.4.10.png')

