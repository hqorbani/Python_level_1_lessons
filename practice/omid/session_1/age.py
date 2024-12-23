from datetime import datetime
 
# دریافت سن کاربر از ورودی
age = int(input("how old ore you: "))
 
# محاسبه سال تولد
current_year = datetime.now().year
birth_year = current_year - age
 
# چاپ سال تولد
print("your year of birth :", birth_year)
