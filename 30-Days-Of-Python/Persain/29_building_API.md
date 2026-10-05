<div align="center">
  <h1> ۳۰ روز با پایتون: روز ۲۹ - ساخت یک API </h1>
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

[<< روز ۲۸](./28_API.md) | [روز ۳۰ >>](./30_conclusions.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [روز ۲۹](#روز-۲۹)
- [ساخت API](#ساخت-api)
  - [ساختار یک API](#ساختار-یک-api)
  - [بازیابی داده با استفاده از get](#بازیابی-داده-با-استفاده-از-get)
  - [دریافت یک سند بر اساس id](#دریافت-یک-سند-بر-اساس-id)
  - [ایجاد داده با استفاده از POST](#ایجاد-داده-با-استفاده-از-post)
  - [به‌روزرسانی با استفاده از PUT](#بهروزرسانی-با-استفاده-از-put)
  - [حذف یک سند با استفاده از Delete](#حذف-یک-سند-با-استفاده-از-delete)
- [💻 تمرینات: روز ۲۹](#-تمرینات-روز-۲۹)

## روز ۲۹

## ساخت API


در این بخش، ما یک API به سبک RESTful را پوشش خواهیم داد که از متدهای درخواست HTTP برای دریافت (GET)، قرار دادن (PUT)، ارسال (POST) و حذف (DELETE) داده‌ها استفاده می‌کند.

API به سبک RESTful یک واسط برنامه‌نویسی کاربردی (API) است که از درخواست‌های HTTP برای دریافت (GET)، قرار دادن (PUT)، ارسال (POST) و حذف (DELETE) داده‌ها استفاده می‌کند. در بخش‌های قبلی، ما با پایتون، فلسک و مانگو‌دی‌بی آشنا شدیم. ما از دانشی که به دست آورده‌ایم برای توسعه یک API به سبک RESTful با استفاده از پایتون فلسک و مانگو‌دی‌بی استفاده خواهیم کرد. هر برنامه‌ای که عملیات CRUD (ایجاد، خواندن، به‌روزرسانی، حذف) را دارد، یک API برای ایجاد داده، دریافت داده، به‌روزرسانی داده یا حذف داده از پایگاه داده دارد.

مرورگر فقط می‌تواند درخواست get را مدیریت کند. بنابراین، ما باید ابزاری داشته باشیم که به ما در مدیریت تمام متدهای درخواست (GET، POST، PUT، DELETE) کمک کند.

نمونه‌هایی از API

- Countries API: https://restcountries.eu/rest/v2/all
- Cats breed API: https://api.thecatapi.com/v1/breeds

[Postman](https://www.getpostman.com/) یک ابزار بسیار محبوب در زمینه توسعه API است. بنابراین، اگر می‌خواهید این بخش را انجام دهید، باید [Postman را دانلود کنید](https://www.getpostman.com/). یک جایگزین برای Postman، [Insomnia](https://insomnia.rest/download) است.

![Postman](../images/postman.png)

### ساختار یک API

یک نقطه پایانی (end point) API یک URL است که می‌تواند به بازیابی، ایجاد، به‌روزرسانی یا حذف یک منبع کمک کند. ساختار آن به این شکل است:
مثال:
https://api.twitter.com/1.1/lists/members.json
اعضای لیست مشخص شده را برمی‌گرداند. اعضای لیست خصوصی فقط در صورتی نشان داده می‌شوند که کاربر احراز هویت شده مالک لیست مشخص شده باشد.
نام شرکت، سپس نسخه و سپس هدف API می‌آید.
متدها:
متدهای HTTP و URLها

API از متدهای HTTP زیر برای دستکاری اشیاء استفاده می‌کند:

```sh
GET        برای بازیابی شیء استفاده می‌شود
POST       برای ایجاد شیء و عملیات روی شیء استفاده می‌شود
PUT        برای به‌روزرسانی شیء استفاده می‌شود
DELETE     برای حذف شیء استفاده می‌شود
```

بیایید یک API بسازیم که اطلاعات مربوط به دانشجویان دوره 30DaysOfPython را جمع‌آوری کند. ما نام، کشور، شهر، تاریخ تولد، مهارت‌ها و بیوگرافی را جمع‌آوری خواهیم کرد.

برای پیاده‌سازی این API، از موارد زیر استفاده خواهیم کرد:

- Postman
- پایتون
- Flask
- MongoDB

### بازیابی داده با استفاده از get

در این مرحله، بیایید از داده‌های ساختگی (dummy data) استفاده کرده و آن را به صورت json برگردانیم. برای بازگرداندن آن به صورت json، از ماژول json و ماژول Response استفاده خواهیم کرد.

```py
# فلاسک را وارد می‌کنیم

from flask import Flask,  Response
import json
import os

app = Flask(__name__)

@app.route('/api/v1.0/students', methods = ['GET'])
def students ():
    student_list = [
        {
            'name':'Asabeneh',
            'country':'Finland',
            'city':'Helsinki',
            'skills':['HTML', 'CSS','JavaScript','Python']
        },
        {
            'name':'David',
            'country':'UK',
            'city':'London',
            'skills':['Python','MongoDB']
        },
        {
            'name':'John',
            'country':'Sweden',
            'city':'Stockholm',
            'skills':['Java','C#']
        }
    ]
    return Response(json.dumps(student_list), mimetype='application/json')


if __name__ == '__main__':
    # برای استقرار
    # تا هم برای تولید و هم برای توسعه کار کند
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)```

وقتی آدرس http://localhost:5000/api/v1.0/students را در مرورگر درخواست می‌کنید، این نتیجه را دریافت خواهید کرد:

![Get on browser](../images/get_on_browser.png)

وقتی آدرس http://localhost:5000/api/v1.0/students را در Postman درخواست می‌کنید، این نتیجه را دریافت خواهید کرد:

![Get on postman](../images/get_on_postman.png)

به جای نمایش داده‌های ساختگی، بیایید اپلیکیشن فلسک را به MongoDB متصل کرده و داده‌ها را از پایگاه داده mongoDB دریافت کنیم.

```py
# فلاسک را وارد می‌کنیم

from flask import Flask,  Response
import json
import pymongo
import os

app = Flask(__name__)

#
MONGODB_URI='mongodb+srv://asabeneh:your_password@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # دسترسی به پایگاه داده

@app.route('/api/v1.0/students', methods = ['GET'])
def students ():

    return Response(json.dumps(student), mimetype='application/json')


if __name__ == '__main__':
    # برای استقرار
    # تا هم برای تولید و هم برای توسعه کار کند
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

با اتصال فلسک، می‌توانیم داده‌های کالکشن students را از پایگاه داده thirty_days_of_python واکشی کنیم.

```sh
[
    {
        "_id": {
            "$oid": "5df68a21f106fe2d315bbc8b"
        },
        "name": "Asabeneh",
        "country": "Finland",
        "city": "Helsinki",
        "age": 38
    },
    {
        "_id": {
            "$oid": "5df68a23f106fe2d315bbc8c"
        },
        "name": "David",
        "country": "UK",
        "city": "London",
        "age": 34
    },
    {
        "_id": {
            "$oid": "5df68a23f106fe2d315bbc8e"
        },
        "name": "Sami",
        "country": "Finland",
        "city": "Helsinki",
        "age": 25
    }
]
```

### دریافت یک سند بر اساس id

ما می‌توانیم با استفاده از یک id به یک سند واحد دسترسی پیدا کنیم، بیایید با استفاده از id به Asabeneh دسترسی پیدا کنیم.
http://localhost:5000/api/v1.0/students/5df68a21f106fe2d315bbc8b

```py
# فلاسک را وارد می‌کنیم

from flask import Flask,  Response
import json
from bson.objectid import ObjectId
import json
from bson.json_util import dumps
import pymongo
import os

app = Flask(__name__)

#
MONGODB_URI='mongodb+srv://asabeneh:your_password@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # دسترسی به پایگاه داده

@app.route('/api/v1.0/students', methods = ['GET'])
def students ():

    return Response(json.dumps(student), mimetype='application/json')
@app.route('/api/v1.0/students/<id>', methods = ['GET'])
def single_student (id):
    student = db.students.find({'_id':ObjectId(id)})
    return Response(dumps(student), mimetype='application/json')

if __name__ == '__main__':
    # برای استقرار
    # تا هم برای تولید و هم برای توسعه کار کند
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

```sh
[
    {
        "_id": {
            "$oid": "5df68a21f106fe2d315bbc8b"
        },
        "name": "Asabeneh",
        "country": "Finland",
        "city": "Helsinki",
        "age": 38
    }
]
```

### ایجاد داده با استفاده از POST

ما از متد درخواست POST برای ایجاد داده استفاده می‌کنیم.

```py
# فلاسک را وارد می‌کنیم

from flask import Flask,  Response
import json
from bson.objectid import ObjectId
import json
from bson.json_util import dumps
import pymongo
from datetime import datetime
import os

app = Flask(__name__)

#
MONGODB_URI='mongodb+srv://asabeneh:your_password@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # دسترسی به پایگاه داده

@app.route('/api/v1.0/students', methods = ['GET'])
def students ():

    return Response(json.dumps(student), mimetype='application/json')
@app.route('/api/v1.0/students/<id>', methods = ['GET'])
def single_student (id):
    student = db.students.find({'_id':ObjectId(id)})
    return Response(dumps(student), mimetype='application/json')
@app.route('/api/v1.0/students', methods = ['POST'])
def create_student ():
    name = request.form['name']
    country = request.form['country']
    city = request.form['city']
    skills = request.form['skills'].split(', ')
    bio = request.form['bio']
    birthyear = request.form['birthyear']
    created_at = datetime.now()
    student = {
        'name': name,
        'country': country,
        'city': city,
        'birthyear': birthyear,
        'skills': skills,
        'bio': bio,
        'created_at': created_at

    }
    db.students.insert_one(student)
    return ;
def update_student (id):
if __name__ == '__main__':
    # برای استقرار
    # تا هم برای تولید و هم برای توسعه کار کند
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

### به‌روزرسانی با استفاده از PUT

```py
# فلاسک را وارد می‌کنیم

from flask import Flask,  Response
import json
from bson.objectid import ObjectId
import json
from bson.json_util import dumps
import pymongo
from datetime import datetime
import os

app = Flask(__name__)

#
MONGODB_URI='mongodb+srv://asabeneh:your_password@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # دسترسی به پایگاه داده

@app.route('/api/v1.0/students', methods = ['GET'])
def students ():

    return Response(json.dumps(student), mimetype='application/json')
@app.route('/api/v1.0/students/<id>', methods = ['GET'])
def single_student (id):
    student = db.students.find({'_id':ObjectId(id)})
    return Response(dumps(student), mimetype='application/json')
@app.route('/api/v1.0/students', methods = ['POST'])
def create_student ():
    name = request.form['name']
    country = request.form['country']
    city = request.form['city']
    skills = request.form['skills'].split(', ')
    bio = request.form['bio']
    birthyear = request.form['birthyear']
    created_at = datetime.now()
    student = {
        'name': name,
        'country': country,
        'city': city,
        'birthyear': birthyear,
        'skills': skills,
        'bio': bio,
        'created_at': created_at

    }
    db.students.insert_one(student)
    return
@app.route('/api/v1.0/students/<id>', methods = ['PUT']) # این دکوراتور route را ایجاد می‌کند
def update_student (id):
    query = {"_id":ObjectId(id)}
    name = request.form['name']
    country = request.form['country']
    city = request.form['city']
    skills = request.form['skills'].split(', ')
    bio = request.form['bio']
    birthyear = request.form['birthyear']
    created_at = datetime.now()
    student = {
        'name': name,
        'country': country,
        'city': city,
        'birthyear': birthyear,
        'skills': skills,
        'bio': bio,
        'created_at': created_at

    }
    db.students.update_one(query, student)
    # return Response(dumps({"result":"a new student has been created"}), mimetype='application/json')
    return
def update_student (id):
if __name__ == '__main__':
    # برای استقرار
    # تا هم برای تولید و هم برای توسعه کار کند
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

### حذف یک سند با استفاده از Delete

```py
# فلاسک را وارد می‌کنیم

from flask import Flask,  Response
import json
from bson.objectid import ObjectId
import json
from bson.json_util import dumps
import pymongo
from datetime import datetime
import os

app = Flask(__name__)

#
MONGODB_URI='mongodb+srv://asabeneh:your_password@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python'] # دسترسی به پایگاه داده

@app.route('/api/v1.0/students', methods = ['GET'])
def students ():

    return Response(json.dumps(student), mimetype='application/json')
@app.route('/api/v1.0/students/<id>', methods = ['GET'])
def single_student (id):
    student = db.students.find({'_id':ObjectId(id)})
    return Response(dumps(student), mimetype='application/json')
@app.route('/api/v1.0/students', methods = ['POST'])
def create_student ():
    name = request.form['name']
    country = request.form['country']
    city = request.form['city']
    skills = request.form['skills'].split(', ')
    bio = request.form['bio']
    birthyear = request.form['birthyear']
    created_at = datetime.now()
    student = {
        'name': name,
        'country': country,
        'city': city,
        'birthyear': birthyear,
        'skills': skills,
        'bio': bio,
        'created_at': created_at

    }
    db.students.insert_one(student)
    return
@app.route('/api/v1.0/students/<id>', methods = ['PUT']) # این دکوراتور route را ایجاد می‌کند
def update_student (id):
    query = {"_id":ObjectId(id)}
    name = request.form['name']
    country = request.form['country']
    city = request.form['city']
    skills = request.form['skills'].split(', ')
    bio = request.form['bio']
    birthyear = request.form['birthyear']
    created_at = datetime.now()
    student = {
        'name': name,
        'country': country,
        'city': city,
        'birthyear': birthyear,
        'skills': skills,
        'bio': bio,
        'created_at': created_at

    }
    db.students.update_one(query, student)
    # return Response(dumps({"result":"a new student has been created"}), mimetype='application/json')
    return
@app.route('/api/v1.0/students/<id>', methods = ['PUT']) # این دکوراتور route را ایجاد می‌کند
def update_student (id):
    query = {"_id":ObjectId(id)}
    name = request.form['name']
    country = request.form['country']
    city = request.form['city']
    skills = request.form['skills'].split(', ')
    bio = request.form['bio']
    birthyear = request.form['birthyear']
    created_at = datetime.now()
    student = {
        'name': name,
        'country': country,
        'city': city,
        'birthyear': birthyear,
        'skills': skills,
        'bio': bio,
        'created_at': created_at

    }
    db.students.update_one(query, student)
    # return Response(dumps({"result":"a new student has been created"}), mimetype='application/json')
    return ;
@app.route('/api/v1.0/students/<id>', methods = ['DELETE'])
def delete_student (id):
    db.students.delete_one({"_id":ObjectId(id)})
    return
if __name__ == '__main__':
    # برای استقرار
    # تا هم برای تولید و هم برای توسعه کار کند
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

## 💻 تمرینات: روز ۲۹

1. مثال بالا را پیاده‌سازی کرده و [این](https://thirtydayofpython-api.herokuapp.com/) را توسعه دهید.

🎉 تبریک می‌گویم ! 🎉

[<< روز ۲۸](./28_API.md) | [روز ۳۰ >>](./30_conclusions.md)
