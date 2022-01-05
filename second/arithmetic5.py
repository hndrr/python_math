def mySum(num):
    runnnig_sum = 0
    for i in range(1, num+1):
        runnnig_sum += i
    return runnnig_sum


print(mySum(10))
print(mySum(100))
print(mySum(1000))
print(mySum(10000))
