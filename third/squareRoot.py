from random import randint


def average(a, b):
    return (a + b) / 2


def squareRoot(num, low, high):
    # lowからhigまでの範囲内で
    # 数当てゲームの戦略を利用することにより
    # 指定された数字の平方根を見つける

    for i in range(20):
        guess = average(low, high)

        if guess ** 2 == num:
            break
        elif guess ** 2 > num:
            # print("違います。もっと小さいです")
            high = guess
        else:
            # print("違います。もっと大きいです")
            low = guess
    print(guess)


squareRoot(60, 7, 8)
squareRoot(200, 10, 20)
squareRoot(1000, 30, 32)
squareRoot(50000, 100, 500)
