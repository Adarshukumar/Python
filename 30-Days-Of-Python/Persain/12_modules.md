<div align="center">
  <h1> ۳۰ روز پایتون: روز ۱۲ - ماژول‌ها </h1>
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

[<< روز ۱۱](./11_functions.md) | [روز ۱۳ >>](./13_list_comprehension.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 روز ۱۲](#-روز-۱۲)
  - [ماژول‌ها](#ماژول‌ها)
    - [ماژول چیست](#ماژول-چیست)
    - [ایجاد یک ماژول](#ایجاد-یک-ماژول)
    - [وارد کردن (Import) یک ماژول](#وارد-کردن-import-یک-ماژول)
    - [وارد کردن توابع از یک ماژول](#وارد-کردن-توابع-از-یک-ماژول)
    - [وارد کردن توابع از یک ماژول و تغییر نام آن‌ها](#وارد-کردن-توابع-از-یک-ماژول-و-تغییر-نام-آن‌ها)
  - [وارد کردن ماژول‌های داخلی (Built-in)](#وارد-کردن-ماژول‌های-داخلی-built-in)
    - [ماژول OS](#ماژول-os)
    - [ماژول Sys](#ماژول-sys)
    - [ماژول Statistics](#ماژول-statistics)
    - [ماژول Math](#ماژول-math)
    - [ماژول String](#ماژول-string)
    - [ماژول Random](#ماژول-random)
  - [💻 تمرین‌ها: روز ۱۲](#-تمرین‌ها-روز-۱۲)
    - [تمرین‌ها: سطح ۱](#تمرین‌ها-سطح-۱)
    - [تمرین‌ها: سطح ۲](#تمرین‌ها-سطح-۲)
    - [تمرین‌ها: سطح ۳](#تمرین‌ها-سطح-۳)

# 📘 روز ۱۲

## ماژول‌ها

### ماژول چیست

ماژول فایلی است حاوی مجموعه‌ای از کدها یا مجموعه‌ای از توابع که می‌توان آن را به یک برنامه اضافه کرد. یک ماژول می‌تواند فایلی حاوی یک متغیر، یک تابع یا یک پایگاه کد بزرگ باشد.

### ایجاد یک ماژول

برای ایجاد یک ماژول، کدهای خود را در یک اسکریپت پایتون می‌نویسیم و آن را با پسوند .py ذخیره می‌کنیم. فایلی به نام mymodule.py در پوشه پروژه خود ایجاد کنید. بیایید کدی را در این فایل بنویسیم.

```py
# فایل mymodule.py
def generate_full_name(firstname, lastname):
    return firstname + ' ' + lastname
```

فایل main.py را در دایرکتوری پروژه خود ایجاد کرده و فایل mymodule.py را وارد (import) کنید.

### وارد کردن (Import) یک ماژول

برای وارد کردن فایل، از کلمه کلیدی _import_ و فقط نام فایل استفاده می‌کنیم.

```py
# فایل main.py
import mymodule
print(mymodule.generate_full_name('Asabeneh', 'Yetayeh')) # Asabeneh Yetayeh
```

### وارد کردن توابع از یک ماژول

ما می‌توانیم توابع زیادی در یک فایل داشته باشیم و می‌توانیم همه توابع را به صورت جداگانه وارد کنیم.

```py
# فایل main.py
from mymodule import generate_full_name, sum_two_nums, person, gravity
print(generate_full_name('Asabneh','Yetayeh'))
print(sum_two_nums(1,9))
mass = 100
weight = mass * gravity
print(weight)
print(person['firstname'])
```

### وارد کردن توابع از یک ماژول و تغییر نام آن‌ها

هنگام وارد کردن، می‌توانیم نام ماژول را تغییر دهیم.

```py
# فایل main.py
from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
print(fullname('Asabneh','Yetayeh'))
print(total(1, 9))
mass = 100
weight = mass * g
print(weight)
print(p)
print(p['firstname'])
```

## وارد کردن ماژول‌های داخلی (Built-in)

مانند سایر زبان‌های برنامه‌نویسی، ما نیز می‌توانیم با استفاده از کلمه کلیدی _import_، ماژول‌ها را با وارد کردن فایل/تابع مربوطه وارد کنیم. بیایید ماژول‌های رایجی را که بیشتر اوقات استفاده خواهیم کرد، وارد کنیم. برخی از ماژول‌های داخلی رایج عبارتند از: _math_، _datetime_، _os_، _sys_، _random_، _statistics_، _collections_، _json_، _re_.

### ماژول OS

با استفاده از ماژول _os_ پایتون، امکان انجام خودکار بسیاری از وظایف سیستم‌عامل وجود دارد. ماژول OS در پایتون توابعی را برای ایجاد، تغییر دایرکتوری کاری فعلی و حذف یک دایرکتوری (پوشه)، دریافت محتویات آن، تغییر و شناسایی دایرکتوری فعلی فراهم می‌کند.

```py
# وارد کردن ماژول
import os
# ایجاد یک دایرکتوری
os.mkdir('directory_name')
# تغییر دایرکتوری فعلی
os.chdir('path')
# دریافت دایرکتوری کاری فعلی
os.getcwd()
# حذف دایرکتوری
os.rmdir()
```

### ماژول Sys

ماژول sys توابع و متغیرهایی را فراهم می‌کند که برای دستکاری بخش‌های مختلف محیط زمان اجرای پایتون استفاده می‌شوند. تابع sys.argv لیستی از آرگومان‌های خط فرمان را که به یک اسکریپت پایتون ارسال شده‌اند، برمی‌گرداند. آیتم با ایندکس 0 در این لیست همیشه نام اسکریپت است، در ایندکس 1 آرگومانی است که از خط فرمان ارسال شده است.

مثالی از فایل script.py:

```py
import sys
#print(sys.argv[0], argv[1],sys.argv[2]) # این خط چاپ می‌کند: filename argument1 argument2
print('Welcome {}. Enjoy {} challenge!'.format(sys.argv[1], sys.argv[2]))
```

حالا برای بررسی نحوه عملکرد این اسکریپت، در خط فرمان نوشتم:

```sh
python script.py Asabeneh 30DaysOfPython```

نتیجه:

```sh
Welcome Asabeneh. Enjoy 30DayOfPython challenge!
```

برخی از دستورات مفید sys:

```py
# برای خروج از sys
sys.exit()
# برای دانستن بزرگترین مقدار صحیحی که یک متغیر می‌تواند بگیرد
sys.maxsize
# برای دانستن مسیر محیطی (environment path)
sys.path
# برای دانستن نسخه پایتونی که استفاده می‌کنید
sys.version
```

### ماژول Statistics

ماژول statistics توابعی برای آمار ریاضی داده‌های عددی فراهم می‌کند. توابع آماری محبوبی که در این ماژول تعریف شده‌اند عبارتند از: _mean_، _median_، _mode_، _stdev_ و غیره.

```py
from statistics import * # وارد کردن تمام ماژول‌های statistics
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3
```

### ماژول Math

ماژولی حاوی بسیاری از عملیات‌ها و ثابت‌های ریاضی.

```py
import math
print(math.pi)           # 3.141592653589793, ثابت پی
print(math.sqrt(2))      # 1.4142135623730951, ریشه دوم
print(math.pow(2, 3))    # 8.0, تابع توان
print(math.floor(9.81))  # 9, گرد کردن به سمت پایین
print(math.ceil(9.81))   # 10, گرد کردن به سمت بالا
print(math.log10(100))   # 2, لگاریتم در مبنای 10
```

اکنون، ما ماژول *math* را وارد کرده‌ایم که حاوی توابع زیادی است که می‌تواند به ما در انجام محاسبات ریاضی کمک کند. برای بررسی اینکه ماژول چه توابعی دارد، می‌توانیم از _help(math)_ یا _dir(math)_ استفاده کنیم. این کار توابع موجود در ماژول را نمایش می‌دهد. اگر بخواهیم فقط یک تابع خاص از ماژول را وارد کنیم، آن را به صورت زیر وارد می‌کنیم:

```py
from math import pi
print(pi)```

همچنین امکان وارد کردن چندین تابع به صورت همزمان وجود دارد

```py
from math import pi, sqrt, pow, floor, ceil, log10
print(pi)                 # 3.141592653589793
print(sqrt(2))            # 1.4142135623730951
print(pow(2, 3))          # 8.0
print(floor(9.81))        # 9
print(ceil(9.81))         # 10
print(math.log10(100))    # 2
```

اما اگر بخواهیم تمام توابع موجود در ماژول math را وارد کنیم، می‌توانیم از * استفاده کنیم.

```py
from math import *
print(pi)                  # 3.141592653589793, ثابت پی
print(sqrt(2))             # 1.4142135623730951, ریشه دوم
print(pow(2, 3))           # 8.0, تابع توان
print(floor(9.81))         # 9, گرد کردن به سمت پایین
print(ceil(9.81))          # 10, گرد کردن به سمت بالا
print(math.log10(100))     # 2
```

هنگام وارد کردن، می‌توانیم نام تابع را نیز تغییر دهیم.

```py
from math import pi as PI
print(PI) # 3.141592653589793
```

### ماژول String

ماژول string یک ماژول مفید برای اهداف بسیاری است. مثال زیر برخی از کاربردهای ماژول string را نشان می‌دهد.

```py
import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

### ماژول Random

تا الان با وارد کردن ماژول‌ها آشنا شده‌اید. بیایید یک وارد کردن دیگر انجام دهیم تا با آن کاملاً آشنا شویم. بیایید ماژول _random_ را وارد کنیم که به ما یک عدد تصادفی بین 0 و 0.9999.... می‌دهد. ماژول _random_ توابع زیادی دارد اما در این بخش ما فقط از _random_ و _randint_ استفاده خواهیم کرد.

```py
from random import random, randint
print(random())   # هیچ آرگومانی نمی‌گیرد؛ مقداری بین 0 و 0.9999 برمی‌گرداند
print(randint(5, 20)) # یک عدد صحیح تصادفی بین [5, 20] به صورت inclusive (شامل خود اعداد) برمی‌گرداند
```

🌕 شما دارید پیشرفت زیادی می‌کنید. ادامه دهید! شما به تازگی چالش‌های روز ۱۲ را به پایان رسانده‌اید و ۱۲ قدم در مسیر خود به سوی بزرگی جلوتر هستید. اکنون تمرین‌هایی برای مغز و عضلات خود انجام دهید.

## 💻 تمرین‌ها: روز ۱۲

### تمرین‌ها: سطح ۱

1.  تابعی بنویسید که یک random_user_id شش رقمی/کاراکتری تولید کند.
    ```py
      print(random_user_id())
      '1ee33d'
    ```
2.  وظیفه قبلی را اصلاح کنید. تابعی به نام user_id_gen_by_user تعریف کنید. این تابع هیچ پارامتری نمی‌گیرد اما دو ورودی را با استفاده از input() دریافت می‌کند. یکی از ورودی‌ها تعداد کاراکترها و ورودی دوم تعداد IDهایی است که قرار است تولید شوند.

```py
print(user_id_gen_by_user()) # ورودی کاربر: 5 5
#خروجی:
#kcsy2
#SMFYb
#bWmeq
#ZXOYh
#2Rgxf
   
print(user_id_gen_by_user()) # 16 5
#1GCSgPLMaBAVQZ26
#YD7eFwNQKNs7qXaT
#ycArC5yrRupyG00S
#UbGxOFI7UXSWAyKN
#dIV0SSUTgAdKwStr
```

3.  تابعی به نام rgb_color_gen بنویسید. این تابع رنگ‌های rgb (3 مقدار که هر کدام در محدوده 0 تا 255 هستند) تولید خواهد کرد.

```py
print(rgb_color_gen())
# rgb(125,244,255) - خروجی باید به این شکل باشد
```

### تمرین‌ها: سطح ۲

1.  تابعی به نام list_of_hexa_colors بنویسید که هر تعداد رنگ هگزادسیمال را در یک آرایه برمی‌گرداند (شش عدد هگزادسیمال که بعد از # نوشته می‌شوند. سیستم اعداد هگزادسیمال از 16 نماد، 0-9 و شش حرف اول الفبا، a-f تشکیل شده است. برای نمونه‌های خروجی به تمرین ۶ مراجعه کنید).
2.  تابعی به نام list_of_rgb_colors بنویسید که هر تعداد رنگ RGB را در یک آرایه برمی‌گرداند.
3.  تابعی به نام generate_colors بنویسید که بتواند هر تعداد رنگ hexa یا rgb تولید کند.

```py
   generate_colors('hexa', 3) # ['#a3e12f','#03ed55','#eb3d2b'] 
   generate_colors('hexa', 1) # ['#b334ef']
   generate_colors('rgb', 3)  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 
   generate_colors('rgb', 1)  # ['rgb(33,79, 176)']
   ```

### تمرین‌ها: سطح ۳

1.  تابع خود را shuffle_list بنامید، این تابع یک لیست به عنوان پارامتر می‌گیرد و یک لیست درهم‌ریخته (shuffled) برمی‌گرداند.
2.  تابعی بنویسید که آرایه‌ای از هفت عدد تصادفی در محدوده 0-9 را برگرداند. همه اعداد باید منحصر به فرد باشند.

🎉 تبریک می‌گویم! 🎉

[<< روز ۱۱](./11_functions.md) | [روز ۱۳ >>](./13_list_comprehension.md)
