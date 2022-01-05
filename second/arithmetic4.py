def mySum(num):
    runnnig_sum = 0
    for i in range(num+1):
        runnnig_sum += i * i + 1
    return runnnig_sum


print(mySum(100))
