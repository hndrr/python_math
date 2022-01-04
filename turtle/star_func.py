import time
from turtle import *

# 形を変える
shape('turtle')


def star(size=100):
    for i in range(5):
        forward(size)
        # 外角
        rt(180 - 180/5)


star(80)

time.sleep(5)
