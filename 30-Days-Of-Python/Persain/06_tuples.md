<div align="center">
  <h1> ۳۰ روز با پایتون: روز ششم - تاپل‌ها</h1>
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

[<< روز پنجم](./05_lists.md) | [روز هفتم >>](./07_sets.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [روز ششم:](#روز-ششم)
  - [تاپل‌ها](#تاپل‌ها)
    - [ایجاد یک تاپل](#ایجاد-یک-تاپل)
    - [طول تاپل](#طول-تاپل)
    - [دسترسی به آیتم‌های تاپل](#دسترسی-به-آیتم‌های-تاپل)
    - [برش زدن تاپل‌ها](#برش-زدن-تاپل‌ها)
    - [تبدیل تاپل‌ها به لیست‌ها](#تبدیل-تاپل‌ها-به-لیست‌ها)
    - [بررسی یک آیتم در یک تاپل](#بررسی-یک-آیتم-در-یک-تاپل)
    - [پیوستن تاپل‌ها](#پیوستن-تاپل‌ها)
    - [حذف تاپل‌ها](#حذف-تاپل‌ها)
  - [💻 تمرینات: روز ششم](#-تمرینات-روز-ششم)
    - [تمرینات: سطح ۱](#تمرینات-سطح-۱)
    - [تمرینات: سطح ۲](#تمرینات-سطح-۲)

# روز ششم:

## تاپل‌ها

تاپل مجموعه‌ای از انواع داده‌های مختلف است که مرتب و غیرقابل تغییر (immutable) است. تاپل‌ها با پرانتز گرد () نوشته می‌شوند. هنگامی که یک تاپل ایجاد می‌شود، نمی‌توانیم مقادیر آن را تغییر دهیم. ما نمی‌توانیم از متدهای `add`, `insert`, `remove` در یک تاپل استفاده کنیم زیرا قابل تغییر (mutable) نیست. برخلاف لیست، تاپل متدهای کمی دارد. متدهای مربوط به تاپل‌ها:

  - `tuple()`: برای ایجاد یک تاپل خالی
  - `count()`: برای شمارش تعداد یک آیتم مشخص در یک تاپل
  - `index()`: برای یافتن اندیس یک آیتم مشخص در یک تاپل
  - عملگر `+`: برای پیوستن دو یا چند تاپل و ایجاد یک تاپل جدید

### ایجاد یک تاپل

  - تاپل خالی: ایجاد یک تاپل خالی

    ```py
    # سینتکس
    empty_tuple = ()
    # یا با استفاده از سازنده (constructor) تاپل
    empty_tuple = tuple()
    ```

  - تاپل با مقادیر اولیه

    ```py
    # سینتکس
    tpl = ('item1', 'item2','item3')
    ```

    ```py
    fruits = ('banana', 'orange', 'mango', 'lemon')
    ```

### طول تاپل

ما از متد `_len()` برای به دست آوردن طول یک تاپل استفاده می‌کنیم.

```py
# سینتکس
tpl = ('item1', 'item2', 'item3')
len(tpl)
```

### دسترسی به آیتم‌های تاپل

  - اندیس‌گذاری مثبت
    مشابه نوع داده لیست، از اندیس‌گذاری مثبت یا منفی برای دسترسی به آیتم‌های تاپل استفاده می‌کنیم.

    ```py
    # سینتکس
    tpl = ('item1', 'item2', 'item3')
    first_item = tpl[0]
    second_item = tpl[1]
    ```

    ```py
    fruits = ('banana', 'orange', 'mango', 'lemon')
    first_fruit = fruits[0]
    second_fruit = fruits[1]
    last_index =len(fruits) - 1
    last_fruit = fruits[last_index]
    ```

  - اندیس‌گذاری منفی
    اندیس‌گذاری منفی به معنای شروع از انتها است، 1- به آخرین آیتم، 2- به دومین آیتم از آخر اشاره دارد و منفی طول لیست/تاپل به اولین آیتم اشاره دارد.

    ```py
    # سینتکس
    tpl = ('item1', 'item2', 'item3','item4')
    first_item = tpl[-4]
    second_item = tpl[-3]
    ```

    ```py
    fruits = ('banana', 'orange', 'mango', 'lemon')
    first_fruit = fruits[-4]
    second_fruit = fruits[-3]
    last_fruit = fruits[-1]
    ```

### برش زدن تاپل‌ها

ما می‌توانیم با مشخص کردن محدوده‌ای از اندیس‌ها برای شروع و پایان در تاپل، یک زیر-تاپل را برش دهیم، مقدار بازگشتی یک تاپل جدید با آیتم‌های مشخص شده خواهد بود.

  - محدوده اندیس‌های مثبت

    ```py
    # سینتکس
    tpl = ('item1', 'item2', 'item3','item4')
    all_items = tpl[0:4]         # تمام آیتم‌ها
    all_items = tpl[0:]         # تمام آیتم‌ها
    middle_two_items = tpl[1:3]  # شامل آیتم در اندیس ۳ نمی‌شود
    ```

    ```py
    fruits = ('banana', 'orange', 'mango', 'lemon')
    all_fruits = fruits[0:4]    # تمام آیتم‌ها
    all_fruits= fruits[0:]      # تمام آیتم‌ها
    orange_mango = fruits[1:3]  # شامل آیتم در اندیس ۳ نمی‌شود
    orange_to_the_rest = fruits[1:]
    ```

  - محدوده اندیس‌های منفی

    ```py
    # سینتکس
    tpl = ('item1', 'item2', 'item3','item4')
    all_items = tpl[-4:]         # تمام آیتم‌ها
    middle_two_items = tpl[-3:-1]  # شامل آیتم در اندیس ۳ (۱-) نمی‌شود
    ```

    ```py
    fruits = ('banana', 'orange', 'mango', 'lemon')
    all_fruits = fruits[-4:]    # تمام آیتم‌ها
    orange_mango = fruits[-3:-1]  # شامل آیتم در اندیس ۳ نمی‌شود
    orange_to_the_rest = fruits[-3:]
    ```

### تبدیل تاپل‌ها به لیست‌ها

ما می‌توانیم تاپل‌ها را به لیست و لیست‌ها را به تاپل تبدیل کنیم. تاپل غیرقابل تغییر است، اگر بخواهیم یک تاپل را تغییر دهیم باید آن را به لیست تبدیل کنیم.

```py
# سینتکس
tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl)
```

```py
fruits = ('banana', 'orange', 'mango', 'lemon')
fruits = list(fruits)
fruits[0] = 'apple'
print(fruits)     # ['apple', 'orange', 'mango', 'lemon']
fruits = tuple(fruits)
print(fruits)     # ('apple', 'orange', 'mango', 'lemon')
```

### بررسی یک آیتم در یک تاپل

ما می‌توانیم با استفاده از `_in_` بررسی کنیم که آیا یک آیتم در یک تاپل وجود دارد یا خیر، این عملگر یک مقدار بولی برمی‌گرداند.

```py
# سینتکس
tpl = ('item1', 'item2', 'item3','item4')
'item2' in tpl # True
```

```py
fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits) # True
print('apple' in fruits) # False
fruits[0] = 'apple' # TypeError: 'tuple' object does not support item assignment
```

### پیوستن تاپل‌ها

ما می‌توانیم دو یا چند تاپل را با استفاده از عملگر `+` به هم بپیوندیم.

```py
# سینتکس
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2
```

```py
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
fruits_and_vegetables = fruits + vegetables
```

### حذف تاپل‌ها

حذف یک آیتم واحد در یک تاپل ممکن نیست اما می‌توان با استفاده از `_del_` خود تاپل را حذف کرد.

```py
# سینتکس
tpl1 = ('item1', 'item2', 'item3')
del tpl1
```

```py
fruits = ('banana', 'orange', 'mango', 'lemon')
del fruits
```

🌕 شما بسیار شجاع هستید که تا اینجا رسیده‌اید. شما به تازگی چالش‌های روز ششم را به پایان رسانده‌اید و ۶ قدم در راه رسیدن به بزرگی جلوتر هستید. اکنون برای مغز و عضلات خود تمریناتی انجام دهید.

## 💻 تمرینات: روز ششم

### تمرینات: سطح ۱

1.  یک تاپل خالی ایجاد کنید.
2.  یک تاپل حاوی نام خواهران و برادران خود ایجاد کنید (خواهر و برادر خیالی مشکلی ندارد).
3.  تاپل‌های برادران و خواهران را به هم بپیوندید و آن را به `siblings` اختصاص دهید.
4.  شما چند خواهر و برادر دارید؟
5.  تاپل `siblings` را تغییر دهید و نام پدر و مادر خود را به آن اضافه کرده و آن را به `family_members` اختصاص دهید.

### تمرینات: سطح ۲

1.  `siblings` و `parents` را از `family_members` باز کنید (Unpack).
2.  تاپل‌های میوه‌ها، سبزیجات و محصولات حیوانی ایجاد کنید. سه تاپل را به هم بپیوندید و آن را به متغیری به نام `food_stuff_tp` اختصاص دهید.
3.  تاپل `food_stuff_tp` را به یک لیست به نام `food_stuff_lt` تغییر دهید.
4.  آیتم یا آیتم‌های میانی را از تاپل `food_stuff_tp` یا لیست `food_stuff_lt` برش دهید.
5.  سه آیتم اول و سه آیتم آخر را از لیست `food_stuff_lt` برش دهید.
6.  تاپل `food_stuff_tp` را به طور کامل حذف کنید.
7.  بررسی کنید که آیا یک آیتم در تاپل وجود دارد:

<!-- end list -->

  - بررسی کنید که آیا 'Estonia' یک کشور نوردیک است.

  - بررسی کنید که آیا 'Iceland' یک کشور نوردیک است.

    ```py
    nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
    ```

[<< روز پنجم](./05_lists.md) | [روز هفتم >>](./07_sets.md)
