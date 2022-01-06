import time
from turtle import *
from random import randint

# 形を変える
shape('turtle')
speed(0)


def wander():
    while True:
        # ３直進する
        fd(3)
        #　亀の動く範囲
        if xcor() >= 200 or xcor() <= -200 or ycor() <= -200 or ycor() >= 200:
            # 左にランダムな角度を回転する
            lt(randint(90, 180))


wander()

time.sleep(5)
