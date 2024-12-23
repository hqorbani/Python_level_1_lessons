capital = 1000
grow_percent = 3
neccessary_percent = 50
# خواسته ها - تفریحات...
dreams_percent = 30
save_percent = 20
number_month = 6


for month in range(1 , number_month + 1):
    grow = capital * grow_percent / 100
    # print(grow)
    neccessary = grow * neccessary_percent / 100
    dreams = grow * dreams_percent / 100
    save = grow * save_percent / 100
    capital = capital + save
    print("month:", month, "neccessary::::",neccessary , "dreams",dreams , "save:",save , "capital:",capital)
