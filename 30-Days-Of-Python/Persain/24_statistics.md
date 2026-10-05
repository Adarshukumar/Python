<div align="center">
  <h1> ۳۰ روز پایتون: روز ۲۴ - آمار</h1>
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

[<< روز ۲۳](./23_virtual_environment.md) | [روز ۲۵ >>](./25_pandas.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 روز ۲۴](#-روز-۲۴)
  - [پایتون برای تحلیل آماری](#پایتون-برای-تحلیل-آماری)
  - [آمار](#آمار)
  - [داده](#داده)
  - [ماژول Statistics](#ماژول-statistics)
- [NumPy](#numpy)

# 📘 روز ۲۴

## پایتون برای تحلیل آماری

## آمار

آمار رشته‌ای است که به مطالعه _جمع‌آوری_، _سازماندهی_، _نمایش_، _تحلیل_، _تفسیر_ و _ارائه_ داده‌ها می‌پردازد.
آمار شاخه‌ای از ریاضیات است که به عنوان پیش‌نیاز برای علم داده و یادگیری ماشین توصیه می‌شود. آمار یک حوزه بسیار گسترده است اما ما در این بخش فقط بر روی مرتبط‌ترین قسمت آن تمرکز خواهیم کرد.
پس از اتمام این چالش، ممکن است به مسیر توسعه وب، تحلیل داده، یادگیری ماشین و علم داده بروید. هر مسیری را که دنبال کنید، در مقطعی از حرفه‌تان با داده‌هایی مواجه خواهید شد که باید روی آنها کار کنید. داشتن دانش آماری به شما کمک می‌کند تا بر اساس داده‌ها تصمیم‌گیری کنید، _همانطور که می‌گویند داده‌ها سخن می‌گویند_.

## داده

داده چیست؟ داده مجموعه‌ای از کاراکترها است که برای هدفی خاص، معمولاً تحلیل، جمع‌آوری و ترجمه می‌شود. این می‌تواند هر کاراکتری باشد، از جمله متن و اعداد، تصاویر، صدا یا ویدیو. اگر داده در یک زمینه قرار نگیرد، برای انسان یا کامپیوتر معنایی ندارد. برای درک داده‌ها، باید با استفاده از ابزارهای مختلف روی آنها کار کنیم.

جریان کاری تحلیل داده، علم داده یا یادگیری ماشین از داده شروع می‌شود. داده می‌تواند از یک منبع داده تأمین شود یا ایجاد گردد. داده‌ها به دو صورت ساختاریافته و بدون ساختار وجود دارند.

داده‌ها را می‌توان در قالب‌های کوچک یا بزرگ یافت. بیشتر انواع داده‌هایی که با آنها مواجه خواهیم شد در بخش مدیریت فایل‌ها پوشش داده شده‌اند.

## ماژول Statistics

ماژول _statistics_ پایتون توابعی برای محاسبه آمار ریاضی داده‌های عددی فراهم می‌کند. این ماژول قصد رقابت با کتابخانه‌های شخص ثالث مانند NumPy، SciPy یا بسته‌های آماری کامل و اختصاصی برای آماردانان حرفه‌ای مانند Minitab، SAS و Matlab را ندارد. هدف آن در سطح ماشین‌حساب‌های گرافیکی و علمی است.

# NumPy

در بخش اول، ما پایتون را به خودی خود یک زبان برنامه‌نویسی همه‌منظوره عالی تعریف کردیم، اما با کمک کتابخانه‌های محبوب دیگر مانند (numpy، scipy، matplotlib، pandas و غیره) به یک محیط قدرتمند برای محاسبات علمی تبدیل می‌شود.

NumPy کتابخانه اصلی برای محاسبات علمی در پایتون است. این کتابخانه یک شیء آرایه چندبعدی با کارایی بالا و ابزارهایی برای کار با آرایه‌ها فراهم می‌کند.

تا به حال، ما از vscode استفاده می‌کردیم اما از این به بعد توصیه می‌کنم از Jupyter Notebook استفاده کنید. برای دسترسی به Jupyter Notebook، بیایید [anaconda](https://www.anaconda.com/) را نصب کنیم. اگر از anaconda استفاده می‌کنید، بیشتر بسته‌های رایج در آن گنجانده شده‌اند و نیازی به نصب بسته‌ها نخواهید داشت.

```sh
asabeneh@Asabeneh:~/Desktop/30DaysOfPython$ pip install numpy
```

## وارد کردن (Importing) NumPy

Jupyter notebook در دسترس است اگر به [jupyter notebook](https://github.com/Asabeneh/data-science-for-everyone/blob/master/numpy/numpy.ipynb) علاقه‌مند هستید.

```py
    # نحوه وارد کردن numpy
    import numpy as np
    # نحوه بررسی نسخه بسته numpy
    print('numpy:', np.__version__)
    # بررسی متدهای موجود
    print(dir(np))
```

## ایجاد آرایه numpy

### ایجاد آرایه‌های int در numpy

```py
    # ایجاد لیست پایتون
    python_list =

    # بررسی انواع داده
    print('Type:', type (python_list)) # <class 'list'>
    #
    print(python_list) #

    two_dimensional_list = [,,]

    print(two_dimensional_list)  # [,,]

    # ایجاد آرایه Numpy (Numerical Python) از لیست پایتون

    numpy_array_from_list = np.array(python_list)
    print(type (numpy_array_from_list))   # <class 'numpy.ndarray'>
    print(numpy_array_from_list) # array()
```

### ایجاد آرایه‌های float در numpy

ایجاد یک آرایه float در numpy از لیست با پارامتر نوع داده float

```py
    # لیست پایتون
    python_list =

    numy_array_from_list2 = np.array(python_list, dtype=float)
    print(numy_array_from_list2) # array([1., 2., 3., 4., 5.])
```

### ایجاد آرایه‌های boolean در numpy

ایجاد یک آرایه boolean در numpy از لیست

```py
    numpy_bool_array = np.array([0, 1, -1, 0, 0], dtype=bool)
    print(numpy_bool_array) # array([False,  True,  True, False, False])
```

### ایجاد آرایه چندبعدی با استفاده از numpy

یک آرایه numpy ممکن است یک یا چند سطر و ستون داشته باشد

```py
    two_dimensional_list = [,,]
    numpy_two_dimensional_list = np.array(two_dimensional_list)
    print(type (numpy_two_dimensional_list))
    print(numpy_two_dimensional_list)
```

```sh
    <class 'numpy.ndarray'>
    [[0 1 2]
     [3 4 5]
     [6 7 8]]
```

### تبدیل آرایه numpy به لیست

```python
# ما همیشه می‌توانیم یک آرایه را با استفاده از tolist() به یک لیست پایتون تبدیل کنیم.
np_to_list = numpy_array_from_list.tolist()
print(type (np_to_list))
print('one dimensional array:', np_to_list)
print('two dimensional array: ', numpy_two_dimensional_list.tolist())
```

```sh
    <class 'list'>
    one dimensional array:
    two dimensional array:  [,,]
```

### ایجاد آرایه numpy از تاپل

```py
# آرایه Numpy از تاپل
# ایجاد تاپل در پایتون
python_tuple = (1,2,3,4,5)
print(type (python_tuple)) # <class 'tuple'>
print('python_tuple: ', python_tuple) # python_tuple:  (1, 2, 3, 4, 5)

numpy_array_from_tuple = np.array(python_tuple)
print(type (numpy_array_from_tuple)) # <class 'numpy.ndarray'>
print('numpy_array_from_tuple: ', numpy_array_from_tuple) # numpy_array_from_tuple:  [1 2 3 4 5]
```

### شکل (Shape) آرایه numpy

متد shape، شکل آرایه را به صورت یک تاپل ارائه می‌دهد. اولین عنصر سطر و دومین عنصر ستون است. اگر آرایه فقط یک بعدی باشد، اندازه آرایه را برمی‌گرداند.

```py
    nums = np.array()
    print(nums)
    print('shape of nums: ', nums.shape)
    numpy_two_dimensional_list = np.array([[0,1,2],[3,4,5],[6,7,8]])
    print(numpy_two_dimensional_list)
    print('shape of numpy_two_dimensional_list: ', numpy_two_dimensional_list.shape)
    three_by_four_array = np.array([[0, 1, 2, 3],
        [4,5,6,7],
        [8,9,10,11]])
    print(three_by_four_array.shape)
    print('shape of three_by_four_array: ', three_by_four_array.shape)
```

```sh
    [1 2 3 4 5]
    shape of nums:  (5,)
    [[0 1 2]
     [3 4 5]
     [6 7 8]]
    shape of numpy_two_dimensional_list:  (3, 3)
    (3, 4)
```

### نوع داده (Data type) آرایه numpy

انواع داده: str، int، float، complex، bool، list، None

```py
int_lists = [-3, -2, -1, 0, 1, 2,3]
int_array = np.array(int_lists)
float_array = np.array(int_lists, dtype=float)

print(int_array)
print(int_array.dtype)
print(float_array)
print(float_array.dtype)
```

```sh
    [-3 -2 -1  0  1  2  3]
    int64
    [-3. -2. -1.  0.  1.  2.  3.]
    float64
```

### اندازه (Size) یک آرایه numpy

در numpy برای دانستن تعداد آیتم‌ها در یک آرایه numpy از size استفاده می‌کنیم.

```py
numpy_array_from_list = np.array()
two_dimensional_list = np.array([,
                             ,
                             ])

print('The size:', numpy_array_from_list.size) # 5
print('The size:', two_dimensional_list.size)  # 3
```

```sh
    The size: 5
    The size: 9
```

## عملیات ریاضی با استفاده از numpy

آرایه NumPy دقیقاً مانند لیست پایتون نیست. برای انجام عملیات ریاضی در لیست پایتون باید روی آیتم‌ها حلقه بزنیم اما numpy اجازه می‌دهد هر عملیات ریاضی را بدون حلقه زدن انجام دهیم.
عملیات ریاضی:

-   جمع (+)
-   تفریق (-)
-   ضرب (*)
-   تقسیم (/)
-   باقیمانده (%)
-   تقسیم صحیح (//)
-   توان (**)

### جمع

```py
# عملیات ریاضی
# جمع
numpy_array_from_list = np.array()
print('original array: ', numpy_array_from_list)
ten_plus_original = numpy_array_from_list  + 10
print(ten_plus_original)
```

```sh
    original array:  [1 2 3 4 5]
    [11 12 13 14 15]
```

### تفریق

```python
# تفریق
numpy_array_from_list = np.array()
print('original array: ', numpy_array_from_list)
ten_minus_original = numpy_array_from_list  - 10
print(ten_minus_original)```

```sh
    original array:  [1 2 3 4 5]
    [-9 -8 -7 -6 -5]
```

### ضرب

```python
# ضرب
numpy_array_from_list = np.array()
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list * 10
print(ten_times_original)
```

```sh
    original array:  [1 2 3 4 5]
    [10 20 30 40 50]
```

### تقسیم

```python
# تقسیم
numpy_array_from_list = np.array()
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list / 10
print(ten_times_original)
```

```sh
    original array:  [1 2 3 4 5]
    [0.1 0.2 0.3 0.4 0.5]
```

### باقیمانده (Modulus)

```python
# باقیمانده؛ یافتن باقیمانده تقسیم
numpy_array_from_list = np.array()
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list % 3
print(ten_times_original)
```

```sh
    original array:  [1 2 3 4 5]
    [1 2 0 1 2]
```

### تقسیم صحیح (Floor Division)

```py
# تقسیم صحیح: نتیجه تقسیم بدون باقیمانده
numpy_array_from_list = np.array()
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list // 10
print(ten_times_original)
```

### توان (Exponential)

```py
# توان، به معنای به توان رساندن یک عدد به عدد دیگر است:
numpy_array_from_list = np.array()
print('original array: ', numpy_array_from_list)
ten_times_original = numpy_array_from_list  ** 2
print(ten_times_original)
```

```sh
    original array:  [1 2 3 4 5]
    [ 1  4  9 16 25]
```

## بررسی انواع داده

```py
# اعداد صحیح، اعشاری
numpy_int_arr = np.array()
numpy_float_arr = np.array([1.1, 2.0,3.2])
numpy_bool_arr = np.array([-3, -2, 0, 1,2,3], dtype='bool')

print(numpy_int_arr.dtype)
print(numpy_float_arr.dtype)
print(numpy_bool_arr.dtype)
```

```sh
    int64
    float64
    bool
```

### تبدیل انواع

ما می‌توانیم انواع داده آرایه‌های numpy را تبدیل کنیم.

1.  Int به Float

```py
numpy_int_arr = np.array(, dtype = 'float')
numpy_int_arr
```

    array([1., 2., 3., 4.])

2.  Float به Int

```py
numpy_int_arr = np.array([1., 2., 3., 4.], dtype = 'int')
numpy_int_arr
```

```sh
    array()
```

3.  Int به boolean

```py
np.array([-3, -2, 0, 1,2,3], dtype='bool')
```

```sh
    array([ True,  True, False,  True,  True,  True])
```

4.  Int به str

```py
numpy_float_list.astype('int').astype('str')
```

```sh
    array(['1', '2', '3'], dtype='<U21')
```

## آرایه‌های چندبعدی

```py
# آرایه ۲ بعدی
two_dimension_array = np.array([(1,2,3),(4,5,6), (7,8,9)])
print(type (two_dimension_array))
print(two_dimension_array)
print('Shape: ', two_dimension_array.shape)
print('Size:', two_dimension_array.size)
print('Data type:', two_dimension_array.dtype)
```

```sh
    <class 'numpy.ndarray'>
    [[1 2 3]
     [4 5 6]
     [7 8 9]]
    Shape:  (3, 3)
    Size: 9
    Data type: int64
```

### دریافت آیتم‌ها از یک آرایه numpy

```py
# آرایه ۲ بعدی
two_dimension_array = np.array([,,])
first_row = two_dimension_array
second_row = two_dimension_array
third_row = two_dimension_array
print('First row:', first_row)
print('Second row:', second_row)
print('Third row: ', third_row)
```

```sh
    First row: [1 2 3]
    Second row: [4 5 6]
    Third row:  [7 8 9]
```

```py
first_column= two_dimension_array[:,0]
second_column = two_dimension_array[:,1]
third_column = two_dimension_array[:,2]
print('First column:', first_column)
print('Second column:', second_column)
print('Third column: ', third_column)
print(two_dimension_array)
```

```sh
    First column: [1 4 7]
    Second column: [2 5 8]
    Third column:  [3 6 9]
    [[1 2 3]
     [4 5 6]
     [7 8 9]]
```

## برش (Slicing) آرایه Numpy

برش در numpy شبیه به برش در لیست پایتون است.

```py
two_dimension_array = np.array([,,])
first_two_rows_and_columns = two_dimension_array[0:2, 0:2]
print(first_two_rows_and_columns)
```

```sh
    [[1 2]
     [4 5]]
```

### چگونه سطرها و کل آرایه را معکوس کنیم؟

```py
two_dimension_array[::]
```

```sh
    array([,
          ,
          ])
```

### معکوس کردن موقعیت سطر و ستون

```py
    two_dimension_array = np.array([,,])
    two_dimension_array[::-1,::-1]
```

```sh
    array([,
          ,
          ])
```

## چگونه مقادیر گمشده را نمایش دهیم؟

```python
    print(two_dimension_array)
    two_dimension_array = 55
    two_dimension_array =44
    print(two_dimension_array)
```

```sh
    [[1 2 3]
     [4 5 6]
     [7 8 9]]
    [[ 1  2  3]
     [ 4 55 44]
     [ 7  8  9]]
```

```py
    # صفرهای Numpy
    # numpy.zeros(shape, dtype=float, order='C')
    numpy_zeroes = np.zeros((3,3),dtype=int,order='C')
    numpy_zeroes
```

```sh
    array([,
          ,
          ])
```

```py
# یک‌های Numpy
numpy_ones = np.ones((3,3),dtype=int,order='C')
print(numpy_ones)
```

```sh
    [[1 1 1]
     [1 1 1]
     [1 1 1]]
```

```py
twoes = numpy_ones * 2```

```py
# تغییر شکل (Reshape)
# numpy.reshape(), numpy.flatten()
first_shape  = np.array([(1,2,3), (4,5,6)])
print(first_shape)
reshaped = first_shape.reshape(3,2)
print(reshaped)
```

```sh
    [[1 2 3]
     [4 5 6]]
    [[1 2]
     [3 4]
     [5 6]]
```

```py
flattened = reshaped.flatten()
flattened
```

```sh
    array()
```

```py
    ## پشته افقی (Horitzontal Stack)
    np_list_one = np.array()
    np_list_two = np.array()

    print(np_list_one + np_list_two)

    print('Horizontal Append:', np.hstack((np_list_one, np_list_two)))
```

```sh
    [5 7 9]
    Horizontal Append: [1 2 3 4 5 6]
```

```py
    ## پشته عمودی (Vertical Stack)
    print('Vertical Append:', np.vstack((np_list_one, np_list_two)))
```

```sh
    Vertical Append: [[1 2 3]
     [4 5 6]]```

#### تولید اعداد تصادفی

```py
    # تولید یک عدد اعشاری تصادفی
    random_float = np.random.random()
    random_float
```

```sh
    0.018929887384753874
```

```py
    # تولید اعداد اعشاری تصادفی
    random_floats = np.random.random(5)
    random_floats
```

```sh
    array([0.26392192, 0.35842215, 0.87908478, 0.41902195, 0.78926418])
```

```py
    # تولید یک عدد صحیح تصادفی بین ۰ و ۱۰
    random_int = np.random.randint(0, 11)
    random_int
```

```sh
    4
```

```py
    # تولید اعداد صحیح تصادفی بین ۲ و ۱۱ و ایجاد یک آرایه یک سطری
    random_int = np.random.randint(2,10, size=4)
    random_int
```

```sh
    array()
```

```py
    # تولید اعداد صحیح تصادفی بین ۰ و ۱۰
    random_int = np.random.randint(2,10, size=(3,3))
    random_int
```

```sh
    array([,
          ,
          ])
```

### تولید اعداد تصادفی

```py
    # np.random.normal(mu, sigma, size)
    normal_array = np.random.normal(79, 15, 80)
    normal_array
```

```sh
    array([ 89.49990595,  82.06056961, 107.21445842,  38.69307086,
            47.85259157,  93.07381061,  76.40724259,  78.55675184,
            72.17358173,  47.9888899 ,  65.10370622,  76.29696568,
            95.58234254,  68.14897213,  38.75862686, 122.5587927 ,
            67.0762565 ,  95.73990864,  81.97454563,  92.54264805,
            59.37035153,  77.76828101,  52.30752166,  64.43109931,
            62.63695351,  90.04616138,  75.70009094,  49.87586877,
            80.22002414,  68.56708848,  76.27791052,  67.24343975,
            81.86363935,  78.22703433, 102.85737041,  65.15700341,
            84.87033426,  76.7569997 ,  64.61321853,  67.37244562,
            74.4068773 ,  58.65119655,  71.66488727,  53.42458179,
            70.26872028,  60.96588544,  83.56129414,  72.14255326,
            81.00787609,  71.81264853,  72.64168853,  86.56608717,
            94.94667321,  82.32676973,  70.5165446 ,  85.43061003,
            72.45526212,  87.34681775,  87.69911217, 103.02831489,
            75.28598596,  67.17806893,  92.41274447, 101.06662611,
            87.70013935,  70.73980645,  46.40368207,  50.17947092,
            61.75618542,  90.26191397,  78.63968639,  70.84550744,
            88.91826581, 103.91474733,  66.3064638 ,  79.49726264,
            70.81087439,  83.90130623,  87.58555972,  59.95462521])
```

## Numpy و آمار

```py
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
plt.hist(normal_array, color="grey", bins=50)
```

```sh
    (array([2., 0., 0., 0., 1., 2., 2., 0., 2., 0., 0., 1., 2., 2., 1., 4., 3.,
            4., 2., 7., 2., 2., 5., 4., 2., 4., 3., 2., 1., 5., 3., 0., 3., 2.,
            1., 0., 0., 1., 3., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 1.]),
     array([ 38.69307086,  40.37038529,  42.04769973,  43.72501417,
             45.4023286 ,  47.07964304,  48.75695748,  50.43427191,
             52.11158635,  53.78890079,  55.46621523,  57.14352966,
             58.8208441 ,  60.49815854,  62.17547297,  63.85278741,
             65.53010185,  67.20741628,  68.88473072,  70.56204516,
             72.23935959,  73.91667403,  75.59398847,  77.27130291,
             78.94861734,  80.62593178,  82.30324622,  83.98056065,
             85.65787509,  87.33518953,  89.01250396,  90.6898184 ,
             92.36713284,  94.04444727,  95.72176171,  97.39907615,
             99.07639058, 100.75370502, 102.43101946, 104.1083339 ,
            105.78564833, 107.46296277, 109.14027721, 110.81759164,
            112.49490608, 114.17222052, 115.84953495, 117.52684939,
            119.20416383, 120.88147826, 122.5587927 ]),
     <a list of 50 Patch objects>)```

### ماتریس در numpy

```py
four_by_four_matrix = np.matrix(np.ones((4,4), dtype=float))
```

```py
four_by_four_matrix
```

```sh
matrix([[1., 1., 1., 1.],
            [1., 1., 1., 1.],
            [1., 1., 1., 1.],
            [1., 1., 1., 1.]])
```

```py
np.asarray(four_by_four_matrix) = 2
four_by_four_matrix
```

```sh
matrix([[1., 1., 1., 1.],
            [1., 1., 1., 1.],
            [2., 2., 2., 2.],
            [1., 1., 1., 1.]])
```

### تابع numpy.arange()

#### Arrange چیست؟

گاهی اوقات، شما می‌خواهید مقادیری ایجاد کنید که در یک بازه تعریف شده به طور مساوی فاصله داشته باشند. به عنوان مثال، اگر می‌خواهید مقادیر از ۱ تا ۱۰ ایجاد کنید؛ می‌توانید از تابع numpy.arange() استفاده کنید.

```py
# ایجاد لیست با استفاده از range(شروع, توقف, گام)
lst = range(0, 11, 2)
lst
```

```python
range(0, 11, 2)
```

```python
for l in lst:
    print(l)
```

```sh
    0
    2
    4
    6
    8
    10
```

```py
# مشابه range، arange در numpy.arange(شروع, توقف, گام)
whole_numbers = np.arange(0, 20, 1)
whole_numbers```

```sh
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
           17, 18, 19])
```

```py
natural_numbers = np.arange(1, 20, 1)
natural_numbers
```

```py
odd_numbers = np.arange(1, 20, 2)
odd_numbers
```

```sh
    array([ 1,  3,  5,  7,  9, 11, 13, 15, 17, 19])```

```py
even_numbers = np.arange(2, 20, 2)
even_numbers
```

```sh
    array([ 2,  4,  6,  8, 10, 12, 14, 16, 18])
```

### ایجاد دنباله‌ای از اعداد با استفاده از linspace

```py
# numpy.linspace()
# numpy.logspace() در پایتون با مثال
# به عنوان مثال، می‌توان از آن برای ایجاد ۱۰ مقدار با فاصله یکسان از ۱ تا ۵ استفاده کرد.
np.linspace(1.0, 5.0, num=10)```

```sh
    array([1.        , 1.44444444, 1.88888889, 2.33333333, 2.77777778,
           3.22222222, 3.66666667, 4.11111111, 4.55555556, 5.        ])
```

```py
# برای عدم شامل کردن آخرین مقدار در بازه
np.linspace(1.0, 5.0, num=5, endpoint=False)
```

```
array([1. , 1.8, 2.6, 3.4, 4.2])
```

```py
# LogSpace
# LogSpace اعداد با فاصله یکسان را در مقیاس لگاریتمی برمی‌گرداند. Logspace پارامترهای مشابهی با np.linspace دارد.

# سینتکس:

# numpy.logspace(start, stop, num, endpoint)

np.logspace(2, 4.0, num=4)
```

```sh

array([  100.        ,   464.15888336,  2154.43469003, 10000.        ])
```

```py
# برای بررسی اندازه یک آرایه
x = np.array(, dtype=np.complex128)
```

```py
x
```

```sh
    array([1.+0.j, 2.+0.j, 3.+0.j])
```

```py
x.itemsize
```

```sh
16
```

```py
# اندیس‌گذاری و برش آرایه‌های NumPy در پایتون
np_list = np.array([(1,2,3), (4,5,6)])
np_list
```

```sh
    array([,
          ])
```

```py
print('First row: ', np_list)
print('Second row: ', np_list)
```

```sh
    First row:  [1 2 3]
    Second row:  [4 5 6]
```

```py
print('First column: ', np_list[:,0])
print('Second column: ', np_list[:,1])
print('Third column: ', np_list[:,2])
```

```sh
    First column:  [1 4]
    Second column:  [2 5]
    Third column:  [3 6]
```

### توابع آماری NumPy با مثال

NumPy دارای توابع آماری بسیار مفیدی برای یافتن حداقل، حداکثر، میانگین، میانه، صدک، انحراف معیار و واریانس و غیره از عناصر داده شده در آرایه است.
این توابع به شرح زیر توضیح داده شده‌اند -
توابع آماری
Numpy به توابع آماری قدرتمندی مجهز است که در زیر لیست شده‌اند:

-   توابع Numpy
    -   حداقل np.min()
    -   حداکثر np.max()
    -   میانگین np.mean()
    -   میانه np.median()
    -   واریانس
    -   صدک
    -   انحراف معیار np.std()

```python
np_normal_dis = np.random.normal(5, 0.5, 100)
np_normal_dis
## min, max, mean, median, sd
print('min: ', two_dimension_array.min())
print('max: ', two_dimension_array.max())
print('mean: ',two_dimension_array.mean())
# print('median: ', two_dimension_array.median())
print('sd: ', two_dimension_array.std())
```

    min:  1
    max:  55
    mean:  14.777777777777779
    sd:  18.913709183069525

```python
min:  1
max:  55
mean:  14.777777777777779
sd:  18.913709183069525
```

```python
print(two_dimension_array)
print('Column with minimum: ', np.amin(two_dimension_array,axis=0))
print('Column with maximum: ', np.amax(two_dimension_array,axis=0))
print('=== Row ==')
print('Row with minimum: ', np.amin(two_dimension_array,axis=1))
print('Row with maximum: ', np.amax(two_dimension_array,axis=1))
```

    [[ 1  2  3]
     [ 4 55 44]
     [ 7  8  9]]
    Column with minimum:  [1 2 3]
    Column with maximum:  [ 7 55 44]
    === Row ==
    Row with minimum:  [1 4 7]
    Row with maximum:  [ 3 55  9]

### چگونه دنباله‌های تکراری ایجاد کنیم؟

```python
a =

# کل 'a' را دو بار تکرار کن
print('Tile:   ', np.tile(a, 2))

# هر عنصر از 'a' را دو بار تکرار کن
print('Repeat: ', np.repeat(a, 2))
```

    Tile:    [1 2 3 1 2 3]
    Repeat:  [1 1 2 2 3 3]

### چگونه اعداد تصادفی تولید کنیم؟

```python
# یک عدد تصادفی بین [۰,۱)
one_random_num = np.random.random()
one_random_in = np.random
print(one_random_num)
```

    0.6149403282678213

```python
0.4763968133790438
```

    0.4763968133790438

```python
# اعداد تصادفی بین [۰,۱) با شکل ۲,۳
r = np.random.random(size=)
print(r)
```

    [[0.13031737 0.4429537  0.1129527 ]
     [0.76811539 0.88256594 0.6754075 ]]

```python
print(np.random.choice(['a', 'e', 'i', 'o', 'u'], size=10))
```

    ['u' 'o' 'o' 'i' 'e' 'e' 'u' 'o' 'u' 'a']

```python
['i' 'u' 'e' 'o' 'a' 'i' 'e' 'u' 'o' 'i']
```

    ['iueoaieuoi']

```python
## اعداد تصادفی بین [۰, ۱] با شکل ۲, ۲
rand = np.random.rand(2,2)
rand
```

    array([[0.97992598, 0.79642484],
           [0.65263629, 0.55763145]])

```python
rand2 = np.random.randn(2,2)
rand2
```

    array([[ 1.65593322, -0.52326621],
           [ 0.39071179, -2.03649407]])

```python
# اعداد صحیح تصادفی بین [۰, ۱۰) با شکل ۵,۳
rand_int = np.random.randint(0, 10, size=)
rand_int
```

    array([[0, 7, 5],
           [4, 1, 4],
           [3, 5, 3],
           [4, 3, 8],
           [4, 6, 7]])

```py
from scipy import stats
np_normal_dis = np.random.normal(5, 0.5, 1000) # میانگین، انحراف معیار، تعداد نمونه‌ها
np_normal_dis
## min, max, mean, median, sd
print('min: ', np.min(np_normal_dis))
print('max: ', np.max(np_normal_dis))
print('mean: ', np.mean(np_normal_dis))
print('median: ', np.median(np_normal_dis))
print('mode: ', stats.mode(np_normal_dis))
print('sd: ', np.std(np_normal_dis))
```

```sh
    min:  3.557811005458804
    max:  6.876317743643499
    mean:  5.035832048106663
    median:  5.020161980441937
    mode:  ModeResult(mode=array([3.55781101]), count=array())
    sd:  0.489682424165213
```

```python
plt.hist(np_normal_dis, color="grey", bins=21)
plt.show()
```

![png](../test_files/test_121_0.png)

```python
# numpy.dot(): ضرب داخلی در پایتون با استفاده از Numpy
# ضرب داخلی
# Numpy کتابخانه‌ای قدرتمند برای محاسبات ماتریسی است. به عنوان مثال، می‌توانید ضرب داخلی را با np.dot محاسبه کنید.

# سینتکس

# numpy.dot(x, y, out=None)
```

### جبر خطی

1.  ضرب داخلی (Dot Product)

```python
## جبر خطی
### ضرب داخلی: حاصل‌ضرب دو آرایه
f = np.array()
g = np.array()
### 1*4+2*5 + 3*6
np.dot(f, g)  # 23
```

### ضرب ماتریسی NumPy با np.matmul()

```python
### Matmul: ضرب ماتریسی دو آرایه
h = [,]
i = [,]
### 1*5+2*7 = 19
np.matmul(h, i)
```

```sh
    array([,
          ])
```

```py
## دترمینان ماتریس ۲*۲
### 5*8-7*6
np.linalg.det(i)
```

```python
np.linalg.det(i)
```

    -1.999999999999999

```python
Z = np.zeros((8,8))
Z[1::2,::2] = 1
Z[::2,1::2] = 1
```

```python
Z
```

    array([[0., 1., 0., 1., 0., 1., 0., 1.],
           [1., 0., 1., 0., 1., 0., 1., 0.],
           [0., 1., 0., 1., 0., 1., 0., 1.],
           [1., 0., 1., 0., 1., 0., 1., 0.],
           [0., 1., 0., 1., 0., 1., 0., 1.],
           [1., 0., 1., 0., 1., 0., 1., 0.],
           [0., 1., 0., 1., 0., 1., 0., 1.],
           [1., 0., 1., 0., 1., 0., 1., 0.]])

```python
new_list = [ x + 2 for x in range(0, 11)]
```

```python
new_list
```

    [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

```python

```

    [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

```python
np_arr = np.array(range(0, 11))
np_arr + 2
```

array([ 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

ما از معادلات خطی برای کمیت‌هایی که رابطه خطی دارند استفاده می‌کنیم. بیایید مثال زیر را ببینیم:

```python
temp = np.array()
pressure = temp * 2 + 5
pressure
```

array([ 7, 9, 11, 13, 15])

```python
plt.plot(temp,pressure)
plt.xlabel('Temperature in oC')
plt.ylabel('Pressure in atm')
plt.title('Temperature vs Pressure')
plt.xticks(np.arange(0, 6, step=0.5))
plt.show()
```

![png](../test_files/test_141_0.png)

برای رسم توزیع نرمال گوسی با استفاده از numpy. همانطور که در زیر مشاهده می‌کنید، numpy می‌تواند اعداد تصادفی تولید کند. برای ایجاد نمونه تصادفی، به میانگین (mu)، انحراف معیار (sigma) و تعداد نقاط داده نیاز داریم.

```python
mu = 28
sigma = 15
samples = 100000

x = np.random.normal(mu, sigma, samples)
ax = sns.distplot(x);
ax.set(xlabel="x", ylabel='y')
plt.show()
```

![png](../test_files/test_143_0.png)

# خلاصه

به طور خلاصه، تفاوت‌های اصلی با لیست‌های پایتون عبارتند از:

1.  آرایه‌ها از عملیات برداری (vectorized operations) پشتیبانی می‌کنند، در حالی که لیست‌ها این‌طور نیستند.
2.  پس از ایجاد یک آرایه، نمی‌توانید اندازه آن را تغییر دهید. باید یک آرایه جدید ایجاد کنید یا روی آرایه موجود بازنویسی کنید.
3.  هر آرایه یک و فقط یک dtype دارد. همه آیتم‌های آن باید از آن dtype باشند.
4.  یک آرایه numpy معادل، فضای بسیار کمتری نسبت به یک لیست از لیست‌های پایتون اشغال می‌کند.
5.  آرایه‌های numpy از اندیس‌گذاری بولی (boolean indexing) پشتیبانی می‌کنند.

## 💻 تمرین‌ها: روز ۲۴

۱. تمام مثال‌ها را تکرار کنید.

🎉 تبریک! 🎉

[<< روز ۲۳](./23_virtual_environment.md) | [روز ۲۵ >>](./25_pandas.md)
