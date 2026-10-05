<div align="center">
  <h1> ۳۰ روز پایتون: روز ۲۲ - وب اسکرپینگ </h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>نویسنده:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small> ویرایش دوم: جولای، ۲۰۲۱</small>
</sub>
</div>

[<< روز ۲۱](./21_classes_and_objects.md) | [روز ۲۳ >>](./23_virtual_environment.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 روز ۲۲](#-روز-۲۲)
  - [وب اسکرپینگ پایتون](#وب-اسکرپینگ-پایتون)
    - [وب اسکرپینگ چیست](#وب-اسکرپینگ-چیست)
  - [💻 تمرین‌ها: روز ۲۲](#-تمرینها-روز-۲۲)

# 📘 روز ۲۲

## وب اسکرپینگ پایتون

### وب اسکرپینگ چیست

اینترنت مملو از حجم عظیمی از داده است که می‌توان از آن برای اهداف مختلف استفاده کرد. برای جمع‌آوری این داده‌ها، باید بدانیم چگونه داده‌ها را از یک وب‌سایت استخراج (scrape) کنیم.

وب اسکرپینگ فرآیند استخراج و جمع‌آوری داده‌ها از وب‌سایت‌ها و ذخیره آن‌ها بر روی یک ماشین محلی یا در یک پایگاه داده است.

در این بخش، از پکیج‌های beautifulsoup و requests برای اسکرپ کردن داده‌ها استفاده خواهیم کرد. نسخه پکیجی که ما استفاده می‌کنیم beautifulsoup 4 است.

برای شروع اسکرپ کردن وب‌سایت‌ها، به _requests_، _beautifoulSoup4_ و یک _وب‌سایت_ نیاز دارید.

```sh
pip install requests
pip install beautifulsoup4
```

برای اسکرپ کردن داده‌ها از وب‌سایت‌ها، درک اولیه‌ای از تگ‌های HTML و انتخابگرهای CSS لازم است. ما با استفاده از تگ‌ها، کلاس‌ها و/یا idهای HTML، محتوای یک وب‌سایت را هدف قرار می‌دهیم.
بیایید ماژول‌های requests و BeautifulSoup را وارد (import) کنیم

```py
import requests
from bs4 import BeautifulSoup
```

بیایید متغیر url را برای وب‌سایتی که قصد اسکرپ کردن آن را داریم، تعریف کنیم.

```py

import requests
from bs4 import BeautifulSoup
url = 'https://archive.ics.uci.edu/ml/datasets.php'

# بیایید از متد get requests برای دریافت داده‌ها از url استفاده کنیم

response = requests.get(url)
# بیایید وضعیت را بررسی کنیم
status = response.status_code
print(status) # 200 به این معنی است که دریافت موفقیت‌آمیز بوده است
```

```sh
200
```

استفاده از beautifulSoup برای پارس کردن محتوای صفحه

```py
import requests
from bs4 import BeautifulSoup
url = 'https://archive.ics.uci.edu/ml/datasets.php'

response = requests.get(url)
content = response.content # ما تمام محتوای وب‌سایت را دریافت می‌کنیم
soup = BeautifulSoup(content, 'html.parser') # beautiful soup به ما فرصت پارس کردن (parsing) می‌دهد
print(soup.title) # <title>UCI Machine Learning Repository: Data Sets</title>
print(soup.title.get_text()) # UCI Machine Learning Repository: Data Sets
print(soup.body) # کل صفحه وب‌سایت را می‌دهد
print(response.status_code)

tables = soup.find_all('table', {'cellpadding':'3'})
# ما جدولی با ویژگی cellpadding و مقدار 3 را هدف قرار داده‌ایم
# ما می‌توانیم با استفاده از id، class یا تگ HTML انتخاب کنیم، برای اطلاعات بیشتر به مستندات beautifulsoup مراجعه کنید
table = tables # نتیجه یک لیست است، ما در حال استخراج داده از آن هستیم
for td in table.find('tr').find_all('td'):
    print(td.text)
```

اگر این کد را اجرا کنید، می‌توانید ببینید که استخراج تا نیمه انجام شده است. شما می‌توانید آن را ادامه دهید زیرا بخشی از تمرین ۱ است.
برای مرجع، [مستندات beautifulsoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#quick-start) را بررسی کنید

🌕 شما بسیار خاص هستید، هر روز در حال پیشرفت هستید. تنها هشت روز تا رسیدن به عظمت باقی مانده است. اکنون برای مغز و عضلات خود چند تمرین انجام دهید.

## 💻 تمرین‌ها: روز ۲۲

۱. وب‌سایت زیر را اسکرپ کرده و داده‌ها را به عنوان یک فایل json ذخیره کنید (url = 'http://www.bu.edu/president/boston-university-facts-stats/').
۲. جدول موجود در این url (https://archive.ics.uci.edu/ml/datasets.php) را استخراج کرده و آن را به یک فایل json تبدیل کنید.
۳. جدول رؤسای جمهور را اسکرپ کرده و داده‌ها را به صورت json ذخیره کنید (https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States). این جدول ساختار چندان منظمی ندارد و اسکرپ کردن آن ممکن است زمان زیادی ببرد.

🎉 تبریک! 🎉

[<< روز ۲۱](./21_classes_and_objects.md) | [روز ۲۳ >>](./23_virtual_environment.md)
