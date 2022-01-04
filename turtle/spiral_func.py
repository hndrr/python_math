import time
from turtle import *

# 形を変える
shape('turtle')


def spiral(size=100):
    for i in range(60):
        size += 5
        rt(5)
        for i in range(4):
            forward(size + 5)
            rt(90)


spiral(5)

time.sleep(5)
