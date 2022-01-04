import time
from turtle import *

# 形を変える
shape('turtle')
speed(10)


def starSpiral(size=100):
    for i in range(60):
        # 5ずつインクリメントする
        size += 5
        # 右に5度
        rt(5)
        # 星を描く
        for i in range(5):
            forward(size)
            # 外角
            rt(180 - 180/5)


starSpiral(5)

time.sleep(5)
