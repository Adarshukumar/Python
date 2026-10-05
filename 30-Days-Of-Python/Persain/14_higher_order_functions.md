<div align="center">
  <h1> ۳۰ روز پایتون: روز ۱۴ - توابع مرتبه بالا</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

  <sub>نویسنده:
  <a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
  <small>ویرایش دوم: جولای ۲۰۲۱</small>
  </sub>
  
</div>

[<< روز ۱۳](./13_list_comprehension.md) | [روز ۱۵>>](./15_python_type_errors.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)
- [📘 روز ۱۴](#-روز-۱۴)
  - [توابع مرتبه بالا](#توابع-مرتبه-بالا)
    - [تابع به عنوان پارامتر](#تابع-به-عنوان-پارامتر)
    - [تابع به عنوان مقدار بازگشتی](#تابع-به-عنوان-مقدار-بازگشتی)
  - [Closureهای پایتون](#closureهای-پایتون)
  - [Decoratorهای پایتون](#decoratorهای-پایتون)
    - [ایجاد Decoratorها](#ایجاد-decoratorها)
    - [اعمال چند Decorator به یک تابع](#اعمال-چند-decorator-به-یک-تابع)
    - [پذیرش پارامتر در توابع Decorator](#پذیرش-پارامتر-در-توابع-decorator)
  - [توابع داخلی مرتبه بالا](#توابع-داخلی-مرتبه-بالا)
    - [پایتون - تابع Map](#پایتون---تابع-map)
    - [پایتون - تابع Filter](#پایتون---تابع-filter)
    - [پایتون - تابع Reduce](#پایتون---تابع-reduce)
  - [💻 تمرین‌ها: روز ۱۴](#-تمرین‌ها-روز-۱۴)
    - [تمرین‌ها: سطح ۱](#تمرین‌ها-سطح-۱)
    - [تمرین‌ها: سطح ۲](#تمرین‌ها-سطح-۲)
    - [تمرین‌ها: سطح ۳](#تمرین‌ها-سطح-۳)

# 📘 روز ۱۴

## توابع مرتبه بالا

در پایتون با توابع به عنوان شهروندان درجه یک (first class citizens) رفتار می‌شود، که به شما امکان می‌دهد عملیات زیر را روی توابع انجام دهید:

- یک تابع می‌تواند یک یا چند تابع را به عنوان پارامتر بپذیرد
- یک تابع می‌تواند به عنوان نتیجه یک تابع دیگر بازگردانده شود
- یک تابع می‌تواند اصلاح شود
- یک تابع می‌تواند به یک متغیر تخصیص داده شود

در این بخش، ما موارد زیر را پوشش خواهیم داد:

1. مدیریت توابع به عنوان پارامتر
2. بازگرداندن توابع به عنوان مقدار بازگشتی از توابع دیگر
3. استفاده از closureها و decoratorهای پایتون

### تابع به عنوان پارامتر

```py
def sum_numbers(nums):  # تابع معمولی
    return sum(nums)    # یک تابع غمگین که از تابع داخلی sum سوءاستفاده می‌کند :<

def higher_order_function(f, lst):  # تابع به عنوان پارامتر
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)       # 15```

### تابع به عنوان مقدار بازگشتی

```py
def square(x):          # تابع توان دو
    return x ** 2

def cube(x):            # تابع توان سه
    return x ** 3

def absolute(x):        # تابع قدر مطلق
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # یک تابع مرتبه بالا که یک تابع را باز می‌گرداند
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(3))       # 9
result = higher_order_function('cube')
print(result(3))       # 27
result = higher_order_function('absolute')
print(result(-3))      # 3
```

از مثال بالا می‌توانید ببینید که تابع مرتبه بالا بسته به پارامتر ارسال شده، توابع مختلفی را باز می‌گرداند.

## Closureهای پایتون

پایتون به یک تابع تودرتو (nested function) اجازه می‌دهد تا به اسکوپ (scope) بیرونی تابع دربرگیرنده خود دسترسی داشته باشد. این قابلیت به عنوان Closure شناخته می‌شود. بیایید نگاهی بیندازیم که closureها در پایتون چگونه کار می‌کنند. در پایتون، closure با تودرتو کردن یک تابع در داخل یک تابع دربرگیرنده دیگر و سپس بازگرداندن تابع داخلی ایجاد می‌شود. مثال زیر را ببینید.

**مثال:**

```py
def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5))  # 15
print(closure_result(10))  # 20
```

## Decoratorهای پایتون

Decorator یک الگوی طراحی (design pattern) در پایتون است که به کاربر اجازه می‌دهد تا قابلیت‌های جدیدی را به یک شیء موجود بدون تغییر ساختار آن اضافه کند. Decoratorها معمولاً قبل از تعریف تابعی که می‌خواهید آن را decorate کنید، فراخوانی می‌شوند.

### ایجاد Decoratorها

برای ایجاد یک تابع decorator، ما به یک تابع بیرونی با یک تابع wrapper داخلی نیاز داریم.

**مثال:**

```py
# تابع معمولی
def greeting():
    return 'Welcome to Python'
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
g = uppercase_decorator(greeting)
print(g())          # WELCOME TO PYTHON

## بیایید مثال بالا را با یک decorator پیاده‌سازی کنیم

'''این تابع decorator یک تابع مرتبه بالا است
که یک تابع را به عنوان پارامتر می‌گیرد'''
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())   # ['WELCOME', 'TO', 'PYTHON']
```

### اعمال چند Decorator به یک تابع

```py
'''این توابع decorator، توابع مرتبه بالایی هستند
که توابع را به عنوان پارامتر می‌گیرند'''

# Decorator اول
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# Decorator دوم
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string
    return wrapper

@split_string_decorator
@uppercase_decorator     # ترتیب decoratorها در این مورد مهم است - تابع .upper() روی لیست‌ها کار نمی‌کند
def greeting():
    return 'Welcome to Python'
print(greeting())   # ['WELCOME', 'TO', 'PYTHON']
```

### پذیرش پارامتر در توابع Decorator

بیشتر اوقات ما نیاز داریم که توابعمان پارامترهایی را بپذیرند، بنابراین ممکن است نیاز به تعریف یک decorator داشته باشیم که پارامترها را بپذیرد.

```py
def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name))

print_full_name("Asabeneh", "Yetayeh",'Finland')
```

## توابع داخلی مرتبه بالا

برخی از توابع داخلی مرتبه بالا که در این بخش پوشش می‌دهیم _map()_، _filter_ و _reduce_ هستند.
تابع لامبدا (Lambda) می‌تواند به عنوان پارامتر ارسال شود و بهترین مورد استفاده از توابع لامبدا در توابعی مانند map، filter و reduce است.

### پایتون - تابع Map

تابع ()map یک تابع داخلی است که یک تابع و یک iterable (شیء قابل پیمایش) را به عنوان پارامتر می‌گیرد.

```py
    # سینتکس
    map(function, iterable)
```

**مثال ۱:**

```py
numbers = [1, 2, 3, 4, 5] # iterable
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
# بیایید آن را با یک تابع لامبدا اعمال کنیم
numbers_squared = map(lambda x : x ** 2, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
```

**مثال ۲:**

```py
numbers_str = ['1', '2', '3', '4', '5']  # iterable
numbers_int = map(int, numbers_str)
print(list(numbers_int))    # [1, 2, 3, 4, 5]
```

**مثال ۳:**

```py
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable

def change_to_upper(name):
    return name.upper()

names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']

# بیایید آن را با یک تابع لامبدا اعمال کنیم
names_upper_cased = map(lambda name: name.upper(), names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']
```

کاری که map واقعاً انجام می‌دهد، پیمایش روی یک لیست است. به عنوان مثال، نام‌ها را به حروف بزرگ تبدیل کرده و یک لیست جدید را باز می‌گرداند.

### پایتون - تابع Filter

تابع ()filter تابع مشخص‌شده را که برای هر آیتم از iterable (لیست) مشخص‌شده، یک مقدار بولین (boolean) برمی‌گرداند، فراخوانی می‌کند. این تابع آیتم‌هایی را که معیار فیلترینگ را برآورده می‌کنند، فیلتر می‌کند.

```py
    # سینتکس
    filter(function, iterable)
```

**مثال ۱:**

```py
# بیایید فقط اعداد زوج را فیلتر کنیم
numbers = [1, 2, 3, 4, 5]  # iterable

def is_even(num):
    if num % 2 == 0:
        return True
    return False

even_numbers = filter(is_even, numbers)
print(list(even_numbers))       # [2, 4]
```

**مثال ۲:**

```py
numbers = [1, 2, 3, 4, 5]  # iterable

def is_odd(num):
    if num % 2 != 0:
        return True
    return False

odd_numbers = filter(is_odd, numbers)
print(list(odd_numbers))       # [1, 3, 5]
```

```py
# فیلتر کردن نام‌های طولانی
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable
def is_name_long(name):
    if len(name) > 7:
        return True
    return False

long_names = filter(is_name_long, names)
print(list(long_names))         # ['Asabeneh']
```

### پایتون - تابع Reduce

تابع _reduce()_ در ماژول functools تعریف شده است و ما باید آن را از این ماژول import کنیم. مانند map و filter، این تابع دو پارامتر، یک تابع و یک iterable، می‌گیرد. با این حال، یک iterable دیگر را باز نمی‌گرداند، بلکه یک مقدار واحد را برمی‌گرداند.
**مثال ۱:**

```py
from functools import reduce

numbers_str = ['1', '2', '3', '4', '5']  # iterable
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)    # 15
```

## 💻 تمرین‌ها: روز ۱۴

```py
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

### تمرین‌ها: سطح ۱

1. تفاوت بین map، filter و reduce را توضیح دهید.
2. تفاوت بین تابع مرتبه بالا، closure و decorator را توضیح دهید.
3. یک تابع فراخوانی قبل از map، filter یا reduce تعریف کنید، به مثال‌ها مراجعه کنید.
4. از حلقه for برای چاپ هر کشور در لیست countries استفاده کنید.
5. از for برای چاپ هر نام در لیست names استفاده کنید.
6. از for برای چاپ هر عدد در لیست numbers استفاده کنید.

### تمرین‌ها: سطح ۲

1. از map برای ایجاد یک لیست جدید با تبدیل هر کشور به حروف بزرگ در لیست countries استفاده کنید.
1. از map برای ایجاد یک لیست جدید با تبدیل هر عدد به توان دوی آن در لیست numbers استفاده کنید.
1. از map برای تبدیل هر نام به حروف بزرگ در لیست names استفاده کنید.
1. از filter برای فیلتر کردن کشورهایی که شامل 'land' هستند، استفاده کنید.
1. از filter برای فیلتر کردن کشورهایی که دقیقاً شش کاراکتر دارند، استفاده کنید.
1. از filter برای فیلتر کردن کشورهایی که شش حرف یا بیشتر در لیست کشورها دارند، استفاده کنید.
1. از filter برای فیلتر کردن کشورهایی که با 'E' شروع می‌شوند، استفاده کنید.
1. دو یا چند پیمایشگر لیست را زنجیره‌ای کنید (مثلاً arr.map(callback).filter(callback).reduce(callback)).
1. تابعی به نام get_string_lists تعریف کنید که یک لیست به عنوان پارامتر می‌گیرد و سپس لیستی را برمی‌گرداند که فقط شامل آیتم‌های رشته‌ای است.
1. از reduce برای جمع کردن تمام اعداد در لیست numbers استفاده کنید.
1. از reduce برای الحاق تمام کشورها و تولید این جمله استفاده کنید: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
1. تابعی به نام categorize_countries تعریف کنید که لیستی از کشورها با الگوی مشترک را برمی‌گرداند (شما می‌توانید [لیست کشورها](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py) را در این مخزن به عنوان countries.js پیدا کنید (مثلاً 'land', 'ia', 'island', 'stan')).
1. تابعی ایجاد کنید که یک دیکشنری برمی‌گرداند، که در آن کلیدها حروف ابتدایی کشورها و مقادیر تعداد نام کشورهایی است که با آن حرف شروع می‌شوند.
2. تابعی به نام get_first_ten_countries تعریف کنید - این تابع لیستی از ده کشور اول را از لیست countries.js در پوشه data برمی‌گرداند.
1. تابعی به نام get_last_ten_countries تعریف کنید که ده کشور آخر در لیست countries را برمی‌گرداند.

### تمرین‌ها: سطح ۳

1. از فایل countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) استفاده کنید و وظایف زیر را دنبال کنید:
   - کشورها را بر اساس نام، پایتخت، جمعیت مرتب کنید.
   - ده زبان پرتکلم را بر اساس موقعیت مکانی مرتب کنید.
   - ده کشور پرجمعیت را مرتب کنید.

🎉 تبریک می‌گویم! 🎉

[<< روز ۱۳](./13_list_comprehension.md) | [روز ۱۵>>](./15_python_type_errors.md)
