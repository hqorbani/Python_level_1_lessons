numbers = [54,65,98,95,78,65,45,87,45,12,54,32,15,8,6,7,17,25,30,41,48,49,43,40,30,25,22,20,19]
# simple moving average: sma
sma = []
period = 3
for i in range(len(numbers) - period + 1):
    counter = i
    step = counter + period
    sum_numbers = 0
    chunked_list = []
    while (counter < step):
        chunked_list.append(numbers[counter] )
        counter += 1
    avg = round(sum(chunked_list) / period , 2)
    sma.append(avg)
print(sma)


