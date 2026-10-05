<div align="center">
  <h1> ۳۰ روز با پایتون: روز ۲۶ - پایتون برای وب </h1>
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
</div>

[<< روز ۲۵ ](./25_pandas.md) | [روز ۲۷ >>](./27_python_with_mongodb.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 روز ۲۶](#-روز-۲۶)
  - [پایتون برای وب](#پایتون-برای-وب)
    - [Flask](#flask)
      - [ساختار پوشه](#ساختار-پوشه)
    - [راه‌اندازی دایرکتوری پروژه](#راهاندازی-دایرکتوری-پروژه)
    - [ایجاد templateها](#ایجاد-templateها)
    - [اسکریپت پایتون](#اسکریپت-پایتون)
    - [ناوبری (Navigation)](#ناوبری-navigation)
    - [استقرار (Deployment)](#استقرار-deployment)
      - [ایجاد حساب کاربری Heroku](#ایجاد-حساب-کاربری-heroku)
      - [ورود به Heroku](#ورود-به-heroku)
      - [ایجاد requirements و Procfile](#ایجاد-requirements-و-procfile)
      - [ارسال پروژه به heroku](#ارسال-پروژه-به-heroku)
  - [تمرینات: روز ۲۶](#تمرینات-روز-۲۶)

# 📘 روز ۲۶

## پایتون برای وب

پایتون یک زبان برنامه‌نویسی همه‌منظوره است و می‌توان از آن در جاهای زیادی استفاده کرد. در این بخش، خواهیم دید که چگونه از پایتون برای وب استفاده می‌کنیم. فریمورک‌های وب پایتون زیادی وجود دارند. Django و Flask محبوب‌ترین آن‌ها هستند. امروز، خواهیم دید که چگونه از Flask برای توسعه وب استفاده کنیم.

### Flask

Flask یک فریمورک توسعه وب است که با پایتون نوشته شده است. Flask از موتور قالب Jinja2 استفاده می‌کند. Flask همچنین می‌تواند با سایر کتابخانه‌های مدرن فرانت‌اند مانند React استفاده شود.

اگر هنوز بسته virtualenv را نصب نکرده‌اید، ابتدا آن را نصب کنید. محیط مجازی به شما امکان می‌دهد تا وابستگی‌های پروژه را از وابستگی‌های ماشین محلی جدا کنید.

#### ساختار پوشه

پس از تکمیل تمام مراحل، ساختار فایل پروژه شما باید به این شکل باشد:

```sh

├── Procfile
├── app.py
├── env
│   ├── bin
├── requirements.txt
├── static
│   └── css
│       └── main.css
└── templates
    ├── about.html
    ├── home.html
    ├── layout.html
    ├── post.html
    └── result.html
```

### راه‌اندازی دایرکتوری پروژه

برای شروع کار با Flask مراحل زیر را دنبال کنید.

مرحله ۱: virtualenv را با استفاده از دستور زیر نصب کنید.

```sh
pip install virtualenv
```

مرحله ۲:

```sh
asabeneh@Asabeneh:~/Desktop$ mkdir python_for_web
asabeneh@Asabeneh:~/Desktop$ cd python_for_web/
asabeneh@Asabeneh:~/Desktop/python_for_web$ virtualenv venv
asabeneh@Asabeneh:~/Desktop/python_for_web$ source venv/bin/activate
(env) asabeneh@Asabeneh:~/Desktop/python_for_web$ pip freeze
(env) asabeneh@Asabeneh:~/Desktop/python_for_web$ pip install Flask
(env) asabeneh@Asabeneh:~/Desktop/python_for_web$ pip freeze
Click==7.0
Flask==1.1.1
itsdangerous==1.1.0
Jinja2==2.10.3
MarkupSafe==1.1.1
Werkzeug==0.16.0
(env) asabeneh@Asabeneh:~/Desktop/python_for_web$```

ما یک دایرکتوری پروژه به نام python_for_web ایجاد کردیم. داخل پروژه یک محیط مجازی *venv* ایجاد کردیم که می‌توانست هر نامی داشته باشد اما من ترجیح می‌دهم آن را _venv_ بنامم. سپس محیط مجازی را فعال کردیم. از pip freeze برای بررسی بسته‌های نصب شده در دایرکتوری پروژه استفاده کردیم. نتیجه pip freeze خالی بود زیرا هنوز بسته‌ای نصب نشده بود.

حالا، بیایید فایل app.py را در دایرکتوری پروژه ایجاد کنیم و کد زیر را بنویسیم. فایل app.py فایل اصلی پروژه خواهد بود. کد زیر دارای ماژول flask و ماژول os است.

### ایجاد routeها

route صفحه اصلی.

```py
# فلاسک را وارد می‌کنیم
from flask import Flask
import os # وارد کردن ماژول سیستم عامل

app = Flask(__name__)

@app.route('/') # این دکوراتور route صفحه اصلی را ایجاد می‌کند
def home ():
    return '<h1>Welcome</h1>'

@app.route('/about')
def about():
    return '<h1>About us</h1>'


if __name__ == '__main__':
    # برای استقرار از environ استفاده می‌کنیم
    # تا هم برای تولید و هم برای توسعه کار کند
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

برای اجرای اپلیکیشن فلسک، `python app.py` را در دایرکتوری اصلی اپلیکیشن فلسک بنویسید.

پس از اجرای `_python app.py_`، لوکال هاست ۵۰۰۰ را بررسی کنید.

بیایید یک route دیگر اضافه کنیم.
ایجاد route درباره ما

```py
# فلاسک را وارد می‌کنیم
from flask import Flask
import os # وارد کردن ماژول سیستم عامل

app = Flask(__name__)

@app.route('/') # این دکوراتور route صفحه اصلی را ایجاد می‌کند
def home ():
    return '<h1>Welcome</h1>'

@app.route('/about')
def about():
    return '<h1>About us</h1>'

if __name__ == '__main__':
    # برای استقرار از environ استفاده می‌کنیم
    # تا هم برای تولید و هم برای توسعه کار کند
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

اکنون، ما route `about` را در کد بالا اضافه کردیم. اگر بخواهیم به جای رشته، یک فایل HTML را رندر کنیم چطور؟ امکان رندر کردن فایل HTML با استفاده از تابع *render_template* وجود دارد. بیایید یک پوشه به نام templates ایجاد کنیم و home.html و about.html را در دایرکتوری پروژه ایجاد کنیم. همچنین بیایید تابع *render_template* را از flask وارد کنیم.

### ایجاد templateها

فایل‌های HTML را داخل پوشه templates ایجاد کنید.

home.html

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>صفحه اصلی</title>
  </head>

  <body>
    <h1>به صفحه اصلی خوش آمدید</h1>
  </body>
</html>
```

about.html

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>درباره ما</title>
  </head>

  <body>
    <h1>درباره ما</h1>
  </body>
</html>
```

### اسکریپت پایتون

app.py

```py
# فلاسک را وارد می‌کنیم
from flask import Flask, render_template
import os # وارد کردن ماژول سیستم عامل

app = Flask(__name__)

@app.route('/') # این دکوراتور route صفحه اصلی را ایجاد می‌کند
def home ():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    # برای استقرار از environ استفاده می‌کنیم
    # تا هم برای تولید و هم برای توسعه کار کند
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

همانطور که می‌بینید برای رفتن به صفحات مختلف یا برای ناوبری به یک نویگیشن نیاز داریم. بیایید به هر صفحه یک لینک اضافه کنیم یا یک layout ایجاد کنیم که برای هر صفحه از آن استفاده کنیم.

### ناوبری (Navigation)

```html
<ul>
  <li><a href="/">صفحه اصلی</a></li>
  <li><a href="/about">درباره ما</a></li>
</ul>
```

اکنون، می‌توانیم با استفاده از لینک بالا بین صفحات جابجا شویم. بیایید یک صفحه اضافی ایجاد کنیم که داده‌های فرم را مدیریت کند. می‌توانید هر نامی برای آن بگذارید، من دوست دارم آن را post.html بنامم.

ما می‌توانیم با استفاده از موتور قالب Jinja2 داده‌ها را به فایل‌های HTML تزریق کنیم.

```py
# فلاسک را وارد می‌کنیم
from flask import Flask, render_template, request, redirect, url_for
import os # وارد کردن ماژول سیستم عامل

app = Flask(__name__)

@app.route('/') # این دکوراتور route صفحه اصلی را ایجاد می‌کند
def home ():
    techs = ['HTML', 'CSS', 'Flask', 'Python']
    name = '30 Days Of Python Programming'
    return render_template('home.html', techs=techs, name = name, title = 'Home')

@app.route('/about')
def about():
    name = '30 Days Of Python Programming'
    return render_template('about.html', name = name, title = 'About Us')

@app.route('/post')
def post():
    name = 'Text Analyzer'
    return render_template('post.html', name = name, title = name)


if __name__ == '__main__':
    # برای استقرار
    # تا هم برای تولید و هم برای توسعه کار کند
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

بیایید templateها را هم ببینیم:

home.html

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>صفحه اصلی</title>
  </head>

  <body>
    <ul>
      <li><a href="/">صفحه اصلی</a></li>
      <li><a href="/about">درباره ما</a></li>
    </ul>
    <h1>به {{name}} خوش آمدید</h1>
     <ul>
    {% for tech in techs %}
      <li>{{tech}}</li>
    {% endfor %}
    </ul>
  </body>
</html>
```

about.html

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>درباره ما</title>
  </head>

  <body>
    <ul>
      <li><a href="/">صفحه اصلی</a></li>
      <li><a href="/about">درباره ما</a></li>
    </ul>
    <h1>درباره ما</h1>
    <h2>{{name}}</h2>
  </body>
</html>```

### ایجاد یک layout

در فایل‌های template، کدهای تکراری زیادی وجود دارد، می‌توانیم یک layout بنویسیم و تکرار را حذف کنیم. بیایید layout.html را داخل پوشه templates ایجاد کنیم.
بعد از ایجاد layout، آن را به هر فایل وارد خواهیم کرد.

#### ارائه فایل استاتیک

یک پوشه static در دایرکتوری پروژه خود ایجاد کنید. داخل پوشه static یک پوشه CSS یا styles ایجاد کنید و یک شیوه نامه CSS ایجاد کنید. ما از ماژول *url_for* برای ارائه فایل استاتیک استفاده می‌کنیم.

layout.html

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link
      href="https://fonts.googleapis.com/css?family=Lato:300,400|Nunito:300,400|Raleway:300,400,500&display=swap"
      rel="stylesheet"
    />
    <link
      rel="stylesheet"
      href="{{ url_for('static', filename='css/main.css') }}"
    />
    {% if title %}
    <title>30 روز با پایتون - {{ title}}</title>
    {% else %}
    <title>30 روز با پایتون</title>
    {% endif %}
  </head>

  <body>
    <header>
      <div class="menu-container">
        <div>
          <a class="brand-name nav-link" href="/">30DaysOfPython</a>
        </div>
        <ul class="nav-lists">
          <li class="nav-list">
            <a class="nav-link active" href="{{ url_for('home') }}">صفحه اصلی</a>
          </li>
          <li class="nav-list">
            <a class="nav-link active" href="{{ url_for('about') }}">درباره ما</a>
          </li>
          <li class="nav-list">
            <a class="nav-link active" href="{{ url_for('post') }}"
              >تحلیلگر متن</a
            >
          </li>
        </ul>
      </div>
    </header>
    <main>
      {% block content %} {% endblock %}
    </main>
  </body>
</html>
```

حالا، بیایید تمام کدهای تکراری را در سایر فایل‌های template حذف کنیم و layout.html را وارد کنیم. href از تابع _url_for_ با نام تابع route برای اتصال هر route ناوبری استفاده می‌کند.

home.html

```html
{% extends 'layout.html' %} {% block content %}
<div class="container">
  <h1>به {{name}} خوش آمدید</h1>
  <p>
    این اپلیکیشن متون را پاکسازی کرده و تعداد کلمات، کاراکترها و
    پرتکرارترین کلمات در متن را تحلیل می‌کند. با کلیک بر روی تحلیلگر متن در
    منو آن را امتحان کنید. برای ساخت این اپلیکیشن وب به تکنولوژی‌های زیر نیاز دارید:
  </p>
  <ul class="tech-lists">
    {% for tech in techs %}
    <li class="tech">{{tech}}</li>

    {% endfor %}
  </ul>
</div>

{% endblock %}
```

about.html

```html
{% extends 'layout.html' %} {% block content %}
<div class="container">
  <h1>درباره {{name}}</h1>
  <p>
    این یک چالش ۳۰ روزه برنامه‌نویسی پایتون است. اگر تا اینجا کدنویسی
    کرده‌اید، شما عالی هستید. برای کار خوب انجام شده تبریک می‌گویم!
  </p>
</div>
{% endblock %}
```

post.html

```html
{% extends 'layout.html' %} {% block content %}
<div class="container">
  <h1>تحلیلگر متن</h1>
  <form action="https://thirtydaysofpython-v1.herokuapp.com/post" method="POST">
    <div>
      <textarea rows="25" name="content" autofocus></textarea>
    </div>
    <div>
      <input type="submit" class="btn" value="پردازش متن" />
    </div>
  </form>
</div>

{% endblock %}
```

متدهای درخواست، متدهای درخواست مختلفی وجود دارند (GET، POST، PUT، DELETE) که متدهای درخواست رایجی هستند و به ما امکان انجام عملیات CRUD (ایجاد، خواندن، به‌روزرسانی، حذف) را می‌دهند.

در route `post`، بسته به نوع درخواست، از متدهای GET و POST به صورت جایگزین استفاده خواهیم کرد، ببینید در کد زیر چگونه به نظر می‌رسد. متد request یک تابع برای مدیریت متدهای درخواست و همچنین دسترسی به داده‌های فرم است.
app.py

```py
# فلاسک را وارد می‌کنیم
from flask import Flask, render_template, request, redirect, url_for
import os # وارد کردن ماژول سیستم عامل

app = Flask(__name__)
# برای جلوگیری از کش شدن فایل استاتیک
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0



@app.route('/') # این دکوراتور route صفحه اصلی را ایجاد می‌کند
def home ():
    techs = ['HTML', 'CSS', 'Flask', 'Python']
    name = '30 Days Of Python Programming'
    return render_template('home.html', techs=techs, name = name, title = 'Home')

@app.route('/about')
def about():
    name = '30 Days Of Python Programming'
    return render_template('about.html', name = name, title = 'About Us')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/post', methods= ['GET','POST'])
def post():
    name = 'Text Analyzer'
    if request.method == 'GET':
         return render_template('post.html', name = name, title = name)
    if request.method =='POST':
        content = request.form['content']
        print(content)
        return redirect(url_for('result'))

if __name__ == '__main__':
    # برای استقرار
    # تا هم برای تولید و هم برای توسعه کار کند
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

تا اینجا، دیدیم که چگونه از template استفاده کنیم و چگونه داده‌ها را به template تزریق کنیم، و چگونه یک layout مشترک داشته باشیم.
حالا، بیایید فایل‌های استاتیک را مدیریت کنیم. یک پوشه به نام static در دایرکتوری پروژه ایجاد کنید و یک پوشه به نام css ایجاد کنید. داخل پوشه css، main.css را ایجاد کنید. فایل main.css شما به layout.html متصل خواهد شد.

نیازی نیست فایل css را بنویسید، آن را کپی کرده و استفاده کنید. بیایید به استقرار (deployment) برویم.

### استقرار (Deployment)

#### ایجاد حساب کاربری Heroku

Heroku یک سرویس استقرار رایگان برای اپلیکیشن‌های فرانت‌اند و فول‌استک ارائه می‌دهد. یک حساب کاربری در [heroku](https://www.heroku.com/) ایجاد کنید و [CLI](https://devcenter.heroku.com/articles/heroku-cli) heroku را برای ماشین خود نصب کنید.
پس از نصب heroku دستور زیر را بنویسید

#### ورود به Heroku

```sh
asabeneh@Asabeneh:~$ heroku login
heroku: Press any key to open up the browser to login or q to exit:
```

بیایید نتیجه را با فشردن هر کلیدی از کیبورد ببینیم. وقتی هر کلیدی را از کیبورد خود فشار دهید، صفحه ورود heroku باز می‌شود و روی صفحه ورود کلیک کنید. سپس ماشین محلی شما به سرور راه دور heroku متصل خواهد شد. اگر به سرور راه دور متصل شوید، این را خواهید دید.

```sh
asabeneh@Asabeneh:~$ heroku login
heroku: Press any key to open up the browser to login or q to exit:
Opening browser to https://cli-auth.heroku.com/auth/browser/be12987c-583a-4458-a2c2-ba2ce7f41610
Logging in... done
Logged in as asabeneh@gmail.com
asabeneh@Asabeneh:~$
```

#### ایجاد requirements و Procfile

قبل از اینکه کد خود را به سرور راه دور ارسال کنیم، به نیازمندی‌ها نیاز داریم

- requirements.txt
- Procfile

```sh
(env) asabeneh@Asabeneh:~/Desktop/python_for_web$ pip freeze
Click==7.0
Flask==1.1.1
itsdangerous==1.1.0
Jinja2==2.10.3
MarkupSafe==1.1.1
Werkzeug==0.16.0
(env) asabeneh@Asabeneh:~/Desktop/python_for_web$ touch requirements.txt
(env) asabeneh@Asabeneh:~/Desktop/python_for_web$ pip freeze > requirements.txt
(env) asabeneh@Asabeneh:~/Desktop/python_for_web$ cat requirements.txt
Click==7.0
Flask==1.1.1
itsdangerous==1.1.0
Jinja2==2.10.3
MarkupSafe==1.1.1
Werkzeug==0.16.0
(env) asabeneh@Asabeneh:~/Desktop/python_for_web$ touch Procfile
(env) asabeneh@Asabeneh:~/Desktop/python_for_web$ ls
Procfile          env/              static/
app.py            requirements.txt  templates/
(env) asabeneh@Asabeneh:~/Desktop/python_for_web$
```

فایل Procfile دستوری را خواهد داشت که اپلیکیشن را در وب سرور، در مورد ما در Heroku، اجرا می‌کند.

```sh
web: python app.py
```

#### ارسال پروژه به heroku

اکنون، آماده استقرار است. مراحل استقرار اپلیکیشن در heroku

1. git init
2. git add .
3. git commit -m "commit message"
4. heroku create 'name of the app as one word'
5. git push heroku master
6. heroku open (برای راه‌اندازی اپلیکیشن مستقر شده)

پس از این مرحله، شما یک اپلیکیشن مانند [این](http://thirdaysofpython-practice.herokuapp.com/) خواهید داشت.

## تمرینات: روز ۲۶

1. شما [این اپلیکیشن](https://thirtydaysofpython-v1-final.herokuapp.com/) را خواهید ساخت. فقط بخش تحلیلگر متن باقی مانده است.


🎉 تبریک می‌گویم ! 🎉

[<< روز ۲۵ ](./25_pandas.md) | [روز ۲۷ >>](./27_python_with_mongodb.md)
