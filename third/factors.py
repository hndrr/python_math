def factors(num):
    # 空の配列を作成
    factorList = []
    # 0は割り切れないので1から
    for i in range(1, num+1):
        # あまりが0のときのみ配列に追加する
        if num % i == 0:
            factorList.append(i)
    return factorList


print(factors(120))
