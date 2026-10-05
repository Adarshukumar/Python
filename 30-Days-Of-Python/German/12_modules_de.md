<div align="center">
  <h1> 30 Tage Python: Tag 12 - Module (Modules)</h1>
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

[<< Tag 11](./11_functions_de.md) | [Tag 13 >>](./13_list_comprehension_de.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Tag 12](#-tag-12)
  - [Module](#module)
    - [Was ist ein Module](#was-ist-ein-module)
    - [Ein Modul erstellen](#ein-modul-erstellen)
    - [Ein Modul importieren](#ein-modul-importieren)
    - [Funktionen gezielt importieren](#funktionen-gezielt-importieren)
    - [Importieren und Umbenennen (As)](#importieren-und-umbenennen-as)
  - [Eingebaute Module](#eingebaute-module)
    - [OS Modul](#os-modul)
    - [Sys Modul](#sys-modul)
    - [Statistics Modul](#statistics-modul)
    - [Math Modul](#math-modul)
    - [String Modul](#string-modul)
    - [Random Modul](#random-modul)
  - [💻 Übungen - Tag 12](#-übungen---tag-12)

# 📘 Tag 12

## Module

### Was ist ein Modul

Ein Modul ist eine Datei, die Code oder Funktionen enthält, die in eine Anwendung eingebunden werden können. Ein Modul kann eine einzelne Variable, eine Funktion oder eine große Codebasis sein.

### Ein Modul erstellen

Um ein Modul zu erstellen, schreiben wir unseren Code in ein Python-Skript und speichern es als `.py` Datei (z. B. `mymodule.py`).

```python
# mymodule.py
def generate_full_name(firstname, lastname):
    return firstname + ' ' + lastname
```

### Ein Modul importieren

Wir nutzen das Schlüsselwort `import`, gefolgt vom Dateinamen (ohne .py).

```python
# main.py
import mymodule
print(mymodule.generate_full_name('Asabeneh', 'Yetayeh'))
```

### Funktionen gezielt importieren

Man kann auch nur bestimmte Teile eines Moduls importieren:
```python
from mymodule import generate_full_name, person
```

### Importieren und Umbenennen (As)

Um Namenskollisionen zu vermeiden oder Schreibarbeit zu sparen:
```python
import mymodule as mm
from math import pi as PI
```

## Eingebaute Module

Python wird mit einer "Batteries Included"-Philosophie ausgeliefert, was bedeutet, dass viele nützliche Module bereits eingebaut sind.

### OS Modul
Ermöglicht Interaktionen mit dem Betriebssystem (Ordner erstellen, Verzeichnisse wechseln, etc.).
```python
import os
os.mkdir('neuer_ordner')
print(os.getcwd()) # Aktuelles Verzeichnis
```

### Sys Modul
Bietet Funktionen und Variablen, um das Python-Laufzeitsystem zu manipulieren (z. B. Kommandozeilenargumente abrufen).
```python
import sys
print(sys.argv) # Liste der Argumente
```

### Statistics Modul
Mathematische Statistik für numerische Daten (`mean`, `median`, `mode`, `stdev`).

### Math Modul
Enthält mathematische Konstanten und Funktionen (`pi`, `sqrt`, `pow`, `floor`, `ceil`).
```python
import math
print(math.sqrt(16)) # 4.0
```

### Random Modul
Erzeugt Zufallszahlen.
```python
from random import random, randint
print(random()) # Zufallszahl zwischen 0 und 1
print(randint(5, 20)) # Zufällige Ganzzahl zwischen 5 und 20
```

---

## 💻 Übungen - Tag 12

### Level 1
1. Schreibe eine Funktion, die eine zufällige 6-stellige `user_id` generiert (z. B. '1ee33d').
2. Erstelle eine Funktion `user_id_gen_by_user`, die via `input()` nach der Anzahl der Zeichen und der Anzahl der zu generierenden IDs fragt.
3. Schreibe `rgb_color_gen`, die eine zufällige RGB-Farbe im Format `rgb(125,244,255)` generiert.

### Level 2
1. Erstelle eine Funktion `list_of_hexa_colors`, die eine Liste von Hexadezimal-Farben zurückgibt (z. B. #a3e12f).
2. Erstelle `list_of_rgb_colors` für RGB-Listen.
3. Schreibe `generate_colors(type, n)`, die entweder Hex- oder RGB-Farben in der gewünschten Anzahl generiert.

### Level 3
1. Erstelle `shuffle_list`, die eine Liste zufällig durchmischt.
2. Schreibe eine Funktion, die 7 einzigartige Zufallszahlen im Bereich 0-9 zurückgibt.

🎉 HERZLICEN GLÜCKWUNSCH! 🎉

[<< Tag 11](./11_functions_de.md) | [Tag 13 >>](./13_list_comprehension_de.md)
