<div align="center">
  <h1> ۳۰ روز با پایتون: روز ۱۸ - عبارات باقاعده </h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

  <sub>نویسنده:
  <a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
  <small> ویرایش اول: نوامبر ۲۲ - دسامبر ۲۲، ۲۰۱۹</small>
  </sub>

</div>

[<< روز ۱۹](./19_file_handling.md) | [روز ۱۷ >>](./17_exception_handling.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 روز ۱۸](#-روز-۱۸)
  - [عبارات باقاعده](#عبارات-باقاعده)
    - [ماژول *re*](#ماژول-re)
    - [متدها در ماژول *re*](#متدها-در-ماژول-re)
      - [Match](#match)
      - [Search](#search)
      - [جستجوی همه تطابق‌ها با استفاده از *findall*](#جستجوی-همه-تطابقها-با-استفاده-از-findall)
      - [جایگزینی یک زیررشته](#جایگزینی-یک-زیررشته)
  - [تقسیم متن با استفاده از RegEx Split](#تقسیم-متن-با-استفاده-از-regex-split)
  - [نوشتن الگوهای RegEx](#نوشتن-الگوهای-regex)
    - [براکت مربعی](#براکت-مربعی)
    - [کاراکتر گریز (\\) در RegEx](#کاراکتر-گریز--در-regex)
    - [یک یا چند بار (+)](#یک-یا-چند-بار-)
    - [نقطه (.)](#نقطه-)
    - [صفر یا چند بار (\*)](#صفر-یا-چند-بار-)
    - [صفر یا یک بار (؟)](#صفر-یا-یک-بار-)
    - [کمیت‌سنج (Quantifier) در RegEx](#کمیتسنج-quantifier-در-regex)
    - [کلاه ^](#کلاه-)
  - [💻 تمرین‌ها: روز ۱۸](#-تمرینها-روز-۱۸)
    - [تمرین‌ها: سطح ۱](#تمرینها-سطح-۱)
    - [تمرین‌ها: سطح ۲](#تمرینها-سطح-۲)
    - [تمرین‌ها: سطح ۳](#تمرینها-سطح-۳)

# 📘 روز ۱۸

## عبارات باقاعده

عبارت باقاعده یا RegEx یک رشته متنی خاص است که به یافتن الگوها در داده‌ها کمک می‌کند. از RegEx می‌توان برای بررسی وجود یک الگو در انواع داده‌های مختلف استفاده کرد. برای استفاده از RegEx در پایتون، ابتدا باید ماژول RegEx را که *re* نامیده می‌شود، وارد کنیم.

### ماژول *re*

پس از وارد کردن ماژول، می‌توانیم از آن برای شناسایی یا یافتن الگوها استفاده کنیم.

```py
import re
```

### متدها در ماژول *re*

برای یافتن یک الگو، از مجموعه‌های مختلف کاراکترهای *re* استفاده می‌کنیم که امکان جستجوی یک تطابق در یک رشته را فراهم می‌کنند.

- *re.match()*: فقط در ابتدای خط اول رشته جستجو می‌کند و در صورت یافتن، اشیاء تطبیق‌یافته را برمی‌گرداند، در غیر این صورت None برمی‌گرداند.
- *re.search*: در صورت وجود تطابق در هر جای رشته، از جمله رشته‌های چندخطی، یک شیء تطبیق را برمی‌گرداند.
- *re.findall*: لیستی حاوی تمام تطابق‌ها را برمی‌گرداند.
- *re.split*: یک رشته را می‌گیرد، آن را در نقاط تطابق تقسیم می‌کند و یک لیست برمی‌گرداند.
- *re.sub*: یک یا چند تطابق را در یک رشته جایگزین می‌کند.

#### Match

```py
# سینتکس
re.match(substring, string, re.I)
# substring یک رشته یا الگو است، string متنی است که در آن به دنبال الگو می‌گردیم، re.I برای نادیده گرفتن حروف بزرگ و کوچک است
```

```py
import re

txt = 'I love to teach python and javaScript'
# یک شیء با span و match برمی‌گرداند
match = re.match('I love to teach', txt, re.I)
print(match)  # <re.Match object; span=(0, 15), match='I love to teach'>
# می‌توانیم موقعیت شروع و پایان تطابق را به صورت یک تاپل با استفاده از span بدست آوریم
span = match.span()
print(span)     # (0, 15)
# بیایید موقعیت شروع و پایان را از span پیدا کنیم
start, end = span
print(start, end)  # 0, 15
substring = txt[start:end]
print(substring)       # I love to teach
```

همانطور که از مثال بالا می‌بینید، الگویی که به دنبال آن هستیم (یا زیررشته‌ای که به دنبال آن هستیم) *I love to teach* است. تابع match **فقط** در صورتی که متن با الگو شروع شود، یک شیء برمی‌گرداند.

```py
import re

txt = 'I love to teach python and javaScript'
match = re.match('I like to teach', txt, re.I)
print(match)  # None
```

رشته با *I like to teach* شروع نمی‌شود، بنابراین هیچ تطابقی وجود نداشت و متد match مقدار None را برگرداند.

#### Search

```py
# سینتکس
re.search(substring, string, re.I)
# substring یک الگو است، string متنی است که در آن به دنبال الگو می‌گردیم، re.I پرچم نادیده گرفتن حروف بزرگ و کوچک است
```

```py
import re

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# یک شیء با span و match برمی‌گرداند
match = re.search('first', txt, re.I)
print(match)  # <re.Match object; span=(100, 105), match='first'>
# می‌توانیم موقعیت شروع و پایان تطابق را به صورت یک تاپل با استفاده از span بدست آوریم
span = match.span()
print(span)     # (100, 105)
# بیایید موقعیت شروع و پایان را از span پیدا کنیم
start, end = span
print(start, end)  # 100 105
substring = txt[start:end]
print(substring)       # first
```

همانطور که می‌بینید، search بسیار بهتر از match است زیرا می‌تواند الگو را در سراسر متن جستجو کند. Search یک شیء تطبیق با اولین تطابقی که پیدا شده است برمی‌گرداند، در غیر این صورت *None* برمی‌گرداند. یک تابع *re* بسیار بهتر *findall* است. این تابع الگو را در کل رشته بررسی می‌کند و تمام تطابق‌ها را به صورت یک لیست برمی‌گرداند.

#### جستجوی همه تطابق‌ها با استفاده از *findall*

*findall()* تمام تطابق‌ها را به صورت یک لیست برمی‌گرداند.

```py
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# یک لیست برمی‌گرداند
matches = re.findall('language', txt, re.I)
print(matches)  # ['language', 'language']
```

همانطور که می‌بینید، کلمه *language* دو بار در رشته پیدا شد. بیایید کمی بیشتر تمرین کنیم.
اکنون به دنبال کلمات Python و python در رشته خواهیم بود:

```py
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# یک لیست برمی‌گرداند
matches = re.findall('python', txt, re.I)
print(matches)  # ['Python', 'python']

```

از آنجایی که از *re.I* استفاده می‌کنیم، هم حروف کوچک و هم حروف بزرگ شامل می‌شوند. اگر پرچم re.I را نداشته باشیم، باید الگوی خود را به طور متفاوتی بنویسیم. بیایید آن را بررسی کنیم:

```py
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

matches = re.findall('Python|python', txt)
print(matches)  # ['Python', 'python']

#
matches = re.findall('[Pp]ython', txt)
print(matches)  # ['Python', 'python']

```

#### جایگزینی یک زیررشته

```py
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.I recommend python for a first programming language

# یا

match_replaced = re.sub('[Pp]ython', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.I recommend python for a first programming language
```

بیایید یک مثال دیگر اضافه کنیم. خواندن رشته زیر واقعاً دشوار است مگر اینکه نماد % را حذف کنیم. جایگزینی % با یک رشته خالی متن را تمیز می‌کند.

```py

txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing.
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs.
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

matches = re.sub('%', '', txt)
print(matches)
```

```sh
I am teacher and I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs. Does this motivate you to be a teacher?
```

## تقسیم متن با استفاده از RegEx Split

```py
txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
print(re.split('\n', txt)) # تقسیم با استفاده از \n - نماد پایان خط
```

```sh
['I am teacher and  I love teaching.', 'There is nothing as rewarding as educating and empowering people.', 'I found teaching more interesting than any other jobs.', 'Does this motivate you to be a teacher?']
```

## نوشتن الگوهای RegEx

برای تعریف یک متغیر رشته‌ای از نقل قول تکی یا دوتایی استفاده می‌کنیم. برای تعریف متغیر RegEx از *r''* استفاده می‌کنیم.
الگوی زیر فقط apple را با حروف کوچک شناسایی می‌کند، برای اینکه آن را نسبت به حروف بزرگ و کوچک غیرحساس کنیم، باید یا الگوی خود را بازنویسی کنیم یا یک پرچم اضافه کنیم.

```py
import re

regex_pattern = r'apple'
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away. '
matches = re.findall(regex_pattern, txt)
print(matches)  # ['apple']

# برای غیرحساس کردن نسبت به حروف بزرگ و کوچک، پرچم اضافه می‌کنیم
matches = re.findall(regex_pattern, txt, re.I)
print(matches)  # ['Apple', 'apple']
# یا می‌توانیم از روش مجموعه کاراکترها استفاده کنیم
regex_pattern = r'[Aa]pple'  # این یعنی حرف اول می‌تواند Apple یا apple باشد
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']

```

* []:  مجموعه‌ای از کاراکترها
  - [a-c] یعنی a یا b یا c
  - [a-z] یعنی هر حرفی از a تا z
  - [A-Z] یعنی هر کاراکتری از A تا Z
  - [0-3] یعنی 0 یا 1 یا 2 یا 3
  - [0-9] یعنی هر عددی از 0 تا 9
  - [A-Za-z0-9] هر کاراکتر تکی که از a تا z، A تا Z یا 0 تا 9 باشد
- \\:  برای گریز از کاراکترهای خاص استفاده می‌شود
  - \d یعنی: تطابق جایی که رشته حاوی ارقام باشد (اعداد از 0-9)
  - \D یعنی: تطابق جایی که رشته حاوی ارقام نباشد
- . : هر کاراکتری به جز کاراکتر خط جدید (\n)
- ^: شروع می‌شود با
  - r'^substring' مثلاً r'^love'، جمله‌ای که با کلمه love شروع می‌شود
  - r'[^abc] یعنی نه a، نه b، نه c.
- $: پایان می‌یابد با
  - r'substring$' مثلاً r'love$'، جمله‌ای که با کلمه love پایان می‌یابد
- *: صفر یا چند بار
  - r'[a]*' یعنی a اختیاری است یا می‌تواند چندین بار تکرار شود.
- +: یک یا چند بار
  - r'[a]+' یعنی حداقل یک بار (یا بیشتر)
- ?: صفر یا یک بار
  - r'[a]?' یعنی صفر بار یا یک بار
- {3}: دقیقاً ۳ کاراکتر
- {3,}: حداقل ۳ کاراکتر
- {3,8}: ۳ تا ۸ کاراکتر
- |: یا این یا آن
  - r'apple|banana' یعنی یا apple یا banana
- (): گرفتن و گروه‌بندی کردن

![Regular Expression cheat sheet](../images/regex.png)

بیایید از مثال‌ها برای روشن کردن فراکاراکترهای بالا استفاده کنیم.

### براکت مربعی

بیایید از براکت مربعی برای شامل کردن حروف کوچک و بزرگ استفاده کنیم.

```py
regex_pattern = r'[Aa]pple' # این براکت مربعی یعنی یا A یا a
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'apple']
```

اگر بخواهیم به دنبال banana بگردیم، الگو را به صورت زیر می‌نویسیم:

```py
regex_pattern = r'[Aa]pple|[Bb]anana' # این براکت مربعی یعنی یا A یا a
txt = 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['Apple', 'banana', 'apple', 'banana']
```

با استفاده از براکت مربعی و عملگر or، موفق شدیم Apple، apple، Banana و banana را استخراج کنیم.

### کاراکتر گریز (\\) در RegEx

```py
regex_pattern = r'\d'  # d یک کاراکتر خاص است که به معنی ارقام است
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2', '0', '1', '9', '8', '2', '0', '2', '1'], این چیزی نیست که ما می‌خواهیم
```

### یک یا چند بار (+)

```py
regex_pattern = r'\d+'  # d یک کاراکتر خاص است که به معنی ارقام است، + یعنی یک یا چند بار
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021'] - حالا بهتر شد!
```

### نقطه (.)

```py
regex_pattern = r'[a].'  # این براکت مربعی یعنی a و . یعنی هر کاراکتری به جز خط جدید
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['an', 'an', 'an', 'a ', 'ar']

regex_pattern = r'[a].+'  # . هر کاراکتر، + هر کاراکتر یک یا چند بار 
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']
```

### صفر یا چند بار (*)

صفر یا چند بار. الگو ممکن است وجود نداشته باشد یا می‌تواند چندین بار تکرار شود.

```py
regex_pattern = r'[a].*'  # . هر کاراکتر، * هر کاراکتر صفر یا چند بار 
txt = '''Apple and banana are fruits'''
matches = re.findall(regex_pattern, txt)
print(matches)  # ['and banana are fruits']
```

### صفر یا یک بار (؟)

صفر یا یک بار. الگو ممکن است وجود نداشته باشد یا ممکن است یک بار تکرار شود.

```py
txt = '''I am not sure if there is a convention how to write the word e-mail.
Some people write it as email others may write it as Email or E-mail.'''
regex_pattern = r'[Ee]-?mail'  # ? در اینجا به این معنی است که '-' اختیاری است
matches = re.findall(regex_pattern, txt)
print(matches)  # ['e-mail', 'email', 'Email', 'E-mail']
```

### کمیت‌سنج (Quantifier) در RegEx

می‌توانیم طول زیررشته‌ای را که در یک متن به دنبال آن هستیم، با استفاده از آکولاد مشخص کنیم. بیایید تصور کنیم که به یک زیررشته با طول ۴ کاراکتر علاقه‌مندیم:

```py
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{4}'  # دقیقاً چهار بار
matches = re.findall(regex_pattern, txt)
print(matches)  # ['2019', '2021']

txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'\d{1, 4}'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2019', '8', '2021']
```

### کلاه ^

- شروع می‌شود با
  
```py
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'^This'  # ^ به معنی شروع می‌شود با
matches = re.findall(regex_pattern, txt)
print(matches)  # ['This']
```

- نفی

```py
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'[^A-Za-z ]+'  # ^ در مجموعه کاراکترها به معنی نفی است، نه A تا Z، نه a تا z، نه فاصله
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6,', '2019', '8', '2021']
```

## 💻 تمرین‌ها: روز ۱۸

### تمرین‌ها: سطح ۱

 ۱. پرتکرارترین کلمه در پاراگراف زیر چیست؟

```py
    paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
```

```sh
    [
    (6, 'love'),
    (5, 'you'),
    (3, 'can'),
    (2, 'what'),
    (2, 'teaching'),
    (2, 'not'),
    (2, 'else'),
    (2, 'do'),
    (2, 'I'),
    (1, 'which'),
    (1, 'to'),
    (1, 'the'),
    (1, 'something'),
    (1, 'if'),
    (1, 'give'),
    (1, 'develop'),
    (1, 'capabilities'),
    (1, 'application'),
    (1, 'an'),
    (1, 'all'),
    (1, 'Python'),
    (1, 'If')
    ]
```

2. موقعیت برخی از ذرات در محور افقی x برابر با ۱۲-، ۴-، ۳- و ۱- در جهت منفی، ۰ در مبدأ، ۴ و ۸ در جهت مثبت است. این اعداد را از کل این متن استخراج کرده و فاصله بین دو ذره دورتر را پیدا کنید.

```py
points = ['-12', '-4', '-3', '-1', '0', '4', '8']
sorted_points =  [-12, -4, -3, -1, 0, 4, 8]
distance = 8 -(-12) # 20
```

### تمرین‌ها: سطح ۲

1. الگویی بنویسید که مشخص کند آیا یک رشته یک متغیر معتبر پایتون است یا خیر.

    ```sh
    is_valid_variable('first_name') # True
    is_valid_variable('first-name') # False
    is_valid_variable('1first_name') # False
    is_valid_variable('firstname') # True
    ```

### تمرین‌ها: سطح ۳

1. متن زیر را تمیز کنید. پس از تمیز کردن، سه کلمه پرتکرار در رشته را بشمارید.

    ```py
    sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

    print(clean_text(sentence));
    I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher
    print(most_frequent_words(cleaned_text)) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]
    ```

🎉 تبریک می‌گویم! 🎉

[<< روز ۱۹](./19_file_handling.md) | [روز ۱۷ >>](./17_exception_handling.md)
