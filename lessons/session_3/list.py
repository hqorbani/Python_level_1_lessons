numbers = [15, 65, 45, 12.5, 34, 654, 6.45, 71.55, 234, 462, 786, 45, 980, 145]
numbers_less_100 =[]
numbers_100_300 =[]
numbers_more_300 =[]
for number in numbers :
    if number < 100:
        numbers_less_100.append(number)
    elif 100 <= number < 300:
        numbers_100_300.append(number)
    else:
        numbers_more_300.append(number)
print("numbers less than 100:")
print(numbers_less_100)
print("numbers between 100 & 300:")
print(numbers_100_300)
print("numbers more than 300:")
print(numbers_more_300)

