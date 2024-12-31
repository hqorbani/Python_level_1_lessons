# تمرین تبدیل الگوریتم به کد پایتون
### الگوریتم زیر را به کد پایتون تبدیل کنید:
### الگوریتم محاسبه درصد تغییر هر عنصر موجود در لیست نسبت به عنصر قبلی خود:

#
#### ۱-	تعریف لیست اعداد و متغیرهای اولیه:
##### -	لیست numbers را تعریف کنید
##### - 	لیست خالی pct_list  را برای ذخیره درصد تغییرات ایجاد کنید.
##### - متغیر period  را برای تعیین بازه تعیین شده تنظیم کنید.
#
#### ۲-	حلقه اصلی برای محاسبه درصد تغییرات:
##### - از یک حلقه for  برای پیمایش لیست numbers  استفاده کنید بطوریکه از ۰ شروع ‌شود و تا (len(numbers) - period + 1) ادامه ‌یابد
##### - در هر تکرار، متغیر counter  را به مقدار i  تنظیم کنید : counter = i .
##### - متغیر step  را به مقدار counter + period  تنظیم کنید.
##### - متغیر sum_numbers  را به مقدار 0 تنظیم کنید.
##### - لیست خالی chunked_list  را برای ذخیره اعداد در بازه تعیین شده ایجاد کنید.
#
#### ۳- حلقه داخلی برای جمع‌آوری اعداد در بازه تعیین شده:
##### - از یک حلقه while  برای جمع‌آوری اعداد در بازه تعیین شده استفاده کنید.
##### - در هر تکرار، عدد فعلی را به chunked_list  اضافه کنید.
##### - مقدار counter  را یک واحد افزایش دهید.
#
#### ۴- محاسبه درصد تغییرات خارج از حلقه داخلی: 
##### - آخرین شاخص chunked_list  را به عنوان last_index  تعیین کنید.
##### - درصد تغییرات را با استفاده از فرمول (chunked_list[last_index] - chunked_list[0]) / chunked_list[0] * 100  محاسبه کنید.
##### - مقدار درصد تغییرات را با استفاده از round  گرد کنید.
##### - درصد تغییرات را به pct_list  اضافه کنید.
#
#### ۵- چاپ نتیجه خارج از حلقه اصلی:
##### - لیست pct_list  را چاپ کنید.
### پایان.

#
#### برای نمونه اگر لیست اعداد بصورت زیر باشد:
```Python
numbers = [54,65,98,95,78,65,45,87,45,12,54,32,15,8,6,7,17,25,30,41,48,49,43,40,30,25,22,20,19]
```
#### خروجی به صورت زیر خواهد بود:
```
[20.37, 50.77, -3.06, -17.89, -16.67, -30.77, 93.33, -48.28, -73.33, 350.0, -40.74, -53.12, -46.67, -25.0, 16.67, 142.86, 47.06, 20.0, 36.67, 17.07, 2.08, -12.24, 
-6.98, -25.0, -16.67, -12.0, -9.09, -5.0]
```