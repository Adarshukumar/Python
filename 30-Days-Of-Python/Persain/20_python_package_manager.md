<div align="center">
  <h1> ۳۰ روز با پایتون: روز ۲۰ - PIP </h1>
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

[<< روز ۲۱](./21_classes_and_objects.md) | [روز ۱۹ >>](./19_file_handling.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 روز ۲۰](#-روز-۲۰)
  - [PIP پایتون - مدیر بسته پایتون](#pip-پایتون---مدیر-بسته-پایتون)
    - [PIP چیست؟](#pip-چیست)
    - [نصب PIP](#نصب-pip)
    - [نصب بسته‌ها با استفاده از pip](#نصب-بستهها-با-استفاده-از-pip)
    - [حذف بسته‌ها](#حذف-بستهها)
    - [لیست بسته‌ها](#لیست-بستهها)
    - [نمایش بسته](#نمایش-بسته)
    - [PIP Freeze](#pip-freeze)
    - [خواندن از URL](#خواندن-از-url)
    - [ایجاد یک بسته](#ایجاد-یک-بسته)
    - [اطلاعات بیشتر در مورد بسته‌ها](#اطلاعات-بیشتر-در-مورد-بستهها)
  - [تمرین‌ها: روز ۲۰](#تمرینها-روز-۲۰)

# 📘 روز ۲۰

## PIP پایتون - مدیر بسته پایتون

### PIP چیست؟

PIP مخفف Preferred Installer Program (برنامه نصب کننده ترجیحی) است. ما از _pip_ برای نصب بسته‌های مختلف پایتون استفاده می‌کنیم.
بسته (Package) یک ماژول پایتون است که می‌تواند شامل یک یا چند ماژول یا بسته‌های دیگر باشد. یک ماژول یا ماژول‌هایی که می‌توانیم در برنامه خود نصب کنیم، یک بسته است.
در برنامه‌نویسی، لازم نیست هر برنامه کاربردی را خودمان بنویسیم، در عوض بسته‌ها را نصب کرده و آنها را در برنامه‌های خود وارد (import) می‌کنیم.

### نصب PIP

اگر pip را نصب نکرده‌اید، بیایید اکنون آن را نصب کنیم. به ترمینال یا خط فرمان خود بروید و این را کپی و جایگذاری کنید:

```sh
asabeneh@Asabeneh:~$ pip install pip
```

با نوشتن دستور زیر بررسی کنید که آیا pip نصب شده است یا خیر:

```sh
pip --version
```

```py
asabeneh@Asabeneh:~$ pip --version
pip 21.1.3 from /usr/local/lib/python3.7/site-packages/pip (python 3.9.6)
```

همانطور که می‌بینید، من از نسخه 21.1.3 pip استفاده می‌کنم. اگر شما عددی کمی پایین‌تر یا بالاتر از این مشاهده کردید، به این معنی است که pip را نصب کرده‌اید.

بیایید برخی از بسته‌هایی را که در جامعه پایتون برای اهداف مختلف استفاده می‌شوند، بررسی کنیم. فقط برای اطلاع شما، بسته‌های زیادی برای استفاده در برنامه‌های مختلف موجود است.

### نصب بسته‌ها با استفاده از pip

بیایید سعی کنیم _numpy_ را که پایتون عددی (numeric python) نامیده می‌شود، نصب کنیم. این یکی از محبوب‌ترین بسته‌ها در جامعه یادگیری ماشین و علم داده است.

- NumPy بسته بنیادی برای محاسبات علمی با پایتون است. این بسته شامل موارد زیر است:
  - یک شیء آرایه N-بعدی قدرتمند
  - توابع پیچیده (broadcasting)
  - ابزارهایی برای ادغام کدهای C/C++ و Fortran
  - قابلیت‌های مفید جبر خطی، تبدیل فوریه و اعداد تصادفی

```sh
asabeneh@Asabeneh:~$ pip install numpy
```

بیایید شروع به استفاده از numpy کنیم. پوسته تعاملی پایتون خود را باز کنید، `python` را بنویسید و سپس numpy را به صورت زیر وارد کنید:

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy
>>> numpy.version.version
'1.20.1'
>>> lst =
>>> np_arr = numpy.array(lst)
>>> np_arr
array()
>>> len(np_arr)
5
>>> np_arr * 2
array([ 2,  4,  6,  8, 10])
>>> np_arr  + 2
array()
>>>
```

Pandas یک کتابخانه منبع باز با مجوز BSD است که ساختارهای داده‌ای با کارایی بالا و آسان برای استفاده و ابزارهای تحلیل داده را برای زبان برنامه‌نویسی پایتون فراهم می‌کند. بیایید برادر بزرگتر numpy، یعنی _pandas_ را نصب کنیم:

```sh
asabeneh@Asabeneh:~$ pip install pandas
```

```py
asabeneh@Asabeneh:~$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import pandas
```

این بخش در مورد numpy یا pandas نیست، در اینجا ما سعی داریم یاد بگیریم که چگونه بسته‌ها را نصب کنیم و چگونه آنها را وارد کنیم. در صورت لزوم، در بخش‌های دیگر در مورد بسته‌های مختلف صحبت خواهیم کرد.

بیایید یک ماژول مرورگر وب (web browser) را وارد کنیم که می‌تواند به ما در باز کردن هر وب‌سایتی کمک کند. نیازی به نصب این ماژول نداریم، زیرا به طور پیش‌فرض با پایتون ۳ نصب شده است. به عنوان مثال، اگر دوست دارید هر تعداد وب‌سایت را در هر زمانی باز کنید یا اگر دوست دارید چیزی را زمان‌بندی کنید، می‌توان از این ماژول _webbrowser_ استفاده کرد.

```py
import webbrowser # ماژول مرورگر وب برای باز کردن وب‌سایت‌ها

# لیستی از آدرس‌ها: پایتون
url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh/',
    'https://github.com/Asabeneh',
    'https://twitter.com/Asabeneh',
]

# لیست وب‌سایت‌های بالا را در تب‌های جداگانه باز می‌کند
for url in url_lists:
    webbrowser.open_new_tab(url)
```

### حذف بسته‌ها

اگر نمی‌خواهید بسته‌های نصب شده را نگه دارید، می‌توانید آنها را با استفاده از دستور زیر حذف کنید.

```sh
pip uninstall packagename
```

### لیست بسته‌ها

برای دیدن بسته‌های نصب شده روی دستگاه خود، می‌توانیم از `pip` و به دنبال آن `list` استفاده کنیم.

```sh
pip list
```

### نمایش بسته

برای نمایش اطلاعات در مورد یک بسته:

```sh
pip show packagename
```

```sh
asabeneh@Asabeneh:~$ pip show pandas
Name: pandas
Version: 1.2.3
Summary: Powerful data structures for data analysis, time series, and statistics
Home-page: http://pandas.pydata.org
Author: None
Author-email: None
License: BSD
Location: /usr/local/lib/python3.7/site-packages
Requires: python-dateutil, pytz, numpy
Required-by:
```

اگر جزئیات بیشتری بخواهیم، کافیست `--verbose` را اضافه کنیم.

```sh
asabeneh@Asabeneh:~$ pip show --verbose pandas
Name: pandas
Version: 1.2.3
Summary: Powerful data structures for data analysis, time series, and statistics
Home-page: http://pandas.pydata.org
Author: None
Author-email: None
License: BSD
Location: /usr/local/lib/python3.7/site-packages
Requires: numpy, pytz, python-dateutil
Required-by:
Metadata-Version: 2.1
Installer: pip
Classifiers:
  Development Status :: 5 - Production/Stable
  Environment :: Console
  Operating System :: OS Independent
  Intended Audience :: Science/Research
  Programming Language :: Python
  Programming Language :: Python :: 3
  Programming Language :: Python :: 3.5
  Programming Language :: Python :: 3.6
  Programming Language :: Python :: 3.7
  Programming Language :: Python :: 3.8
  Programming Language :: Cython
  Topic :: Scientific/Engineering
Entry-points:
  [pandas_plotting_backends]
  matplotlib = pandas:plotting._matplotlib
```

### PIP Freeze

بسته‌های پایتون نصب شده را به همراه نسخه آنها تولید می‌کند و خروجی برای استفاده در یک فایل نیازمندی‌ها (requirements file) مناسب است. فایل `requirements.txt` فایلی است که باید شامل تمام بسته‌های پایتون نصب شده در یک پروژه پایتون باشد.

```sh
asabeneh@Asabeneh:~$ pip freeze
docutils==0.11
Jinja2==2.7.2
MarkupSafe==0.19
Pygments==1.6
Sphinx==1.2.2
```

دستور `pip freeze` به ما بسته‌های استفاده شده، نصب شده و نسخه آنها را می‌دهد. ما از آن با فایل `requirements.txt` برای استقرار (deployment) استفاده می‌کنیم.

### خواندن از URL

تا به حال با نحوه خواندن یا نوشتن روی فایلی که در دستگاه محلی شما قرار دارد، آشنا شده‌اید. گاهی اوقات، ما می‌خواهیم از یک وب‌سایت با استفاده از URL یا از یک API بخوانیم.
API مخفف Application Program Interface (رابط برنامه‌نویسی کاربردی) است. این وسیله‌ای برای تبادل داده‌های ساختاریافته بین سرورها، عمدتاً به صورت داده‌های JSON است. برای باز کردن یک اتصال شبکه، به بسته‌ای به نام _requests_ نیاز داریم - این بسته به ما امکان می‌دهد یک اتصال شبکه باز کرده و عملیات CRUD (ایجاد، خواندن، به‌روزرسانی و حذف) را پیاده‌سازی کنیم. در این بخش، ما فقط بخش خواندن یا گرفتن (getting) از CRUD را پوشش خواهیم داد.

بیایید _requests_ را نصب کنیم:

```py
asabeneh@Asabeneh:~$ pip install requests
```

ما متدهای _get_، _status_code_، _headers_، _text_ و _json_ را در ماژول _requests_ خواهیم دید:
  - _get()_: برای باز کردن یک شبکه و واکشی داده از URL - یک شیء response برمی‌گرداند.
  - _status_code_: پس از واکشی داده، می‌توانیم وضعیت عملیات را بررسی کنیم (موفق، خطا و غیره).
  - _headers_: برای بررسی انواع هدر.
  - _text_: برای استخراج متن از شیء response واکشی شده.
  - _json_: برای استخراج داده‌های JSON.
بیایید یک فایل txt را از این وب‌سایت بخوانیم: https://www.w3.org/TR/PNG/iso_8859-1.txt.

```py
import requests # وارد کردن ماژول request

url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt' # متنی از یک وب‌سایت

response = requests.get(url) # باز کردن یک شبکه و واکشی داده
print(response)
print(response.status_code) # کد وضعیت، موفق: ۲۰۰
print(response.headers)     # اطلاعات هدرها
print(response.text) # تمام متن صفحه را می‌دهد
```

```sh
<Response>
200
{'date': 'Sun, 08 Dec 2019 18:00:31 GMT', 'last-modified': 'Fri, 07 Nov 2003 05:51:11 GMT', 'etag': '"17e9-3cb82080711c0;50c0b26855880-gzip"', 'accept-ranges': 'bytes', 'cache-control': 'max-age=31536000', 'expires': 'Mon, 07 Dec 2020 18:00:31 GMT', 'vary': 'Accept-Encoding', 'content-encoding': 'gzip', 'access-control-allow-origin': '*', 'content-length': '1616', 'content-type': 'text/plain', 'strict-transport-security': 'max-age=15552000; includeSubdomains; preload', 'content-security-policy': 'upgrade-insecure-requests'}
```

- بیایید از یک API بخوانیم. API مخفف Application Program Interface است. این وسیله‌ای برای تبادل داده‌های ساختاریافته بین سرورها، عمدتاً به صورت داده‌های JSON است. یک نمونه از API: https://restcountries.eu/rest/v2/all. بیایید این API را با استفاده از ماژول _requests_ بخوانیم.

```py
import requests
url = 'https://restcountries.eu/rest/v2/all'  # API کشورها
response = requests.get(url)  # باز کردن یک شبکه و واکشی داده
print(response) # شیء response
print(response.status_code)  # کد وضعیت، موفق: ۲۰۰
countries = response.json()
print(countries[:1])  # ما فقط کشور اول را برش دادیم، برای دیدن همه کشورها برش را حذف کنید
```

```sh
<Response>
200
[{'alpha2Code': 'AF',
  'alpha3Code': 'AFG',
  'altSpellings': ['AF', 'Afġānistān'],
  'area': 652230.0,
  'borders': ['IRN', 'PAK', 'TKM', 'UZB', 'TJK', 'CHN'],
  'callingCodes': ['93'],
  'capital': 'Kabul',
  'cioc': 'AFG',
  'currencies': [{'code': 'AFN', 'name': 'Afghan afghani', 'symbol': '؋'}],
  'demonym': 'Afghan',
  'flag': 'https://restcountries.eu/data/afg.svg',
  'gini': 27.8,
  'languages': [{'iso639_1': 'ps',
                 'iso639_2': 'pus',
                 'name': 'Pashto',
                 'nativeName': 'پښتو'},
                {'iso639_1': 'uz',
                 'iso639_2': 'uzb',
                 'name': 'Uzbek',
                 'nativeName': 'Oʻzbek'},
                {'iso639_1': 'tk',
                 'iso639_2': 'tuk',
                 'name': 'Turkmen',
                 'nativeName': 'Türkmen'}],
  'latlng': [33.0, 65.0],
  'name': 'Afghanistan',
  'nativeName': 'افغانستان',
  'numericCode': '004',
  'population': 27657145,
  'region': 'Asia',
  'regionalBlocs': [{'acronym': 'SAARC',
                     'name': 'South Asian Association for Regional Cooperation',
                     'otherAcronyms': [],
                     'otherNames': []}],
  'subregion': 'Southern Asia',
  'timezones': ['UTC+04:30'],
  'topLevelDomain': ['.af'],
  'translations': {'br': 'Afeganistão',
                   'de': 'Afghanistan',
                   'es': 'Afganistán',
                   'fa': 'افغانستان',
                   'fr': 'Afghanistan',
                   'hr': 'Afganistan',
                   'it': 'Afghanistan',
                   'ja': 'アフガニスタン',
                   'nl': 'Afghanistan',
                   'pt': 'Afeganistão'}}]
```

اگر در حال واکشی داده‌های JSON هستیم، از متد _json()_ از شیء response استفاده می‌کنیم. برای txt، html، xml و سایر فرمت‌های فایل می‌توانیم از _text_ استفاده کنیم.

### ایجاد یک بسته

ما تعداد زیادی فایل را بر اساس معیارهایی در پوشه‌ها و زیرپوشه‌های مختلف سازماندهی می‌کنیم تا بتوانیم آنها را به راحتی پیدا و مدیریت کنیم. همانطور که می‌دانید، یک ماژول می‌تواند شامل چندین شیء مانند کلاس‌ها، توابع و غیره باشد. یک بسته می‌تواند شامل یک یا چند ماژول مرتبط باشد. یک بسته در واقع یک پوشه است که شامل یک یا چند فایل ماژول است. بیایید با استفاده از مراحل زیر، بسته‌ای به نام mypackage ایجاد کنیم:

یک پوشه جدید به نام mypackage در داخل پوشه 30DaysOfPython ایجاد کنید.
یک فایل خالی **__init__**.py در پوشه mypackage ایجاد کنید.
ماژول‌های arithmetic.py و greet.py را با کدهای زیر ایجاد کنید:

```py
# mypackage/arithmetics.py
# arithmetics.py
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total


def subtract(a, b):
    return (a - b)


def multiple(a, b):
    return a * b


def division(a, b):
    return a / b


def remainder(a, b):
    return a % b


def power(a, b):
    return a ** b
```

```py
# mypackage/greet.py
# greet.py
def greet_person(firstname, lastname):
    return f'{firstname} {lastname}, welcome to 30DaysOfPython Challenge!'
```

ساختار پوشه بسته شما باید به این شکل باشد:

```sh
─ mypackage
    ├── __init__.py
    ├── arithmetic.py
    └── greet.py
```

حالا بیایید پوسته تعاملی پایتون را باز کرده و بسته‌ای را که ایجاد کرده‌ایم امتحان کنیم:

```sh
asabeneh@Asabeneh:~/Desktop/30DaysOfPython$ python
Python 3.9.6 (default, Jun 28 2021, 15:26:21)
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from mypackage import arithmetics
>>> arithmetics.add_numbers(1, 2, 3, 5)
11
>>> arithmetics.subtract(5, 3)
2
>>> arithmetics.multiple(5, 3)
15
>>> arithmetics.division(5, 3)
1.6666666666666667
>>> arithmetics.remainder(5, 3)
2
>>> arithmetics.power(5, 3)
125
>>> from mypackage import greet
>>> greet.greet_person('Asabeneh', 'Yetayeh')
'Asabeneh Yetayeh, welcome to 30DaysOfPython Challenge!'
>>>
```

همانطور که می‌بینید، بسته ما به خوبی کار می‌کند. پوشه بسته شامل یک فایل ویژه به نام **__init__**.py است - این فایل محتویات بسته را ذخیره می‌کند. اگر **__init__**.py را در پوشه بسته قرار دهیم، پایتون شروع به شناسایی آن به عنوان یک بسته می‌کند.
فایل **__init__**.py منابع مشخص شده از ماژول‌های خود را برای وارد شدن به سایر فایل‌های پایتون در معرض دید قرار می‌دهد. یک فایل **__init__**.py خالی، تمام توابع را هنگام وارد کردن یک بسته در دسترس قرار می‌دهد. **__init__**.py برای اینکه پوشه توسط پایتون به عنوان یک بسته شناسایی شود، ضروری است.

### اطلاعات بیشتر در مورد بسته‌ها

- پایگاه داده
  - SQLAlchemy یا SQLObject - دسترسی شیءگرا به چندین سیستم پایگاه داده مختلف
    - _pip install SQLAlchemy_
- توسعه وب
  - Django - چارچوب وب سطح بالا.
    - _pip install django_
  - Flask - میکرو چارچوب برای پایتون بر اساس Werkzeug، Jinja 2. (دارای مجوز BSD)
    - _pip install flask_
- تجزیه کننده HTML
  - [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - تجزیه کننده HTML/XML که برای پروژه‌های سریع مانند استخراج داده از صفحات وب (screen-scraping) طراحی شده است، مارک‌آپ‌های نامعتبر را می‌پذیرد.
    - _pip install beautifulsoup4_
  - PyQuery - jQuery را در پایتون پیاده‌سازی می‌کند؛ ظاهراً سریع‌تر از BeautifulSoup است.

- پردازش XML
  - ElementTree - نوع Element یک شیء کانتینر ساده اما انعطاف‌پذیر است که برای ذخیره ساختارهای داده سلسله مراتبی، مانند مجموعه اطلاعات ساده شده XML، در حافظه طراحی شده است. --توجه: پایتون ۲.۵ و بالاتر ElementTree را در کتابخانه استاندارد خود دارد.
- رابط کاربری گرافیکی (GUI)
  - PyQt - اتصالاتی برای چارچوب چندسکویی Qt.
  - TkInter - ابزار سنتی رابط کاربری پایتون.
- تحلیل داده، علم داده و یادگیری ماشین
  - Numpy: Numpy (پایتون عددی) به عنوان یکی از محبوب‌ترین کتابخانه‌های یادگیری ماشین در پایتون شناخته می‌شود.
  - Pandas: یک کتابخانه تحلیل داده، علم داده و یادگیری ماشین در پایتون است که ساختارهای داده سطح بالا و طیف گسترده‌ای از ابزارها را برای تحلیل فراهم می‌کند.
  - SciPy: SciPy یک کتابخانه یادگیری ماشین برای توسعه‌دهندگان برنامه‌ها و مهندسان است. کتابخانه SciPy شامل ماژول‌هایی برای بهینه‌سازی، جبر خطی، انتگرال‌گیری، پردازش تصویر و آمار است.
  - Scikit-Learn: این کتابخانه بر پایه NumPy و SciPy ساخته شده است. به عنوان یکی از بهترین کتابخانه‌ها برای کار با داده‌های پیچیده در نظر گرفته می‌شود.
  - TensorFlow: یک کتابخانه یادگیری ماشین است که توسط گوگل ساخته شده است.
  - Keras: به عنوان یکی از جالب‌ترین کتابخانه‌های یادگیری ماشین در پایتون در نظر گرفته می‌شود. مکانیزم ساده‌تری برای بیان شبکه‌های عصبی فراهم می‌کند. Keras همچنین برخی از بهترین ابزارها را برای کامپایل مدل‌ها، پردازش مجموعه داده‌ها، تجسم نمودارها و موارد دیگر ارائه می‌دهد.
- شبکه:
  - requests: بسته‌ای است که می‌توانیم از آن برای ارسال درخواست به یک سرور (GET, POST, DELETE, PUT) استفاده کنیم.
    - _pip install requests_

🌕 شما همیشه در حال پیشرفت هستید و ۲۰ قدم در مسیر خود به سوی بزرگی جلوتر هستید. اکنون چند تمرین برای مغز و عضلات خود انجام دهید.

## تمرین‌ها: روز ۲۰

۱. این url را بخوانید و ۱۰ کلمه پرتکرار را پیدا کنید. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
۲. API گربه‌ها را بخوانید: cats_api = 'https://api.thecatapi.com/v1/breeds' و موارد زیر را پیدا کنید:
   ۱. حداقل، حداکثر، میانگین، میانه و انحراف معیار وزن گربه‌ها بر حسب واحدهای متریک.
   ۲. حداقل، حداکثر، میانگین، میانه و انحراف معیار طول عمر گربه‌ها بر حسب سال.
   ۳. یک جدول فراوانی از کشور و نژاد گربه‌ها ایجاد کنید.
۳. [API کشورها](https://restcountries.eu/rest/v2/all) را بخوانید و موارد زیر را پیدا کنید:
   ۱. ۱۰ کشور بزرگ.
   ۲. ۱۰ زبان پرگویش‌ترین.
   ۳. تعداد کل زبان‌ها در API کشورها.
۴. UCI یکی از رایج‌ترین مکان‌ها برای به دست آوردن مجموعه داده برای علم داده و یادگیری ماشین است. محتوای UCL (https://archive.ics.uci.edu/ml/datasets.php) را بخوانید. بدون کتابخانه‌های اضافی این کار دشوار خواهد بود، بنابراین ممکن است آن را با BeautifulSoup4 امتحان کنید.

🎉 تبریک می‌گویم! 🎉

[<< روز ۲۱](./21_classes_and_objects.md) | [روز ۱۹ >>](./19_file_handling.md)
