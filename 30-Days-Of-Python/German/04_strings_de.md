<div align="center">
  <h1> 30 Tage Python: Tag 4 - Zeichenketten (Strings)</h1>
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

[<< Tag 3](./03_operators_de.md) | [Tag 5 >>](./05_lists_de.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [Tag 4](#tag-4)
  - [Zeichenketten (Strings)](#zeichenketten-strings)
    - [Einen String erstellen](#einen-string-erstellen)
    - [String-Konkatenation (Verknüpfung)](#string-konkatenation-verknüpfung)
    - [Escape-Sequenzen in Strings](#escape-sequenzen-in-strings)
    - [String-Formatierung](#string-formatierung)
      - [Alter Stil (% Operator)](#alter-stil--operator)
      - [Neuer Stil (str.format)](#neuer-stil-strformat)
      - [String Interpolation / f-Strings (Python 3.6+)](#string-interpolation--f-strings-python-36)
    - [Python Strings als Sequenzen von Zeichen](#python-strings-als-sequenzen-von-zeichen)
      - [Zeichen entpacken (Unpacking)](#zeichen-entpacken-unpacking)
      - [Zugriff auf Zeichen per Index](#zugriff-auf-zeichen-per-index)
      - [Slicing (Teilstücke extrahieren)](#slicing-teilstücke-extrahieren)
      - [Einen String umkehren](#einen-string-umkehren)
      - [Zeichen beim Slicing überspringen](#zeichen-beim-slicing-überspringen)
    - [String-Methoden](#string-methoden)
  - [💻 Übungen - Tag 4](#-übungen---tag-4)

# Tag 4

## Zeichenketten (Strings)

Text wird in Python als Datentyp "String" bezeichnet. Jede Information, die als Text geschrieben wird, ist ein String. Alles, was in einfachen ('), doppelten (") oder dreifachen (""") Anführungszeichen steht, wird als String behandelt. Es gibt viele Methoden und Funktionen, um mit Strings zu arbeiten. Mit `len()` kannst du die Länge eines Strings ermitteln.

### Einen String erstellen

```python
letter = 'P'                # Ein String kann ein einzelnes Zeichen sein...
greeting = 'Hallo, Welt!'   # ...oder ein ganzer Satz.
sentence = "Ich hoffe, dir macht die 30 Tage Python Herausforderung Spaß"
```

Mehrzeilige Strings werden mit dreifachen Anführungszeichen erstellt:
```python
multiline_string = '''Ich bin Lehrer und liebe das Unterrichten.
Es gibt nichts Schöneres, als Menschen zu helfen, ihr Potenzial zu entfalten.
Deshalb habe ich 30 Tage Python erstellt.'''
```

### String-Konkatenation (Verknüpfung)

Du kannst Strings miteinander verbinden. Das nennt man Konkatenation.
```python
first_name = 'Asabeneh'
last_name = 'Yetayeh'
full_name = first_name + ' ' + last_name
print(full_name) # Asabeneh Yetayeh
```

### Escape-Sequenzen in Strings

Ein Backslash (`\`) gefolgt von einem Zeichen ist eine Escape-Sequenz:
- `\n`: Neue Zeile
- `\t`: Tabulator (8 Leerzeichen)
- `\\`: Backslash selbst
- `\'`: Einfaches Anführungszeichen
- `\"`: Doppeltes Anführungszeichen

### String-Formatierung

#### Alter Stil (% Operator)
Hierbei werden Platzhalter wie `%s` (String), `%d` (Integer) oder `%f` (Float) genutzt.
```python
first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formatted_string = 'Ich bin %s %s. Ich unterrichte %s' %(first_name, last_name, language)
```

#### Neuer Stil (str.format)
Eingeführt mit Python 3. Nutzt geschweifte Klammern `{}`.
```python
formatted_string = 'Ich bin {} {}. Ich unterrichte {}'.format(first_name, last_name, language)
```

#### String Interpolation / f-Strings (Python 3.6+)
Der modernste und am einfachsten zu lesende Weg. Strings beginnen mit einem `f`.
```python
a, b = 4, 3
print(f'{a} + {b} = {a + b}') # 4 + 3 = 7
```

### Python Strings als Sequenzen von Zeichen

Strings sind geordnete Sequenzen. Du kannst auf einzelne Zeichen zugreifen.

#### Zugriff per Index
In der Programmierung beginnt das Zählen bei **Null**.
```python
language = 'Python'
first_letter = language[0] # P
last_letter = language[-1] # n (negativer Index zählt von hinten)
```

#### Slicing (Teilstücke)
Du kannst Bereiche eines Strings extrahieren: `string[start:stop:step]`.
```python
language = 'Python'
first_three = language[0:3] # Pyt (bis Index 3, aber ohne 3)
reverse_string = language[::-1] # nohtyP (String umdrehen)
```

### String-Methoden

Es gibt unzählige Methoden. Hier die wichtigsten:
- `capitalize()`: Erster Buchstabe groß.
- `upper()`: Alles groß.
- `lower()`: Alles klein.
- `count(substring)`: Zählt Vorkommen eines Teilstrings.
- `endswith(substring)`: Prüft, ob der String so endet.
- `find(substring)`: Findet den ersten Index des Teilstrings (sonst -1).
- `replace(old, new)`: Ersetzt Textteile.
- `split(separator)`: Teilt den String in eine Liste auf.
- `strip()`: Entfernt Leerzeichen am Anfang und Ende.
- `join(list)`: Verbindet Listenelemente zu einem String.

---

## 💻 Übungen - Tag 4

1. Verbinde 'Thirty', 'Days', 'Of', 'Python' zu einem einzigen String 'Thirty Days Of Python'.
2. Verbinde 'Coding', 'For', 'All' zu 'Coding For All'.
3. Deklariere eine Variable `company` mit dem Wert "Coding For All".
4. Gib die Variable `company` aus.
5. Gib die Länge des Strings `company` aus.
6. Wandle alle Zeichen in Großbuchstaben um (`upper()`).
7. Wandle alle Zeichen in Kleinbuchstaben um (`lower()`).
8. Nutze `capitalize()`, `title()`, `swapcase()`, um "Coding For All" zu formatieren.
9. Schneide das erste Wort von "Coding For All" ab.
10. Prüfe, ob "Coding For All" das Wort "Coding" enthält (nutze `index` oder `find`).
11. Ersetze 'Coding' in 'Coding For All' durch 'Python'.
12. Ändere "Python for Everyone" zu "Python for All" mit `replace`.
13. Teile 'Coding For All' an den Leerzeichen auf (`split`).
14. Teile "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" an den Kommas auf.
15. Welches Zeichen ist bei Index 0 in "Coding For All"?
16. Was ist der letzte Index in "Coding For All"?
17. Welches Zeichen ist bei Index 10?
18. Erstelle ein Akronym für 'Python For Everyone' (PFE).
19. Erstelle ein Akronym für 'Coding For All' (CFA).
20. Nutze `index`, um das erste Vorkommen von 'C' in 'Coding For All' zu finden.
21. Nutze `index`, um das erste Vorkommen von 'F' zu finden.
22. Nutze `rfind`, um das letzte Vorkommen von 'l' in 'Coding For All People' zu finden.
23. Finde das erste Vorkommen von 'because' in: 'You cannot end a sentence with because because because is a conjunction'.
24. Finde das letzte Vorkommen von 'because'.
25. Schneide den Teil 'because because because' aus dem Satz heraus.
26. Prüfe, ob 'Coding For All' mit 'Coding' beginnt.
27. Prüfe, ob es mit 'coding' endet.
28. Entferne führende und abschließende Leerzeichen von '&nbsp;&nbsp; Coding For All &nbsp;&nbsp;&nbsp; &nbsp;'.
29. Welche Variable gibt bei `isidentifier()` True zurück: `30DaysOfPython` oder `thirty_days_of_python`?
30. Verbinde die Liste `['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']` mit einem `# ` zu einem String.
31. Nutze `\n`, um zwei Sätze in verschiedenen Zeilen auszugeben.
32. Nutze `\t`, um eine Tabelle mit Name, Alter, Land und Stadt zu erstellen.
33. Nutze String-Formatierung, um die Fläche eines Kreises mit Radius 10 anzuzeigen.
34. Erstelle die folgende Ausgabe mit f-strings:
```
8 + 6 = 14
8 - 6 = 2
...
8 ** 6 = 262144
```

🎉 HERZLICHEN GLÜCKWUNSCH! 🎉

[<< Tag 3](./03_operators_de.md) | [Tag 5 >>](./05_lists_de.md)
