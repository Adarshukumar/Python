<div align="center">
  <h1> ۳۰ روز پایتون: روز ۱۱ - توابع</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>نویسنده:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small> ویرایش دوم: ژوئیه، ۲۰۲۱</small>
</sub>

</div>

[<< روز ۱۰](./10_loops.md) | [روز ۱۲ >>](./12_modules.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 روز ۱۱](#-روز-۱۱)
  - [توابع](#توابع)
    - [تعریف یک تابع](#تعریف-یک-تابع)
    - [اعلام و فراخوانی یک تابع](#اعلام-و-فراخوانی-یک-تابع)
    - [تابع بدون پارامتر](#تابع-بدون-پارامتر)
    - [تابع بازگشت‌دهنده مقدار - بخش ۱](#تابع-بازگشت‌دهنده-مقدار---بخش-۱)
    - [تابع با پارامترها](#تابع-با-پارامترها)
    - [گذراندن آرگومان‌ها با کلید و مقدار](#گذراندن-آرگومان‌ها-با-کلید-و-مقدار)
    - [تابع بازگشت‌دهنده مقدار - بخش ۲](#تابع-بازگشت‌دهنده-مقدار---بخش-۲)
    - [تابع با پارامترهای پیش‌فرض](#تابع-با-پارامترهای-پیش‌فرض)
    - [تعداد دلخواه آرگومان‌ها](#تعداد-دلخواه-آرگومان‌ها)
    - [پارامترهای پیش‌فرض و تعداد دلخواه در توابع](#پارامترهای-پیش‌فرض-و-تعداد-دلخواه-در-توابع)
    - [تابع به عنوان پارامتر تابع دیگر](#تابع-به-عنوان-پارامتر-تابع-دیگر)
  - [شهادت](#شهادت)
  - [💻 تمرین‌ها: روز ۱۱](#-تمرین‌ها-روز-۱۱)
    - [تمرین‌ها: سطح ۱](#تمرین‌ها-سطح-۱)
    - [تمرین‌ها: سطح ۲](#تمرین‌ها-سطح-۲)
    - [تمرین‌ها: سطح ۳](#تمرین‌ها-سطح-۳)

# 📘 روز ۱۱

## توابع

تاکنون بسیاری از توابع داخلی پایتون را دیده‌ایم. در این بخش، بر روی توابع سفارشی تمرکز خواهیم کرد. تابع چیست؟ قبل از اینکه شروع به ساخت توابع کنیم، بیایید یاد بگیریم که تابع چیست و چرا به آنها نیاز داریم؟

### تعریف یک تابع

تابع یک بلوک کد قابل استفاده مجدد یا دستورات برنامه‌نویسی است که برای انجام یک وظیفه خاص طراحی شده است. برای تعریف یا اعلام یک تابع، پایتون کلمه کلیدی _def_ را فراهم می‌کند. در ادامه نحو تعریف یک تابع آمده است. بلوک کد تابع تنها زمانی اجرا می‌شود که تابع فراخوانی یا احضار شود.

### اعلام و فراخوانی یک تابع

وقتی یک تابع می‌سازیم، به آن اعلام تابع می‌گوییم. وقتی شروع به استفاده از آن می‌کنیم، به آن _فراخوانی_ یا _احضار_ تابع می‌گوییم. تابع می‌تواند با یا بدون پارامتر اعلام شود.

```py
# نحو
# اعلام یک تابع
def function_name():
    کدها
    کدها
# فراخوانی یک تابع
function_name()
```

### تابع بدون پارامتر

تابع می‌تواند بدون پارامتر اعلام شود.

**مثال:**

```py
def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name () # فراخوانی یک تابع

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()
```

### تابع بازگشت‌دهنده مقدار - بخش ۱

توابع با استفاده از دستور `return` مقادیر را برمی‌گردانند. اگر تابعی دستور `return` نداشته باشد، مقدار `None` را برمی‌گرداند. بیایید توابع بالا را با استفاده از `return` بازنویسی کنیم. از این به بعد، هنگام فراخوانی یک تابع، مقداری از آن دریافت می‌کنیم و آن را چاپ می‌کنیم.

```py
def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print(generate_full_name())

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    return total
print(add_two_numbers())
```

### تابع با پارامترها

در یک تابع می‌توانیم انواع داده‌های مختلف (عدد، رشته، بولی، لیست، تاپل، دیکشنری یا مجموعه) را به عنوان پارامتر بگذرانیم.

- پارامتر تکی: اگر تابع ما پارامتری بگیرد، باید تابع را با یک آرگومان فراخوانی کنیم.

```py
  # نحو
  # اعلام یک تابع
  def function_name(parameter):
    کدها
    کدها
  # فراخوانی تابع
  print(function_name(argument))
```

**مثال:**

```py
def greetings (name):
    message = name + ', welcome to Python for Everyone!'
    return message

print(greetings('Asabeneh'))

def add_ten(num):
    ten = 10
    return num + ten
print(add_ten(90))

def square_number(x):
    return x * x
print(square_number(2))

def area_of_circle (r):
    PI = 3.14
    area = PI * r ** 2
    return area
print(area_of_circle(10))

def sum_of_numbers(n):
    total = 0
    for i in range(n+1):
        total+=i
    return total
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
```

- دو پارامتر: یک تابع ممکن است پارامتر یا پارامترهایی داشته باشد یا نداشته باشد. یک تابع همچنین ممکن است دو یا چند پارامتر داشته باشد. اگر تابع ما پارامترهایی بگیرد، باید آن را با آرگومان‌ها فراخوانی کنیم. بیایید یک تابع با دو پارامتر بررسی کنیم:

```py
  # نحو
  # اعلام یک تابع
  def function_name(para1, para2):
    کدها
    کدها
  # فراخوانی تابع
  print(function_name(arg1, arg2))
```

**مثال:**

```py
def generate_full_name (first_name, last_name):
    space = ' '
    full_name = first_name + space + last_name
    return full_name
print('Full Name: ', generate_full_name('Asabeneh','Yetayeh'))

def sum_two_numbers (num_one, num_two):
    sum = num_one + num_two
    return sum
print('Sum of two numbers: ', sum_two_numbers(1, 9))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age

print('Age: ', calculate_age(2021, 1819))

def weight_of_object (mass, gravity):
    weight = str(mass * gravity)+ ' N' # مقدار باید ابتدا به رشته تبدیل شود
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100, 9.81))
```

### گذراندن آرگومان‌ها با کلید و مقدار

اگر آرگومان‌ها را با کلید و مقدار بگذرانیم، ترتیب آرگومان‌ها اهمیتی ندارد.

```py
# نحو
# اعلام یک تابع
def function_name(para1, para2):
    کدها
    کدها
# فراخوانی تابع
print(function_name(para1 = 'John', para2 = 'Doe')) # ترتیب آرگومان‌ها اینجا اهمیتی ندارد
```

**مثال:**

```py
def print_fullname(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    print(full_name)
print_fullname(firstname = 'Asabeneh', lastname = 'Yetayeh')

def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(num2 = 3, num1 = 2)) # ترتیب اهمیتی ندارد
```

### تابع بازگشت‌دهنده مقدار - بخش ۲

اگر با یک تابع مقداری برنگردانیم، تابع ما به طور پیش‌فرض _None_ را برمی‌گرداند. برای بازگرداندن مقداری با یک تابع، از کلمه کلیدی _return_ به دنبال متغیری که برمی‌گردانیم استفاده می‌کنیم. می‌توانیم هر نوع داده‌ای را از یک تابع برگردانیم.

- بازگشت یک رشته:
**مثال:**

```py
def print_name(firstname):
    return firstname
print_name('Asabeneh') # Asabeneh

def print_full_name(firstname, lastname):
    space = ' '
    full_name = firstname  + space + lastname
    return full_name
print_full_name(firstname='Asabeneh', lastname='Yetayeh')
```

- بازگشت یک عدد:

**مثال:**

```py
def add_two_numbers (num1, num2):
    total = num1 + num2
    return total
print(add_two_numbers(2, 3))

def calculate_age (current_year, birth_year):
    age = current_year - birth_year
    return age
print('Age: ', calculate_age(2019, 1819))
```

- بازگشت یک بولی:
  **مثال:**

```py
def is_even (n):
    if n % 2 == 0:
        print('even')
        return True    # return اجرای بیشتر تابع را متوقف می‌کند، مشابه break 
    return False
print(is_even(10)) # True
print(is_even(7)) # False
```

- بازگشت یک لیست:
  **مثال:**

```py
def find_even_numbers(n):
    evens = []
    for i in range(n + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
print(find_even_numbers(10))
```

### تابع با پارامترهای پیش‌فرض

گاهی اوقات مقادیر پیش‌فرض را به پارامترها می‌گذرانیم، وقتی تابع را احضار می‌کنیم. اگر آرگومان‌هایی را هنگام فراخوانی تابع نگذرانیم، مقادیر پیش‌فرض آنها استفاده خواهد شد.

```py
# نحو
# اعلام یک تابع
def function_name(param = value):
    کدها
    کدها
# فراخوانی تابع
function_name()
function_name(arg)
```

**مثال:**

```py
def greetings (name = 'Peter'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings())
print(greetings('Asabeneh'))

def generate_full_name (first_name = 'Asabeneh', last_name = 'Yetayeh'):
    space = ' '
    full_name = first_name + space + last_name
    return full_name

print(generate_full_name())
print(generate_full_name('David','Smith'))

def calculate_age (birth_year,current_year = 2021):
    age = current_year - birth_year
    return age;
print('Age: ', calculate_age(1821))

def weight_of_object (mass, gravity = 9.81):
    weight = str(mass * gravity)+ ' N' # مقدار باید ابتدا به رشته تبدیل شود
    return weight
print('Weight of an object in Newtons: ', weight_of_object(100)) # 9.81 - میانگین گرانش روی سطح زمین
print('Weight of an object in Newtons: ', weight_of_object(100, 1.62)) # گرانش روی سطح ماه
```

### تعداد دلخواه آرگومان‌ها

اگر تعداد آرگومان‌هایی که به تابع خود می‌گذرانیم را ندانیم، می‌توانیم تابعی ایجاد کنیم که تعداد دلخواهی آرگومان را بگیرد با اضافه کردن \* قبل از نام پارامتر.

```py
# نحو
# اعلام یک تابع
def function_name(*args):
    کدها
    کدها
# فراخوانی تابع
function_name(param1, param2, param3,..)
```

**مثال:**

```py
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # همان total = total + num 
    return total
print(sum_all_nums(2, 3, 5)) # 10
```

### پارامترهای پیش‌فرض و تعداد دلخواه در توابع

```py
def generate_groups (team,*args):
    print(team)
    for i in args:
        print(i)
generate_groups('Team-1','Asabeneh','Brook','David','Eyob')
```

### بازکردن دیکشنری (Dictionary unpacking)

می‌توانید تابعی که آرگومان‌های نام‌دار می‌گیرد را با یک دیکشنری که کلیدهایش با نام پارامترها یکی‌ست، صدا بزنید. برای این کار از ``**`` استفاده می‌کنیم.

```py
# تعریف تابعی که دو آرگومان می‌گیرد: 'name' و 'location'
def greet(name, location):
    # پیام خوش‌آمدگویی با استفاده از آرگومان‌های ورودی چاپ می‌کند
    print("Hi there", name, "how is the weather in", location)

# فراخوانی تابع با استفاده از آرگومان‌های کلیدی (keyword)
greet(name="Alice", location="New York")  
# خروجی: Hi there Alice how is the weather in New York

# ساخت یک دیکشنری با کلیدهای برابر با نام پارامترها
my_dict = {"name": "Alice", "location": "New York"}

# فراخوانی تابع با بازکردن دیکشنری (Dictionary unpacking)
greet(**my_dict)  
# عملگر ** دیکشنری را باز می‌کند و جفت کلید-مقدارها را به صورت آرگومان نام‌دار ارسال می‌کند
# خروجی: Hi there Alice how is the weather in New York
```

### تعداد دلخواه آرگومان‌های نام‌دار

می‌توانید تابعی تعریف کنید که تعداد دلخواهی آرگومان نام‌دار بگیرد.

```py
def arbitrary_named_args(**args):
    print("تعدادی آرگومان نام‌دار به صورت دلخواه گرفتم، مجموعاً", len(args))
    print("آرگومان‌ها به صورت دیکشنری به تابع داده شده‌اند:", type(args))
    print("بیایید آنها را چاپ کنیم:")
    for k, v in args.items():
        print(" * کلید:", k, "مقدار:", v)
```

در کل، مگر در مواقع ضروری، از این روش استفاده نکنید چون فهمیدن اینکه تابع چه آرگومان‌هایی می‌گیرد و چه کاری انجام می‌دهد را سخت می‌کند.

### تابع به عنوان پارامتر تابع دیگر

```py
# می‌توانید توابع را به عنوان پارامتر بگذرانید
def square_number (n):
    return n ** n
def do_something(f, x):
    return f(x)
print(do_something(square_number, 3)) # 27
```

🌕 شما تا اینجا دستاوردهای زیادی داشته‌اید. ادامه دهید! شما چالش‌های روز ۱۱ را به پایان رساندید و ۱۱ گام جلوتر در مسیر بزرگی هستید. حالا چند تمرین برای مغز و عضلاتتان انجام دهید.

## اظهارات

حالا زمان آن است که افکار خود را در مورد نویسنده و ۳۰روزپایتون بیان کنید. می‌توانید اظهارات خود را در این [لینک](https://testimonial-s3sw.onrender.com/) بگذارید.

## 💻 تمرین‌ها: روز ۱۱

### تمرین‌ها: سطح ۱

۱. تابعی به نام _add_two_numbers_ اعلام کنید. دو پارامتر می‌گیرد و مجموع را برمی‌گرداند.
۲. مساحت دایره به صورت زیر محاسبه می‌شود: area = π x r x r. تابعی بنویسید که _area_of_circle_ را محاسبه کند.
۳. تابعی به نام add_all_nums بنویسید که تعداد دلخواهی آرگومان می‌گیرد و همه آرگومان‌ها را جمع می‌کند. بررسی کنید که آیا همه آیتم‌های لیست از نوع عدد هستند. اگر نه، بازخورد مناسبی بدهید.
۴. دما در °C می‌تواند با استفاده از این فرمول به °F تبدیل شود: °F = (°C x 9/5) + 32. تابعی بنویسید که °C را به °F تبدیل کند، _convert_celsius_to-fahrenheit_.
۵. تابعی به نام check-season بنویسید، که یک پارامتر ماه می‌گیرد و فصل را برمی‌گرداند: پاییز، زمستان، بهار یا تابستان.
۶. تابعی به نام calculate_slope بنویسید که شیب یک معادله خطی را برمی‌گرداند.
۷. معادله درجه دوم به صورت زیر محاسبه می‌شود: ax² + bx + c = ۰. تابعی بنویسید که مجموعه راه‌حل یک معادله درجه دوم را محاسبه کند، _solve_quadratic_eqn_.
۸. تابعی به نام print_list اعلام کنید. یک لیست را به عنوان پارامتر می‌گیرد و هر عنصر لیست را چاپ می‌کند.
۹. تابعی به نام reverse_list اعلام کنید. یک آرایه را به عنوان پارامتر می‌گیرد و معکوس آرایه را برمی‌گرداند (از حلقه‌ها استفاده کنید).

```py
print(reverse_list([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]
print(reverse_list(["A", "B", "C"]))
# ["C", "B", "A"]
```

۱۰. تابعی به نام capitalize_list_items اعلام کنید. یک لیست را به عنوان پارامتر می‌گیرد و لیستی از آیتم‌های بزرگ‌نوشته‌شده را برمی‌گرداند.
۱۱. تابعی به نام add_item اعلام کنید. یک لیست و یک پارامتر آیتم می‌گیرد. لیستی با آیتم اضافه‌شده در انتها برمی‌گرداند.

```py
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_stuff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat']
numbers = [2, 3, 7, 9]
print(add_item(numbers, 5))    #  [2, 3, 7, 9, 5]
```

۱۲. تابعی به نام remove_item اعلام کنید. یک لیست و یک پارامتر آیتم می‌گیرد. لیستی با آیتم حذف‌شده از آن برمی‌گرداند.

```py
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  # [2, 7, 9]
```

۱۳. تابعی به نام sum_of_numbers اعلام کنید. یک پارامتر عدد می‌گیرد و همه اعداد در آن محدوده را جمع می‌کند.

```py
print(sum_of_numbers(5))  # 15
print(sum_of_numbers(10)) # 55
print(sum_of_numbers(100)) # 5050
```

۱۴. تابعی به نام sum_of_odds اعلام کنید. یک پارامتر عدد می‌گیرد و همه اعداد فرد در آن محدوده را جمع می‌کند.
۱۵. تابعی به نام sum_of_even اعلام کنید. یک پارامتر عدد می‌گیرد و همه اعداد زوج در آن محدوده را جمع می‌کند.

### تمرین‌ها: سطح ۲

۱. تابعی به نام evens_and_odds اعلام کنید. یک عدد صحیح مثبت را به عنوان پارامتر می‌گیرد و تعداد زوج‌ها و فردها در عدد را شمارش می‌کند.

```py
    print(evens_and_odds(100))
    # تعداد فردها ۵۰ است.
    # تعداد زوج‌ها ۵۱ است.
```

۲. تابع خود را به نام factorial صدا بزنید، یک عدد صحیح را به عنوان پارامتر می‌گیرد و فاکتوریل عدد را برمی‌گرداند.
۳. تابع خود را با نام _is_empty_ صدا بزنید، یک پارامتر می‌گیرد و بررسی می‌کند آیا تهی است یا نه.
۴. توابع مختلفی بنویسید که برای لیست‌ها به کار می‌روند. باید توابعی مانند calculate_mean، calculate_median، calculate_mode، calculate_range، calculate_variance و calculate_std (انحراف معیار) را بسازید.
۵. تابعی به نام _greet_ بنویسید که یک آرگومان پیش‌فرض به نام _name_ می‌گیرد. اگر هیچ آرگومانی ارسال نشود، باید "Hello, Guest!" را چاپ کند، در غیر این صورت باید شخص را با نام مورد نظر خوشامد بگوید.

```py
    greet()
    # "سلام، مهمان!"
    greet("Alice")
    # "سلام، Alice!"
```
۶. تابعی به نام _show_args_ بسازید که تعداد دلخواهی از آرگومان‌های نام‌دار را می‌گیرد و نام و مقدارشان را چاپ می‌کند.
   ```py
   show_args(name="Alice", age=30, city="New York")
   # خروجی: نام: Alice، سن: 30، شهر: New York
   show_args(name="Bob", pet="Fluffy, the bunny")
   # خروجی: نام: Bob، حیوان خانگی: Fluffy, the bunny
   ```

### تمرین‌ها: سطح ۳

۱. تابعی به نام is_prime بنویسید، که بررسی می‌کند آیا یک عدد اول است.
۲. تابعی بنویسید که بررسی می‌کند آیا همه آیتم‌ها در لیست منحصر به فرد هستند.
۳. تابعی بنویسید که بررسی می‌کند آیا همه آیتم‌های لیست از یک نوع داده هستند.
۴. تابعی بنویسید که بررسی می‌کند آیا متغیر ارائه‌شده یک متغیر معتبر پایتون است.
۵. به پوشه data بروید و به فایل countries-data.py دسترسی پیدا کنید.

- تابعی به نام most_spoken_languages در جهان ایجاد کنید. باید ۱۰ یا ۲۰ زبان پرگویش جهان را به ترتیب نزولی برگرداند.
- تابعی به نام most_populated_countries ایجاد کنید. باید ۱۰ یا ۲۰ کشور پرجمعیت را به ترتیب نزولی برگرداند.

🎉 تبریک ! 🎉

[<< روز ۱۰](./10_loops.md) | [روز ۱۲ >>](./12_modules.md)
