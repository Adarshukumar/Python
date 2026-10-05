<div align="center">
  <h1> ۳۰ روز با پایتون: روز ۱۰ - حلقه‌ها</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>نویسنده:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small> ویرایش دوم: جولای ۲۰۲۱</small>
</sub>
</div>

[<< روز ۹](./09_conditionals.md) | [روز ۱۱ >>](./11_functions.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 روز ۱۰](#-روز-۱۰)
  - [حلقه‌ها](#حلقه‌ها)
    - [حلقه While](#حلقه-while)
    - [Break و Continue - بخش ۱](#break-و-continue---بخش-۱)
    - [حلقه For](#حلقه-for)
    - [Break و Continue - بخش ۲](#break-و-continue---بخش-۲)
    - [تابع Range](#تابع-range)
    - [حلقه For تودرتو](#حلقه-for-تودرتو)
    - [For Else](#for-else)
    - [Pass](#pass)
  - [💻 تمرین‌ها: روز ۱۰](#-تمرین‌ها-روز-۱۰)
    - [تمرین‌ها: سطح ۱](#تمرین‌ها-سطح-۱)
    - [تمرین‌ها: سطح ۲](#تمرین‌ها-سطح-۲)
    - [تمرین‌ها: سطح ۳](#تمرین‌ها-سطح-۳)

# 📘 روز ۱۰

## حلقه‌ها

زندگی پر از کارهای روزمره است. در برنامه‌نویسی نیز ما کارهای تکراری زیادی انجام می‌دهیم. برای مدیریت کارهای تکراری، زبان‌های برنامه‌نویسی از حلقه‌ها استفاده می‌کنند. زبان برنامه‌نویسی پایتون نیز دو نوع حلقه زیر را ارائه می‌دهد:

۱. حلقه while
۲. حلقه for

### حلقه While

ما از کلمه رزرو شده _while_ برای ساختن حلقه while استفاده می‌کنیم. این حلقه برای اجرای مکرر یک بلوک از دستورات تا زمانی که یک شرط معین برآورده شود، استفاده می‌شود. هنگامی که شرط نادرست (false) می‌شود، خطوط کد بعد از حلقه به اجرا ادامه می‌دهند.

```py
  # سینتکس
while condition:
    # کد اینجا قرار می‌گیرد
```

**مثال:**

```py
count = 0
while count < 5:
    print(count)
    count = count + 1
#اعداد ۰ تا ۴ را چاپ می‌کند
```

در حلقه while بالا، شرط زمانی که count برابر ۵ شود نادرست می‌شود. در آن زمان حلقه متوقف می‌شود.
اگر علاقه‌مند باشیم که بلوک کد را پس از اینکه شرط دیگر درست نبود اجرا کنیم، می‌توانیم از _else_ استفاده کنیم.

```py
  # سینتکس
while condition:
    # کد اینجا قرار می‌گیرد
else:
    # کد اینجا قرار می‌گیرد
```

**مثال:**

```py
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)
```

شرط حلقه بالا زمانی که count برابر ۵ شود نادرست خواهد بود و حلقه متوقف می‌شود، و اجرای دستور else شروع می‌شود. در نتیجه ۵ چاپ خواهد شد.


### Break و Continue - بخش ۱

- Break: ما از break زمانی استفاده می‌کنیم که بخواهیم از حلقه خارج شویم یا آن را متوقف کنیم.

```py
# سینتکس
while condition:
    # کد اینجا قرار می‌گیرد
    if another_condition:
        break
```

**مثال:**

```py
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break
```

حلقه while بالا فقط ۰، ۱، ۲ را چاپ می‌کند، اما وقتی به ۳ می‌رسد متوقف می‌شود.

- Continue: با دستور continue می‌توانیم از تکرار فعلی صرف‌نظر کرده و به تکرار بعدی ادامه دهیم:

```py
  # سینتکس
while condition:
    # کد اینجا قرار می‌گیرد
    if another_condition:
        continue
```

**مثال:**

```py
count = 0
while count < 5:
    if count == 3:
        count += 1 # count + 1
        continue
    print(count)
    count = count + 1
```

حلقه while بالا فقط ۰، ۱، ۲ و ۴ را چاپ می‌کند (۳ را رد می‌کند).

### حلقه For

کلمه کلیدی _for_ برای ایجاد یک حلقه for استفاده می‌شود، مشابه سایر زبان‌های برنامه‌نویسی، اما با تفاوت‌هایی در سینتکس. حلقه برای پیمایش یک دنباله (که می‌تواند یک لیست، یک تاپل، یک دیکشنری، یک مجموعه یا یک رشته باشد) استفاده می‌شود.

- استفاده از حلقه For بر روی لیست

```py
# سینتکس
for iterator in lst:
    # کد اینجا قرار می‌گیرد
```

**مثال:**

```py
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number یک نام موقت برای اشاره به آیتم‌های لیست است، که فقط در داخل این حلقه معتبر است
    print(number)       # اعداد به ترتیب از ۰ تا ۵، هر کدام در یک خط چاپ می‌شوند
```

- استفاده از حلقه For بر روی رشته
```py
# سینتکس
for iterator in string:
    # کد اینجا قرار می‌گیرد
```

**مثال:**

```py
language = 'Python'
for letter in language:
    print(letter)


for i in range(len(language)):
    print(language[i])
```

- استفاده از حلقه For بر روی تاپل
```py
# سینتکس
for iterator in tpl:
    # کد اینجا قرار می‌گیرد
```

**مثال:**

```py
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
```

- استفاده از حلقه For بر روی دیکشنری
  پیمایش یک دیکشنری، کلیدهای آن را به شما می‌دهد.

```py
  # سینتکس
for iterator in dct:
    # کد اینجا قرار می‌گیرد
```

**مثال:**

```py
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # به این ترتیب هم کلیدها و هم مقادیر چاپ می‌شوند
```

- حلقه‌ها در مجموعه

```py
# سینتکس
for iterator in st:
    # کد اینجا قرار می‌گیرد
```

**مثال:**

```py
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)
```

### Break و Continue - بخش ۲

یادآوری کوتاه:
_Break_: ما از break استفاده می‌کنیم زمانی که می‌خواهیم حلقه را قبل از اینکه به طور کامل اجرا شود متوقف کنیم.

```py
# سینتکس
for iterator in sequence:
    # کد اینجا قرار می‌گیرد
    if condition:
        break
```

**مثال:**

```py
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        break
```

در مثال بالا، حلقه زمانی که به ۳ می‌رسد متوقف می‌شود.

Continue: ما از continue استفاده می‌کنیم زمانی که بخواهیم برخی از مراحل تکرار حلقه را رد کنیم.

```py
  # سینتکس
for iterator in sequence:
    # کد اینجا قرار می‌گیرد
    if condition:
        continue
```

**مثال:**

```py
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # برای شرط‌های کوتاه، هر دو عبارت if و else مورد نیاز است
print('outside the loop')
```

در مثال بالا، اگر عدد برابر با ۳ باشد، مرحله *بعد* از شرط (اما داخل حلقه) نادیده گرفته می‌شود و اجرای حلقه در صورت وجود تکرارهای باقیمانده ادامه می‌یابد.

### تابع Range

تابع _range()_ برای ایجاد لیستی از اعداد استفاده می‌شود. _range(start, end, step)_ سه پارامتر می‌گیرد: شروع، پایان و گام. به طور پیش‌فرض از ۰ شروع می‌شود و گام آن ۱ است. دنباله range حداقل به ۱ آرگومان (پایان) نیاز دارد.
ایجاد دنباله‌ها با استفاده از range

```py
lst = list(range(11)) 
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # ۲ آرگومان، شروع و پایان دنباله را مشخص می‌کنند، گام به طور پیش‌فرض ۱ است
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}

# برای پیمایش به عقب از ابتدا تا انتها
lst = list(range(11,0,-2))
print(lst) # [11,9,7,5,3,1]
```

```py
# سینتکس
for iterator in range(start, end, step):
```

**مثال:**

```py
for number in range(11):
    print(number)   # اعداد ۰ تا ۱۰ را چاپ می‌کند، بدون احتساب ۱۱
```

### حلقه For تودرتو

می‌توانیم حلقه‌ها را در داخل یکدیگر بنویسیم.

```py
# سینتکس
for x in y:
    for t in x:
        print(t)
```

**مثال:**

```py
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill)
```

### For Else

اگر بخواهیم پیامی را هنگام پایان حلقه اجرا کنیم، از else استفاده می‌کنیم.

```py
# سینتکس
for iterator in range(start, end, step):
    # کاری انجام بده
else:
    print('حلقه به پایان رسید')
```

**مثال:**

```py
for number in range(11):
    print(number)   # اعداد ۰ تا ۱۰ را چاپ می‌کند، بدون احتساب ۱۱
else:
    print('حلقه در', number, 'متوقف می‌شود')
```

### Pass

در پایتون، زمانی که یک دستور مورد نیاز است (بعد از دو نقطه)، اما نمی‌خواهیم هیچ کدی در آنجا اجرا کنیم، می‌توانیم کلمه _pass_ را برای جلوگیری از خطا بنویسیم. همچنین می‌توانیم از آن به عنوان یک جایگزین برای دستورات آینده استفاده کنیم.

**مثال:**

```py
for number in range(6):
    pass
```

🌕 شما به یک نقطه عطف بزرگ رسیدید، شما غیرقابل توقف هستید. ادامه دهید! شما به تازگی چالش‌های روز ۱۰ را به پایان رسانده‌اید و ۱۰ قدم در راه رسیدن به بزرگی خود جلوتر هستید. اکنون چند تمرین برای مغز و عضلات خود انجام دهید.

## 💻 تمرین‌ها: روز ۱۰

### تمرین‌ها: سطح ۱

۱. با استفاده از حلقه for از ۰ تا ۱۰ پیمایش کنید، همین کار را با حلقه while انجام دهید.
۲. با استفاده از حلقه for از ۱۰ تا ۰ پیمایش کنید، همین کار را با حلقه while انجام دهید.
۳. حلقه‌ای بنویسید که هفت بار print() را فراخوانی کند تا مثلث زیر را در خروجی بدست آوریم:

   ```py
     #
     ##
     ###
     ####
     #####
     ######
     #######
   ```

۴. از حلقه‌های تودرتو برای ایجاد شکل زیر استفاده کنید:

   ```sh
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   # # # # # # # #
   ```

۵. الگوی زیر را چاپ کنید:

   ```sh
   0 x 0 = 0
   1 x 1 = 1
   2 x 2 = 4
   3 x 3 = 9
   4 x 4 = 16
   5 x 5 = 25
   6 x 6 = 36
   7 x 7 = 49
   8 x 8 = 64
   9 x 9 = 81
   10 x 10 = 100
   ```

۶. با استفاده از حلقه for، لیست ['Python', 'Numpy','Pandas','Django', 'Flask'] را پیمایش کرده و آیتم‌ها را چاپ کنید.
۷. از حلقه for برای پیمایش از ۰ تا ۱۰۰ استفاده کنید و فقط اعداد زوج را چاپ کنید.
۸. از حلقه for برای پیمایش از ۰ تا ۱۰۰ استفاده کنید و فقط اعداد فرد را چاپ کنید.
   
### تمرین‌ها: سطح ۲
    
۱.  با استفاده از حلقه for از ۰ تا ۱۰۰ پیمایش کنید و مجموع همه اعداد را چاپ کنید.

```sh
The sum of all numbers is 5050.
```

۱. با استفاده از حلقه for از ۰ تا ۱۰۰ پیمایش کنید و مجموع همه اعداد زوج و مجموع همه اعداد فرد را چاپ کنید.

```sh
The sum of all evens is 2550. And the sum of all odds is 2500.
```

### تمرین‌ها: سطح ۳

۱. به پوشه data بروید و از فایل [countries.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries.py) استفاده کنید. کشورها را پیمایش کرده و همه کشورهایی که شامل کلمه _land_ هستند را استخراج کنید.
۱. این یک لیست میوه است: ['banana', 'orange', 'mango', 'lemon']. ترتیب آن را با استفاده از حلقه معکوس کنید.
۲. به پوشه data بروید و از فایل [countries_data.py](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py) استفاده کنید. 
   ۱. تعداد کل زبان‌ها در داده‌ها چقدر است؟
   ۲. ده زبان پرگویشور از داده‌ها را پیدا کنید.
   ۳. ۱۰ کشور پرجمعیت جهان را پیدا کنید.

🎉 تبریک! 🎉

[<< روز ۹](./09_conditionals.md) | [روز ۱۱ >>](./11_functions.md)
