import time
from turtle import *

# 形を変える
shape('turtle')


def tri(size=100):
    for i in range(3):
        forward(size)
        rt(240)
        # 逆三角形：外角＝180-内角60度
        # rt(120)


tri(80)

time.sleep(5)
