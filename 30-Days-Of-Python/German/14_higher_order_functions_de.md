<div align="center">
  <h1> 30 Tage Python: Tag 14 - Funktionen höherer Ordnung</h1>
  <a class="header-badge" target="_blank" href="https://www.linkedin.com/in/asabeneh/">
  <img src="https://img.shields.io/badge/style--5eba00.svg?label=LinkedIn&logo=linkedin&style=social">
  </a>
  <a class="header-badge" target="_blank" href="https://twitter.com/Asabeneh">
  <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/asabeneh?style=social">
  </a>

<sub>Autor:
<a href="https://www.linkedin.com/in/asabeneh/" target="_blank">Asabeneh Yetayeh</a><br>
<small> Zweite Edition: Juli 2021</small>
</sub>

</div>

[<< Tag 13](./13_list_comprehension_de.md) | [Tag 15 >>](./15_python_type_errors_de.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Tag 14](#-tag-14)
  - [Funktionen höherer Ordnung](#funktionen-höherer-ordnung)
    - [Funktion als Parameter](#funktion-als-parameter)
    - [Funktion als Rückgabewert](#funktion-als-rückgabewert)
  - [Python Closures (Abschlüsse)](#python-closures-abschlüsse)
  - [Python Decorators (Dekoratoren)](#python-decorators-dekoratoren)
  - [Eingebaute Funktionen höherer Ordnung](#eingebaute-funktionen-höherer-ordnung)
    - [Map-Funktion](#map-funktion)
    - [Filter-Funktion](#filter-funktion)
    - [Reduce-Funktion](#reduce-funktion)
  - [💻 Übungen - Tag 14](#-übungen---tag-14)

# 📘 Tag 14

## Funktionen höherer Ordnung

In Python werden Funktionen als "First Class Citizens" behandelt. Das bedeutet:
- Eine Funktion kann eine oder mehrere Funktionen als Parameter annehmen.
- Eine Funktion kann eine Funktion als Ergebnis zurückgeben.
- Eine Funktion kann modifiziert oder einer Variablen zugewiesen werden.

### Funktion als Parameter

```python
def sum_numbers(nums):
    return sum(nums)

def higher_order_function(f, lst):
    return f(lst)

result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result) # 15
```

### Funktion als Rückgabewert

```python
def square(x): return x ** 2
def cube(x): return x ** 3

def higher_order_function(type):
    if type == 'square':
        return square
    elif type == 'cube':
        return cube

result = higher_order_function('square')
print(result(3)) # 9
```

## Python Closures (Abschlüsse)

Ein Closure erlaubt es einer inneren Funktion, auf den Gültigkeitsbereich (Scope) der äußeren Funktion zuzugreifen, selbst wenn die äußere Funktion bereits fertig ausgeführt wurde.

```python
def add_ten():
    ten = 10
    def add(num):
        return num + ten
    return add

closure_result = add_ten()
print(closure_result(5)) # 15
```

## Python Decorators (Dekoratoren)

Ein Decorator ist ein Design-Pattern, das es ermöglicht, die Funktionalität eines Objekts zu erweitern, ohne dessen Struktur zu verändern. Man nutzt dafür das `@`-Symbol.

```python
def uppercase_decorator(function):
    def wrapper():
        func = function()
        return func.upper()
    return wrapper

@uppercase_decorator
def greeting():
    return 'Willkommen zu Python'

print(greeting()) # WILLKOMMEN ZU PYTHON
```

## Eingebaute Funktionen höherer Ordnung

### Map-Funktion
Wendet eine Funktion auf jedes Element einer Sequenz an.
```python
numbers = [1, 2, 3, 4]
squared = map(lambda x: x**2, numbers)
print(list(squared)) # [1, 4, 9, 16]
```

### Filter-Funktion
Filtert Elemente heraus, die eine bestimmte Bedingung (True/False) erfüllen.
```python
numbers = [1, 2, 3, 4, 5]
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens)) # [2, 4]
```

### Reduce-Funktion
Reduziert eine Sequenz auf einen einzigen Wert (muss aus `functools` importiert werden).
```python
from functools import reduce
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, numbers)
print(total) # 15
```

---

## 💻 Übungen - Tag 14

### Level 1
1. Erkläre den Unterschied zwischen `map`, `filter` und `reduce`.
2. Erkläre den Unterschied zwischen Higher Order Function, Closure und Decorator.
3. Gib alle Länder, Namen und Zahlen aus den gegebenen Listen mit einer Schleife aus.

### Level 2
1. Nutze `map`, um alle Länder in der Liste in Großbuchstaben umzuwandeln.
2. Nutze `map`, um alle Zahlen zu quadrieren.
3. Nutze `filter`, um Länder zu filtern, die das Wort "land" enthalten.
4. Nutze `filter`, um Länder mit genau 6 Zeichen zu finden.
5. Schreibe eine Funktion `get_string_lists`, die nur die String-Elemente aus einer gemischten Liste filtert.
6. Nutze `reduce`, um alle Zahlen zu summieren.
7. Nutze `reduce`, um alle Länder zu einem Satz zu verbinden.

### Level 3
1. Nutze die `countries_data.py`:
   - Sortiere Länder nach Name, Hauptstadt und Bevölkerung.
   - Finde die 10 am häufigsten gesprochenen Sprachen.
   - Finde die 10 bevölkerungsreichsten Länder.

🎉 HERZLICEN GLÜCKWUNSCH! 🎉

[<< Tag 13](./13_list_comprehension_de.md) | [Tag 15 >>](./15_python_type_errors_de.md)
