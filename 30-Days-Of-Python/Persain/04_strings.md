<div align="center">
  <h1> ۳۰ روز با پایتون: روز چهارم - رشته‌ها</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="دنبال کردن در توییتر" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>نویسنده:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small> ویرایش دوم: ژوئیه ۲۰۲۱</small>
</sub>

</div>

[<< روز سوم](./03_operators.md) | [روز پنجم >>](./05_lists.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [روز چهارم](#روز-چهارم)
  - [رشته‌ها](#رشته‌ها)
    - [ایجاد یک رشته](#ایجاد-یک-رشته)
    - [الحاق رشته‌ها](#الحاق-رشته‌ها)
    - [سکانس‌های گریز در رشته‌ها](#سکانس‌های-گریز-در-رشته‌ها)
    - [قالب‌بندی رشته](#قالب‌بندی-رشته)
      - [قالب‌بندی رشته به سبک قدیم (عملگر %)](#قالب‌بندی-رشته-به-سبک-قدیم-عملگر)
      - [قالب‌بندی رشته به سبک جدید (str.format)](#قالب‌بندی-رشته-به-سبک-جدید-strformat)
      - [درون‌یابی رشته / f-String ها (پایتون 3.6+)](#درون‌یابی-رشته--f-string-ها-پایتون-36)
    - [رشته‌های پایتون به عنوان دنباله‌ای از کاراکترها](#رشته‌های-پایتون-به-عنوان-دنباله‌ای-از-کاراکترها)
      - [باز کردن کاراکترها](#باز-کردن-کاراکترها)
      - [دسترسی به کاراکترها در رشته‌ها بر اساس اندیس](#دسترسی-به-کاراکترها-در-رشته‌ها-بر-اساس-اندیس)
      - [برش زدن رشته‌های پایتون](#برش-زدن-رشته‌های-پایتون)
      - [معکوس کردن یک رشته](#معکوس-کردن-یک-رشته)
      - [رد کردن کاراکترها هنگام برش زدن](#رد-کردن-کاراکترها-هنگام-برش-زدن)
    - [متدهای رشته](#متدهای-رشته)
  - [💻 تمرینات - روز چهارم](#-تمرینات---روز-چهارم)

# روز چهارم

## رشته‌ها

متن یک نوع داده رشته‌ای است. هر نوع داده‌ای که به صورت متن نوشته شود، یک رشته است. هر داده‌ای که داخل تک کوتیشن، دابل کوتیشن یا سه کوتیشن قرار گیرد، رشته محسوب می‌شود. متدهای رشته و توابع داخلی مختلفی برای کار با نوع داده رشته وجود دارد. برای بررسی طول یک رشته از متد `len()` استفاده کنید.

### ایجاد یک رشته

```py
letter = 'P'                # یک رشته می‌تواند یک کاراکتر یا مجموعه‌ای از متون باشد
print(letter)               # P
print(len(letter))          # 1
greeting = 'Hello, World!'  # رشته می‌تواند با استفاده از تک کوتیشن یا دابل کوتیشن ساخته شود، "Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 13
sentence = "I hope you are enjoying 30 days of Python Challenge"
print(sentence)
```

رشته چند خطی با استفاده از سه تک کوتیشن (''') یا سه دابل کوتیشن (""") ایجاد می‌شود. مثال زیر را ببینید.

```py
multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)

# روش دیگری برای انجام همین کار
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)
```

### الحاق رشته‌ها

ما می‌توانیم رشته‌ها را به هم متصل کنیم. ادغام یا اتصال رشته‌ها را الحاق می‌نامند. مثال زیر را ببینید:

```py
first_name = 'Asabeneh'
last_name = 'Yetayeh'
space = ' '
full_name = first_name  +  space + last_name
print(full_name) # Asabeneh Yetayeh
# بررسی طول یک رشته با استفاده از تابع داخلی len()
print(len(first_name))  # 8
print(len(last_name))   # 7
print(len(first_name) > len(last_name)) # True
print(len(full_name)) # 16
```

### سکانس‌های گریز در رشته‌ها

در پایتون و دیگر زبان‌های برنامه‌نویسی، `\` و به دنبال آن یک کاراکتر، یک سکانس گریز است. بیایید رایج‌ترین کاراکترهای گریز را ببینیم:

  - `\n`: خط جدید
  - `\t`: تب به معنای (۸ فاصله)
  - `\\`: بک‌اسلش
  - `\'`: تک کوتیشن (')
  - `\"`: دابل کوتیشن (")

حالا بیایید کاربرد سکانس‌های گریز بالا را با مثال ببینیم.

```py
print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # شکست خط
print('Days\tTopics\tExercises') # اضافه کردن فاصله تب یا ۴ فاصله
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
print('This is a backslash  symbol (\\)') # برای نوشتن یک بک‌اسلش
print('In every programming language it starts with \"Hello, World!\"') # برای نوشتن دابل کوتیشن داخل تک کوتیشن

# خروجی
I hope every one is enjoying the Python Challenge.
Are you ?
Days  Topics  Exercises
Day 1 5     5
Day 2 6     20
Day 3 5     23
Day 4 1     35
This is a backslash  symbol (\)
In every programming language it starts with "Hello, World!"
```

### قالب‌بندی رشته

#### قالب‌بندی رشته به سبک قدیم (عملگر %)

در پایتون راه‌های زیادی برای قالب‌بندی رشته‌ها وجود دارد. در این بخش، برخی از آنها را پوشش خواهیم داد.
عملگر `"%"` برای قالب‌بندی مجموعه‌ای از متغیرهای محصور در یک "تاپل" (یک لیست با اندازه ثابت)، به همراه یک رشته قالب، که حاوی متن عادی به همراه "مشخص‌کننده‌های آرگومان"، نمادهای ویژه‌ای مانند `"%s"`، `"%d"`، `"%f"`، `%.<small>تعداد ارقام</small>f"` است، استفاده می‌شود.

  - `%s` - رشته (یا هر شیء با نمایش رشته‌ای، مانند اعداد)
  - `%d` - اعداد صحیح
  - `%f` - اعداد ممیز شناور
  - `%.<small>تعداد ارقام</small>f` - اعداد ممیز شناور با دقت ثابت

<!-- end list -->

```py
# فقط رشته‌ها
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
print(formated_string)

# رشته‌ها و اعداد
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area) # 2 به ۲ رقم معنی‌دار بعد از نقطه اشاره دارد

python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
formated_string = 'The following are python libraries:%s' % (python_libraries)
print(formated_string) # "The following are python libraries:['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']"
```

#### قالب‌بندی رشته به سبک جدید (str.format)

این قالب‌بندی در نسخه ۳ پایتون معرفی شده است.

```py
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = 'I am {} {}. I teach {}'.format(first_name, last_name, language)
print(formated_string)
a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))
print('{} - {} = {}'.format(a, b, a - b))
print('{} * {} = {}'.format(a, b, a * b))
print('{} / {} = {:.2f}'.format(a, b, a / b)) # آن را به دو رقم بعد از اعشار محدود می‌کند
print('{} % {} = {}'.format(a, b, a % b))
print('{} // {} = {}'.format(a, b, a // b))
print('{} ** {} = {}'.format(a, b, a ** b))

# خروجی
4 + 3 = 7
4 - 3 = 1
4 * 3 = 12
4 / 3 = 1.33
4 % 3 = 1
4 // 3 = 1
4 ** 3 = 64

# رشته‌ها و اعداد
radius = 10
pi = 3.14
area = pi * radius ** 2
formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area) # ۲ رقم بعد از اعشار
print(formated_string)
```

#### درون‌یابی رشته / f-String ها (پایتون 3.6+)

یکی دیگر از روش‌های جدید قالب‌بندی رشته، درون‌یابی رشته یا f-string است. رشته‌ها با f شروع می‌شوند و ما می‌توانیم داده‌ها را در موقعیت‌های مربوطه تزریق کنیم.

```py
a = 4
b = 3
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')
```

### رشته‌های پایتون به عنوان دنباله‌ای از کاراکترها

رشته‌های پایتون دنباله‌ای از کاراکترها هستند و متدهای اصلی دسترسی خود را با دیگر دنباله‌های مرتب اشیاء در پایتون - لیست‌ها و تاپل‌ها - به اشتراک می‌گذارند. ساده‌ترین راه برای استخراج کاراکترهای تکی از رشته‌ها (و اعضای جداگانه از هر دنباله) این است که آنها را در متغیرهای مربوطه باز کنید.

#### باز کردن کاراکترها

```py
language = 'Python'
a,b,c,d,e,f = language # باز کردن کاراکترهای دنباله در متغیرها
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n
```

#### دسترسی به کاراکترها در رشته‌ها بر اساس اندیس

در برنامه‌نویسی شمارش از صفر شروع می‌شود. بنابراین، حرف اول یک رشته در اندیس صفر قرار دارد و حرف آخر یک رشته در اندیس طول رشته منهای یک است.

```py
language = 'Python'
first_letter = language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter) # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n
```

اگر بخواهیم از سمت راست شروع کنیم می‌توانیم از اندیس‌گذاری منفی استفاده کنیم. ۱- آخرین اندیس است.

```py
language = 'Python'
last_letter = language[-1]
print(last_letter) # n
second_last = language[-2]
print(second_last) # o
```

#### برش زدن رشته‌های پایتون

در پایتون می‌توانیم رشته‌ها را به زیررشته‌ها برش دهیم.

```py
language = 'Python'
first_three = language[0:3] # از اندیس صفر شروع می‌شود و تا ۳ ولی خود ۳ را شامل نمی‌شود
print(first_three) #Pyt
last_three = language[3:6]
print(last_three) # hon
# روش دیگر
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon
```

#### معکوس کردن یک رشته

ما می‌توانیم به راحتی رشته‌ها را در پایتون معکوس کنیم.

```py
greeting = 'Hello, World!'
print(greeting[::-1]) # !dlroW ,olleH
```

#### رد کردن کاراکترها هنگام برش زدن

امکان رد کردن کاراکترها هنگام برش زدن با ارسال آرگومان گام به متد برش وجود دارد.

```py
language = 'Python'
pto = language[0:6:2] #
print(pto) # Pto
```

### متدهای رشته

متدهای رشته زیادی وجود دارند که به ما امکان قالب‌بندی رشته‌ها را می‌دهند. برخی از متدهای رشته را در مثال زیر ببینید:

  - `capitalize()`: کاراکتر اول رشته را به حرف بزرگ تبدیل می‌کند.

<!-- end list -->

```py
challenge = 'thirty days of python'
print(challenge.capitalize()) # 'Thirty days of python'
```

  - `count()`: تعداد وقوع زیررشته را در رشته برمی‌گرداند، `count(substring, start=.., end=..)` . `start` اندیس شروع برای شمارش و `end` آخرین اندیس برای شمارش است.

<!-- end list -->

```py
challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1, 
print(challenge.count('th')) # 2`
```

  - `endswith()`: بررسی می‌کند که آیا یک رشته با پسوند مشخصی خاتمه می‌یابد.

<!-- end list -->

```py
challenge = 'thirty days of python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False
```

  - `expandtabs()`: کاراکتر تب را با فاصله جایگزین می‌کند، اندازه تب پیش‌فرض ۸ است. این متد آرگومان اندازه تب را می‌پذیرد.

<!-- end list -->

```py
challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10)) # 'thirty    days      of        python'
```

  - `find()`: اندیس اولین وقوع یک زیررشته را برمی‌گرداند، در صورت عدم وجود -۱ را برمی‌گرداند.

<!-- end list -->

```py
challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0
```

  - `rfind()`: اندیس آخرین وقوع یک زیررشته را برمی‌گرداند، در صورت عدم وجود -۱ را برمی‌گرداند.

<!-- end list -->

```py
challenge = 'thirty days of python'
print(challenge.rfind('y'))  # 16
print(challenge.rfind('th')) # 17
```

  - `format()`: رشته را به خروجی زیباتری قالب‌بندی می‌کند.
    برای اطلاعات بیشتر در مورد قالب‌بندی رشته این [لینک](https://www.programiz.com/python-programming/methods/string/format) را بررسی کنید.

<!-- end list -->

```py
first_name = 'Asabeneh'
last_name = 'Yetayeh'
age = 250
job = 'teacher'
country = 'Finland'
sentence = 'I am {} {}. I am a {}. I am {} years old. I live in {}.'.format(first_name, last_name, job, age, country)
print(sentence) # I am Asabeneh Yetayeh. I am 250 years old. I am a teacher. I live in Finland.

radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The area of a circle with radius {} is {}'.format(str(radius), str(area))
print(result) # The area of a circle with radius 10 is 314
```

  - `index()`: پایین‌ترین اندیس یک زیررشته را برمی‌گرداند، آرگومان‌های اضافی اندیس شروع و پایان را مشخص می‌کنند (پیش‌فرض ۰ و طول رشته - ۱). اگر زیررشته پیدا نشود، `valueError` ایجاد می‌کند.

<!-- end list -->

```py
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string))  # 7
print(challenge.index(sub_string, 9)) # error
```

  - `rindex()`: بالاترین اندیس یک زیررشته را برمی‌گرداند، آرگومان‌های اضافی اندیس شروع و پایان را مشخص می‌کنند (پیش‌فرض ۰ و طول رشته - ۱).

<!-- end list -->

```py
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.rindex(sub_string))  # 7
print(challenge.rindex(sub_string, 9)) # error
print(challenge.rindex('on', 8)) # 19
```

  - `isalnum()`: کاراکتر حرفی-عددی (alphanumeric) را بررسی می‌کند.

<!-- end list -->

```py
challenge = 'ThirtyDaysPython'
print(challenge.isalnum()) # True

challenge = '30DaysPython'
print(challenge.isalnum()) # True

challenge = 'thirty days of python'
print(challenge.isalnum()) # False, فاصله یک کاراکتر حرفی-عددی نیست

challenge = 'thirty days of python 2019'
print(challenge.isalnum()) # False
```

  - `isalpha()`: بررسی می‌کند که آیا تمام عناصر رشته حروف الفبا هستند (a-z و A-Z).

<!-- end list -->

```py
challenge = 'thirty days of python'
print(challenge.isalpha()) # False, فاصله یک بار دیگر مستثنی شده است
challenge = 'ThirtyDaysPython'
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha())      # False
```

  - `isdecimal()`: بررسی می‌کند که آیا تمام کاراکترهای یک رشته دهدهی (decimal) هستند (۰-۹).

<!-- end list -->

```py
challenge = 'thirty days of python'
print(challenge.isdecimal())  # False
challenge = '123'
print(challenge.isdecimal())  # True
challenge = '\u00B2'
print(challenge.isdigit())   # True
challenge = '12 3'
print(challenge.isdecimal())  # False, فاصله مجاز نیست
```

  - `isdigit()`: بررسی می‌کند که آیا تمام کاراکترهای یک رشته عدد هستند (۰-۹ و برخی دیگر از کاراکترهای یونیکد برای اعداد).

<!-- end list -->

```py
challenge = 'Thirty'
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.isdigit())   # True
challenge = '\u00B2'
print(challenge.isdigit())   # True
```

  - `isnumeric()`: بررسی می‌کند که آیا تمام کاراکترهای یک رشته عددی یا مرتبط با عدد هستند (درست مانند `isdigit()`، فقط نمادهای بیشتری مانند ½ را می‌پذیرد).

<!-- end list -->

```py
num = '10'
print(num.isnumeric()) # True
num = '\u00BD' # ½
print(num.isnumeric()) # True
num = '10.5'
print(num.isnumeric()) # False
```

  - `isidentifier()`: یک شناسه (identifier) معتبر را بررسی می‌کند - بررسی می‌کند که آیا یک رشته نام متغیر معتبری است.

<!-- end list -->

```py
challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, زیرا با عدد شروع می‌شود
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True
```

  - `islower()`: بررسی می‌کند که آیا تمام کاراکترهای الفبایی در رشته حروف کوچک هستند.

<!-- end list -->

```py
challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False
```

  - `isupper()`: بررسی می‌کند که آیا تمام کاراکترهای الفبایی در رشته حروف بزرگ هستند.

<!-- end list -->

```py
challenge = 'thirty days of python'
print(challenge.isupper()) #  False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True
```

  - `join()`: یک رشته الحاق شده را برمی‌گرداند.

<!-- end list -->

```py
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = ' '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'
```

```py
web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '# '.join(web_tech)
print(result) # 'HTML# CSS# JavaScript# React'
```

  - `strip()`: تمام کاراکترهای داده شده را از ابتدا و انتهای رشته حذف می‌کند.

<!-- end list -->

```py
challenge = 'thirty days of pythoonnn'
print(challenge.strip('noth')) # 'irty days of py'
```

  - `replace()`: زیررشته را با یک رشته داده شده جایگزین می‌کند.

<!-- end list -->

```py
challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # 'thirty days of coding'
```

  - `split()`: رشته را با استفاده از رشته داده شده یا فاصله به عنوان جداکننده، تقسیم می‌کند.

<!-- end list -->

```py
challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']
challenge = 'thirty, days, of, python'
print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python']
```

  - `title()`: یک رشته با حالت عنوان (title case) برمی‌گرداند.

<!-- end list -->

```py
challenge = 'thirty days of python'
print(challenge.title()) # Thirty Days Of Python
```

  - `swapcase()`: تمام کاراکترهای بزرگ را به کوچک و تمام کاراکترهای کوچک را به بزرگ تبدیل می‌کند.

<!-- end list -->

```py
challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON
```

  - `startswith()`: بررسی می‌کند که آیا رشته با رشته مشخص شده شروع می‌شود.

<!-- end list -->

```py
challenge = 'thirty days of python'
print(challenge.startswith('thirty')) # True

challenge = '30 days of python'
print(challenge.startswith('thirty')) # False
```

🌕 شما یک فرد فوق‌العاده هستید و پتانسیل قابل توجهی دارید. شما به تازگی چالش‌های روز چهارم را به پایان رسانده‌اید و چهار قدم در راه رسیدن به بزرگی جلوتر هستید. اکنون برای مغز و عضلات خود تمریناتی انجام دهید.

## 💻 تمرینات - روز چهارم

1.  رشته‌های 'Thirty'، 'Days'، 'Of'، 'Python' را به یک رشته واحد، 'Thirty Days Of Python' الحاق کنید.
2.  رشته‌های 'Coding'، 'For'، 'All' را به یک رشته واحد، 'Coding For All' الحاق کنید.
3.  متغیری به نام `company` تعریف کرده و مقدار اولیه "Coding For All" را به آن اختصاص دهید.
4.  متغیر `company` را با استفاده از `_print()` چاپ کنید.
5.  طول رشته `company` را با استفاده از متد `_len()` و `_print()` چاپ کنید.
6.  تمام کاراکترها را با استفاده از متد `_upper()` به حروف بزرگ تبدیل کنید.
7.  تمام کاراکترها را با استفاده از متد `_lower()` به حروف کوچک تبدیل کنید.
8.  از متدهای `capitalize()`، `title()`، `swapcase()` برای قالب‌بندی مقدار رشته `_Coding For All_` استفاده کنید.
9.  کلمه اول رشته `_Coding For All_` را برش دهید (slice کنید).
10. بررسی کنید که آیا رشته `_Coding For All_` حاوی کلمه `Coding` است یا خیر، با استفاده از متد `index`، `find` یا متدهای دیگر.
11. کلمه `coding` را در رشته 'Coding For All' با `Python` جایگزین کنید.
12. عبارت 'Python for Everyone' را با استفاده از متد `replace` یا متدهای دیگر به 'Python for All' تغییر دهید.
13. رشته 'Coding For All' را با استفاده از فاصله به عنوان جداکننده تقسیم کنید (`split()`).
14. رشته "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" را در کاما تقسیم کنید.
15. کاراکتر در اندیس ۰ در رشته `_Coding For All_` چیست؟
16. آخرین اندیس رشته `_Coding For All_` چیست؟
17. کاراکتر در اندیس ۱۰ در رشته "Coding For All" چیست؟
18. یک مخفف یا سرواژه برای نام 'Python For Everyone' ایجاد کنید.
19. یک مخفف یا سرواژه برای نام 'Coding For All' ایجاد کنید.
20. از `index` برای تعیین موقعیت اولین وقوع `C` در `Coding For All` استفاده کنید.
21. از `index` برای تعیین موقعیت اولین وقوع `F` در `Coding For All` استفاده کنید.
22. از `rfind` برای تعیین موقعیت آخرین وقوع `l` در `Coding For All People` استفاده کنید.
23. از `index` یا `find` برای یافتن موقعیت اولین وقوع کلمه 'because' در جمله زیر استفاده کنید: 'You cannot end a sentence with because because because is a conjunction'
24. از `rindex` برای یافتن موقعیت آخرین وقوع کلمه `because` در جمله زیر استفاده کنید: 'You cannot end a sentence with because because because is a conjunction'
25. عبارت 'because because because' را از جمله زیر برش دهید: 'You cannot end a sentence with because because because is a conjunction'
26. موقعیت اولین وقوع کلمه 'because' را در جمله زیر پیدا کنید: 'You cannot end a sentence with because because because is a conjunction'
27. عبارت 'because because because' را از جمله زیر برش دهید: 'You cannot end a sentence with because because because is a conjunction'
28. آیا 'Coding For All' با زیررشته `_Coding_` شروع می‌شود؟
29. آیا 'Coding For All' با زیررشته `_coding_` خاتمه می‌یابد؟
30. در رشته داده شده '   Coding For All      '، فضاهای خالی اضافی سمت چپ و راست را حذف کنید.
31. کدام یک از متغیرهای زیر هنگام استفاده از متد `isidentifier()` مقدار `True` را برمی‌گرداند؟
      - `30DaysOfPython`
      - `thirty_days_of_python`
32. لیست زیر حاوی نام برخی از کتابخانه‌های پایتون است: `['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']`. لیست را با یک رشته هش با فاصله به هم متصل کنید.
33. از سکانس گریز خط جدید برای جدا کردن جملات زیر استفاده کنید.
    ```py
    I am enjoying this challenge.
    I just wonder what is next.
    ```
34. از سکانس گریز تب برای نوشتن خطوط زیر استفاده کنید.
    ```py
    Name      Age     Country   City
    Asabeneh  250     Finland   Helsinki
    ```
35. با استفاده از متد قالب‌بندی رشته، موارد زیر را نمایش دهید:

<!-- end list -->

```sh
radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square.
```

36. موارد زیر را با استفاده از متدهای قالب‌بندی رشته ایجاد کنید:

<!-- end list -->

```sh
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
```

🎉 تبریک می‌گویم\! 🎉

[<< روز سوم](./03_operators.md) | [روز پنجم >>](./05_lists.md)
