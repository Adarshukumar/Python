<div align="center">
  <h1> ۳۰ روز پایتون: روز ۱۵ - خطاهای نوع در پایتون </h1>
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

[<< روز ۱۴](./14_higher_order_functions.md) | [روز ۱۶ >>](./16_python_datetime.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)
- [📘 روز ۱۵](#-روز-۱۵)
  - [انواع خطاهای پایتون](#انواع-خطاهای-پایتون)
    - [SyntaxError](#syntaxerror)
    - [NameError](#nameerror)
    - [IndexError](#indexerror)
    - [ModuleNotFoundError](#modulenotfounderror)
    - [AttributeError](#attributeerror)
    - [KeyError](#keyerror)
    - [TypeError](#typeerror)
    - [ImportError](#importerror)
    - [ValueError](#valueerror)
    - [ZeroDivisionError](#zerodivisionerror)
  - [💻 تمرین‌ها: روز ۱۵](#-تمرین‌ها-روز-۱۵)

# 📘 روز ۱۵

## انواع خطاهای پایتون

وقتی کد می‌نویسیم، رایج است که یک غلط املایی یا خطای رایج دیگری داشته باشیم. اگر کد ما اجرا نشود، مفسر پایتون پیامی را نمایش می‌دهد که حاوی بازخوردی با اطلاعاتی در مورد محل وقوع مشکل و نوع خطا است. همچنین گاهی اوقات پیشنهادهایی برای رفع احتمالی آن به ما ارائه می‌دهد. درک انواع مختلف خطاها در زبان‌های برنامه‌نویسی به ما کمک می‌کند تا کد خود را به سرعت اشکال‌زدایی (debug) کنیم و همچنین ما را در کاری که انجام می‌دهیم بهتر می‌کند.

بیایید رایج‌ترین انواع خطا را یک به یک ببینیم. ابتدا بیایید شل تعاملی پایتون (Python interactive shell) خود را باز کنیم. به ترمینال کامپیوتر خود بروید و 'python' را بنویسید. شل تعاملی پایتون باز خواهد شد.

### SyntaxError

**مثال ۱: SyntaxError**

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print 'hello world'
  File "<stdin>", line 1
    print 'hello world'
                      ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello world')?
>>>
```

همانطور که می‌بینید، ما یک خطای نحوی (syntax error) داشتیم زیرا فراموش کردیم رشته را داخل پرانتز قرار دهیم و پایتون از قبل راه‌حل را پیشنهاد می‌دهد. بیایید آن را اصلاح کنیم.

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print 'hello world'
  File "<stdin>", line 1
    print 'hello world'
                      ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('hello world')?
>>> print('hello world')
hello world
>>>
```

خطا از نوع _SyntaxError_ بود. پس از اصلاح، کد ما بدون هیچ مشکلی اجرا شد. بیایید انواع خطای بیشتری را ببینیم.

### NameError

**مثال ۱: NameError**

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print(age)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'age' is not defined
>>>
```

همانطور که از پیام بالا می‌بینید، نام age تعریف نشده است. بله، درست است که ما متغیر age را تعریف نکرده بودیم اما سعی داشتیم آن را طوری چاپ کنیم که گویی آن را تعریف کرده‌ایم. حالا، بیایید با تعریف و تخصیص یک مقدار به آن، این مشکل را برطرف کنیم.

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print(age)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'age' is not defined
>>> age = 25
>>> print(age)
25
>>>
```

نوع خطا _NameError_ بود. ما با تعریف نام متغیر، خطا را اشکال‌زدایی کردیم.

### IndexError

**مثال ۱: IndexError**

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> numbers = [1, 2, 3, 4, 5]
>>> numbers[5]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>>
```

در مثال بالا، پایتون یک _IndexError_ ایجاد کرد، زیرا لیست فقط اندیس‌هایی از ۰ تا ۴ دارد، بنابراین این اندیس خارج از محدوده بود.

### ModuleNotFoundError

**مثال ۱: ModuleNotFoundError**

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
>>>
```

در مثال بالا، من عمداً یک s اضافی به math اضافه کردم و خطای _ModuleNotFoundError_ ایجاد شد. بیایید با حذف s اضافی از math آن را اصلاح کنیم.

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
>>> import math
>>>
```

ما آن را اصلاح کردیم، پس بیایید از برخی از توابع ماژول math استفاده کنیم.

### AttributeError

**مثال ۱: AttributeError**

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
>>> import math
>>> math.PI
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'math' has no attribute 'PI'
>>>
```

همانطور که می‌بینید، دوباره اشتباه کردم! به جای `pi`، سعی کردم ثابت `PI` را از ماژول `math` فراخوانی کنم. این کار باعث بروز خطای `AttributeError` شد، به این معنی که این ویژگی در ماژول وجود ندارد. بیایید آن را با تغییر `PI` به `pi` اصلاح کنیم.

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import maths
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'maths'
>>> import math
>>> math.PI
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'math' has no attribute 'PI'
>>> math.pi
3.141592653589793
>>>
```

حالا، وقتی pi را از ماژول math فراخوانی می‌کنیم، نتیجه را دریافت کردیم.

### KeyError

**مثال ۱: KeyError**

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> users = {'name':'Asab', 'age':250, 'country':'Finland'}
>>> users['name']
'Asab'
>>> users['county']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'county'
>>>
```

همانطور که می‌بینید، در کلیدی که برای گرفتن مقدار دیکشنری استفاده شد، یک غلط املایی وجود داشت. بنابراین، این یک key error است و رفع آن کاملاً ساده است. بیایید این کار را انجام دهیم!

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> user = {'name':'Asab', 'age':250, 'country':'Finland'}
>>> user['name']
'Asab'
>>> user['county']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'county'
>>> user['country']
'Finland'
>>>
```

ما خطا را اشکال‌زدایی کردیم، کد ما اجرا شد و ما مقدار را دریافت کردیم.

### TypeError

**مثال ۱: TypeError**

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 4 + '3'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>>
```

در مثال بالا، یک TypeError ایجاد می‌شود زیرا ما نمی‌توانیم یک عدد را به یک رشته اضافه کنیم. راه‌حل اول این است که رشته را به int یا float تبدیل کنیم. راه‌حل دیگر این است که عدد را به یک رشته تبدیل کنیم (در این صورت نتیجه '43' خواهد بود). بیایید راه‌حل اول را دنبال کنیم.

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 4 + '3'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 4 + int('3')
7
>>> 4 + float('3')
7.0
>>>
```

خطا برطرف شد و ما نتیجه‌ای را که انتظار داشتیم، دریافت کردیم.

### ImportError

**مثال ۱: TypeError**

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from math import power
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'power' from 'math'
>>>
```

تابعی به نام power در ماژول math وجود ندارد، نام آن چیز دیگری است: _pow_. بیایید آن را اصلاح کنیم:

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from math import power
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: cannot import name 'power' from 'math'
>>> from math import pow
>>> pow(2,3)
8.0
>>>
```

### ValueError

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> int('12a')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '12a'
>>>
```

در این حالت ما نمی‌توانیم رشته داده شده را به عدد تبدیل کنیم، به دلیل وجود حرف 'a' در آن.

### ZeroDivisionError

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 1/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>>
```

ما نمی‌توانیم یک عدد را بر صفر تقسیم کنیم.

ما برخی از انواع خطاهای پایتون را پوشش دادیم، اگر می‌خواهید در مورد آن بیشتر بدانید، مستندات پایتون در مورد انواع خطاهای پایتون را بررسی کنید.
اگر در خواندن انواع خطاها خوب باشید، قادر خواهید بود باگ‌های خود را به سرعت برطرف کنید و همچنین به برنامه‌نویس بهتری تبدیل خواهید شد.

🌕 شما در حال درخشیدن هستید. شما نیمی از راه خود را به سوی عظمت طی کرده‌اید. اکنون چند تمرین برای مغز و عضلات خود انجام دهید.

## 💻 تمرین‌ها: روز ۱۵

۱. شل تعاملی پایتون خود را باز کنید و تمام مثال‌های پوشش داده شده در این بخش را امتحان کنید.

🎉 تبریک می‌گویم! 🎉

[<< روز ۱۴](./14_higher_order_functions.md) | [روز ۱۶ >>](./16_python_datetime.md)
