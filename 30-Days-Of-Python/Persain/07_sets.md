<div align="center">
  <h1> ۳۰ روز پایتون: روز 7 - دیکشنری‌ها</h1>
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

[\<\< روز ۶](./06_tuples.md) | [روز ۸ \>\>](./08_dictionaries.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 روز ۷](#-روز-۷)
  - [مجموعه‌ها](#مجموعهها)
    - [ایجاد یک مجموعه](#ایجاد-یک-مجموعه)
    - [گرفتن طول مجموعه](#گرفتن-طول-مجموعه)
    - [دسترسی به آیتم‌ها در یک مجموعه](#دسترسی-به-آیتمها-در-یک-مجموعه)
    - [بررسی یک آیتم](#بررسی-یک-آیتم)
    - [افزودن آیتم به یک مجموعه](#افزودن-آیتم-به-یک-مجموعه)
    - [حذف آیتم‌ها از یک مجموعه](#حذف-آیتمها-از-یک-مجموعه)
    - [پاک کردن آیتم‌ها در یک مجموعه](#پاک-کردن-آیتمها-در-یک-مجموعه)
    - [حذف یک مجموعه](#حذف-یک-مجموعه)
    - [تبدیل لیست به مجموعه](#تبدیل-لیست-به-مجموعه)
    - [ادغام مجموعه‌ها](#ادغام-مجموعهها)
    - [پیدا کردن آیتم‌های اشتراک](#پیدا-کردن-آیتمهای-اشتراک)
    - [بررسی زیرمجموعه و ابرمجموعه](#بررسی-زیرمجموعه-و-ابرمجموعه)
    - [بررسی تفاضل بین دو مجموعه](#بررسی-تفاضل-بین-دو-مجموعه)
    - [یافتن تفاضل متقارن بین دو مجموعه](#یافتن-تفاضل-متقارن-بین-دو-مجموعه)
    - [مجموعه‌های مجزا](#مجموعههای-مجزا)
  - [💻 تمرینات: روز ۷](#-تمرینات-روز-۷)
    - [تمرینات: سطح ۱](#تمرینات-سطح-۱)
    - [تمرینات: سطح ۲](#تمرینات-سطح-۲)
    - [تمرینات: سطح ۳](#تمرینات-سطح-۳)

# 📘 روز ۷

## مجموعه‌ها

مجموعه (Set) یک کالکشن از آیتم‌ها است. اجازه دهید شما را به درس ریاضیات دوران ابتدایی یا دبیرستان برگردانم. تعریف ریاضی مجموعه در پایتون نیز قابل استفاده است. مجموعه، کالکشنی از عناصر متمایز، نامرتب و بدون ایندکس است. در پایتون از مجموعه برای ذخیره آیتم‌های منحصر به فرد استفاده می‌شود و امکان یافتن *اجتماع* (*union*)، *اشتراک* (*intersection*)، *تفاضل* (*difference*)، *تفاضل متقارن* (*symmetric difference*)، *زیرمجموعه* (*subset*)، *ابرمجموعه* (*super set*) و *مجموعه مجزا* (*disjoint set*) در میان مجموعه‌ها وجود دارد.

### ایجاد یک مجموعه

برای ایجاد یک مجموعه خالی، از تابع set() استفاده می‌کنیم. استفاده از آکولاد خالی {} یک دیکشنری ایجاد می‌کند.

  - ایجاد یک مجموعه خالی

<!-- end list -->

```py
# syntax
st = set()
```

  - ایجاد یک مجموعه با آیتم‌های اولیه

<!-- end list -->

```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
```

**مثال:**

```py
# syntax
fruits = {'banana', 'orange', 'mango', 'lemon'}
```

### گرفتن طول مجموعه

ما از متد `**len()**` برای پیدا کردن طول یک مجموعه استفاده می‌کنیم.

```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
len(st)
```

**مثال:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
len(fruits)
```

### دسترسی به آیتم‌ها در یک مجموعه

ما برای دسترسی به آیتم‌ها از حلقه‌ها استفاده می‌کنیم. این موضوع را در بخش حلقه‌ها خواهیم دید.

### بررسی یک آیتم

برای بررسی اینکه آیا یک آیتم در یک لیست وجود دارد یا نه، از عملگر عضویت `_in_` استفاده می‌کنیم.

```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
print("Does set st contain item3? ", 'item3' in st) # Does set st contain item3? True
```

**مثال:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
print('mango' in fruits ) # True
```

### افزودن آیتم به یک مجموعه

هنگامی که یک مجموعه ایجاد شد، نمی‌توانیم هیچ آیتمی را تغییر دهیم اما می‌توانیم آیتم‌های اضافی به آن اضافه کنیم.

  - افزودن یک آیتم با استفاده از `_add()_`

<!-- end list -->

```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')
```

**مثال:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')
```

  - افزودن چندین آیتم با استفاده از `_update()_`
    متد `_update()_` اجازه می‌دهد چندین آیتم به یک مجموعه اضافه کنیم. `_update()_` یک آرگومان از نوع لیست می‌گیرد.

<!-- end list -->

```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5','item6','item7'])
```

**مثال:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)
```

### حذف آیتم‌ها از یک مجموعه

ما می‌توانیم با استفاده از متد `_remove()_` یک آیتم را از مجموعه حذف کنیم. اگر آیتم پیدا نشود، متد `_remove()_` خطا ایجاد می‌کند، بنابراین بهتر است بررسی کنیم که آیا آیتم در مجموعه داده شده وجود دارد یا خیر. با این حال، متد `_discard()_` هیچ خطایی ایجاد نمی‌کند.

```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')
```

متد `pop()` یک آیتم تصادفی را از لیست حذف کرده و آیتم حذف شده را برمی‌گرداند.

**مثال:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()  # یک آیتم تصادفی را از مجموعه حذف می‌کند

```

اگر به آیتم حذف شده علاقه داریم.

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
removed_item = fruits.pop() 
```

### پاک کردن آیتم‌ها در یک مجموعه

اگر بخواهیم مجموعه را پاک یا خالی کنیم از متد `_clear_` استفاده می‌کنیم.

```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.clear()
```

**مثال:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.clear()
print(fruits) # set()
```

### حذف یک مجموعه

اگر بخواهیم خود مجموعه را حذف کنیم از عملگر `_del_` استفاده می‌کنیم.

```py
# syntax
st = {'item1', 'item2', 'item3', 'item4'}
del st
```

**مثال:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
del fruits
```

### تبدیل لیست به مجموعه

ما می‌توانیم لیست را به مجموعه و مجموعه را به لیست تبدیل کنیم. تبدیل لیست به مجموعه موارد تکراری را حذف می‌کند و فقط آیتم‌های منحصر به فرد حفظ می‌شوند.

```py
# syntax
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)  # {'item2', 'item4', 'item1', 'item3'} - ترتیب تصادفی است، زیرا مجموعه‌ها به طور کلی نامرتب هستند
```

**مثال:**

```py
fruits = ['banana', 'orange', 'mango', 'lemon','orange', 'banana']
fruits = set(fruits) # {'mango', 'lemon', 'banana', 'orange'}
```

### ادغام مجموعه‌ها

ما می‌توانیم دو مجموعه را با استفاده از متدهای _union()_ یا _update()_ یا نماد _|_ با هم ادغام کنیم.
z
  - Union (اجتماع)
    این متد یک مجموعه جدید را برمی‌گرداند.

<!-- end list -->

```py
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2) #st3 = st1 | st2
```

**مثال:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables)) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}
# یا با استفاده از این
print(fruits | vegetables)
```

  - Update
    این متد یک مجموعه را در مجموعه داده شده درج می‌کند.

<!-- end list -->

```py
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2) # محتویات st2 به st1 اضافه می‌شود
```

**مثال:**

```py
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
fruits.update(vegetables)
print(fruits) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}
```

### پیدا کردن آیتم‌های اشتراک

اشتراک (Intersection) یک مجموعه شامل آیتم‌هایی که در هر دو مجموعه وجود دارند را برمی‌گرداند یا می‌توان از نماد _&_ استفاده کرد. به مثال زیر توجه کنید

```py
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2) # {'item3', 'item2'}
# یا با استفاده از این: st1 & st2
```

**مثال:**

```py
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.intersection(even_numbers) # {0, 2, 4, 6, 8, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.intersection(dragon)     # {'o', 'n'}
# python & dragon
```

### بررسی زیرمجموعه و ابرمجموعه

یک مجموعه می‌تواند زیرمجموعه یا ابرمجموعه مجموعه‌های دیگر باشد:

  - زیرمجموعه: `_issubset()_`
  - ابرمجموعه: `_issuperset_`

<!-- end list -->

```py
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) # True
st1.issuperset(st2) # True
```

**مثال:**

```py
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.issubset(even_numbers) # False, زیرا یک ابرمجموعه است
whole_numbers.issuperset(even_numbers) # True

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.issubset(dragon)     # False
```

### بررسی تفاضل بین دو مجموعه

این متد تفاضل بین دو مجموعه را برمی‌گرداند یا می‌توان از نماد _-_ برای این کار استفاده کرد.

```py
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1) # set() : st2 - st1
st1.difference(st2) # {'item1', 'item4'} => st1\st2 : st2 - st1
```

**مثال:**

```py
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.difference(even_numbers) # {1, 3, 5, 7, 9}

python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.difference(dragon)     # {'p', 'y', 't'}  - نتیجه نامرتب است (ویژگی مجموعه‌ها)
# python - dragon
dragon.difference(python)     # {'d', 'r', 'a', 'g'}
# dragon - python
```

### یافتن تفاضل متقارن بین دو مجموعه

این متد تفاضل متقارن بین دو مجموعه را برمی‌گرداند. این بدان معناست که مجموعه‌ای را برمی‌گرداند که شامل تمام آیتم‌های هر دو مجموعه است، به جز آیتم‌هایی که در هر دو مجموعه وجود دارند، به زبان ریاضی: (A\\B) ∪ (B\\A)

```py
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# به معنی (A\B)∪(B\A) است
st2.symmetric_difference(st1) # {'item1', 'item4'} : st2 ^ st1
```

**مثال:**

```py
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
some_numbers = {1, 2, 3, 4, 5}
whole_numbers.symmetric_difference(some_numbers) # {0, 6, 7, 8, 9, 10}

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.symmetric_difference(dragon)  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}
# python ^ dragon
```

### مجموعه‌های مجزا

اگر دو مجموعه آیتم یا آیتم‌های مشترکی نداشته باشند، ما آنها را مجموعه‌های مجزا (disjoint sets) می‌نامیم. ما می‌توانیم با استفاده از متد `_isdisjoint()_` بررسی کنیم که آیا دو مجموعه مشترک هستند یا مجزا.

```py
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.isdisjoint(st1) # False
```

**مثال:**

```py
even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers) # True, چون هیچ آیتم مشترکی وجود ندارد

python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.isdisjoint(dragon)  # False, آیتم‌های مشترک وجود دارد {'o', 'n'}
```

🌕 شما یک ستاره در حال طلوع هستید. شما به تازگی چالش‌های روز ۷ را به پایان رسانده‌اید و ۷ قدم در مسیر خود به سوی عظمت جلوتر هستید. اکنون برای مغز و عضلات خود چند تمرین انجام دهید.

## 💻 تمرینات: روز ۷

```py
# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
```

### تمرینات: سطح ۱

۱. طول مجموعه it\_companies را پیدا کنید.
۲. 'Twitter' را به it\_companies اضافه کنید.
۳. چندین شرکت IT را به طور همزمان به مجموعه it\_companies اضافه کنید.
۴. یکی از شرکت‌ها را از مجموعه it\_companies حذف کنید.
۵. تفاوت بین `remove` و `discard` چیست؟

### تمرینات: سطح ۲

۱. A و B را ادغام کنید (Join).
۲. اشتراک A و B را پیدا کنید.
۳. آیا A زیرمجموعه B است؟
۴. آیا A و B مجموعه‌های مجزا هستند؟
۵. A را با B و B را با A ادغام کنید.
۶. تفاضل متقارن بین A و B چیست؟
۷. مجموعه‌ها را به طور کامل حذف کنید.

### تمرینات: سطح ۳

۱. لیست سنین (ages) را به یک مجموعه تبدیل کنید و طول لیست و مجموعه را مقایسه کنید، کدام یک بزرگتر است؟
۲. تفاوت بین انواع داده‌های زیر را توضیح دهید: رشته (string)، لیست (list)، تاپل (tuple) و مجموعه (set).
۳. *I am a teacher and I love to inspire and teach people.* در این جمله چند کلمه منحصر به فرد استفاده شده است؟ از متد `split` و مجموعه برای به دست آوردن کلمات منحصر به فرد استفاده کنید.

🎉 تبریک می‌گویم\! 🎉

[\<\< روز ۶](./06_tuples.md) | [روز ۸ \>\>](./08_dictionaries.md)
