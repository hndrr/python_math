import time
from turtle import *

# 形を変える
shape('turtle')


def polygon(num_sides, size):
    for i in range(size):
        forward(num_sides)
        rt(360/size)


polygon(40, 20)

time.sleep(5)
