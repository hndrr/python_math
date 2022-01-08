from random import randint


def numberGame():
    # 1~100までの数字をランダムに選ぶ
    num = randint(1, 100)

    print('1から100までのどれかを思い浮かべてます')
    guess = int(input("いくつだとおもいますか？"))

    while guess:
        # 入力した数字が正解かどうかを判定する
        if num == guess:
            print("正解")
            break
        elif num > guess:
            print("違います。もっと大きいです")
        else:
            print("違います。もっと小さいです")
        guess = int(input("いくつだとおもいますか？"))


numberGame()
