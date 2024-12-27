numbers = [15, 65, 45, 12.5, 34, 654, 6.45, 71.55, 234, 462, 786, 45, 980, 145]
max_number = numbers[0]
min_number = numbers[0]
for i in range(0, len(numbers)):
    if numbers[i] > max_number :
        max_number = numbers[i]
    if numbers[i] < min_number:
        min_number = numbers[i]
print(f"max number: {max_number}")
print(f"min number: {min_number}")
