<div align="center">
  <h1> ۳۰ روز با پایتون: روز ۱۹ - کار با فایل‌ها </h1>
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

[<< روز ۲۰](./20_python_package_manager.md) | [روز ۱۸ >>](./18_regular_expressions.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 روز ۱۹](#-روز-۱۹)
  - [کار با فایل‌ها](#کار-با-فایلها)
    - [باز کردن فایل‌ها برای خواندن](#باز-کردن-فایلها-برای-خواندن)
    - [باز کردن فایل‌ها برای نوشتن و به‌روزرسانی](#باز-کردن-فایلها-برای-نوشتن-و-بهروزرسانی)
    - [حذف فایل‌ها](#حذف-فایلها)
  - [انواع فایل](#انواع-فایل)
    - [فایل با پسوند txt](#فایل-با-پسوند-txt)
    - [فایل با پسوند json](#فایل-با-پسوند-json)
    - [تبدیل JSON به دیکشنری](#تبدیل-json-به-دیکشنری)
    - [تبدیل دیکشنری به JSON](#تبدیل-دیکشنری-به-json)
    - [ذخیره به عنوان فایل JSON](#ذخیره-به-عنوان-فایل-json)
    - [فایل با پسوند csv](#فایل-با-پسوند-csv)
    - [فایل با پسوند xlsx](#فایل-با-پسوند-xlsx)
    - [فایل با پسوند xml](#فایل-با-پسوند-xml)
  - [💻 تمرین‌ها: روز ۱۹](#-تمرینها-روز-۱۹)
    - [تمرین‌ها: سطح ۱](#تمرینها-سطح-۱)
    - [تمرین‌ها: سطح ۲](#تمرینها-سطح-۲)
    - [تمرین‌ها: سطح ۳](#تمرینها-سطح-۳)

# 📘 روز ۱۹

## کار با فایل‌ها

تاکنون انواع مختلف داده در پایتون را دیده‌ایم. ما معمولاً داده‌های خود را در فرمت‌های فایل مختلف ذخیره می‌کنیم. علاوه بر کار با فایل‌ها، در این بخش با فرمت‌های مختلف فایل (.txt, .json, .xml, .csv, .tsv, .excel) نیز آشنا خواهیم شد. ابتدا، بیایید با کار با فایل‌ها با فرمت رایج (.txt) آشنا شویم.

کار با فایل‌ها بخش مهمی از برنامه‌نویسی است که به ما امکان ایجاد، خواندن، به‌روزرسانی و حذف فایل‌ها را می‌دهد. در پایتون برای کار با داده‌ها از تابع داخلی _open()_ استفاده می‌کنیم.

```py
# سینتکس
open('filename', mode) # mode (r, a, w, x, t, b) می‌تواند برای خواندن، نوشتن، به‌روزرسانی باشد
```

- "r" - خواندن (Read) - مقدار پیش‌فرض. فایلی را برای خواندن باز می‌کند، اگر فایل وجود نداشته باشد خطا برمی‌گرداند.
- "a" - الصاق (Append) - فایلی را برای الصاق باز می‌کند، اگر فایل وجود نداشته باشد آن را ایجاد می‌کند.
- "w" - نوشتن (Write) - فایلی را برای نوشتن باز می‌کند، اگر فایل وجود نداشته باشد آن را ایجاد می‌کند.
- "x" - ایجاد (Create) - فایل مشخص شده را ایجاد می‌کند، اگر فایل وجود داشته باشد خطا برمی‌گرداند.
- "t" - متنی (Text) - مقدار پیش‌فرض. حالت متنی.
- "b" - باینری (Binary) - حالت باینری (مثلاً برای تصاویر).

### باز کردن فایل‌ها برای خواندن

حالت پیش‌فرض _open_ خواندن است، بنابراین لازم نیست 'r' یا 'rt' را مشخص کنیم. من فایلی به نام reading_file_example.txt را در پوشه files ایجاد و ذخیره کرده‌ام. بیایید ببینیم چگونه انجام می‌شود:

```py
f = open('./files/reading_file_example.txt')
print(f) # <_io.TextIOWrapper name='./files/reading_file_example.txt' mode='r' encoding='UTF-8'>
```

همانطور که در مثال بالا می‌بینید، من فایل باز شده را چاپ کردم و اطلاعاتی در مورد آن به من داد. فایل باز شده متدهای مختلف خواندن دارد: _read()_، _readline_، _readlines_. یک فایل باز شده باید با متد _close()_ بسته شود.

- _read()_: کل متن را به صورت رشته می‌خواند. اگر بخواهیم تعداد کاراکترهایی را که می‌خواهیم بخوانیم محدود کنیم، می‌توانیم با ارسال یک مقدار int به متد *read(number)* آن را محدود کنیم.

```py
f = open('./files/reading_file_example.txt')
txt = f.read()
print(type(txt))
print(txt)
f.close()
```

```sh
# خروجی
<class 'str'>
This is an example to show how to open a file and read.
This is the second line of the text.
```

به جای چاپ کل متن، بیایید ۱۰ کاراکتر اول فایل متنی را چاپ کنیم.

```py
f = open('./files/reading_file_example.txt')
txt = f.read(10)
print(type(txt))
print(txt)
f.close()
```

```sh
# خروجی
<class 'str'>
This is an
```

- _readline()_: فقط خط اول را می‌خواند.

```py
f = open('./files/reading_file_example.txt')
line = f.readline()
print(type(line))
print(line)
f.close()
```

```sh
# خروجی
<class 'str'>
This is an example to show how to open a file and read.
```

- _readlines()_: تمام متن را خط به خط می‌خواند و لیستی از خطوط را برمی‌گرداند.

```py
f = open('./files/reading_file_example.txt')
lines = f.readlines()
print(type(lines))
print(lines)
f.close()
```

```sh
# خروجی
<class 'list'>
['This is an example to show how to open a file and read.\n', 'This is the second line of the text.']
```

روش دیگر برای گرفتن تمام خطوط به صورت لیست، استفاده از _splitlines()_ است:

```py
f = open('./files/reading_file_example.txt')
lines = f.read().splitlines()
print(type(lines))
print(lines)
f.close()
```

```sh
# خروجی
<class 'list'>
['This is an example to show how to open a file and read.', 'This is the second line of the text.']
```

بعد از باز کردن یک فایل، باید آن را ببندیم. احتمال فراموش کردن بستن آن‌ها زیاد است. روش جدیدی برای باز کردن فایل‌ها با استفاده از _with_ وجود دارد - که فایل‌ها را به طور خودکار می‌بندد. بیایید مثال قبلی را با روش _with_ بازنویسی کنیم:

```py
with open('./files/reading_file_example.txt') as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)
```

```sh
# خروجی
<class 'list'>
['This is an example to show how to open a file and read.', 'This is the second line of the text.']
```

### باز کردن فایل‌ها برای نوشتن و به‌روزرسانی

برای نوشتن در یک فایل موجود، باید یک حالت به عنوان پارامتر به تابع _open()_ اضافه کنیم:

- "a" - الصاق (append) - به انتهای فایل اضافه می‌کند، اگر فایل وجود نداشته باشد یک فایل جدید ایجاد می‌کند.
- "w" - نوشتن (write) - هر محتوای موجود را بازنویسی می‌کند، اگر فایل وجود نداشته باشد آن را ایجاد می‌کند.

بیایید متنی را به فایلی که در حال خواندن آن بودیم اضافه کنیم:

```py
with open('./files/reading_file_example.txt','a') as f:
    f.write('This text has to be appended at the end')
```

متد زیر یک فایل جدید ایجاد می‌کند، اگر فایل وجود نداشته باشد:

```py
with open('./files/writing_file_example.txt','w') as f:
    f.write('This text will be written in a newly created file')
```

### حذف فایل‌ها

در بخش قبلی دیدیم که چگونه با استفاده از ماژول _os_ یک پوشه را ایجاد و حذف کنیم. حالا دوباره، اگر بخواهیم فایلی را حذف کنیم از ماژول _os_ استفاده می‌کنیم.

```py
import os
os.remove('./files/example.txt')

```

اگر فایل وجود نداشته باشد، متد remove خطا ایجاد می‌کند، بنابراین خوب است که از شرطی مانند این استفاده کنیم:

```py
import os
if os.path.exists('./files/example.txt'):
    os.remove('./files/example.txt')
else:
    print('The file does not exist')
```

## انواع فایل

### فایل با پسوند txt

فایل با پسوند _txt_ یک فرمت بسیار رایج از داده است و ما آن را در بخش قبلی پوشش دادیم. بیایید به فایل JSON برویم.

### فایل با پسوند json

JSON مخفف JavaScript Object Notation است. در واقع، این یک شیء جاوا اسکریپت یا دیکشنری پایتون است که به رشته تبدیل شده است.

_مثال:_

```py
# دیکشنری
person_dct= {
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}
# JSON: یک رشته از یک دیکشنری
person_json = "{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}"

# ما از سه نقل قول استفاده می‌کنیم و آن را چند خطی می‌کنیم تا خواناتر شود
person_json = '''{
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}'''
```

### تبدیل JSON به دیکشنری

برای تبدیل JSON به دیکشنری، ابتدا ماژول json را وارد می‌کنیم و سپس از متد _loads_ استفاده می‌کنیم.

```py
import json
# JSON
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''
# بیایید JSON را به دیکشنری تبدیل کنیم
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])
```

```sh
# خروجی
<class 'dict'>
{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}
Asabeneh
```

### تبدیل دیکشنری به JSON

برای تبدیل دیکشنری به JSON از متد _dumps_ از ماژول json استفاده می‌کنیم.

```py
import json
# دیکشنری پایتون
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
# بیایید آن را به json تبدیل کنیم
person_json = json.dumps(person, indent=4) # indent می‌تواند ۲، ۴، ۸ باشد. این json را زیباتر می‌کند
print(type(person_json))
print(person_json)
```

```sh
# خروجی
# وقتی آن را چاپ می‌کنید، نقل قول ندارد، اما در واقع یک رشته است
# JSON نوع ندارد، یک نوع رشته است.
<class 'str'>
{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": [
        "JavaScrip",
        "React",
        "Python"
    ]
}
```

### ذخیره به عنوان فایل JSON

ما همچنین می‌توانیم داده‌های خود را به عنوان یک فایل json ذخیره کنیم. بیایید آن را با استفاده از مراحل زیر به عنوان یک فایل json ذخیره کنیم. برای نوشتن یک فایل json، از متد json.dump() استفاده می‌کنیم، که می‌تواند دیکشنری، فایل خروجی، ensure_ascii و indent را بگیرد.

```py
import json
# دیکشنری پایتون
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
with open('./files/json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)
```

در کد بالا، از encoding و indentation استفاده کردیم. Indentation خواندن فایل json را آسان می‌کند.

### فایل با پسوند csv

CSV مخفف Comma Separated Values (مقادیر جدا شده با کاما) است. CSV یک فرمت فایل ساده است که برای ذخیره داده‌های جدولی مانند یک صفحه گسترده یا پایگاه داده استفاده می‌شود. CSV یک فرمت داده بسیار رایج در علم داده است.

**مثال:**

```csv
"name","country","city","skills"
"Asabeneh","Finland","Helsinki","JavaScript"
```

**مثال:**

```py
import csv
with open('./files/csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # از متد reader برای خواندن csv استفاده می‌کنیم
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'نام ستون‌ها: {", ".join(row)}')
            line_count += 1
        else:
            print(
                f'\t{row} یک معلم است. او در {row}، {row} زندگی می‌کند.')
            line_count += 1
    print(f'تعداد خطوط: {line_count}')
```

```sh
# خروجی:
نام ستون‌ها: name, country, city, skills
تعداد خطوط: 1
        Asabeneh یک معلم است. او در Finland، Helsinki زندگی می‌کند.
تعداد خطوط: 2
```

### فایل با پسوند xlsx

برای خواندن فایل‌های اکسل باید بسته _xlrd_ را نصب کنیم. این موضوع را بعد از پوشش نصب بسته با استفاده از pip پوشش خواهیم داد.

```py
import xlrd
excel_book = xlrd.open_workbook('sample.xls')
print(excel_book.nsheets)
print(excel_book.sheet_names)
```

### فایل با پسوند xml

XML یک فرمت داده ساختاریافته دیگر است که شبیه HTML است. در XML تگ‌ها از پیش تعریف نشده‌اند. خط اول یک اعلان XML است. تگ person ریشه XML است. person یک ویژگی gender دارد.
**مثال: XML**

```xml
<?xml version="1.0"?>
<person gender="female">
  <name>Asabeneh</name>
  <country>Finland</country>
  <city>Helsinki</city>
  <skills>
    <skill>JavaScrip</skill>
    <skill>React</skill>
    <skill>Python</skill>
  </skills>
</person>
```

برای اطلاعات بیشتر در مورد نحوه خواندن یک فایل XML [مستندات](https://docs.python.org/2/library/xml.etree.elementtree.html) را بررسی کنید.

```py
import xml.etree.ElementTree as ET
tree = ET.parse('./files/xml_example.xml')
root = tree.getroot()
print('تگ ریشه:', root.tag)
print('ویژگی:', root.attrib)
for child in root:
    print('فیلد: ', child.tag)
```

```sh
# خروجی
تگ ریشه: person
ویژگی: {'gender': 'male'}
فیلد: name
فیلد: country
فیلد: city
فیلد: skills
```

🌕 شما در حال پیشرفت بزرگی هستید. شتاب خود را حفظ کنید، کار خوب را ادامه دهید. اکنون چند تمرین برای مغز و عضلات خود انجام دهید.

## 💻 تمرین‌ها: روز ۱۹

### تمرین‌ها: سطح ۱

1. تابعی بنویسید که تعداد خطوط و تعداد کلمات یک متن را بشمارد. همه فایل‌ها در پوشه data قرار دارند:
   الف) فایل obama_speech.txt را بخوانید و تعداد خطوط و کلمات را بشمارید.
   ب) فایل michelle_obama_speech.txt را بخوانید و تعداد خطوط و کلمات را بشمارید.
   ج) فایل donald_speech.txt را بخوانید و تعداد خطوط و کلمات را بشمارید.
   د) فایل melina_trump_speech.txt را بخوانید و تعداد خطوط و کلمات را بشمارید.
2. فایل داده countries_data.json را در پوشه data بخوانید، تابعی ایجاد کنید که ده زبان پرگویشور را پیدا کند.

   ```py
   # خروجی شما باید به این شکل باشد
   print(most_spoken_languages(filename='./data/countries_data.json', 10))
   [(91, 'English'),
   (45, 'French'),
   (25, 'Arabic'),
   (24, 'Spanish'),
   (9, 'Russian'),
   (9, 'Portuguese'),
   (8, 'Dutch'),
   (7, 'German'),
   (5, 'Chinese'),
   (4, 'Swahili'),
   (4, 'Serbian')]

   # خروجی شما باید به این شکل باشد
   print(most_spoken_languages(filename='./data/countries_data.json', 3))
   [(91, 'English'),
   (45, 'French'),
   (25, 'Arabic')]
   ```

3. فایل داده countries_data.json را در پوشه data بخوانید، تابعی ایجاد کنید که لیستی از ده کشور پرجمعیت را ایجاد کند.

   ```py
   # خروجی شما باید به این شکل باشد
   print(most_populated_countries(filename='./data/countries_data.json', 10))

   [
   {'country': 'China', 'population': 1377422166},
   {'country': 'India', 'population': 1295210000},
   {'country': 'United States of America', 'population': 323947000},
   {'country': 'Indonesia', 'population': 258705000},
   {'country': 'Brazil', 'population': 206135893},
   {'country': 'Pakistan', 'population': 194125062},
   {'country': 'Nigeria', 'population': 186988000},
   {'country': 'Bangladesh', 'population': 161006790},
   {'country': 'Russian Federation', 'population': 146599183},
   {'country': 'Japan', 'population': 126960000}
   ]

   # خروجی شما باید به این شکل باشد

   print(most_populated_countries(filename='./data/countries_data.json', 3))
   [
   {'country': 'China', 'population': 1377422166},
   {'country': 'India', 'population': 1295210000},
   {'country': 'United States of America', 'population': 323947000}
   ]
   ```

### تمرین‌ها: سطح ۲

1. تمام آدرس‌های ایمیل ورودی را به صورت یک لیست از فایل email_exchange_big.txt استخراج کنید.
2. رایج‌ترین کلمات در زبان انگلیسی را پیدا کنید. نام تابع خود را find_most_common_words بگذارید، این تابع دو پارامتر می‌گیرد - یک رشته یا یک فایل و یک عدد صحیح مثبت که تعداد کلمات را نشان می‌دهد. تابع شما باید آرایه‌ای از تاپل‌ها را به ترتیب نزولی برگرداند. خروجی را بررسی کنید.

```py
    # خروجی شما باید به این شکل باشد
    print(find_most_common_words('sample.txt', 10))
    [(10, 'the'),
    (8, 'be'),
    (6, 'to'),
    (6, 'of'),
    (5, 'and'),
    (4, 'a'),
    (4, 'in'),
    (3, 'that'),
    (2, 'have'),
    (2, 'I')]

    # خروجی شما باید به این شکل باشد
    print(find_most_common_words('sample.txt', 5))

    [(10, 'the'),
    (8, 'be'),
    (6, 'to'),
    (6, 'of'),
    (5, 'and')]
```

3. از تابع find_most_frequent_words برای پیدا کردن موارد زیر استفاده کنید:
   الف) ده کلمه پرتکرار استفاده شده در [سخنرانی اوباما](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/obama_speech.txt)
   ب) ده کلمه پرتکرار استفاده شده در [سخنرانی میشل](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/michelle_obama_speech.txt)
   ج) ده کلمه پرتکرار استفاده شده در [سخنرانی ترامپ](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/donald_speech.txt)
   د) ده کلمه پرتکرار استفاده شده در [سخنرانی ملانیا](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/melina_trump_speech.txt)
4. یک برنامه پایتون بنویسید که شباهت بین دو متن را بررسی کند. این برنامه یک فایل یا یک رشته را به عنوان پارامتر می‌گیرد و شباهت دو متن را ارزیابی می‌کند. به عنوان مثال، شباهت بین متن سخنرانی‌های [میشل](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/michelle_obama_speech.txt) و [ملانیا](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/melina_trump_speech.txt) را بررسی کنید. ممکن است به چند تابع نیاز داشته باشید، تابعی برای تمیز کردن متن (clean_text)، تابعی برای حذف کلمات کمکی (remove_support_words) و در نهایت تابعی برای بررسی شباهت متن (check_text_similarity). لیست [کلمات ایست (stop words)](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/stop_words.py) در پوشه data قرار دارد.
8. ۱۰ کلمه پرتکرار در فایل romeo_and_juliet.txt را پیدا کنید.
9. فایل [hacker news csv](https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/hacker_news.csv) را بخوانید و موارد زیر را پیدا کنید:
   الف) تعداد خطوط حاوی python یا Python را بشمارید.
   ب) تعداد خطوط حاوی JavaScript، javascript یا Javascript را بشمارید.
   ج) تعداد خطوط حاوی Java و نه JavaScript را بشمارید.

🎉 تبریک می‌گویم! 🎉

[<< روز ۲۰](./20_python_package_manager.md) | [روز ۱۸ >>](./18_regular_expressions.md)
