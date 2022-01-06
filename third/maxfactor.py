def factors(num):
    # 空の配列を作成
    factorList = []
    # 0は割り切れないので1から
    for i in range(1, num+1):
        # あまりが0のときのみ配列に追加する
        if num % i == 0:
            factorList.append(i)
    return factorList


def gcf(num, num2):
    gcfList = factors(num)
    gcfList2 = factors(num2)
    gcfList3 = []
    for i in gcfList:
        if i in gcfList2:
            gcfList3.append(i)
    return gcfList3.pop()


def gcf2(num, num2):
    gcfList = []
    numList = factors(num)
    for i in range(0, len(numList)):
        if num2 % numList[i] == 0:
            gcfList.append(numList[i])
    lastNum = len(gcfList) - 1
    return gcfList[lastNum]


print(gcf(150, 138))
print(gcf2(150, 138))
