<div align="center">
  <h1> ۳۰ روز با پایتون: روز پنجم - لیست‌ها</h1>
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

[<< روز چهارم](./04_strings.md) | [روز ششم >>](./06_tuples.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [روز پنجم](#روز-پنجم)
  - [لیست‌ها](#لیست‌ها)
    - [نحوه ایجاد یک لیست](#نحوه-ایجاد-یک-لیست)
    - [دسترسی به آیتم‌های لیست با استفاده از اندیس‌گذاری مثبت](#دسترسی-به-آیتم‌های-لیست-با-استفاده-از-اندیس‌گذاری-مثبت)
    - [دسترسی به آیتم‌های لیست با استفاده از اندیس‌گذاری منفی](#دسترسی-به-آیتم‌های-لیست-با-استفاده-از-اندیس‌گذاری-منفی)
    - [باز کردن آیتم‌های لیست](#باز-کردن-آیتم‌های-لیست)
    - [برش زدن آیتم‌ها از یک لیست](#برش-زدن-آیتم‌ها-از-یک-لیست)
    - [تغییر دادن لیست‌ها](#تغییر-دادن-لیست‌ها)
    - [بررسی آیتم‌ها در یک لیست](#بررسی-آیتم‌ها-در-یک-لیست)
    - [اضافه کردن آیتم‌ها به یک لیست](#اضافه-کردن-آیتم‌ها-به-یک-لیست)
    - [درج کردن آیتم‌ها در یک لیست](#درج-کردن-آیتم‌ها-در-یک-لیست)
    - [حذف آیتم‌ها از یک لیست](#حذف-آیتم‌ها-از-یک-لیست)
    - [حذف آیتم‌ها با استفاده از Pop](#حذف-آیتم‌ها-با-استفاده-از-pop)
    - [حذف آیتم‌ها با استفاده از Del](#حذف-آیتم‌ها-با-استفاده-از-del)
    - [پاک کردن آیتم‌های لیست](#پاک-کردن-آیتم‌های-لیست)
    - [کپی کردن یک لیست](#کپی-کردن-یک-لیست)
    - [پیوستن لیست‌ها](#پیوستن-لیست‌ها)
    - [شمردن آیتم‌ها در یک لیست](#شمردن-آیتم‌ها-در-یک-لیست)
    - [یافتن اندیس یک آیتم](#یافتن-اندیس-یک-آیتم)
    - [معکوس کردن یک لیست](#معکوس-کردن-یک-لیست)
    - [مرتب‌سازی آیتم‌های لیست](#مرتب‌سازی-آیتم‌های-لیست)
  - [💻 تمرینات: روز پنجم](#-تمرینات-روز-پنجم)
    - [تمرینات: سطح ۱](#تمرینات-سطح-۱)
    - [تمرینات: سطح ۲](#تمرینات-سطح-۲)

# روز پنجم

## لیست‌ها

چهار نوع داده مجموعه‌ای (collection) در پایتون وجود دارد:

  - **لیست (List)**: مجموعه‌ای است که مرتب و قابل تغییر (modifiable) است. اعضای تکراری را مجاز می‌داند.
  - **تاپل (Tuple)**: مجموعه‌ای است که مرتب و غیرقابل تغییر یا unmodifiable (immutable) است. اعضای تکراری را مجاز می‌داند.
  - **مجموعه (Set)**: مجموعه‌ای است که نامرتب، بدون اندیس و غیرقابل تغییر است، اما می‌توانیم آیتم‌های جدیدی به مجموعه اضافه کنیم. اعضای تکراری مجاز نیستند.
  - **دیکشنری (Dictionary)**: مجموعه‌ای است که نامرتب، قابل تغییر (modifiable) و اندیس‌گذاری شده است. هیچ عضو تکراری ندارد.

لیست مجموعه‌ای از انواع داده‌های مختلف است که مرتب و قابل تغییر (mutable) است. یک لیست می‌تواند خالی باشد یا ممکن است آیتم‌هایی از انواع داده‌های مختلف داشته باشد.

### نحوه ایجاد یک لیست

در پایتون می‌توانیم لیست‌ها را به دو روش ایجاد کنیم:

  - استفاده از تابع داخلی list

<!-- end list -->

```py
# سینتکس
lst = list()
```

```py
empty_list = list() # این یک لیست خالی است، هیچ آیتمی در لیست وجود ندارد
print(len(empty_list)) # 0
```

  - استفاده از براکت، []

<!-- end list -->

```py
# سینتکس
lst = []
```

```py
empty_list = [] # این یک لیست خالی است، هیچ آیتمی در لیست وجود ندارد
print(len(empty_list)) # 0
```

لیست‌ها با مقادیر اولیه. ما از `_len()` برای پیدا کردن طول یک لیست استفاده می‌کنیم.

```py
fruits = ['banana', 'orange', 'mango', 'lemon']                     # لیستی از میوه‌ها
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']      # لیستی از سبزیجات
animal_products = ['milk', 'meat', 'butter', 'yoghurt']             # لیستی از محصولات حیوانی
web_techs = ['HTML', 'CSS', 'JS', 'React','Redux', 'Node', 'MongDB'] # لیستی از تکنولوژی‌های وب
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']

# چاپ لیست‌ها و طول آنها
print('Fruits:', fruits)
print('Number of fruits:', len(fruits))
print('Vegetables:', vegetables)
print('Number of vegetables:', len(vegetables))
print('Animal products:',animal_products)
print('Number of animal products:', len(animal_products))
print('Web technologies:', web_techs)
print('Number of web technologies:', len(web_techs))
print('Countries:', countries)
print('Number of countries:', len(countries))
```

```sh
خروجی
Fruits: ['banana', 'orange', 'mango', 'lemon']
Number of fruits: 4
Vegetables: ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
Number of vegetables: 5
Animal products: ['milk', 'meat', 'butter', 'yoghurt']
Number of animal products: 4
Web technologies: ['HTML', 'CSS', 'JS', 'React', 'Redux', 'Node', 'MongDB']
Number of web technologies: 7
Countries: ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']
Number of countries: 5
```

  - لیست‌ها می‌توانند آیتم‌هایی از انواع داده‌های مختلف داشته باشند

<!-- end list -->

```py
lst = ['Asabeneh', 250, True, {'country':'Finland', 'city':'Helsinki'}] # لیستی شامل انواع داده‌های مختلف
```

### دسترسی به آیتم‌های لیست با استفاده از اندیس‌گذاری مثبت

ما به هر آیتم در یک لیست با استفاده از اندیس آن دسترسی پیدا می‌کنیم. اندیس یک لیست از 0 شروع می‌شود. تصویر زیر به وضوح نشان می‌دهد که اندیس از کجا شروع می‌شود.

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[0] # ما با استفاده از اندیس به اولین آیتم دسترسی پیدا می‌کنیم
print(first_fruit)      # banana
second_fruit = fruits[1]
print(second_fruit)     # orange
last_fruit = fruits[3]
print(last_fruit) # lemon
# آخرین اندیس
last_index = len(fruits) - 1
last_fruit = fruits[last_index]
```

### دسترسی به آیتم‌های لیست با استفاده از اندیس‌گذاری منفی

اندیس‌گذاری منفی به معنای شروع از انتها است، 1- به آخرین آیتم، 2- به دومین آیتم از آخر اشاره دارد.

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
first_fruit = fruits[-4]
last_fruit = fruits[-1]
second_last = fruits[-2]
print(first_fruit)      # banana
print(last_fruit)       # lemon
print(second_last)      # mango
```

### باز کردن آیتم‌های لیست

```py
lst = ['item1','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4', 'item5']
```

```py
# مثال اول
fruits = ['banana', 'orange', 'mango', 'lemon','lime','apple']
first_fruit, second_fruit, third_fruit, *rest = fruits 
print(first_fruit)     # banana
print(second_fruit)    # orange
print(third_fruit)     # mango
print(rest)           # ['lemon','lime','apple']
# مثال دوم در مورد باز کردن لیست
first, second, third,*rest, tenth = [1,2,3,4,5,6,7,8,9,10]
print(first)          # 1
print(second)         # 2
print(third)          # 3
print(rest)           # [4,5,6,7,8,9]
print(tenth)          # 10
# مثال سوم در مورد باز کردن لیست
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)
```

### برش زدن آیتم‌ها از یک لیست

  - اندیس‌گذاری مثبت: ما می‌توانیم با مشخص کردن شروع، پایان و گام، محدوده‌ای از اندیس‌های مثبت را مشخص کنیم، مقدار بازگشتی یک لیست جدید خواهد بود. (مقادیر پیش‌فرض برای شروع = 0، پایان = `len(lst) - 1` (آخرین آیتم)، گام = 1)

<!-- end list -->

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4] # این تمام میوه‌ها را برمی‌گرداند
# این نیز نتیجه‌ای مشابه بالایی خواهد داد
all_fruits = fruits[0:] # اگر مشخص نکنیم کجا متوقف شود، بقیه را می‌گیرد
orange_and_mango = fruits[1:3] # این شامل اندیس اول نمی‌شود
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[::2] # در اینجا از آرگومان سوم، گام، استفاده کردیم. هر آیتم دومی را می‌گیرد - ['banana', 'mango']
```

  - اندیس‌گذاری منفی: ما می‌توانیم با مشخص کردن شروع، پایان و گام، محدوده‌ای از اندیس‌های منفی را مشخص کنیم، مقدار بازگشتی یک لیست جدید خواهد بود.

<!-- end list -->

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[-4:] # این تمام میوه‌ها را برمی‌گرداند
orange_and_mango = fruits[-3:-1] # این شامل آخرین اندیس نمی‌شود، ['orange', 'mango']
orange_mango_lemon = fruits[-3:] # این از -3 تا انتها را می‌دهد، ['orange', 'mango', 'lemon']
reverse_fruits = fruits[::-1] # یک گام منفی لیست را به ترتیب معکوس می‌گیرد، ['lemon', 'mango', 'orange', 'banana']
```

### تغییر دادن لیست‌ها

لیست یک مجموعه مرتب از آیتم‌ها است که قابل تغییر یا modifiable است. بیایید لیست میوه‌ها را تغییر دهیم.

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
print(fruits)       #  ['avocado', 'orange', 'mango', 'lemon']
fruits[1] = 'apple'
print(fruits)       #  ['avocado', 'apple', 'mango', 'lemon']
last_index = len(fruits) - 1
fruits[last_index] = 'lime'
print(fruits)        #  ['avocado', 'apple', 'mango', 'lime']
```

### بررسی آیتم‌ها در یک لیست

بررسی اینکه آیا یک آیتم عضو یک لیست است با استفاده از عملگر `*in*`. مثال زیر را ببینید.

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
does_exist = 'lime' in fruits
print(does_exist)  # False
```

### اضافه کردن آیتم‌ها به یک لیست

برای اضافه کردن آیتم به انتهای یک لیست موجود از متد `*append()*` استفاده می‌کنیم.

```py
# سینتکس
lst = list()
lst.append(item)
```

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple']
fruits.append('lime')   # ['banana', 'orange', 'mango', 'lemon', 'apple', 'lime']
print(fruits)
```

### درج کردن آیتم‌ها در یک لیست

ما می‌توانیم از متد `*insert()*` برای درج یک آیتم واحد در یک اندیس مشخص در یک لیست استفاده کنیم. توجه داشته باشید که سایر آیتم‌ها به سمت راست منتقل می‌شوند. متد `*insert()*` دو آرگومان می‌گیرد: اندیس و یک آیتم برای درج.

```py
# سینتکس
lst = ['item1', 'item2']
lst.insert(index, item)
```

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # درج سیب بین پرتقال و انبه
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')   # ['banana', 'orange', 'apple', 'lime', 'mango', 'lemon']
print(fruits)
```

### حذف آیتم‌ها از یک لیست

متد `remove` یک آیتم مشخص را از یک لیست حذف می‌کند.

```py
# سینتکس
lst = ['item1', 'item2']
lst.remove(item)
```

```py
fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon', 'banana'] - این متد اولین وقوع آیتم را در لیست حذف می‌کند
fruits.remove('lemon')
print(fruits)  # ['orange', 'mango', 'banana']
```

### حذف آیتم‌ها با استفاده از Pop

متد `*pop()*` اندیس مشخص شده را حذف می‌کند، (یا آخرین آیتم اگر اندیس مشخص نشده باشد):

```py
# سینتکس
lst = ['item1', 'item2']
lst.pop()       # آخرین آیتم
lst.pop(index)
```

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)       # ['banana', 'orange', 'mango']

fruits.pop(0)
print(fruits)       # ['orange', 'mango']
```

### حذف آیتم‌ها با استفاده از Del

کلمه کلیدی `*del*` اندیس مشخص شده را حذف می‌کند و همچنین می‌تواند برای حذف آیتم‌ها در محدوده اندیس استفاده شود. همچنین می‌تواند لیست را به طور کامل حذف کند.

```py
# سینتکس
lst = ['item1', 'item2']
del lst[index] # فقط یک آیتم
del lst        # برای حذف کامل لیست
```

```py
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits)       # ['orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[1]
print(fruits)       # ['orange', 'lemon', 'kiwi', 'lime']
del fruits[1:3]     # این آیتم‌ها را بین اندیس‌های داده شده حذف می‌کند، بنابراین آیتم با اندیس 3 را حذف نمی‌کند!
print(fruits)       # ['orange', 'lime']
del fruits
print(fruits)       # این باید بدهد: NameError: name 'fruits' is not defined
```

### پاک کردن آیتم‌های لیست

متد `*clear()*` لیست را خالی می‌کند:

```py
# سینتکس
lst = ['item1', 'item2']
lst.clear()
```

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)       # []
```

### کپی کردن یک لیست

امکان کپی کردن یک لیست با تخصیص مجدد آن به یک متغیر جدید به روش زیر وجود دارد: `list2 = list1`. اکنون، `list2` یک مرجع از `list1` است، هر تغییری که در `list2` ایجاد کنیم، `list1` اصلی را نیز تغییر می‌دهد. اما موارد زیادی وجود دارد که ما دوست نداریم نسخه اصلی را تغییر دهیم بلکه دوست داریم یک کپی متفاوت داشته باشیم. یکی از راه‌های جلوگیری از مشکل بالا استفاده از `_copy()` است.

```py
# سینتکس
lst = ['item1', 'item2']
lst_copy = lst.copy()
```

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)       # ['banana', 'orange', 'mango', 'lemon']
```

### پیوستن لیست‌ها

چندین راه برای پیوستن، یا الحاق، دو یا چند لیست در پایتون وجود دارد.

  - عملگر پلاس (+)

<!-- end list -->

```py
# سینتکس
list3 = list1 + list2
```

```py
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers) # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables ) # ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
```

  - پیوستن با استفاده از متد `extend()`
    متد `*extend()*` اجازه می‌دهد تا لیستی را به لیستی دیگر اضافه کنید. مثال زیر را ببینید.

<!-- end list -->

```py
# سینتکس
list1 = ['item1', 'item2']
list2 = ['item3', 'item4', 'item5']
list1.extend(list2) # ['item1', 'item2', 'item3', 'item4', 'item5']
```

```py
num1 = [0, 1, 2, 3]
num2= [4, 5, 6]
num1.extend(num2)
print('Numbers:', num1) # Numbers: [0, 1, 2, 3, 4, 5, 6]
negative_numbers = [-5,-4,-3,-2,-1]
positive_numbers = [1, 2, 3,4,5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print('Integers:', negative_numbers) # Integers: [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits.extend(vegetables)
print('Fruits and vegetables:', fruits ) # Fruits and vegetables: ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
```

### شمردن آیتم‌ها در یک لیست

متد `*count()*` تعداد دفعاتی که یک آیتم در یک لیست ظاهر می‌شود را برمی‌گرداند:

```py
# سینتکس
lst = ['item1', 'item2']
lst.count(item)
```

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.count(24))           # 3
```

### یافتن اندیس یک آیتم

متد `*index()*` اندیس یک آیتم را در لیست برمی‌گرداند:

```py
# سینتکس
lst = ['item1', 'item2']
lst.index(item)
```

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   # 1
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))           # 2, اولین وقوع
```

### معکوس کردن یک لیست

متد `*reverse()*` ترتیب یک لیست را معکوس می‌کند.

```py
# سینتکس
lst = ['item1', 'item2']
lst.reverse()
```

```py
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits) # ['lemon', 'mango', 'orange', 'banana']
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print(ages) # [24, 25, 24, 26, 25, 24, 19, 22]
```

### مرتب‌سازی آیتم‌های لیست

برای مرتب‌سازی لیست‌ها می‌توانیم از متد `_sort()` یا توابع داخلی `_sorted()` استفاده کنیم. متد `_sort()` آیتم‌های لیست را به ترتیب صعودی مرتب می‌کند و لیست اصلی را تغییر می‌دهد. اگر آرگومان `reverse` متد `_sort()` برابر با `true` باشد، لیست را به ترتیب نزولی مرتب می‌کند.

  - `sort()`: این متد لیست اصلی را تغییر می‌دهد.

    ```py
    # سینتکس
    lst = ['item1', 'item2']
    lst.sort()                # صعودی
    lst.sort(reverse=True)    # نزولی
    ```

    **مثال:**

    ```py
    fruits = ['banana', 'orange', 'mango', 'lemon']
    fruits.sort()
    print(fruits)             # مرتب شده بر اساس حروف الفبا، ['banana', 'lemon', 'mango', 'orange']
    fruits.sort(reverse=True)
    print(fruits) # ['orange', 'mango', 'lemon', 'banana']
    ages = [22, 19, 24, 25, 26, 24, 25, 24]
    ages.sort()
    print(ages) #  [19, 22, 24, 24, 24, 25, 25, 26]

    ages.sort(reverse=True)
    print(ages) #  [26, 25, 25, 24, 24, 24, 22, 19]
    ```

    `sorted()`: لیست مرتب شده را بدون تغییر لیست اصلی برمی‌گرداند.
    **مثال:**

    ```py
    fruits = ['banana', 'orange', 'mango', 'lemon']
    print(sorted(fruits))   # ['banana', 'lemon', 'mango', 'orange']
    # ترتیب معکوس
    fruits = ['banana', 'orange', 'mango', 'lemon']
    fruits = sorted(fruits,reverse=True)
    print(fruits)     # ['orange', 'mango', 'lemon', 'banana']
    ```

🌕 شما سخت‌کوش هستید و تاکنون به دستاوردهای زیادی رسیده‌اید. شما به تازگی چالش‌های روز پنجم را به پایان رسانده‌اید و ۵ قدم در راه رسیدن به بزرگی جلوتر هستید. اکنون برای مغز و عضلات خود تمریناتی انجام دهید.

## 💻 تمرینات: روز پنجم

### تمرینات: سطح ۱

1.  یک لیست خالی تعریف کنید.

2.  یک لیست با بیش از ۵ آیتم تعریف کنید.

3.  طول لیست خود را پیدا کنید.

4.  آیتم اول، آیتم میانی و آیتم آخر لیست را بدست آورید.

5.  لیستی به نام `mixed_data_types` تعریف کنید، (نام، سن، قد، وضعیت تاهل، آدرس) خود را در آن قرار دهید.

6.  یک متغیر لیستی به نام `it_companies` تعریف کرده و مقادیر اولیه Facebook، Google، Microsoft، Apple، IBM، Oracle و Amazon را به آن اختصاص دهید.

7.  لیست را با استفاده از `_print()` چاپ کنید.

8.  تعداد شرکت‌ها را در لیست چاپ کنید.

9.  شرکت اول، میانی و آخر را چاپ کنید.

10. لیست را پس از تغییر یکی از شرکت‌ها چاپ کنید.

11. یک شرکت IT به `it_companies` اضافه کنید.

12. یک شرکت IT را در وسط لیست شرکت‌ها درج کنید.

13. نام یکی از `it_companies` را به حروف بزرگ تغییر دهید (به جز IBM\!).

14. `it_companies` را با یک رشته `'#;&nbsp; '` به هم بپیوندید.

15. بررسی کنید که آیا شرکت خاصی در لیست `it_companies` وجود دارد یا خیر.

16. لیست را با استفاده از متد `sort()` مرتب کنید.

17. لیست را با استفاده از متد `reverse()` به ترتیب نزولی معکوس کنید.

18. ۳ شرکت اول را از لیست برش دهید.

19. ۳ شرکت آخر را از لیست برش دهید.

20. شرکت یا شرکت‌های IT میانی را از لیست برش دهید.

21. اولین شرکت IT را از لیست حذف کنید.

22. شرکت یا شرکت‌های IT میانی را از لیست حذف کنید.

23. آخرین شرکت IT را از لیست حذف کنید.

24. تمام شرکت‌های IT را از لیست حذف کنید.

25. لیست شرکت‌های IT را از بین ببرید.

26. لیست‌های زیر را به هم بپیوندید:

    ```py
    front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
    back_end = ['Node','Express', 'MongoDB']
    ```

27. پس از پیوستن لیست‌ها در سوال ۲۶، لیست پیوسته را کپی کرده و به متغیری به نام `full_stack` اختصاص دهید، سپس `Python` و `SQL` را بعد از `Redux` درج کنید.

### تمرینات: سطح ۲

1.  لیست زیر شامل سن ۱۰ دانشجو است:

<!-- end list -->

```sh
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
```

  - لیست را مرتب کرده و حداقل و حداکثر سن را پیدا کنید.
  - حداقل سن و حداکثر سن را دوباره به لیست اضافه کنید.
  - میانه سن را پیدا کنید (یک آیتم میانی یا دو آیتم میانی تقسیم بر دو).
  - میانگین سن را پیدا کنید (مجموع تمام آیتم‌ها تقسیم بر تعداد آنها).
  - دامنه سن‌ها را پیدا کنید (حداکثر منهای حداقل).
  - مقدار (`min` - `average`) و (`max` - `average`) را مقایسه کنید، از متد `_abs()` استفاده کنید.

<!-- end list -->

2.  کشور(های) میانی را در [لیست کشورها](https://github.com/Asabeneh/30-Days-Of-Python/tree/master/data/countries.py) پیدا کنید.
3.  لیست کشورها را به دو لیست مساوی تقسیم کنید اگر زوج است، در غیر این صورت یک کشور بیشتر برای نیمه اول.
4.  `['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']`. سه کشور اول را باز کنید و بقیه را به عنوان کشورهای اسکاندیناوی در نظر بگیرید.

🎉 تبریک می‌گویم\! 🎉

[<< روز چهارم](./04_strings.md) | [روز ششم >>](./06_tuples.md)
