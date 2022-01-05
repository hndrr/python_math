def average3(numbers):
    # 合計を項目数で割る
    return (sum(numbers) / len(numbers))


print(average3([8, 11, 15]))

d = [53, 28, 54, 84, 65, 60, 22, 93, 62, 27, 16,
     25, 74, 42, 4, 42, 15, 96, 11, 70, 83, 97, 75]
print(average3(d))
