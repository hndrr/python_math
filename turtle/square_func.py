import time
from turtle import *

# 形を変える
shape('turtle')
# 右に45度


def square(size):
    for i in range(4):
        forward(size)
        rt(90)


square(100)

time.sleep(5)
