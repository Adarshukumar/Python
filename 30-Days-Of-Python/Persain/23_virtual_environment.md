<div align="center">
  <h1> ۳۰ روز پایتون: روز ۲۳ - محیط مجازی </h1>
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

[<< روز ۲۲](./22_web_scraping.md) | [روز ۲۴ >>](./24_statistics.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 روز ۲۳](#-روز-۲۳)
  - [راه‌اندازی محیط‌های مجازی](#راهاندازی-محیطهای-مجازی)
  - [💻 تمرین‌ها: روز ۲۳](#-تمرینها-روز-۲۳)

# 📘 روز ۲۳

## راه‌اندازی محیط‌های مجازی

برای شروع یک پروژه، بهتر است که یک محیط مجازی داشته باشید. محیط مجازی می‌تواند به ما در ایجاد یک محیط ایزوله یا جدا کمک کند. این کار به ما کمک می‌کند تا از تداخل وابستگی‌ها (dependencies) در پروژه‌های مختلف جلوگیری کنیم. اگر `pip freeze` را در ترمینال خود بنویسید، تمام پکیج‌های نصب شده روی کامپیوتر خود را خواهید دید. اگر از virtualenv استفاده کنیم، فقط به پکیج‌هایی دسترسی خواهیم داشت که مختص آن پروژه هستند. ترمینال خود را باز کرده و virtualenv را نصب کنید.

```sh
asabeneh@Asabeneh:~$ pip install virtualenv
```

داخل پوشه 30DaysOfPython یک پوشه به نام flask_project ایجاد کنید.

پس از نصب پکیج virtualenv به پوشه پروژه خود بروید و با نوشتن دستور زیر یک محیط مجازی ایجاد کنید:

برای مک/لینوکس:
```sh
asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ virtualenv venv

```

برای ویندوز:
```sh
C:\Users\User\Documents\30DaysOfPython\flask_project>python -m venv venv
```

من ترجیح می‌دهم پروژه جدید را venv بنامم، اما شما می‌توانید نام دیگری برای آن انتخاب کنید. بیایید با استفاده از دستور ls (یا dir برای خط فرمان ویندوز) بررسی کنیم که آیا venv ایجاد شده است.

```sh
asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ ls
venv/
```

بیایید با نوشتن دستور زیر در پوشه پروژه، محیط مجازی را فعال کنیم.

برای مک/لینوکس:
```sh
asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ source venv/bin/activate
```
فعال‌سازی محیط مجازی در ویندوز ممکن است در Windows Power shell و git bash متفاوت باشد.

برای Windows Power Shell:
```sh
C:\Users\User\Documents\30DaysOfPython\flask_project> venv\Scripts\activate
```

برای Windows Git bash:
```sh
C:\Users\User\Documents\30DaysOfPython\flask_project> venv\Scripts\. activate
```

پس از نوشتن دستور فعال‌سازی، دایرکتوری پروژه شما با venv شروع می‌شود. مثال زیر را ببینید.

```sh
(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$
```

حالا، بیایید با نوشتن `pip freeze` پکیج‌های موجود در این پروژه را بررسی کنیم. هیچ پکیجی را نخواهید دید.

ما قصد داریم یک پروژه کوچک فلسک انجام دهیم، بنابراین بیایید پکیج فلسک را در این پروژه نصب کنیم.

```sh
(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ pip install Flask
```

حالا، بیایید `pip freeze` را بنویسیم تا لیستی از پکیج‌های نصب شده در پروژه را ببینیم:

```sh
(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ pip freeze
Click==7.0
Flask==1.1.1
itsdangerous==1.1.0
Jinja2==2.10.3
MarkupSafe==1.1.1
Werkzeug==0.16.0
```

وقتی کارتان تمام شد، باید با استفاده از `deactivate` پروژه فعال را غیرفعال کنید.

```sh
(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython$ deactivate
```

ماژول‌های لازم برای کار با فلسک نصب شده‌اند. اکنون، دایرکتوری پروژه شما برای یک پروژه فلسک آماده است. شما باید venv را در فایل .gitignore خود قرار دهید تا آن را به گیت‌هاب push نکنید.

## 💻 تمرین‌ها: روز ۲۳

۱. بر اساس مثال بالا، یک دایرکتوری پروژه با یک محیط مجازی ایجاد کنید.

🎉 تبریک! 🎉

[<< روز ۲۲](./22_web_scraping.md) | [روز ۲۴ >>](./24_statistics.md)
