capital = 2000
grow_percent = 4
neccessary_percent = 50
# خواسته ها - تفریحات...
dreams_percent = 30
save_percent = 20
number_month = 16


for month in range(1 , number_month + 1):
    grow = capital * grow_percent / 100
    # print(grow)
    neccessary = round(grow * neccessary_percent / 100 , 2)
    dreams = round(grow * dreams_percent / 100 , 2)
    save = round(grow * save_percent / 100 , 2)
    capital = round(capital + save , 2)
    # print("month:", month, "neccessary:",neccessary , "dreams:",dreams , "save:",save , "capital:",capital)
    print(f"ماه: {month} ---- zarooriat:{neccessary} ---- arezoha: {dreams} ---- pasandaz: {save} , sarmaye: {capital}")
