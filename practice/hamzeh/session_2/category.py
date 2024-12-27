numbers = [15, 65, 45, 12.5, 34, 654, 6.45, 71.55, 234, 462, 786, 45, 980, 145 , 645]

for i in range(0,len(numbers)):
    if numbers[i] < 100:
        print(f"{numbers[i]} is less than 100")
    elif 100 <= numbers[i] < 300:
        print(f"{numbers[i]} is between 100 & 300")
    else:
        print(f"{numbers[i]} is more than 300")
