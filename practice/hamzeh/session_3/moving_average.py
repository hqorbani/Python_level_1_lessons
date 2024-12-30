numbers = [54,65,98,95,78,65,45,87,45,12,54,32,15,8,6,7,17,25,30,41,48,49,43,40,30,25,22,20,19]
ma = []
period = 3
for i in range(len(numbers)):
    counter = i
    step = counter + period
    sum_numbers = 0
    while ((counter < (step)) & (step < len(numbers))):
        # print(numbers[counter])
        sum_numbers += numbers[counter] 
        counter += 1
    avg = round(sum_numbers / period , 2)
    ma.append(avg)

print(ma)

