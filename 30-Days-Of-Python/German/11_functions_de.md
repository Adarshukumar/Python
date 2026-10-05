<div align="center">
  <h1> 30 Tage Python: Tag 11 - Funktionen (Functions)</h1>
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

[<< Tag 10](./10_loops_de.md) | [Tag 12 >>](./12_modules_de.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Tag 11](#-tag-11)
  - [Funktionen](#funktionen)
    - [Eine Funktion definieren](#eine-funktion-definieren)
    - [Funktionen deklarieren und aufrufen](#funktionen-deklarieren-und-aufrufen)
    - [Funktionen ohne Parameter](#funktionen-ohne-parameter)
    - [Funktionen mit Rückgabewerten (Return)](#funktionen-mit-rückgabewerten-return)
    - [Funktionen mit Parametern](#funktionen-mit-parametern)
    - [Standardparameter](#standardparameter)
    - [Variable Anzahl an Argumenten (*args & **kwargs)](#variable-anzahl-an-argumenten-args--kwargs)
    - [Funktion als Parameter](#funktion-als-parameter)
  - [💻 Übungen - Tag 11](#-übungen---tag-11)

# 📘 Tag 11

## Funktionen

Bisher haben wir viele eingebaute Funktionen genutzt. Jetzt lernen wir, wie wir unsere eigenen Funktionen erstellen. Eine Funktion ist ein wiederverwendbarer Codeblock, der eine bestimmte Aufgabe erfüllt.

### Eine Funktion definieren

Python nutzt das Schlüsselwort `def`, um eine Funktion zu deklarieren. Der Codeblock innerhalb der Funktion wird nur ausgeführt, wenn die Funktion **aufgerufen** (invoked) wird.

```python
# Syntax
def funktions_name():
    code
```

### Funktionen deklarieren und aufrufen

```python
def generate_full_name():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    print(first_name + ' ' + last_name)

generate_full_name() # Aufruf der Funktion
```

### Funktionen mit Rückgabewerten (Return)

Mit `return` gibt eine Funktion ein Ergebnis an den Aufrufer zurück. Ohne `return` gibt die Funktion standardmäßig `None` zurück.

```python
def add_two_numbers():
    return 2 + 3

result = add_two_numbers()
print(result) # 5
```

### Funktionen mit Parametern

Parameter ermöglichen es uns, Daten in die Funktion einzuspeisen.

- **Einzelner Parameter:**
```python
def greetings(name):
    return f'{name}, willkommen zu Python!'

print(greetings('Asabeneh'))
```

- **Mehrere Parameter:**
```python
def calculate_age(current_year, birth_year):
    return current_year - birth_year

print(calculate_age(2021, 1990))
```

### Standardparameter

Wir können Parametern Standardwerte zuweisen. Diese werden genutzt, wenn beim Aufruf kein Argument übergeben wird.
```python
def weight_of_object(mass, gravity = 9.81):
    return mass * gravity

print(weight_of_object(100)) # Nutzt 9.81
print(weight_of_object(100, 1.62)) # Nutzt Mond-Gravitation
```

### Variable Anzahl an Argumenten (*args & **kwargs)

- `*args`: Wenn du nicht weißt, wie viele Argumente übergeben werden, nutzt du `*args`. Sie werden als **Tupel** behandelt.
- `**kwargs`: Für eine variable Anzahl an **benannten Argumenten**. Sie werden als **Dictionary** behandelt.

```python
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num
    return total

print(sum_all_nums(1, 2, 3, 4)) # 10
```

### Funktion als Parameter

In Python sind Funktionen "First-Class Citizens", was bedeutet, dass man sie wie Variablen behandeln und an andere Funktionen übergeben kann.

---

## 💻 Übungen - Tag 11

### Level 1
1. Deklariere eine Funktion `add_two_numbers`.
2. Berechne die Fläche eines Kreises (`area_of_circle`).
3. Schreibe `add_all_nums`, die eine beliebige Anzahl an Zahlen summiert. Prüfe, ob die Eingaben Zahlen sind.
4. Wandle Celsius in Fahrenheit um.
5. Schreibe `check_season`, die basierend auf einem Monat die Jahreszeit zurückgibt.
6. Berechne die Steigung einer linearen Gleichung.
7. Löse eine quadratische Gleichung (`solve_quadratic_eqn`).
8. `print_list`: Gibt jedes Element einer Liste aus.
9. `reverse_list`: Gibt eine Liste umgekehrt zurück (nutze Schleifen).
10. `capitalize_list_items`: Schreibt alle Elemente einer Liste groß.
11. `add_item` / `remove_item`: Fügt ein Element am Ende hinzu bzw. entfernt es.
12. Summiere alle Zahlen in einem Bereich (`sum_of_numbers`).

### Level 2
1. `evens_and_odds`: Zählt die Anzahl der geraden und ungeraden Zahlen in einem Bereich.
2. Berechne die Fakultät (`factorial`) einer Zahl.
3. `is_empty`: Prüft, ob ein Parameter leer ist.
4. Berechne statistische Werte für eine Liste: Durchschnitt (Mean), Median, Modus, Varianz, Standardabweichung.
5. `greet`: Begrüßt einen Nutzer oder einen "Gast" als Standard.

### Level 3
1. `is_prime`: Prüft, ob eine Zahl eine Primzahl ist.
2. Prüfe, ob alle Elemente einer Liste einzigartig sind.
3. Prüfe, ob alle Elemente einer Liste denselben Datentyp haben.
4. Finde die meistgesprochenen Sprachen und bevölkerungsreichsten Länder aus der `countries-data.py`.

🎉 HERZLICEN GLÜCKWUNSCH! 🎉

[<< Tag 10](./10_loops_de.md) | [Tag 12 >>](./12_modules_de.md)
