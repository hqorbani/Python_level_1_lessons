def sum_2_numbers(number_1 , number_2):
    result = number_1 + number_2
    return result

def area_rectangle(ertfa , pahna):
    return ertfa * pahna / 2

#simple moving average: sma
def sma(numbers: list , period: int):
    ma = []
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
    return ma