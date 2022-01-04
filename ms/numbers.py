first_input = input("First Number:")
if first_input.isdecimal():
    first_number = int(first_input)
second_input = input("Second Number:")
if second_input.isdecimal():
    second_number = int(second_input)
if first_input.isdecimal() and second_input.isdecimal():
    print(first_number + second_number)
else:
    print("Invalid Input")
