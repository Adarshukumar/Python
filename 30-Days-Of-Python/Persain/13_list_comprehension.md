<div align="center">
  <h1> ۳۰ روز پایتون: روز ۱۳ - List Comprehension</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>نویسنده:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small> ویرایش دوم: جولای، ۲۰۲۱</small>
</sub>

</div>

[<< روز ۱۲](./12_modules.md) | [روز ۱۴ >>](./14_higher_order_functions.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 روز ۱۳](#-روز-۱۳)
  - [List Comprehension](#list-comprehension)
  - [تابع لامبدا (Lambda Function)](#تابع-لامبدا-lambda-function)
    - [ایجاد یک تابع لامبدا](#ایجاد-یک-تابع-لامبدا)
    - [تابع لامبدا درون یک تابع دیگر](#تابع-لامبدا-درون-یک-تابع-دیگر)
  - [💻 تمرین‌ها: روز ۱۳](#-تمرین‌ها-روز-۱۳)

# 📘 روز ۱۳

## List Comprehension

List comprehension در پایتون یک روش فشرده برای ایجاد یک لیست از یک دنباله است. این یک روش کوتاه برای ایجاد یک لیست جدید است. List comprehension به طور قابل توجهی سریع‌تر از پردازش یک لیست با استفاده از حلقه _for_ است.

```py
# سینتکس
[expression for i in iterable if condition]
```

**مثال ۱:**

برای مثال اگر بخواهید یک رشته را به لیستی از کاراکترها تبدیل کنید. می‌توانید از چند روش استفاده کنید. بیایید برخی از آنها را ببینیم:

```py
# یک روش
language = 'Python'
lst = list(language) # تبدیل رشته به لیست
print(type(lst))     # list
print(lst)           # ['P', 'y', 't', 'h', 'o', 'n']

# روش دوم: list comprehension
lst = [i for i in language]
print(type(lst)) # list
print(lst)       # ['P', 'y', 't', 'h', 'o', 'n']
```

**مثال ۲:**

برای مثال اگر بخواهید لیستی از اعداد تولید کنید

```py
# تولید اعداد
numbers = [i for i in range(11)]  # برای تولید اعداد از 0 تا 10
print(numbers)                    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# امکان انجام عملیات ریاضی در حین تکرار وجود دارد
squares = [i * i for i in range(11)]
print(squares)                    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# همچنین امکان ساخت لیستی از تاپل‌ها نیز وجود دارد
numbers = [(i, i * i) for i in range(11)]
print(numbers)                             # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
```

**مثال ۳:**

List comprehension را می‌توان با عبارت if ترکیب کرد.

```py
# تولید اعداد زوج
even_numbers = [i for i in range(21) if i % 2 == 0]  # برای تولید لیست اعداد زوج در بازه 0 تا 21
print(even_numbers)                    # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# تولید اعداد فرد
odd_numbers = [i for i in range(21) if i % 2 != 0]  # برای تولید اعداد فرد در بازه 0 تا 21
print(odd_numbers)                      # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# فیلتر کردن اعداد: بیایید اعداد زوج مثبت را از لیست زیر فیلتر کنیم
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in numbers if i % 2 == 0 and i > 0]
print(positive_even_numbers)                    # [4, 6, 8, 10]

# مسطح کردن یک آرایه سه بعدی
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list = [ number for row in list_of_lists for number in row]
print(flattened_list)    # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## تابع لامبدا (Lambda Function)

تابع لامبدا یک تابع کوچک و بی‌نام است. این تابع می‌تواند هر تعداد آرگومان بگیرد، اما تنها می‌تواند یک عبارت داشته باشد. تابع لامبدا شبیه توابع بی‌نام در جاوااسکریپت است. ما زمانی به آن نیاز داریم که بخواهیم یک تابع بی‌نام را درون یک تابع دیگر بنویسیم.

### ایجاد یک تابع لامبدا

برای ایجاد یک تابع لامبدا از کلمه کلیدی _lambda_ و به دنبال آن یک یا چند پارامتر و سپس یک عبارت استفاده می‌کنیم. سینتکس و مثال زیر را ببینید. تابع لامبدا از return استفاده نمی‌کند اما به طور صریح عبارت را برمی‌گرداند.

```py
# سینتکس
x = lambda param1, param2, param3: param1 + param2 + param3
print(x(arg1, arg2, arg3))```

**مثال:**

```py
# تابع نام‌دار
def add_two_nums(a, b):
    return a + b

print(add_two_nums(2, 3))     # 5
# بیایید تابع بالا را به یک تابع لامبدا تغییر دهیم
add_two_nums = lambda a, b: a + b
print(add_two_nums(2,3))    # 5

# تابع لامبدای خود-فراخوان (self-invoking)
(lambda a, b: a + b)(2,3) # 5 - برای دیدن نتیجه در کنسول باید آن را در print() قرار دهید

square = lambda x : x ** 2
print(square(3))    # 9
cube = lambda x : x ** 3
print(cube(3))    # 27

# چندین متغیر
multiple_variable = lambda a, b, c: a ** 2 - 3 * b + 4 * c
print(multiple_variable(5, 5, 3)) # 22
```

### تابع لامبدا درون یک تابع دیگر

استفاده از یک تابع لامبدا درون یک تابع دیگر.

```py
def power(x):
    return lambda n : x ** n

cube = power(2)(3)   # تابع power اکنون برای اجرا به ۲ آرگومان نیاز دارد، در پرانتزهای جداگانه
print(cube)          # 8
two_power_of_five = power(2)(5) 
print(two_power_of_five)  # 32
```

🌕 به کار خوب خود ادامه دهید. این روند را حفظ کنید، آسمان حد شماست! شما به تازگی چالش‌های روز ۱۳ را به پایان رسانده‌اید و ۱۳ قدم در مسیر خود به سوی بزرگی جلوتر هستید. اکنون تمرین‌هایی برای مغز و عضلات خود انجام دهید.

## 💻 تمرین‌ها: روز ۱۳

۱. فقط اعداد منفی و صفر را در لیست با استفاده از list comprehension فیلتر کنید.
   ```py
   numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
   ```
۲. لیستِ لیست‌هایِ لیست‌های زیر را به یک لیست یک بعدی مسطح کنید:

   ```py
   list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

   output
   [1, 2, 3, 4, 5, 6, 7, 8, 9]
   ```

۳. با استفاده از list comprehension لیست تاپل‌های زیر را ایجاد کنید:
   ```py
   [(0, 1, 0, 0, 0, 0, 0),
   (1, 1, 1, 1, 1, 1, 1),
   (2, 1, 2, 4, 8, 16, 32),
   (3, 1, 3, 9, 27, 81, 243),
   (4, 1, 4, 16, 64, 256, 1024),
   (5, 1, 5, 25, 125, 625, 3125),
   (6, 1, 6, 36, 216, 1296, 7776),
   (7, 1, 7, 49, 343, 2401, 16807),
   (8, 1, 8, 64, 512, 4096, 32768),
   (9, 1, 9, 81, 729, 6561, 59049),
   (10, 1, 10, 100, 1000, 10000, 100000)]
   ```
۴. لیست زیر را به یک لیست جدید مسطح کنید:
   ```py
   countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
   output:
   [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
   ```
۵. لیست زیر را به لیستی از دیکشنری‌ها تغییر دهید:
   ```py
   countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
   output:
   [{'country': 'FINLAND', 'city': 'HELSINKI'},
   {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
   {'country': 'NORWAY', 'city': 'OSLO'}]
   ```
۶. لیستِ لیست‌های زیر را به لیستی از رشته‌های به هم چسبیده تغییر دهید:
   ```py
   names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
   output
   ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
   ```
۷. یک تابع لامبدا بنویسید که بتواند شیب یا عرض از مبدأ توابع خطی را حل کند.

🎉 تبریک می‌گویم! 🎉

[<< روز ۱۲](./12_modules.md) | [روز ۱۴ >>](./14_higher_order_functions.md)
