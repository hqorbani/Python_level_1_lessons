# # internal functions:
# print("hello")
# print( 5 + 6 - 3)
# age = input("please enter your age:")
# print(age)
from funcs import *
#-----------------------------
# print(sum_2_numbers(6,5))
# print(sum_2_numbers(60,5))
#-----------------------------
# height = 165
# width = 45
# area = area_rectangle(height , width)
# print("area: " , area)
# area = area_rectangle(125 , 654)
# print("area: " , area)
#-----------------------------
# height = float(input("please enter height:"))
# width = float(input("please enter width:"))
# area = area_rectangle(height , width)
# print("area: " , area)
#-----------------------------
numbers = [54,65,98,95,78,65,45,87,45,12,54,32,15,8,6,7,17,25,30,41,48,49,43,40,30,25,22,20,19]
sma_list = sma(numbers , 5)
# print(sma_list)
# print(sma(numbers , 3))

period_numbers = 3
sma_list = sma(period= period_numbers , numbers= numbers)
print(sma_list)
sma_list_2 = sma(sma_list , 3)
print(sma_list_2)
