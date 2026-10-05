<div align="center">
  <h1> ۳۰ روز با پایتون: روز ۹ - دستورات شرطی</h1>
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

[<< روز ۸](./08_dictionaries.md) | [روز ۱۰ >>](./10_loops.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 روز ۹](#-روز-۹)
  - [دستورات شرطی](#دستورات-شرطی)
    - [شرط If](#شرط-if)
    - [If Else](#if-else)
    - [If Elif Else](#if-elif-else)
    - [شکل کوتاه](#شکل-کوتاه)
    - [شرط‌های تودرتو](#شرط‌های-تودرتو)
    - [شرط If و عملگرهای منطقی](#شرط-if-و-عملگرهای-منطقی)
    - [عملگرهای منطقی If و Or](#عملگرهای-منطقی-if-و-or)
  - [💻 تمرین‌ها: روز ۹](#-تمرین‌ها-روز-۹)
    - [تمرین‌ها: سطح ۱](#تمرین‌ها-سطح-۱)
    - [تمرین‌ها: سطح ۲](#تمرین‌ها-سطح-۲)
    - [تمرین‌ها: سطح ۳](#تمرین‌ها-سطح-۳)

# 📘 روز ۹

## دستورات شرطی

به‌طور پیش‌فرض، دستورات در اسکریپت پایتون به ترتیب از بالا به پایین اجرا می‌شوند. اگر منطق پردازش ایجاب کند، جریان اجرای ترتیبی می‌تواند به دو روش تغییر کند:

- اجرای شرطی: یک بلوک از یک یا چند دستور در صورت درست (true) بودن یک عبارت خاص اجرا خواهد شد.
- اجرای تکراری: یک بلوک از یک یا چند دستور تا زمانی که یک عبارت خاص درست (true) باشد، به طور مکرر اجرا خواهد شد. در این بخش، ما دستورات _if_، _else_ و _elif_ را پوشش خواهیم داد. عملگرهای مقایسه‌ای و منطقی که در بخش‌های قبل یاد گرفتیم در اینجا مفید خواهند بود.

### شرط If

در پایتون و سایر زبان‌های برنامه‌نویسی، کلمه کلیدی _if_ برای بررسی درست بودن یک شرط و اجرای یک بلوک کد استفاده می‌شود. تورفتگی بعد از دو نقطه را به خاطر بسپارید.

```py
# سینتکس
if condition:
    # این بخش از کد برای شرایط درست اجرا می‌شود
```

**مثال: ۱**

```py
a = 3
if a > 0:
    print('A is a positive number')
# A is a positive number
```

همانطور که در مثال بالا می‌بینید، ۳ بزرگتر از ۰ است. شرط درست بود و بلوک کد اجرا شد. با این حال، اگر شرط نادرست باشد، نتیجه را نمی‌بینیم. برای دیدن نتیجه شرط نادرست، باید بلوک دیگری داشته باشیم که _else_ خواهد بود.

### If Else

اگر شرط درست باشد، بلوک اول اجرا می‌شود، در غیر این صورت شرط else اجرا خواهد شد.

```py
# سینتکس
if condition:
    # این بخش از کد برای شرایط درست اجرا می‌شود
else:
     # این بخش از کد برای شرایط نادرست اجرا می‌شود
```

**مثال:**

```py
a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')
```

شرط بالا نادرست است، بنابراین بلوک else اجرا شد. اگر شرایط ما بیش از دو حالت باشد چه؟ می‌توانیم از _elif_ استفاده کنیم.

### If Elif Else

در زندگی روزمره، ما به صورت روزانه تصمیم‌گیری می‌کنیم. ما با بررسی یک یا دو شرط تصمیم نمی‌گیریم بلکه با چندین شرط. همانند زندگی، برنامه‌نویسی نیز پر از شرط است. ما از _elif_ زمانی استفاده می‌کنیم که چندین شرط داشته باشیم.

```py
# سینتکس
if condition:
    # کد
elif condition:
    # کد
else:
    # کد

```

**مثال:**

```py
a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')
```

### شکل کوتاه

```py
# سینتکس
code if condition else code
```

**مثال:**

```py
a = 3
print('A is positive') if a > 0 else print('A is negative') # شرط اول برقرار شد، 'A is positive' چاپ می‌شود
```

### شرط‌های تودرتو

شرط‌ها می‌توانند تودرتو باشند.

```py
# سینتکس
if condition:
    # کد
    if condition:
    # کد
```

**مثال:**

```py
a = 0
if a > 0:
    if a % 2 == 0:
        print('A is a positive and even integer')
    else:
        print('A is a positive number')
elif a == 0:
    print('A is zero')
else:
    print('A is a negative number')

```

می‌توانیم با استفاده از عملگر منطقی _and_ از نوشتن شرط‌های تودرتو جلوگیری کنیم.

### شرط If و عملگرهای منطقی

```py
# سینتکس
if condition and condition:
    # کد
```

**مثال:**

```py
a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')
```

### عملگرهای منطقی If و Or

```py
# سینتکس
if condition or condition:
    # کد
```

**مثال:**

```py
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')
```

🌕 شما عالی عمل می‌کنید. هرگز تسلیم نشوید زیرا چیزهای بزرگ زمان می‌برند. شما به تازگی چالش‌های روز ۹ را به پایان رسانده‌اید و ۹ قدم در راه رسیدن به بزرگی خود جلوتر هستید. اکنون چند تمرین برای مغز و عضلات خود انجام دهید.

## 💻 تمرین‌ها: روز ۹

### تمرین‌ها: سطح ۱

۱. ورودی کاربر را با استفاده از `input(“Enter your age: ”)‍` دریافت کنید. اگر کاربر ۱۸ سال یا بیشتر سن داشت، به او بازخورد دهید: شما برای رانندگی به اندازه کافی بزرگ شده‌اید. اگر زیر ۱۸ سال بود، به او بازخورد دهید تا تعداد سال‌های باقیمانده را منتظر بماند. خروجی:

    ```sh
    Enter your age: 30
    You are old enough to learn to drive.
    Output:
    Enter your age: 15
    You need 3 more years to learn to drive.
    ```

۲. مقادیر `my_age` و `your_age` را با استفاده از `if...else` مقایسه کنید. چه کسی بزرگتر است (من یا شما)؟ از `input(“Enter your age: ”)‍` برای دریافت سن به عنوان ورودی استفاده کنید. می‌توانید از یک شرط تودرتو برای چاپ "سال" برای اختلاف سنی ۱ سال، "سال‌ها" برای اختلاف‌های بزرگتر، و یک متن سفارشی اگر `my_age = your_age` استفاده کنید. خروجی:

    ```sh
    Enter your age: 30
    You are 5 years older than me.
    ```

۳. دو عدد از کاربر با استفاده از `input` دریافت کنید. اگر a بزرگتر از b بود، `a is greater than b` را برگردانید، اگر a کوچکتر از b بود، `a is smaller than b` را برگردانید، در غیر این صورت `a is equal to b` را برگردانید. خروجی:

```sh
Enter number one: 4
Enter number two: 3
4 is greater than 3
```

### تمرین‌ها: سطح ۲

   ۱. کدی بنویسید که به دانش‌آموزان بر اساس نمراتشان نمره بدهد:

        ```sh
        90-100, A
        80-89, B
        70-79, C
        60-69, D
        0-59, F
        ```

   ۲. ماه را از ورودی کاربر دریافت کنید، سپس بررسی کنید که فصل پاییز، زمستان، بهار یا تابستان است. اگر ورودی کاربر:
    سپتامبر، اکتبر یا نوامبر باشد، فصل پاییز است.
    دسامبر، ژانویه یا فوریه باشد، فصل زمستان است.
    مارس، آوریل یا مه باشد، فصل بهار است.
    ژوئن، ژوئیه یا اوت باشد، فصل تابستان است.
   
   ۳. لیست زیر شامل چند میوه است:

    ```sh
    fruits = ['banana', 'orange', 'mango', 'lemon']
    ```

    اگر میوه‌ای در لیست وجود نداشت، آن را به لیست اضافه کرده و لیست اصلاح شده را چاپ کنید. اگر میوه وجود داشت، چاپ کنید ('That fruit already exist in the list').

### تمرین‌ها: سطح ۳

   ۱. در اینجا یک دیکشنری شخص داریم. با خیال راحت آن را تغییر دهید!

```py
        person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
```

     * بررسی کنید که آیا دیکشنری شخص کلید `skills` را دارد، اگر چنین است مهارت میانی را در لیست `skills` چاپ کنید.
     * بررسی کنید که آیا دیکشنری شخص کلید `skills` را دارد، اگر چنین است بررسی کنید که آیا شخص مهارت 'Python' را دارد و نتیجه را چاپ کنید.
     * اگر مهارت‌های یک شخص فقط شامل `JavaScript` و `React` باشد، چاپ کنید ('He is a front end developer')، اگر مهارت‌های شخص شامل `Node`، `Python`، `MongoDB` باشد، چاپ کنید ('He is a backend developer')، اگر مهارت‌های شخص شامل `React`، `Node` و `MongoDB` باشد، چاپ کنید ('He is a fullstack developer')، در غیر این صورت چاپ کنید ('unknown title') - برای نتایج دقیق‌تر می‌توان شرایط بیشتری را تودرتو کرد!
     * اگر شخص متاهل است و در فنلاند زندگی می‌کند، اطلاعات را در قالب زیر چاپ کنید:

```py
    Asabeneh Yetayeh lives in Finland. He is married.
```

🎉 تبریک! 🎉

[<< روز ۸](./08_dictionaries.md) | [روز ۱۰ >>](./10_loops.md)
