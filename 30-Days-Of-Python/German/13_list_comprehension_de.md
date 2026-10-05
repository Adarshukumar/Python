<div align="center">
  <h1> 30 Tage Python: Tag 13 - List Comprehension & Lambda-Funktionen</h1>
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

[<< Tag 12](./12_modules_de.md) | [Tag 14 >>](./14_higher_order_functions_de.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Tag 13](#-tag-13)
  - [List Comprehension (Listen-Abstraktion)](#list-comprehension-listen-abstraktion)
  - [Lambda-Funktionen (Anonyme Funktionen)](#lambda-funktionen-anonyme-funktionen)
    - [Eine Lambda-Funktion erstellen](#eine-lambda-funktion-erstellen)
    - [Lambda innerhalb anderer Funktionen](#lambda-innerhalb-anderer-funktionen)
  - [💻 Übungen - Tag 13](#-übungen---tag-13)

# 📘 Tag 13

## List Comprehension (Listen-Abstraktion)

List Comprehension ist ein kompakter Weg, um in Python eine neue Liste aus einer bestehenden Sequenz zu erstellen. Es ist kürzer und oft deutlich schneller als eine herkömmliche `for`-Schleife.

```python
# Syntax
[ausdruck for element in iterierbar if bedingung]
```

**Beispiel 1: String in eine Liste von Zeichen umwandeln**
```python
language = 'Python'
# Der klassische Weg:
lst = list(language)
# Mit List Comprehension:
lst = [i for i in language]
print(lst) # ['P', 'y', 't', 'h', 'o', 'n']
```

**Beispiel 2: Zahlen und mathematische Operationen**
```python
# Zahlen von 0 bis 10 generieren
numbers = [i for i in range(11)]
# Quadrate berechnen
squares = [i * i for i in range(11)] # [0, 1, 4, 9, 16, ...]
# Liste von Tupeln erstellen (Zahl, Quadrat)
num_tuples = [(i, i * i) for i in range(11)]
```

**Beispiel 3: Mit Bedingungen (if)**
```python
# Nur gerade Zahlen filtern
evens = [i for i in range(21) if i % 2 == 0]
```

## Lambda-Funktionen (Anonyme Funktionen)

Eine Lambda-Funktion ist eine kleine, anonyme Funktion ohne Namen. Sie kann beliebig viele Argumente haben, aber nur **einen Ausdruck**. Sie ähnelt den anonymen Funktionen (Arrow Functions) in JavaScript.

### Eine Lambda-Funktion erstellen

Wir nutzen das Schlüsselwort `lambda`, gefolgt von Parametern, einem Doppelpunkt und dem Ausdruck.

```python
# Syntax
x = lambda param1, param2: param1 + param2
print(x(5, 3)) # 8
```

**Beispiel:**
```python
# Normale Funktion
def add(a, b): return a + b

# Als Lambda
add_lambda = lambda a, b: a + b
print(add_lambda(2, 3)) # 5
```

### Lambda innerhalb anderer Funktionen

Lambdas sind besonders nützlich, wenn sie von einer anderen Funktion zurückgegeben werden.

```python
def power(x):
    return lambda n : x ** n

cube = power(2)(3) # 2 hoch 3 = 8
```

---

## 💻 Übungen - Tag 13

1. Filtere nur negative Zahlen und die Null aus einer Liste mit List Comprehension:
   `numbers = [-4, -3, -2, -1, 0, 2, 4, 6]`
2. "Flache" eine verschachtelte Liste (`list of lists`) in eine eindimensionale Liste ab:
   `list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]` -> `[1, 2, 3, 4, 5, 6, 7, 8, 9]`
3. Erstelle mit List Comprehension eine Liste von Tupeln (Zahl, 1, Zahl, Quadrat, Kubik, etc.) – siehe Original-Tabelle.
4. Wandle eine Liste von Ländern (mit Hauptstädten) in ein neues Format um (Land, Kürzel, Stadt in Großbuchstaben).
5. Wandle eine Liste von Ländern in eine Liste von Dictionaries um (Keys: 'country', 'city').
6. Verbinde Vornamen und Nachnamen aus einer Liste von Listen zu einer Liste von kompletten Namen (Strings).
7. Schreibe eine Lambda-Funktion, die die Steigung oder den y-Achsenabschnitt einer linearen Funktion berechnet.

🎉 HERZLICEN GLÜCKWUNSCH! 🎉

[<< Tag 12](./12_modules_de.md) | [Tag 14 >>](./14_higher_order_functions_de.md)
