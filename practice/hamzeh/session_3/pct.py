numbers = [54,65,98,95,78,65,45,87,45,12,54,32,15,8,6,7,17,25,30,41,48,49,43,40,30,25,22,20,19]

pct_list = []
period = 2
for i in range(len(numbers) - period + 1):
    counter = i
    step = counter + period
    sum_numbers = 0
    chunked_list = []
    while (counter < step):
        chunked_list.append(numbers[counter] )
        counter += 1
    last_index = len(chunked_list) - 1
    pct = (chunked_list[last_index] - chunked_list[0]) / chunked_list[0] * 100
    pct = round(pct , 2)
    pct_list.append(pct)
print(pct_list)


