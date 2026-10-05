<div align="center">
  <h1> 30 Tage Python: Tag 17 - Ausnahmebehandlung & Packing/Unpacking</h1>
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

[<< Tag 16](./16_python_datetime_de.md) | [Tag 18 >>](./18_regular_expressions_de.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Tag 17](#-tag-17)
  - [Ausnahmebehandlung (Exception Handling)](#ausnahmebehandlung-exception-handling)
  - [Packing und Unpacking von Argumenten](#packing-und-unpacking-von-argumenten)
    - [Unpacking (Entpacken)](#unpacking-entpacken)
    - [Packing (Verpacken)](#packing-verpacken)
  - [Enumerate](#enumerate)
  - [Zip](#zip)
  - [💻 Übungen - Tag 17](#-übungen---tag-17)

# 📘 Tag 17

## Ausnahmebehandlung (Exception Handling)

Python nutzt `try` und `except`, um Fehler elegant abzufangen. Ein Programm sollte bei einem Fehler nicht einfach abstürzen ("crash"), sondern kontrolliert reagieren ("graceful exit"). Das macht Anwendungen robuster gegen falsche Benutzereingaben oder externe Probleme (z. B. fehlende Dateien).

```python
# Syntax
try:
    code_der_einen_fehler_verursachen_koennte
except:
    code_der_ausgefuehrt_wird_wenn_ein_fehler_auftritt
```

**Beispiel mit spezifischen Fehlern:**
```python
try:
    name = input('Name: ')
    year = int(input('Geburtsjahr: '))
    age = 2021 - year
    print(f'Hallo {name}, du bist {age} Jahre alt.')
except ValueError:
    print('Bitte gib eine gültige Zahl für das Jahr ein!')
except Exception as e:
    print(f'Ein unerwarteter Fehler ist aufgetreten: {e}')
finally:
    print('Dieser Teil wird IMMER ausgeführt (z.B. zum Aufräumen).')
```

## Packing und Unpacking von Argumenten

In Python nutzen wir Symbole, um Sammlungen in einzelne Argumente zu zerlegen oder umgekehrt.

- `*` wird für **Listen/Tupel** verwendet.
- `**` wird für **Dictionaries** verwendet.

### Unpacking (Entpacken)

Wenn eine Funktion einzelne Werte erwartet, du aber eine Liste hast:
```python
def add(a, b, c):
    return a + b + c

nums = [1, 2, 3]
# print(add(nums)) # Fehler!
print(add(*nums)) # Funktioniert: 6
```

### Packing (Verpacken)

Wenn du nicht weißt, wie viele Argumente übergeben werden, kannst du sie "einpacken":
```python
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4, 5)) # 15
```

## Enumerate

Wenn du beim Iterieren durch eine Liste auch den **Index** (die Position) wissen möchtest:
```python
countries = ['Finnland', 'Schweden', 'Norwegen']
for index, country in enumerate(countries):
    print(f'{index}. {country}')
# 0. Finnland, 1. Schweden, ...
```

## Zip

Mit `zip` kannst du mehrere Listen gleichzeitig in einer Schleife durchlaufen:
```python
fruits = ['Banane', 'Orange']
prices = [1.2, 0.8]

for fruit, price in zip(fruits, prices):
    print(f'{fruit} kostet {price}€')
```

---

## 💻 Übungen - Tag 17

1. Gegeben ist die Liste: `names = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland', 'Estonia', 'Russia']`.
   Entpacke die ersten fünf Länder in eine Variable `nordic_countries`. Speichere 'Estonia' in `es` und 'Russia' in `ru`.

🎉 HERZLICEN GLÜCKWUNSCH! 🎉

[<< Tag 16](./16_python_datetime_de.md) | [Tag 18 >>](./18_regular_expressions_de.md)
