<div align="center">
  <h1> ۳۰ روز پایتون: روز ۲۱ - کلاس‌ها و اشیاء</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>نویسنده:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small>ویرایش دوم: جولای، ۲۰۲۱</small>
</sub>

</div>

[<< روز ۲۰](./20_python_package_manager.md) | [روز ۲۲ >>](./22_web_scraping.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 روز ۲۱](#-روز-۲۱)
  - [کلاس‌ها و اشیاء](#کلاسها-و-اشیاء)
    - [ایجاد یک کلاس](#ایجاد-یک-کلاس)
    - [ایجاد یک شیء](#ایجاد-یک-شیء)
    - [سازنده کلاس](#سازنده-کلاس)
    - [متدهای پیش‌فرض شیء](#متدهای-پیشفرض-شیء)
    - [متدی برای تغییر مقادیر پیش‌فرض کلاس](#متدی-برای-تغییر-مقادیر-پیشفرض-کلاس)
    - [ارث‌بری (Inheritance)](#ارثبری-inheritance)
    - [بازنویسی (Overriding) متد والد](#بازنویسی-overriding-متد-والد)
  - [💻 تمرین‌ها: روز ۲۱](#-تمرینها-روز-۲۱)
    - [تمرین‌ها: سطح ۱](#تمرینها-سطح-۱)
    - [تمرین‌ها: سطح ۲](#تمرینها-سطح-۲)
    - [تمرین‌ها: سطح ۳](#تمرینها-سطح-۳)

# 📘 روز ۲۱

## کلاس‌ها و اشیاء

پایتون یک زبان برنامه‌نویسی شیءگرا است. [9] همه چیز در پایتون یک شیء (object) است، با خصوصیات (properties) و متدهای (methods) خود. [9, 14] یک عدد، رشته، لیست، دیکشنری، تاپل، مجموعه و غیره که در یک برنامه استفاده می‌شود، یک شیء از یک کلاس داخلی مربوط به خود است. ما کلاس را برای ایجاد یک شیء می‌سازیم. یک کلاس مانند یک سازنده شیء (object constructor) یا یک «طرح اولیه» (blueprint) برای ایجاد اشیاء است. [14] ما برای ایجاد یک شیء، یک کلاس را نمونه‌سازی (instantiate) می‌کنیم. کلاس، صفات (attributes) و رفتار (behavior) شیء را تعریف می‌کند، در حالی که شیء، از طرف دیگر، نماینده کلاس است.

ما از همان ابتدای این چالش، ندانسته با کلاس‌ها و اشیاء کار کرده‌ایم. هر عنصری در یک برنامه پایتون، یک شیء از یک کلاس است. [3]
بیایید بررسی کنیم که آیا همه چیز در پایتون یک کلاس است یا نه:

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> num = 10
>>> type(num)
<class 'int'>
>>> string = 'string'
>>> type(string)
<class 'str'>
>>> boolean = True
>>> type(boolean)
<class 'bool'>
>>> lst = []
>>> type(lst)
<class 'list'>
>>> tpl = ()
>>> type(tpl)
<class 'tuple'>
>>> set1 = set()
>>> type(set1)
<class 'set'>
>>> dct = {}
>>> type(dct)
<class 'dict'>
```

### ایجاد یک کلاس

برای ایجاد یک کلاس، به کلمه کلیدی **class** و سپس نام کلاس و یک دو نقطه نیاز داریم. نام کلاس باید به صورت **CamelCase** باشد.

```sh
# syntax
class ClassName:
  code goes here
```

**مثال:**

```py
class Person:
  pass
print(Person)
```

```sh
<__main__.Person object at 0x10804e510>
```

### ایجاد یک شیء

ما می‌توانیم با فراخوانی کلاس، یک شیء ایجاد کنیم.

```py
p = Person()
print(p)
```

### سازنده کلاس

در مثال‌های بالا، ما یک شیء از کلاس Person ایجاد کرده‌ایم. با این حال، یک کلاس بدون سازنده (constructor) در کاربردهای واقعی چندان مفید نیست. [12] بیایید از تابع سازنده استفاده کنیم تا کلاس خود را مفیدتر کنیم. مانند تابع سازنده در جاوا یا جاوا اسکریپت، پایتون نیز یک تابع سازنده داخلی به نام **__init__**() دارد. [3, 4, 14] تابع سازنده **__init__** دارای پارامتر self است که یک ارجاع به نمونه فعلی کلاس است.
**مثال‌ها:**

```py
class Person:
      def __init__ (self, name):
        # self allows to attach parameter to the class
          self.name =name

p = Person('Asabeneh')
print(p.name)
print(p)
```

```sh
# output
Asabeneh
<__main__.Person object at 0x2abf46907e80>
```

بیایید پارامترهای بیشتری به تابع سازنده اضافه کنیم.

```py
class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city


p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
print(p.firstname)
print(p.lastname)
print(p.age)
print(p.country)
print(p.city)
```

```sh
# output
Asabeneh
Yetayeh
250
Finland
Helsinki```

### متدهای شیء

اشیاء می‌توانند متد داشته باشند. متدها توابعی هستند که به شیء تعلق دارند. [16]

**مثال:**

```py
class Person:
      def __init__(self, firstname, lastname, age, country, city):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'

p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
print(p.person_info())
```

```sh
# output
Asabeneh Yetayeh is 250 years old. He lives in Helsinki, Finland
```

### متدهای پیش‌فرض شیء

گاهی اوقات، ممکن است بخواهید برای متدهای شیء خود مقادیر پیش‌فرض داشته باشید. اگر در سازنده، برای پارامترها مقادیر پیش‌فرض تعیین کنیم، می‌توانیم از بروز خطا هنگام فراخوانی یا نمونه‌سازی کلاس بدون پارامتر جلوگیری کنیم. بیایید ببینیم چگونه به نظر می‌رسد:

**مثال:**

```py
class Person:
      def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'

p1 = Person()
print(p1.person_info())
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())
```

```sh
# output
Asabeneh Yetayeh is 250 years old. He lives in Helsinki, Finland.
John Doe is 30 years old. He lives in Noman city, Nomanland.
```

### متدی برای تغییر مقادیر پیش‌فرض کلاس

در مثال زیر، در کلاس Person، تمام پارامترهای سازنده دارای مقادیر پیش‌فرض هستند. علاوه بر این، ما یک پارامتر skills داریم که می‌توانیم با استفاده از یک متد به آن دسترسی پیدا کنیم. بیایید متد add_skill را برای افزودن مهارت‌ها به لیست skills ایجاد کنیم.

```py
class Person:
      def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
          self.firstname = firstname
          self.lastname = lastname
          self.age = age
          self.country = country
          self.city = city
          self.skills = []

      def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'
      def add_skill(self, skill):
          self.skills.append(skill)

p1 = Person()
print(p1.person_info())
p1.add_skill('HTML')
p1.add_skill('CSS')
p1.add_skill('JavaScript')
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())
print(p1.skills)
print(p2.skills)
```

```sh
# output
Asabeneh Yetayeh is 250 years old. He lives in Helsinki, Finland.
John Doe is 30 years old. He lives in Noman city, Nomanland.
['HTML', 'CSS', 'JavaScript']
[]
```

### ارث‌بری (Inheritance)

با استفاده از ارث‌بری می‌توانیم از کدهای کلاس والد مجدداً استفاده کنیم. [6, 8] ارث‌بری به ما این امکان را می‌دهد که کلاسی را تعریف کنیم که تمام متدها و خصوصیات را از کلاس والد به ارث ببرد. [6, 11] کلاس والد یا سوپرکلاس یا کلاس پایه، کلاسی است که تمام متدها و خصوصیات را ارائه می‌دهد. کلاس فرزند کلاسی است که از کلاس دیگری یا کلاس والد ارث می‌برد. [7, 8]
بیایید با ارث‌بری از کلاس Person، یک کلاس Student ایجاد کنیم.

```py
class Student(Person):
    pass


s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)

```

```sh
output
Eyob Yetayeh is 30 years old. He lives in Helsinki, Finland.
['JavaScript', 'React', 'Python']
Lidiya Teklemariam is 28 years old. He lives in Espoo, Finland.
['Organizing', 'Marketing', 'Digital Marketing']
```

ما در کلاس فرزند، سازنده **__init__**() را فراخوانی نکردیم. اگر آن را فراخوانی نکنیم، همچنان می‌توانیم به تمام خصوصیات از کلاس والد دسترسی داشته باشیم. اما اگر سازنده را فراخوانی کنیم، می‌توانیم با فراخوانی _super_ به خصوصیات والد دسترسی پیدا کنیم.
ما می‌توانیم یک متد جدید به کلاس فرزند اضافه کنیم یا می‌توانیم متدهای کلاس والد را با ایجاد متدی با همان نام در کلاس فرزند، بازنویسی (override) کنیم. [2] وقتی تابع **__init__**() را اضافه می‌کنیم، کلاس فرزند دیگر تابع **__init__**() والد را به ارث نخواهد برد. [7]

### بازنویسی (Overriding) متد والد

```py
class Student(Person):
    def __init__ (self, firstname='Asabeneh', lastname='Yetayeh',age=250, country='Finland', city='Helsinki', gender='male'):
        self.gender = gender
        super().__init__(firstname, lastname,age, country, city)
    def person_info(self):
        gender = 'He' if self.gender =='male' else 'She'
        return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'

s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki','male')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo', 'female')
print(s1.person_info())
s1.add_skill('JavaScript')
s1.add_skill('React')
s1.add_skill('Python')
print(s1.skills)

print(s2.person_info())
s2.add_skill('Organizing')
s2.add_skill('Marketing')
s2.add_skill('Digital Marketing')
print(s2.skills)```

```sh
Eyob Yetayeh is 30 years old. He lives in Helsinki, Finland.
['JavaScript', 'React', 'Python']
Lidiya Teklemariam is 28 years old. She lives in Espoo, Finland.
['Organizing', 'Marketing', 'Digital Marketing']
```

ما می‌توانیم از تابع داخلی super() یا نام والد یعنی Person برای به ارث بردن خودکار متدها و خصوصیات از والدش استفاده کنیم. در مثال بالا ما متد والد را بازنویسی کردیم. متد فرزند یک ویژگی متفاوت دارد، می‌تواند تشخیص دهد که جنسیت مذکر است یا مؤنث و ضمیر مناسب (He/She) را تخصیص دهد.

🌕 اکنون، شما با یک قدرت فوق‌العاده برنامه‌نویسی کاملاً شارژ شده‌اید. حالا برای مغز و عضلات خود چند تمرین انجام دهید.

## 💻 تمرین‌ها: روز ۲۱

### تمرین‌ها: سطح ۱

1. پایتون ماژولی به نام _statistics_ دارد و ما می‌توانیم از این ماژول برای انجام تمام محاسبات آماری استفاده کنیم. با این حال، برای یادگیری نحوه ساختن تابع و استفاده مجدد از آن، بیایید سعی کنیم برنامه‌ای توسعه دهیم که معیارهای گرایش به مرکز یک نمونه (میانگین، میانه، مد) و معیارهای پراکندگی (دامنه، واریانس، انحراف معیار) را محاسبه کند. علاوه بر این معیارها، حداقل، حداکثر، تعداد، صدک و توزیع فراوانی نمونه را پیدا کنید. شما می‌توانید کلاسی به نام Statistics ایجاد کنید و تمام توابعی که محاسبات آماری را انجام می‌دهند به عنوان متدهای کلاس Statistics ایجاد کنید. خروجی زیر را بررسی کنید.

```py
ages =

print('Count:', data.count()) # 25
print('Sum: ', data.sum()) # 744
print('Min: ', data.min()) # 24
print('Max: ', data.max()) # 38
print('Range: ', data.range()) # 14
print('Mean: ', data.mean()) # 30
print('Median: ', data.median()) # 29
print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', data.std()) # 4.2
print('Variance: ', data.var()) # 17.5
print('Frequency Distribution: ', data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]
```

```sh
# you output should look like this
print(data.describe())
Count: 25
Sum:  744
Min:  24
Max:  38
Range:  14
Mean:  30
Median:  29
Mode:  (26, 5)
Variance:  17.5
Standard Deviation:  4.2
Frequency Distribution: [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]
```

### تمرین‌ها: سطح ۲

۱. یک کلاس به نام `PersonAccount` بسازید. این کلاس دارای ویژگی‌های `firstname` (نام)، `lastname` (نام خانوادگی)، `incomes` (درآمدها) و `expenses` (هزینه‌ها) است. همچنین دارای متدهای `total_income` (مجموع درآمد)، `total_expense` (مجموع هزینه)، `account_info` (اطلاعات حساب)، `add_income` (افزودن درآمد)، `add_expense` (افزودن هزینه) و `account_balance` (موجودی حساب) می‌باشد. درآمدها مجموعه‌ای از مبالغ درآمد به همراه توضیحات آن‌هاست. همین امر در مورد هزینه‌ها نیز صادق است.

🎉 تبریک! 🎉

[<< روز ۲۰](./20_python_package_manager.md) | [روز ۲۲ >>](./22_web_scraping.md)
