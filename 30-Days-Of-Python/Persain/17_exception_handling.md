<div align="center">
  <h1> ۳۰ روز با پایتون: روز ۱۷ - مدیریت استثناء </h1>
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

[<< روز ۱۸](./18_regular_expressions.md) | [روز ۱۶ >>](./16_python_datetime.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 روز ۱۷](#-روز-۱۷)
  - [مدیریت استثناء](#مدیریت-استثناء)
  - [پکینگ و آنپکینگ آرگومان‌ها در پایتون](#پکینگ-و-آنپکینگ-آرگومانها-در-پایتون)
    - [آنپکینگ](#آنپکینگ)
      - [آنپکینگ لیست‌ها](#آنپکینگ-لیستها)
      - [آنپکینگ دیکشنری‌ها](#آنپکینگ-دیکشنریها)
    - [پکینگ](#پکینگ)
    - [پکینگ لیست‌ها](#پکینگ-لیستها)
      - [پکینگ دیکشنری‌ها](#پکینگ-دیکشنریها)
  - [اسپردینگ در پایتون](#اسپردینگ-در-پایتون)
  - [Enumerate](#enumerate)
  - [Zip](#zip)
  - [تمرین‌ها: روز ۱۷](#تمرینها-روز-۱۷)

# 📘 روز ۱۷

## مدیریت استثناء

پایتون از _try_ و _except_ برای مدیریت خطاها به صورت کنترل‌شده (gracefully) استفاده می‌کند. خروج کنترل‌شده (یا مدیریت کنترل‌شده) خطاها یک اصطلاح برنامه‌نویسی ساده است - یک برنامه یک وضعیت خطای جدی را شناسایی کرده و در نتیجه به صورت کنترل‌شده "خارج می‌شود". اغلب برنامه به عنوان بخشی از خروج کنترل‌شده، یک پیام خطای توصیفی را در ترمینال یا لاگ چاپ می‌کند، این کار باعث می‌شود برنامه ما مستحکم‌تر (robust) شود. علت یک استثناء اغلب خارج از خود برنامه است. نمونه‌هایی از استثناءها می‌تواند ورودی نادرست، نام فایل اشتباه، عدم توانایی در پیدا کردن فایل، یا یک دستگاه ورودی/خروجی خراب باشد. مدیریت کنترل‌شده خطاها از کرش کردن برنامه‌های ما جلوگیری می‌کند.

ما انواع مختلف _خطاهای_ پایتون را در بخش قبلی پوشش داده‌ایم. اگر از _try_ و _except_ در برنامه خود استفاده کنیم، در آن بلوک‌ها خطایی ایجاد نخواهد شد.

![Try and Except](../images/try_except.png)

```py
try:
    # کدی که در صورت اجرای موفق در این بلوک قرار می‌گیرد
except:
    # کدی که در صورت بروز خطا در این بلوک اجرا می‌شود
```

**مثال:**

```py
try:
    print(10 + '5')
except:
    print('مشکلی پیش آمد')
```

در مثال بالا، عملوند دوم یک رشته است. می‌توانستیم آن را به float یا int تغییر دهیم تا با عدد جمع شود و کار کند. اما بدون هیچ تغییری، بلوک دوم، یعنی _except_، اجرا خواهد شد.

**مثال:**

```py
try:
    name = input('نام خود را وارد کنید:')
    year_born = input('سال تولدتان را وارد کنید:')
    age = 2019 - year_born
    print(f'شما {name} هستید. و سن شما {age} است.')
except:
    print('مشکلی پیش آمد')
```

```sh
مشکلی پیش آمد
```

در مثال بالا، بلوک استثناء اجرا خواهد شد و ما دقیقاً نمی‌دانیم مشکل چیست. برای تحلیل مشکل، می‌توانیم از انواع مختلف خطاها با except استفاده کنیم.

در مثال زیر، هم خطا را مدیریت می‌کند و هم به ما می‌گوید چه نوع خطایی رخ داده است.

```py
try:
    name = input('نام خود را وارد کنید:')
    year_born = input('سال تولدتان را وارد کنید:')
    age = 2019 - year_born
    print(f'شما {name} هستید. و سن شما {age} است.')
except TypeError:
    print('خطای نوع (Type error) رخ داد')
except ValueError:
    print('خطای مقدار (Value error) رخ داد')
except ZeroDivisionError:
    print('خطای تقسیم بر صفر رخ داد')
```

```sh
Enter your name:Asabeneh
Year you born:1920
خطای نوع (Type error) رخ داد
```

در کد بالا، خروجی _TypeError_ خواهد بود.
حالا، یک بلوک اضافی اضافه کنیم:

```py
try:
    name = input('نام خود را وارد کنید:')
    year_born = input('سال تولدتان را وارد کنید:')
    age = 2019 - int(year_born)
    print(f'شما {name} هستید. و سن شما {age} است.')
except TypeError:
    print('خطای نوع (Type error) رخ داد')
except ValueError:
    print('خطای مقدار (Value error) رخ داد')
except ZeroDivisionError:
    print('خطای تقسیم بر صفر رخ داد')
else:
    print('من معمولاً با بلوک try اجرا می‌شوم')
finally:
    print('من همیشه اجرا می‌شوم.')
```

```sh
Enter your name:Asabeneh
Year you born:1920
شما Asabeneh هستید. و سن شما 99 است.
من معمولاً با بلوک try اجرا می‌شوم
من همیشه اجرا می‌شوم.
```

همچنین می‌توان کد بالا را به صورت زیر کوتاه کرد:

```py
try:
    name = input('نام خود را وارد کنید:')
    year_born = input('سال تولدتان را وارد کنید:')
    age = 2019 - int(year_born)
    print(f'شما {name} هستید. و سن شما {age} است.')
except Exception as e:
    print(e)

```

## پکینگ و آنپکینگ آرگومان‌ها در پایتون

ما از دو عملگر استفاده می‌کنیم:

- \* برای تاپل‌ها
- \*\* برای دیکشنری‌ها

بیایید مثال زیر را در نظر بگیریم. این تابع فقط آرگومان‌ها را می‌پذیرد اما ما یک لیست داریم. می‌توانیم لیست را آنپک کرده و آن را به آرگومان‌ها تبدیل کنیم.

### آنپکینگ

#### آنپکینگ لیست‌ها

```py
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst =
print(sum_of_five_nums(lst)) # TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'
```

وقتی این کد را اجرا می‌کنیم، با خطا مواجه می‌شویم، زیرا این تابع به عنوان آرگومان اعداد را می‌پذیرد (نه یک لیست). بیایید لیست را آنپک/تخریب (unpack/destructure) کنیم.

```py
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst =
print(sum_of_five_nums(*lst))  # 15
```

همچنین می‌توانیم از آنپکینگ در تابع داخلی range که به یک نقطه شروع و پایان نیاز دارد، استفاده کنیم.

```py
numbers = range(2, 7)  # فراخوانی عادی با آرگومان‌های جداگانه
print(list(numbers)) #
args =
numbers = range(*args)  # فراخوانی با آرگومان‌های آنپک‌شده از یک لیست
print(list(numbers))      #
```

یک لیست یا تاپل را نیز می‌توان به این صورت آنپک کرد:

```py
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']
numbers =
one, *middle, last = numbers
print(one, middle, last)      #  1 7
```

#### آنپکینگ دیکشنری‌ها

```py
def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'
dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}
print(unpacking_person_info(**dct)) # Asabeneh lives in Finland, Helsinki. He is 250 years old.
```

### پکینگ

گاهی اوقات ما هرگز نمی‌دانیم چه تعداد آرگومان باید به یک تابع پایتون ارسال شود. می‌توانیم از روش پکینگ استفاده کنیم تا به تابع خود اجازه دهیم تعداد نامحدود یا دلخواهی از آرگومان‌ها را بپذیرد.

### پکینگ لیست‌ها

```py
def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s
print(sum_all(1, 2, 3))             # 6
print(sum_all(1, 2, 3, 4, 5, 6, 7)) # 28
```

#### پکینگ دیکشنری‌ها

```py
def packing_person_info(**kwargs):
    # نوع kwargs را بررسی می‌کنیم و می‌بینیم که از نوع dict است
    # print(type(kwargs))
    # چاپ آیتم‌های دیکشنری
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name="Asabeneh",
      country="Finland", city="Helsinki", age=250))
```

```sh
name = Asabeneh
country = Finland
city = Helsinki
age = 250
{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
```

## اسپردینگ در پایتون

مانند جاوا اسکریپت، اسپردینگ (spreading) در پایتون نیز امکان‌پذیر است. بیایید آن را در مثال زیر بررسی کنیم:

```py
lst_one =
lst_two =
lst = [0, *lst_one, *lst_two]
print(lst)          #
country_lst_one = ['Finland', 'Sweden', 'Norway']
country_lst_two = ['Denmark', 'Iceland']
nordic_countries = [*country_lst_one, *country_lst_two]
print(nordic_countries)  # ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
```

## Enumerate

اگر به اندیس یک لیست علاقه‌مند باشیم، از تابع داخلی _enumerate_ برای به دست آوردن اندیس هر آیتم در لیست استفاده می‌کنیم.

```py
for index, item in enumerate():
    print(index, item)
```

```py
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
for index, i in enumerate(countries):
    if i == 'Finland':
        print(f'The country {i} has been found at index {index}')
```

```sh
The country Finland has been found at index 0.
```

## Zip

گاهی اوقات می‌خواهیم لیست‌ها را هنگام پیمایش در آن‌ها ترکیب کنیم. مثال زیر را ببینید:

```py
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})

print(fruits_and_veges)
```

```sh
[{'fruit': 'banana', 'veg': 'Tomato'}, {'fruit': 'orange', 'veg': 'Potato'}, {'fruit': 'mango', 'veg': 'Cabbage'}, {'fruit': 'lemon', 'veg': 'Onion'}, {'fruit': 'lime', 'veg': 'Carrot'}]
```

🌕 شما مصمم هستید. شما ۱۷ قدم در مسیر خود به سوی بزرگی جلوتر هستید. اکنون چند تمرین برای مغز و عضلات خود انجام دهید.

## تمرین‌ها: روز ۱۷

1. `names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']`. پنج کشور اول را آنپک کرده و در متغیری به نام `nordic_countries` ذخیره کنید، و `Estonia` و `Russia` را به ترتیب در `es` و `ru` ذخیره کنید.

🎉 تبریک می‌گویم! 🎉

[<< روز ۱۸](./18_regular_expressions.md) | [روز ۱۶ >>](./16_python_datetime.md)
