<div align="center">
  <h1> ۳۰ روز با پایتون: روز ۲۵ - Pandas </h1>
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

[<< روز ۲۴](./24_statistics.md) | [روز ۲۶ >>](./26_python_web.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 روز ۲۵](#-روز-۲۵)
  - [Pandas](#pandas)
    - [نصب Pandas](#نصب-pandas)
    - [وارد کردن Pandas](#وارد-کردن-pandas)
    - [ایجاد Series در Pandas با ایندکس پیش‌فرض](#ایجاد-series-در-pandas-با-ایندکس-پیشفرض)
    - [ایجاد Series در Pandas با ایندکس سفارشی](#ایجاد-series-در-pandas-با-ایندکس-سفارشی)
    - [ایجاد Series در Pandas از یک دیکشنری](#ایجاد-series-در-pandas-از-یک-دیکشنری)
    - [ایجاد یک Series ثابت در Pandas](#ایجاد-یک-series-ثابت-در-pandas)
    - [ایجاد یک Series در Pandas با استفاده از Linspace](#ایجاد-یک-series-در-pandas-با-استفاده-از-linspace)
  - [DataFrameها](#dataframeها)
    - [ایجاد DataFrame از لیستی از لیست‌ها](#ایجاد-dataframe-از-لیستی-از-لیستها)
    - [ایجاد DataFrame با استفاده از دیکشنری](#ایجاد-dataframe-با-استفاده-از-دیکشنری)
    - [ایجاد DataFrame از لیستی از دیکشنری‌ها](#ایجاد-dataframe-از-لیستی-از-دیکشنریها)
  - [خواندن فایل CSV با استفاده از Pandas](#خواندن-فایل-csv-با-استفاده-از-pandas)
    - [کاوش داده‌ها](#کاوش-دادهها)
  - [تغییر یک DataFrame](#تغییر-یک-dataframe)
    - [ایجاد یک DataFrame](#ایجاد-یک-dataframe)
    - [افزودن یک ستون جدید](#افزودن-یک-ستون-جدید)
    - [تغییر مقادیر ستون](#تغییر-مقادیر-ستون)
    - [قالب‌بندی ستون‌های DataFrame](#قالببندی-ستونهای-dataframe)
  - [بررسی نوع داده‌های مقادیر ستون](#بررسی-نوع-دادههای-مقادیر-ستون)
    - [ایندکس‌گذاری بولین](#ایندکسگذاری-بولین)
  - [تمرینات: روز ۲۵](#تمرینات-روز-۲۵)
  
# 📘 روز ۲۵

## Pandas

Pandas یک کتابخانه متن‌باز، با کارایی بالا و با ساختارهای داده و ابزارهای تحلیل داده آسان برای زبان برنامه‌نویسی پایتون است.
Pandas ساختارهای داده و ابزارهایی را اضافه می‌کند که برای کار با داده‌های جدولی مانند *Series* و *DataFrames* طراحی شده‌اند.
Pandas ابزارهایی برای دستکاری داده‌ها فراهم می‌کند: 

- تغییر شکل (reshaping)
- ادغام (merging)
- مرتب‌سازی (sorting)
- برش‌دهی (slicing)
- تجمیع (aggregation)
- جایگزینی مقادیر گمشده (imputation).
اگر از anaconda استفاده می‌کنید، نیازی به نصب pandas ندارید.

### نصب Pandas

برای مک:
```py
pip install conda
conda install pandas
```

برای ویندوز:
```py
pip install conda
pip install pandas
```

ساختار داده Pandas بر اساس *Series* و *DataFrames* است.

یک *series* یک *ستون* است و یک DataFrame یک *جدول چندبعدی* است که از مجموعه‌ای از *series*ها تشکیل شده است. برای ایجاد یک series در pandas باید از numpy برای ایجاد آرایه‌های یک‌بعدی یا یک لیست پایتون استفاده کنیم.
بیایید یک مثال از series ببینیم:

Names Pandas Series

![pandas series](../images/pandas-series-1.png) 

Countries Series

![pandas series](../images/pandas-series-2.png) 

Cities Series

![pandas series](../images/pandas-series-3.png)

همانطور که می‌بینید، pandas series تنها یک ستون از داده‌ها است. اگر بخواهیم چندین ستون داشته باشیم از data frames استفاده می‌کنیم. مثال زیر pandas DataFrames را نشان می‌دهد.

بیایید یک مثال از یک pandas data frame ببینیم:

![Pandas data frame](../images/pandas-dataframe-1.png)

Data frame مجموعه‌ای از سطرها و ستون‌ها است. به جدول زیر نگاه کنید؛ این جدول ستون‌های بسیار بیشتری نسبت به مثال بالا دارد:

![Pandas data frame](../images/pandas-dataframe-2.png)

در ادامه، خواهیم دید که چگونه pandas را وارد کنیم و چگونه با استفاده از pandas، Series و DataFrames ایجاد کنیم.

### وارد کردن Pandas

```python
import pandas as pd # وارد کردن pandas با نام مستعار pd
import numpy  as np # وارد کردن numpy با نام مستعار np
```

### ایجاد Series در Pandas با ایندکس پیش‌فرض

```python
nums =
s = pd.Series(nums)
print(s)
```

```sh
    0    1
    1    2
    2    3
    3    4
    4    5
    dtype: int64
```

### ایجاد Series در Pandas با ایندکس سفارشی

```python
nums =
s = pd.Series(nums, index=)
print(s)
```

```sh
    1    1
    2    2
    3    3
    4    4
    5    5
    dtype: int64
```

```python
fruits = ['Orange','Banana','Mango']
fruits = pd.Series(fruits, index=)
print(fruits)
```

```sh
    1    Orange
    2    Banana
    3     Mango
    dtype: object
```

### ایجاد Series در Pandas از یک دیکشنری

```python
dct = {'name':'Asabeneh','country':'Finland','city':'Helsinki'}
```

```python
s = pd.Series(dct)
print(s)
```

```sh
    name       Asabeneh
    country     Finland
    city       Helsinki
    dtype: object
```

### ایجاد یک Series ثابت در Pandas

```python
s = pd.Series(10, index =)
print(s)
```

```sh
    1    10
    2    10
    3    10
    dtype: int64
```

### ایجاد یک Series در Pandas با استفاده از Linspace

```python
s = pd.Series(np.linspace(5, 20, 10)) # linspace(شروع, پایان, تعداد آیتم‌ها)
print(s)```

```sh
    0     5.000000
    1     6.666667
    2     8.333333
    3    10.000000
    4    11.666667
    5    13.333333
    6    15.000000
    7    16.666667
    8    18.333333
    9    20.000000
    dtype: float64
```

## DataFrameها

DataFrameهای Pandas را می‌توان به روش‌های مختلفی ایجاد کرد.

### ایجاد DataFrame از لیستی از لیست‌ها

```python
data = [
    ['Asabeneh', 'Finland', 'Helsink'], 
    ['David', 'UK', 'London'],
    ['John', 'Sweden', 'Stockholm']
]
df = pd.DataFrame(data, columns=['Names','Country','City'])
print(df)
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Names</th>
      <th>Country</th>
      <th>City</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>Asabeneh</td>
      <td>Finland</td>
      <td>Helsink</td>
    </tr>
    <tr>
      <td>1</td>
      <td>David</td>
      <td>UK</td>
      <td>London</td>
    </tr>
    <tr>
      <td>2</td>
      <td>John</td>
      <td>Sweden</td>
      <td>Stockholm</td>
    </tr>
  </tbody>
</table>

### ایجاد DataFrame با استفاده از دیکشنری

```python
data = {'Name': ['Asabeneh', 'David', 'John'], 'Country':[
    'Finland', 'UK', 'Sweden'], 'City': ['Helsiki', 'London', 'Stockholm']}
df = pd.DataFrame(data)
print(df)
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Country</th>
      <th>City</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>Asabeneh</td>
      <td>Finland</td>
      <td>Helsiki</td>
    </tr>
    <tr>
      <td>1</td>
      <td>David</td>
      <td>UK</td>
      <td>London</td>
    </tr>
    <tr>
      <td>2</td>
      <td>John</td>
      <td>Sweden</td>
      <td>Stockholm</td>
    </tr>
  </tbody>
</table>

### ایجاد DataFrame از لیستی از دیکشنری‌ها

```python
data = [
    {'Name': 'Asabeneh', 'Country': 'Finland', 'City': 'Helsinki'},
    {'Name': 'David', 'Country': 'UK', 'City': 'London'},
    {'Name': 'John', 'Country': 'Sweden', 'City': 'Stockholm'}]
df = pd.DataFrame(data)
print(df)
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Country</th>
      <th>City</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>Asabeneh</td>
      <td>Finland</td>
      <td>Helsinki</td>
    </tr>
    <tr>
      <td>1</td>
      <td>David</td>
      <td>UK</td>
      <td>London</td>
    </tr>
    <tr>
      <td>2</td>
      <td>John</td>
      <td>Sweden</td>
      <td>Stockholm</td>
    </tr>
  </tbody>
</table>

## خواندن فایل CSV با استفاده از Pandas

برای دانلود فایل CSV مورد نیاز در این مثال، استفاده از کنسول/خط فرمان کافی است:

```sh
curl -O https://raw.githubusercontent.com/Asabeneh/30-Days-Of-Python/master/data/weight-height.csv
```

فایل دانلود شده را در پوشه کاری خود قرار دهید.

```python
import pandas as pd

df = pd.read_csv('weight-height.csv')
print(df)
```

### کاوش داده‌ها

بیایید با استفاده از ()head فقط ۵ سطر اول را بخوانیم.

```python
print(df.head()) # پنج سطر را می‌دهد، می‌توانیم با ارسال آرگومان به متد ()head تعداد سطرها را افزایش دهیم
```


<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Gender</th>
      <th>Height</th>
      <th>Weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>Male</td>
      <td>73.847017</td>
      <td>241.893563</td>
    </tr>
    <tr>
      <td>1</td>
      <td>Male</td>
      <td>68.781904</td>
      <td>162.310473</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Male</td>
      <td>74.110105</td>
      <td>212.740856</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Male</td>
      <td>71.730978</td>
      <td>220.042470</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Male</td>
      <td>69.881796</td>
      <td>206.349801</td>
    </tr>
  </tbody>
</table>

بیایید با استفاده از متد ()tail، آخرین رکوردهای dataframe را نیز بررسی کنیم.

```python
print(df.tail()) # tails پنج سطر آخر را می‌دهد، می‌توانیم با ارسال آرگومان به متد tail تعداد سطرها را افزایش دهیم
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Gender</th>
      <th>Height</th>
      <th>Weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>9995</td>
      <td>Female</td>
      <td>66.172652</td>
      <td>136.777454</td>
    </tr>
    <tr>
      <td>9996</td>
      <td>Female</td>
      <td>67.067155</td>
      <td>170.867906</td>
    </tr>
    <tr>
      <td>9997</td>
      <td>Female</td>
      <td>63.867992</td>
      <td>128.475319</td>
    </tr>
    <tr>
      <td>9998</td>
      <td>Female</td>
      <td>69.034243</td>
      <td>163.852461</td>
    </tr>
    <tr>
      <td>9999</td>
      <td>Female</td>
      <td>61.944246</td>
      <td>113.649103</td>
    </tr>
  </tbody>
</table>

همانطور که می‌بینید، فایل csv سه ستون دارد: Gender، Height و Weight. اگر DataFrame سطرهای زیادی داشت، دانستن تمام ستون‌ها دشوار بود. بنابراین، باید از یک متد برای دانستن ستون‌ها استفاده کنیم. ما تعداد سطرها را نمی‌دانیم. بیایید از متد shape استفاده کنیم.

```python
print(df.shape) # همانطور که می‌بینید ۱۰۰۰۰ سطر و سه ستون
```

    (10000, 3)

بیایید با استفاده از columns تمام ستون‌ها را بگیریم.

```python
print(df.columns)
```

    Index(['Gender', 'Height', 'Weight'], dtype='object')

حالا، بیایید با استفاده از کلید ستون، یک ستون خاص را بگیریم.

```python
heights = df['Height'] # این اکنون یک series است
```

```python
print(heights)
```

```sh
    0       73.847017
    1       68.781904
    2       74.110105
    3       71.730978
    4       69.881796
              ...    
    9995    66.172652
    9996    67.067155
    9997    63.867992
    9998    69.034243
    9999    61.944246
    Name: Height, Length: 10000, dtype: float64
```

```python
weights = df['Weight'] # این اکنون یک series است
```

```python
print(weights)
```

```sh
    0       241.893563
    1       162.310473
    2       212.740856
    3       220.042470
    4       206.349801
               ...    
    9995    136.777454
    9996    170.867906
    9997    128.475319
    9998    163.852461
    9999    113.649103
    Name: Weight, Length: 10000, dtype: float64
```

```python
print(len(heights) == len(weights))
```

    True

متد ()describe مقادیر آماری توصیفی یک مجموعه داده را فراهم می‌کند.

```python
print(heights.describe()) # اطلاعات آماری درباره داده‌های قد را می‌دهد
```

```sh
    count    10000.000000
    mean        66.367560
    std          3.847528
    min         54.263133
    25%         63.505620
    50%         66.318070
    75%         69.174262
    max         78.998742
    Name: Height, dtype: float64
```

```python
print(weights.describe())
```

```sh
    count    10000.000000
    mean       161.440357
    std         32.108439
    min         64.700127
    25%        135.818051
    50%        161.212928
    75%        187.169525
    max        269.989699
    Name: Weight, dtype: float64```

```python
print(df.describe())  # describe همچنین می‌تواند اطلاعات آماری از یک dataFrame بدهد
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Height</th>
      <th>Weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>count</td>
      <td>10000.000000</td>
      <td>10000.000000</td>
    </tr>
    <tr>
      <td>mean</td>
      <td>66.367560</td>
      <td>161.440357</td>
    </tr>
    <tr>
      <td>std</td>
      <td>3.847528</td>
      <td>32.108439</td>
    </tr>
    <tr>
      <td>min</td>
      <td>54.263133</td>
      <td>64.700127</td>
    </tr>
    <tr>
      <td>25%</td>
      <td>63.505620</td>
      <td>135.818051</td>
    </tr>
    <tr>
      <td>50%</td>
      <td>66.318070</td>
      <td>161.212928</td>
    </tr>
    <tr>
      <td>75%</td>
      <td>69.174262</td>
      <td>187.169525</td>
    </tr>
    <tr>
      <td>max</td>
      <td>78.998742</td>
      <td>269.989699</td>
    </tr>
  </tbody>
</table>

مشابه ()describe، متد ()info نیز اطلاعاتی درباره مجموعه داده می‌دهد.

## تغییر یک DataFrame

تغییر یک DataFrame:
    * ما می‌توانیم یک DataFrame جدید ایجاد کنیم
    * ما می‌توانیم یک ستون جدید ایجاد کرده و آن را به DataFrame اضافه کنیم،
    * ما می‌توانیم یک ستون موجود را از DataFrame حذف کنیم،
    * ما می‌توانیم یک ستون موجود در DataFrame را تغییر دهیم،
    * ما می‌توانیم نوع داده مقادیر ستون در DataFrame را تغییر دهیم

### ایجاد یک DataFrame

مثل همیشه، ابتدا بسته‌های لازم را وارد می‌کنیم. اکنون، بیایید pandas و numpy، دو دوست همیشگی را وارد کنیم.

```python
import pandas as pd
import numpy as np
data = [
    {"Name": "Asabeneh", "Country":"Finland","City":"Helsinki"},
    {"Name": "David", "Country":"UK","City":"London"},
    {"Name": "John", "Country":"Sweden","City":"Stockholm"}]
df = pd.DataFrame(data)
print(df)
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Country</th>
      <th>City</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>Asabeneh</td>
      <td>Finland</td>
      <td>Helsinki</td>
    </tr>
    <tr>
      <td>1</td>
      <td>David</td>
      <td>UK</td>
      <td>London</td>
    </tr>
    <tr>
      <td>2</td>
      <td>John</td>
      <td>Sweden</td>
      <td>Stockholm</td>
    </tr>
  </tbody>
</table>

افزودن یک ستون به DataFrame مانند افزودن یک کلید به دیکشنری است.

ابتدا بیایید از مثال قبلی برای ایجاد یک DataFrame استفاده کنیم. پس از ایجاد DataFrame، شروع به تغییر ستون‌ها و مقادیر ستون‌ها خواهیم کرد.

### افزودن یک ستون جدید

بیایید یک ستون وزن (Weight) به DataFrame اضافه کنیم

```python
weights =
df['Weight'] = weights
df
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Country</th>
      <th>City</th>
      <th>Weight</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>Asabeneh</td>
      <td>Finland</td>
      <td>Helsinki</td>
      <td>74</td>
    </tr>
    <tr>
      <td>1</td>
      <td>David</td>
      <td>UK</td>
      <td>London</td>
      <td>78</td>
    </tr>
    <tr>
      <td>2</td>
      <td>John</td>
      <td>Sweden</td>
      <td>Stockholm</td>
      <td>69</td>
    </tr>
  </tbody>
</table>

بیایید یک ستون قد (Height) نیز به DataFrame اضافه کنیم

```python
heights =
df['Height'] = heights
print(df)
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Country</th>
      <th>City</th>
      <th>Weight</th>
      <th>Height</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>Asabeneh</td>
      <td>Finland</td>
      <td>Helsinki</td>
      <td>74</td>
      <td>173</td>
    </tr>
    <tr>
      <td>1</td>
      <td>David</td>
      <td>UK</td>
      <td>London</td>
      <td>78</td>
      <td>175</td>
    </tr>
    <tr>
      <td>2</td>
      <td>John</td>
      <td>Sweden</td>
      <td>Stockholm</td>
      <td>69</td>
      <td>169</td>
    </tr>
  </tbody>
</table>

همانطور که در DataFrame بالا می‌بینید، ما ستون‌های جدید Weight و Height را اضافه کردیم. بیایید یک ستون اضافی دیگر به نام BMI (شاخص توده بدنی) با محاسبه BMI آنها با استفاده از جرم و قدشان اضافه کنیم. BMI برابر است با جرم تقسیم بر مجذور قد (به متر) - Weight/Height * Height.

همانطور که می‌بینید، قد به سانتی‌متر است، بنابراین باید آن را به متر تغییر دهیم. بیایید سطر قد را تغییر دهیم.

### تغییر مقادیر ستون

```python
df['Height'] = df['Height'] * 0.01
df
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Country</th>
      <th>City</th>
      <th>Weight</th>
      <th>Height</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>Asabeneh</td>
      <td>Finland</td>
      <td>Helsinki</td>
      <td>74</td>
      <td>1.73</td>
    </tr>
    <tr>
      <td>1</td>
      <td>David</td>
      <td>UK</td>
      <td>London</td>
      <td>78</td>
      <td>1.75</td>
    </tr>
    <tr>
      <td>2</td>
      <td>John</td>
      <td>Sweden</td>
      <td>Stockholm</td>
      <td>69</td>
      <td>1.69</td>
    </tr>
  </tbody>
</table>

```python
# استفاده از توابع کد ما را تمیزتر می‌کند، اما می‌توانید bmi را بدون آن محاسبه کنید
def calculate_bmi ():
    weights = df['Weight']
    heights = df['Height']
    bmi = []
    for w,h in zip(weights, heights):
        b = w/(h*h)
        bmi.append(b)
    return bmi
    
bmi = calculate_bmi()

```


```python
df['BMI'] = bmi
df
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Country</th>
      <th>City</th>
      <th>Weight</th>
      <th>Height</th>
      <th>BMI</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>Asabeneh</td>
      <td>Finland</td>
      <td>Helsinki</td>
      <td>74</td>
      <td>1.73</td>
      <td>24.725183</td>
    </tr>
    <tr>
      <td>1</td>
      <td>David</td>
      <td>UK</td>
      <td>London</td>
      <td>78</td>
      <td>1.75</td>
      <td>25.469388</td>
    </tr>
    <tr>
      <td>2</td>
      <td>John</td>
      <td>Sweden</td>
      <td>Stockholm</td>
      <td>69</td>
      <td>1.69</td>
      <td>24.158818</td>
    </tr>
  </tbody>
</table>

### قالب‌بندی ستون‌های DataFrame

مقادیر ستون BMI در DataFrame از نوع float با ارقام معنی‌دار زیادی بعد از اعشار هستند. بیایید آن را به یک رقم معنی‌دار بعد از نقطه تغییر دهیم.

```python
df['BMI'] = round(df['BMI'], 1)
print(df)
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Country</th>
      <th>City</th>
      <th>Weight</th>
      <th>Height</th>
      <th>BMI</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>Asabeneh</td>
      <td>Finland</td>
      <td>Helsinki</td>
      <td>74</td>
      <td>1.73</td>
      <td>24.7</td>
    </tr>
    <tr>
      <td>1</td>
      <td>David</td>
      <td>UK</td>
      <td>London</td>
      <td>78</td>
      <td>1.75</td>
      <td>25.5</td>
    </tr>
    <tr>
      <td>2</td>
      <td>John</td>
      <td>Sweden</td>
      <td>Stockholm</td>
      <td>69</td>
      <td>1.69</td>
      <td>24.2</td>
    </tr>
  </tbody>
</table>

اطلاعات در DataFrame هنوز کامل به نظر نمی‌رسد، بیایید ستون‌های سال تولد و سال جاری را اضافه کنیم.

```python
birth_year = ['1769', '1985', '1990']
current_year = pd.Series(2020, index=)
df['Birth Year'] = birth_year
df['Current Year'] = current_year
df
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Country</th>
      <th>City</th>
      <th>Weight</th>
      <th>Height</th>
      <th>BMI</th>
      <th>Birth Year</th>
      <th>Current Year</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>Asabeneh</td>
      <td>Finland</td>
      <td>Helsinki</td>
      <td>74</td>
      <td>1.73</td>
      <td>24.7</td>
      <td>1769</td>
      <td>2020</td>
    </tr>
    <tr>
      <td>1</td>
      <td>David</td>
      <td>UK</td>
      <td>London</td>
      <td>78</td>
      <td>1.75</td>
      <td>25.5</td>
      <td>1985</td>
      <td>2020</td>
    </tr>
    <tr>
      <td>2</td>
      <td>John</td>
      <td>Sweden</td>
      <td>Stockholm</td>
      <td>69</td>
      <td>1.69</td>
      <td>24.2</td>
      <td>1990</td>
      <td>2020</td>
    </tr>
  </tbody>
</table>

## بررسی نوع داده‌های مقادیر ستون

```python
print(df.Weight.dtype)
```

```sh
    dtype('int64')
```

```python
df['Birth Year'].dtype # این یک شیء رشته‌ای می‌دهد، باید آن را به عدد تغییر دهیم

```

```python
df['Birth Year'] = df['Birth Year'].astype('int')
print(df['Birth Year'].dtype) # بیایید اکنون نوع داده را بررسی کنیم
```

```sh
    dtype('int32')
```

حالا همین کار را برای سال جاری انجام می‌دهیم:

```python
df['Current Year'] = df['Current Year'].astype('int')
df['Current Year'].dtype
```

```sh
    dtype('int32')
```

اکنون، مقادیر ستون سال تولد و سال جاری از نوع integer هستند. می‌توانیم سن را محاسبه کنیم.

```python
ages = df['Current Year'] - df['Birth Year']
ages
```

    0    251
    1     35
    2     30
    dtype: int32

```python
df['Ages'] = ages
print(df)
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Country</th>
      <th>City</th>
      <th>Weight</th>
      <th>Height</th>
      <th>BMI</th>
      <th>Birth Year</th>
      <th>Current Year</th>
      <th>Ages</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>Asabeneh</td>
      <td>Finland</td>
      <td>Helsinki</td>
      <td>74</td>
      <td>1.73</td>
      <td>24.7</td>
      <td>1769</td>
      <td>2019</td>
      <td>250</td>
    </tr>
    <tr>
      <td>1</td>
      <td>David</td>
      <td>UK</td>
      <td>London</td>
      <td>78</td>
      <td>1.75</td>
      <td>25.5</td>
      <td>1985</td>
      <td>2019</td>
      <td>34</td>
    </tr>
    <tr>
      <td>2</td>
      <td>John</td>
      <td>Sweden</td>
      <td>Stockholm</td>
      <td>69</td>
      <td>1.69</td>
      <td>24.2</td>
      <td>1990</td>
      <td>2019</td>
      <td>29</td>
    </tr>
  </tbody>
</table>

فردی که در سطر اول قرار دارد تاکنون ۲۵۱ سال زندگی کرده است. بعید است کسی اینقدر عمر کند. یا این یک اشتباه تایپی است یا داده‌ها ساختگی هستند. پس بیایید آن داده را با میانگین ستون‌ها بدون در نظر گرفتن داده پرت پر کنیم.

mean = (35 + 30)/ 2

```python
mean = (35 + 30)/ 2
print('Mean: ',mean)	#خوب است که توضیحاتی به خروجی اضافه کنیم، تا بدانیم هر چیز چیست
```

```sh
   Mean:  32.5
```

### ایندکس‌گذاری بولین

```python
print(df[df['Ages'] > 120])```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Country</th>
      <th>City</th>
      <th>Weight</th>
      <th>Height</th>
      <th>BMI</th>
      <th>Birth Year</th>
      <th>Current Year</th>
      <th>Ages</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>0</td>
      <td>Asabeneh</td>
      <td>Finland</td>
      <td>Helsinki</td>
      <td>74</td>
      <td>1.73</td>
      <td>24.7</td>
      <td>1769</td>
      <td>2020</td>
      <td>251</td>
    </tr>
  </tbody>
</table>


```python
print(df[df['Ages'] < 120])
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Name</th>
      <th>Country</th>
      <th>City</th>
      <th>Weight</th>
      <th>Height</th>
      <th>BMI</th>
      <th>Birth Year</th>
      <th>Current Year</th>
      <th>Ages</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>David</td>
      <td>UK</td>
      <td>London</td>
      <td>78</td>
      <td>1.75</td>
      <td>25.5</td>
      <td>1985</td>
      <td>2020</td>
      <td>35</td>
    </tr>
    <tr>
      <td>2</td>
      <td>John</td>
      <td>Sweden</td>
      <td>Stockholm</td>
      <td>69</td>
      <td>1.69</td>
      <td>24.2</td>
      <td>1990</td>
      <td>2020</td>
      <td>30</td>
    </tr>
  </tbody>
</table>

## تمرینات: روز ۲۵

1. فایل hacker_news.csv را از پوشه data بخوانید
2. پنج سطر اول را بگیرید
3. پنج سطر آخر را بگیرید
4. ستون title را به عنوان یک pandas series بگیرید
5. تعداد سطرها و ستون‌ها را بشمارید
    - عناوینی که شامل python هستند را فیلتر کنید
    - عناوینی که شامل JavaScript هستند را فیلتر کنید
    - داده‌ها را کاوش کرده و مفهوم آن را درک کنید

🎉 تبریک می‌گویم ! 🎉

[<< روز ۲۴](./24_statistics.md) | [روز ۲۶ >>](./26_python_web.md)
