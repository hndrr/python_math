import time
from turtle import *

# 形を変える
shape('turtle')
# 右に45度


def circle(size=100):
    for i in range(60):
        rt(5)
        for i in range(4):
            forward(size)
            rt(90)


circle(80)

time.sleep(5)
