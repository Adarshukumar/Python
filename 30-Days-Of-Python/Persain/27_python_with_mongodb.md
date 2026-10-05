<div align="center">
  <h1> ۳۰ روز با پایتون: روز ۲۷ - پایتون با MongoDB </h1>
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

[<< روز ۲۶](./26_python_web.md) | [روز ۲۸ >>](./28_API.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 روز ۲۷](#-روز-۲۷)
- [پایتون با MongoDB](#پایتون-با-mongodb)
  - [MongoDB](#mongodb)
    - [SQL در مقابل NoSQL](#sql-در-مقابل-nosql)
    - [دریافت رشته اتصال (MongoDB URI)](#دریافت-رشته-اتصال-mongodb-uri)
    - [اتصال اپلیکیشن Flask به کلاستر MongoDB](#اتصال-اپلیکیشن-flask-به-کلاستر-mongodb)
    - [ایجاد پایگاه داده و کالکشن](#ایجاد-پایگاه-داده-و-کالکشن)
    - [درج چندین سند در کالکشن](#درج-چندین-سند-در-کالکشن)
    - [جستجو در MongoDB](#جستجو-در-mongodb)
    - [جستجو با کوئری](#جستجو-با-کوئری)
    - [کوئری جستجو با اصلاح‌کننده](#کوئری-جستجو-با-اصلاحکننده)
    - [محدود کردن اسناد](#محدود-کردن-اسناد)
    - [جستجو با مرتب‌سازی](#جستجو-با-مرتبسازی)
    - [به‌روزرسانی با کوئری](#بهروزرسانی-با-کوئری)
    - [حذف سند](#حذف-سند)
    - [حذف یک کالکشن](#حذف-یک-کالکشن)
  - [💻 تمرینات: روز ۲۷](#-تمرینات-روز-۲۷)

# 📘 روز ۲۷

# پایتون با MongoDB

پایتون یک تکنولوژی بک‌اند است و می‌تواند به برنامه‌های پایگاه داده مختلفی متصل شود. این زبان می‌تواند هم به پایگاه‌های داده SQL و هم noSQL متصل شود. در این بخش، ما پایتون را به پایگاه داده MongoDB که یک پایگاه داده noSQL است متصل می‌کنیم.

## MongoDB

MongoDB یک پایگاه داده NoSQL است. MongoDB داده‌ها را در یک سند شبیه به JSON ذخیره می‌کند که MongoDB را بسیار انعطاف‌پذیر و مقیاس‌پذیر می‌سازد. بیایید به اصطلاحات مختلف پایگاه‌های داده SQL و NoSQL نگاهی بیندازیم. جدول زیر تفاوت بین پایگاه‌های داده SQL و NoSQL را مشخص می‌کند.

### SQL در مقابل NoSQL

![SQL در مقابل NoSQL](../images/mongoDB/sql-vs-nosql.png)

در این بخش، ما بر روی پایگاه داده NoSQL یعنی MongoDB تمرکز خواهیم کرد. بیایید با کلیک بر روی دکمه sign in و سپس کلیک بر روی register در صفحه بعد، در [mongoDB](https://www.mongodb.com/) ثبت‌نام کنیم.

![صفحات ثبت‌نام MongoDB](../images/mongoDB/mongodb-signup-page.png)

فیلدها را کامل کرده و روی continue کلیک کنید

![ثبت‌نام Mongodb](../images/mongoDB/mongodb-register.png)

طرح رایگان را انتخاب کنید

![طرح رایگان Mongodb](../images/mongoDB/mongodb-free.png)

نزدیک‌ترین منطقه رایگان را انتخاب کرده و نامی برای کلاستر خود انتخاب کنید.

![نام کلاستر Mongodb](../images/mongoDB/mongodb-cluster-name.png)

اکنون، یک sandbox رایگان ایجاد شده است

![sandbox در Mongodb](../images/mongoDB/mongodb-sandbox.png)

دسترسی از تمام هاست‌های محلی

![اجازه دسترسی IP در Mongodb](../images/mongoDB/mongodb-allow-ip-access.png)

کاربر و رمز عبور را اضافه کنید

![افزودن کاربر در Mongodb](../images/mongoDB/mongodb-add-user.png)

یک لینک uri برای mongoDB ایجاد کنید

![ایجاد uri در Mongodb](../images/mongoDB/mongodb-create-uri.png)

درایور پایتون نسخه ۳.۶ یا بالاتر را انتخاب کنید

![درایور پایتون برای Mongodb](../images/mongoDB/mongodb-python-driver.png)

### دریافت رشته اتصال (MongoDB URI)

لینک رشته اتصال را کپی کنید و چیزی شبیه به این دریافت خواهید کرد:

```sh
mongodb+srv://asabeneh:<password>@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority
```

نگران url نباشید، این وسیله‌ای برای اتصال اپلیکیشن شما به mongoDB است.
بیایید جایگزین `password` را با رمز عبوری که برای افزودن کاربر استفاده کردید، جایگزین کنیم.

**مثال:**

```sh
mongodb+srv://asabeneh:123123123@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority
```

اکنون، من همه چیز را جایگزین کردم و رمز عبور 123123 و نام پایگاه داده `thirty_days_python` است. این فقط یک مثال است، رمز عبور شما باید قوی‌تر از رمز عبور مثال باشد.

پایتون برای دسترسی به پایگاه داده mongoDB به یک درایور mongoDB نیاز دارد. ما از `_pymongo_` به همراه `_dnspython_` برای اتصال اپلیکیشن خود به پایگاه داده mongoDB استفاده خواهیم کرد. داخل دایرکتوری پروژه خود `pymongo` و `dnspython` را نصب کنید.

```sh
pip install pymongo dnspython
```

ماژول "dnspython" باید برای استفاده از URIهای `mongodb+srv://` نصب شود. `dnspython` یک جعبه ابزار DNS برای پایتون است. تقریباً از همه انواع رکوردها پشتیبانی می‌کند.

### اتصال اپلیکیشن Flask به کلاستر MongoDB

```py
# فلاسک را وارد می‌کنیم
from flask import Flask, render_template
import os # وارد کردن ماژول سیستم عامل
MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
print(client.list_database_names())

app = Flask(__name__)
if __name__ == '__main__':
    # برای استقرار از environ استفاده می‌کنیم
    # تا هم برای تولید و هم برای توسعه کار کند
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

```

وقتی کد بالا را اجرا می‌کنیم، پایگاه‌های داده پیش‌فرض mongoDB را دریافت می‌کنیم.

```sh
['admin', 'local']
```

### ایجاد پایگاه داده و کالکشن

بیایید یک پایگاه داده ایجاد کنیم، پایگاه داده و کالکشن در mongoDB در صورت عدم وجود ایجاد می‌شوند. بیایید یک پایگاه داده به نام `thirty_days_of_python` و یک کالکشن `students` ایجاد کنیم.

برای ایجاد یک پایگاه داده:

```sh
db = client.name_of_databse # می‌توانیم یک پایگاه داده را به این صورت یا به روش دوم ایجاد کنیم
db = client['name_of_database']
```

```py
# فلاسک را وارد می‌کنیم
from flask import Flask, render_template
import os # وارد کردن ماژول سیستم عامل
MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
# ایجاد پایگاه داده
db = client.thirty_days_of_python
# ایجاد کالکشن students و درج یک سند
db.students.insert_one({'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250})
print(client.list_database_names())

app = Flask(__name__)
if __name__ == '__main__':
    # برای استقرار از environ استفاده می‌کنیم
    # تا هم برای تولید و هم برای توسعه کار کند
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

پس از ایجاد پایگاه داده، ما همچنین یک کالکشن `students` ایجاد کردیم و از متد `insert_one()` برای درج یک سند استفاده کردیم.
اکنون، پایگاه داده `thirty_days_of_python` و کالکشن `students` ایجاد شده و سند درج شده است.
کلاستر mongoDB خود را بررسی کنید و هم پایگاه داده و هم کالکشن را خواهید دید. داخل کالکشن، یک سند وجود خواهد داشت.

```sh
['thirty_days_of_python', 'admin', 'local']
```

اگر این را در کلاستر mongoDB ببینید، به این معنی است که شما با موفقیت یک پایگاه داده و یک کالکشن ایجاد کرده‌اید.

![ایجاد پایگاه داده و کالکشن](../images/mongoDB/mongodb-creating_database.png)

اگر در تصویر دیده باشید، سند با یک id طولانی ایجاد شده است که به عنوان کلید اصلی عمل می‌کند. هر بار که ما یک سند ایجاد می‌کنیم، mongoDB یک id منحصربه‌فرد برای آن ایجاد می‌کند.

### درج چندین سند در کالکشن

متد `insert_one()` در هر بار یک آیتم را درج می‌کند. اگر بخواهیم چندین سند را به یکباره درج کنیم، یا از متد `insert_many()` یا از حلقه for استفاده می‌کنیم.
ما می‌توانیم از حلقه for برای درج چندین سند به یکباره استفاده کنیم.

```py
# فلاسک را وارد می‌کنیم
from flask import Flask, render_template
import os # وارد کردن ماژول سیستم عامل
MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)

students = [
        {'name':'David','country':'UK','city':'London','age':34},
        {'name':'John','country':'Sweden','city':'Stockholm','age':28},
        {'name':'Sami','country':'Finland','city':'Helsinki','age':25},
    ]
for student in students:
    db.students.insert_one(student)


app = Flask(__name__)
if __name__ == '__main__':
    # برای استقرار از environ استفاده می‌کنیم
    # تا هم برای تولید و هم برای توسعه کار کند
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

### جستجو در MongoDB

متدهای `find()` و `findOne()` متدهای رایجی برای یافتن داده در یک کالکشن در پایگاه داده mongoDB هستند. این مشابه دستور SELECT در پایگاه داده MySQL است.
بیایید از متد `_find_one()_` برای دریافت یک سند در یک کالکشن پایگاه داده استفاده کنیم.

- `_find_one({"_id": ObjectId("id"})`: اگر id ارائه نشود، اولین رخداد را دریافت می‌کند

```py
# فلاسک را وارد می‌کنیم
from flask import Flask, render_template
import os # وارد کردن ماژول سیستم عامل
MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # دسترسی به پایگاه داده
student = db.students.find_one()
print(student)


app = Flask(__name__)
if __name__ == '__main__':
    # برای استقرار از environ استفاده می‌کنیم
    # تا هم برای تولید و هم برای توسعه کار کند
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Helsinki', 'city': 'Helsinki', 'age': 250}
```

کوئری بالا اولین ورودی را برمی‌گرداند اما ما می‌توانیم با استفاده از `_id` خاص، سند خاصی را هدف قرار دهیم. بیایید یک مثال انجام دهیم، از id دیوید برای دریافت شیء دیوید استفاده کنیم.
`'_id':ObjectId('5df68a23f106fe2d315bbc8c')`

```py
# فلاسک را وارد می‌کنیم
from flask import Flask, render_template
import os # وارد کردن ماژول سیستم عامل
from bson.objectid import ObjectId # شیء id
MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # دسترسی به پایگاه داده
student = db.students.find_one({'_id':ObjectId('5df68a23f106fe2d315bbc8c')})
print(student)

app = Flask(__name__)
if __name__ == '__main__':
    # برای استقرار از environ استفاده می‌کنیم
    # تا هم برای تولید و هم برای توسعه کار کند
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
```

ما دیدیم که چگونه از `_find_one()_` با استفاده از مثال‌های بالا استفاده کنیم. بیایید به `_find()_` برویم

- `_find()`: در صورتی که یک شیء کوئری ارسال نکنیم، تمام رخدادها را از یک کالکشن برمی‌گرداند. این شیء از نوع `pymongo.cursor` است.

```py
# فلاسک را وارد می‌کنیم
from flask import Flask, render_template
import os # وارد کردن ماژول سیستم عامل

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # دسترسی به پایگاه داده
students = db.students.find()
for student in students:
    print(student)

app = Flask(__name__)
if __name__ == '__main__':
    # برای استقرار از environ استفاده می‌کنیم
    # تا هم برای تولید و هم برای توسعه کار کند
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
{'_id': ObjectId('5df68a23f106fe2d315bbc8d'), 'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

ما می‌توانیم با ارسال یک شیء دوم در `_find({}, {})_` مشخص کنیم که کدام فیلدها برگردانده شوند. 0 به معنای عدم نمایش و ۱ به معنای نمایش است، اما نمی‌توانیم 0 و 1 را با هم ترکیب کنیم، به جز برای `_id`.

```py
# فلاسک را وارد می‌کنیم
from flask import Flask, render_template
import os # وارد کردن ماژول سیستم عامل

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # دسترسی به پایگاه داده
students = db.students.find({}, {"_id":0,  "name": 1, "country":1}) # 0 به معنای عدم نمایش و ۱ به معنای نمایش است
for student in students:
    print(student)

app = Flask(__name__)
if __name__ == '__main__':
    # برای استقرار از environ استفاده می‌کنیم
    # تا هم برای تولید و هم برای توسعه کار کند
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'name': 'Asabeneh', 'country': 'Finland'}
{'name': 'David', 'country': 'UK'}
{'name': 'John', 'country': 'Sweden'}
{'name': 'Sami', 'country': 'Finland'}
```

### جستجو با کوئری

در mongoDB، متد `find` یک شیء کوئری می‌گیرد. ما می‌توانیم یک شیء کوئری ارسال کرده و اسنادی را که می‌خواهیم فیلتر کنیم، فیلتر کنیم.

```py
# فلاسک را وارد می‌کنیم
from flask import Flask, render_template
import os # وارد کردن ماژول سیستم عامل

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # دسترسی به پایگاه داده

query = {
    "country":"Finland"
}
students = db.students.find(query)

for student in students:
    print(student)


app = Flask(__name__)
if __name__ == '__main__':
    # برای استقرار از environ استفاده می‌کنیم
    # تا هم برای تولید و هم برای توسعه کار کند
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

کوئری با اصلاح‌کننده‌ها

```py
# فلاسک را وارد می‌کنیم
from flask import Flask, render_template
import os # وارد کردن ماژول سیستم عامل
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # دسترسی به پایگاه داده

query = {
    "city":"Helsinki"
}
students = db.students.find(query)
for student in students:
    print(student)


app = Flask(__name__)
if __name__ == '__main__':
    # برای استقرار از environ استفاده می‌کنیم
    # تا هم برای تولید و هم برای توسعه کار کند
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

### کوئری جستجو با اصلاح‌کننده

```py
# فلاسک را وارد می‌کنیم
from flask import Flask, render_template
import os # وارد کردن ماژول سیستم عامل
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # دسترسی به پایگاه داده
query = {
    "country":"Finland",
    "city":"Helsinki"
}
students = db.students.find(query)
for student in students:
    print(student)


app = Flask(__name__)
if __name__ == '__main__':
    # برای استقرار از environ استفاده می‌کنیم
    # تا هم برای تولید و هم برای توسعه کار کند
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

کوئری با اصلاح‌کننده‌ها

```py
# فلاسک را وارد می‌کنیم
from flask import Flask, render_template
import os # وارد کردن ماژول سیستم عامل
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # دسترسی به پایگاه داده
query = {"age":{"$gt":30}}
students = db.students.find(query)
for student in students:
    print(student)

app = Flask(__name__)
if __name__ == '__main__':
    # برای استقرار از environ استفاده می‌کنیم
    # تا هم برای تولید و هم برای توسعه کار کند
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
```

```py
# فلاسک را وارد می‌کنیم
from flask import Flask, render_template
import os # وارد کردن ماژول سیستم عامل
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # دسترسی به پایگاه داده
query = {"age":{"$lt":30}}
students = db.students.find(query)
for student in students:
    print(student)
```

```sh
{'_id': ObjectId('5df68a23f106fe2d315bbc8d'), 'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

### محدود کردن اسناد

ما می‌توانیم تعداد اسنادی که برمی‌گردانیم را با استفاده از متد `_limit()_` محدود کنیم.

```py
# فلاسک را وارد می‌کنیم
from flask import Flask, render_template
import os # وارد کردن ماژول سیستم عامل
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # دسترسی به پایگاه داده
db.students.find().limit(3)
```

### جستجو با مرتب‌سازی

به طور پیش‌فرض، مرتب‌سازی به صورت صعودی است. ما می‌توانیم با افزودن پارامتر 1-، مرتب‌سازی را به نزولی تغییر دهیم.

```py
# فلاسک را وارد می‌کنیم
from flask import Flask, render_template
import os # وارد کردن ماژول سیستم عامل
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # دسترسی به پایگاه داده
students = db.students.find().sort('name')
for student in students:
    print(student)


students = db.students.find().sort('name',-1)
for student in students:
    print(student)

students = db.students.find().sort('age')
for student in students:
    print(student)

students = db.students.find().sort('age',-1)
for student in students:
    print(student)

app = Flask(__name__)
if __name__ == '__main__':
    # برای استقرار از environ استفاده می‌کنیم
    # تا هم برای تولید و هم برای توسعه کار کند
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)```

ترتیب صعودی

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
{'_id': ObjectId('5df68a23f106fe2d315bbc8d'), 'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

ترتیب نزولی

```sh
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
{'_id': ObjectId('5df68a23f106fe2d315bbc8d'), 'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250}
```

### به‌روزرسانی با کوئری

ما از متد `update_one()` برای به‌روزرسانی یک آیتم استفاده خواهیم کرد. این متد دو شیء می‌گیرد، یکی کوئری و دیگری شیء جدید است.
سن شخص اول، Asabeneh، بسیار غیرمحتمل است. بیایید سن Asabeneh را به‌روزرسانی کنیم.

```py
# فلاسک را وارد می‌کنیم
from flask import Flask, render_template
import os # وارد کردن ماژول سیستم عامل
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # دسترسی به پایگاه داده

query = {'age':250}
new_value = {'$set':{'age':38}}

db.students.update_one(query, new_value)
# بیایید نتیجه را بررسی کنیم که آیا سن اصلاح شده است یا خیر
for student in db.students.find():
    print(student)


app = Flask(__name__)
if __name__ == '__main__':
    # برای استقرار از environ استفاده می‌کنیم
    # تا هم برای تولید و هم برای توسعه کار کند
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 38}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
{'_id': ObjectId('5df68a23f106fe2d315bbc8d'), 'name': 'John', 'country': 'Sweden', 'city': 'Stockholm', 'age': 28}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

وقتی می‌خواهیم چندین سند را به یکباره به‌روزرسانی کنیم، از متد `upate_many()` استفاده می‌کنیم.

### حذف سند

متد `delete_one()` یک سند را حذف می‌کند. متد `delete_one()` یک پارامتر شیء کوئری می‌گیرد. این متد فقط اولین رخداد را حذف می‌کند.
بیایید جان را از کالکشن حذف کنیم.

```py
# فلاسک را وارد می‌کنیم
from flask import Flask, render_template
import os # وارد کردن ماژول سیستم عامل
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # دسترسی به پایگاه داده

query = {'name':'John'}
db.students.delete_one(query)

for student in db.students.find():
    print(student)
# بیایید نتیجه را بررسی کنیم که آیا سن اصلاح شده است یا خیر
for student in db.students.find():
    print(student)


app = Flask(__name__)
if __name__ == '__main__':
    # برای استقرار از environ استفاده می‌کنیم
    # تا هم برای تولید و هم برای توسعه کار کند
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
{'_id': ObjectId('5df68a21f106fe2d315bbc8b'), 'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 38}
{'_id': ObjectId('5df68a23f106fe2d315bbc8c'), 'name': 'David', 'country': 'UK', 'city': 'London', 'age': 34}
{'_id': ObjectId('5df68a23f106fe2d315bbc8e'), 'name': 'Sami', 'country': 'Finland', 'city': 'Helsinki', 'age': 25}
```

همانطور که می‌بینید جان از کالکشن حذف شده است.

وقتی می‌خواهیم چندین سند را حذف کنیم، از متد `delete_many()` استفاده می‌کنیم، که یک شیء کوئری می‌گیرد. اگر یک شیء کوئری خالی به `delete_many({})` ارسال کنیم، تمام اسناد موجود در کالکشن را حذف خواهد کرد.

### حذف یک کالکشن

با استفاده از متد `_drop()` می‌توانیم یک کالکشن را از پایگاه داده حذف کنیم.

```py
# فلاسک را وارد می‌کنیم
from flask import Flask, render_template
import os # وارد کردن ماژول سیستم عامل
import pymongo

MONGODB_URI = 'mongodb+srv://asabeneh:your_password_goes_here@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # دسترسی به پایگاه داده
db.students.drop()
```

اکنون، ما کالکشن `students` را از پایگاه داده حذف کرده‌ایم.

## 💻 تمرینات: روز ۲۷

🎉 تبریک می‌گویم ! 🎉

[<< روز ۲۶](./26_python_web.md) | [روز ۲۸ >>](./28_API.md)
