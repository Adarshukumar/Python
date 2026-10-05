<div align="center">
  <h1> ۳۰ روز پایتون: روز ۸ - دیکشنری‌ها</h1>
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

[<< روز ۷ ](./07_sets.md) | [روز ۹ >>](./09_conditionals.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 روز ۸](#-روز-۸)
  - [دیکشنری‌ها](#دیکشنریها)
    - [ایجاد یک دیکشنری](#ایجاد-یک-دیکشنری)
    - [طول دیکشنری](#طول-دیکشنری)
    - [دسترسی به آیتم‌های دیکشنری](#دسترسی-به-آیتمهای-دیکشنری)
    - [افزودن آیتم به دیکشنری](#افزودن-آیتم-به-دیکشنری)
    - [ویرایش آیتم‌ها در دیکشنری](#ویرایش-آیتمها-در-دیکشنری)
    - [بررسی وجود کلید در دیکشنری](#بررسی-وجود-کلید-در-دیکشنری)
    - [حذف زوج‌های کلید و مقدار از دیکشنری](#حذف-زوجهای-کلید-و-مقدار-از-دیکشنری)
    - [تبدیل دیکشنری به فهرستی از آیتم‌ها](#تبدیل-دیکشنری-به-فهرستی-از-آیتمها)
    - [پاک‌سازی دیکشنری](#پاکسازی-دیکشنری)
    - [حذف یک دیکشنری](#حذف-یک-دیکشنری)
    - [کپی گرفتن از دیکشنری](#کپی-گرفتن-از-دیکشنری)
    - [دریافت کلیدهای دیکشنری به صورت فهرست](#دریافت-کلیدهای-دیکشنری-به-صورت-فهرست)
    - [دریافت مقادیر دیکشنری به صورت فهرست](#دریافت-مقادیر-دیکشنری-به-صورت-فهرست)
  - [💻 تمرین‌ها: روز ۸](#-تمرینها-روز-۸)

# 📘 روز ۸

## دیکشنری‌ها

دیکشنری یک نوع دادهٔ مجموعه‌ایِ بدون ترتیب، قابل تغییر (mutable) و زوجی (کلید: مقدار) است.

### ایجاد یک دیکشنری

برای ایجاد دیکشنری از آکولادها {} یا تابع داخلی *dict()* استفاده می‌کنیم.

```py
# سینتکس
empty_dict = {}
# دیکشنری با مقادیر داده
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}


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
```

دیکشنری بالا نشان می‌دهد که مقدار می‌تواند هر نوع داده‌ای باشد: string، boolean، list، tuple، set یا یک دیکشنری.

### طول دیکشنری

تعداد زوج‌های 'کلید: مقدار' را در دیکشنری بررسی می‌کند.

```py
# سینتکس
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(len(dct)) # 4
```

**مثال:**

```py
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_married':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(len(person)) # 7

```

### دسترسی به آیتم‌های دیکشنری

می‌توانیم با ارجاع به نام کلید، به آیتم‌های دیکشنری دسترسی پیدا کنیم.

```py
# سینتکس
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct['key1']) # value1
print(dct['key4']) # value4
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
print(person['first_name']) # Asabeneh
print(person['country'])    # Finland
print(person['skills'])     # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person['skills'][0])  # JavaScript
print(person['address']['street']) # Space street
print(person['city'])       # Error
```

دسترسی به یک آیتم با نام کلید اگر کلید وجود نداشته باشد خطا ایجاد می‌کند. برای اجتناب از این خطا ابتدا باید بررسی کنیم که آیا کلید وجود دارد یا می‌توانیم از متد *get* استفاده کنیم. متد get اگر کلید وجود نداشته باشد مقدار None (نوع دادهٔ NoneType) را برمی‌گرداند.

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
print(person.get('first_name')) # Asabeneh
print(person.get('country'))    # Finland
print(person.get('skills')) #['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person.get('city'))   # None
```

### افزودن آیتم به دیکشنری

می‌توانیم زوج‌های کلید و مقدار جدید به دیکشنری اضافه کنیم

```py
# سینتکس
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key5'] = 'value5'
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
person['job_title'] = 'Instructor'
person['skills'].append('HTML')
print(person)
```

### ویرایش آیتم‌ها در دیکشنری

می‌توانیم آیتم‌ها را در یک دیکشنری ویرایش کنیم

```py
# سینتکس
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key1'] = 'value-one'
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
person['first_name'] = 'Eyob'
person['age'] = 252
```

### بررسی وجود کلید در دیکشنری

برای بررسی وجود یک کلید در دیکشنری از عملگر *in* استفاده می‌کنیم

```py
# سینتکس
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct) # True
print('key5' in dct) # False
```

### حذف زوج‌های کلید و مقدار از دیکشنری

* *pop(key)*: آیتم با نام کلید مشخص‌شده را حذف می‌کند:
* *popitem()*: آخرین آیتم را حذف می‌کند
* *del*: آیتم با نام کلید مشخص‌شده را حذف می‌کند

```py
# سینتکس
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.pop('key1') # removes key1 item
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct.popitem() # removes the last item
del dct['key2'] # removes key2 item
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
person.pop('first_name')        # Removes the firstname item
person.popitem()                # Removes the address item
del person['is_married']        # Removes the is_married item
```

### تبدیل دیکشنری به فهرستی از آیتم‌ها

متد *items()* دیکشنری را به فهرستی از تاپل‌ها تبدیل می‌کند.

```py
# سینتکس
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])
```

### پاک‌سازی دیکشنری

اگر آیتم‌های یک دیکشنری را نمی‌خواهیم، می‌توانیم با متد *clear()* آن‌ها را پاک کنیم

```py
# سینتکس
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.clear()) # None
```

### حذف یک دیکشنری

اگر از دیکشنری استفاده نمی‌کنیم می‌توانیم آن را به طور کامل حذف کنیم

```py
# سینتکس
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct
```

### کپی گرفتن از دیکشنری

می‌توانیم با متد *copy()* از دیکشنری کپی بگیریم. با استفاده از copy می‌توانیم از تغییر (mutation) دیکشنری اصلی جلوگیری کنیم.

```py
# سینتکس
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
```

### دریافت کلیدهای دیکشنری به صورت فهرست

متد *keys()* همهٔ کلیدهای یک دیکشنری را به صورت یک فهرست به ما می‌دهد.

```py
# سینتکس
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
print(keys)     # dict_keys(['key1', 'key2', 'key3', 'key4'])
```

### دریافت مقادیر دیکشنری به صورت فهرست

متد *values* همهٔ مقادیر یک دیکشنری را به صورت یک فهرست به ما می‌دهد.

```py
# سینتکس
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values)     # dict_values(['value1', 'value2', 'value3', 'value4'])
```

🌕 تو شگفت‌انگیزی. حالا با قدرت دیکشنری‌ها شارژ فوق‌العاده‌ای گرفته‌ای. همین حالا چالش‌های روز ۸ را کامل کردی و ۸ قدم به سوی عظمت جلوتر رفتی. حالا کمی تمرین برای مغز و عضلاتت انجام بده.

## 💻 تمرین‌ها: روز ۸

1. یک دیکشنری خالی به نام dog ایجاد کن
2. name، color، breed، legs، age را به دیکشنری dog اضافه کن
3. یک دیکشنری student بساز و first\_name، last\_name، gender، age، marital status، skills، country، city و address را به عنوان کلیدهای آن اضافه کن
4. طول دیکشنری student را بگیر
5. مقدار skills را بگیر و نوع دادهٔ آن را بررسی کن؛ باید list باشد
6. مقادیر skills را با افزودن یک یا دو مهارت تغییر بده
7. کلیدهای دیکشنری را به صورت فهرست بگیر
8. مقادیر دیکشنری را به صورت فهرست بگیر
9. دیکشنری را با استفاده از متد *items()* به یک فهرست از تاپل‌ها تبدیل کن
10. یکی از آیتم‌های دیکشنری را حذف کن
11. یکی از دیکشنری‌ها را حذف کن

🎉 تبریک! 🎉

[<< روز ۷ ](./07_sets.md) | [روز ۹ >>](./09_conditionals.md)

