<div align="center">
  <h1> 30 Tage Python: Tag 18 - Reguläre Ausdrücke (Regular Expressions)</h1>
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

[<< Tag 17](./17_exception_handling_de.md) | [Tag 19 >>](./19_file_handling_de.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Tag 18](#-tag-18)
  - [Reguläre Ausdrücke](#reguläre-ausdrücke)
    - [Das re-Modul](#das-re-modul)
    - [Methoden im re-Modul](#methoden-im-re-modul)
      - [Match](#match)
      - [Search](#search)
      - [Findall](#findall)
      - [Sub (Ersetzen)](#sub-ersetzen)
      - [Split](#split)
    - [Regex-Muster schreiben](#regex-muster-schreiben)
  - [💻 Übungen - Tag 18](#-übungen---tag-18)

# 📘 Tag 18

## Reguläre Ausdrücke

Ein regulärer Ausdruck (Regular Expression oder kurz **RegEx**) ist eine spezielle Zeichenfolge, die hilft, Muster in Texten zu finden. RegEx wird verwendet, um Daten zu validieren, zu suchen oder zu ersetzen. In Python nutzen wir dafür das eingebaute Modul `re`.

### Das re-Modul

Zuerst müssen wir das Modul importieren:
```python
import re
```

### Methoden im re-Modul

- `re.match()`: Sucht **nur am Anfang** der ersten Zeile.
- `re.search()`: Sucht im **gesamten String** nach dem ersten Vorkommen.
- `re.findall()`: Gibt eine **Liste aller Treffer** zurück.
- `re.split()`: Teilt den String an den Stellen, an denen das Muster passt.
- `re.sub()`: Ersetzt einen oder mehrere Treffer durch einen neuen Text.

#### Match
```python
import re
txt = 'Ich liebe es, Python zu lernen'
match = re.match('Ich liebe', txt, re.I) # re.I ignoriert Groß/Kleinschreibung
print(match) # <re.Match object; span=(0, 9), match='Ich liebe'>
```

#### Search
```python
match = re.search('Python', txt, re.I)
print(match.span()) # (14, 20) - Start- und Endposition
```

#### Findall
```python
txt = 'Python ist toll. Ich mag Python.'
matches = re.findall('Python', txt)
print(matches) # ['Python', 'Python']
```

#### Sub (Ersetzen)
```python
txt = 'Ich liebe %Python% und %Java%.'
clean_txt = re.sub('%', '', txt)
print(clean_txt) # Ich liebe Python und Java.
```

### Regex-Muster schreiben

Um ein Regex-Muster zu definieren, nutzen wir in Python "Raw Strings" mit einem vorangestellten `r`, z. B. `r'apple'`.

**Wichtige Meta-Charaktere:**
- `[]`: Ein Zeichensatz (z. B. `[a-z]` für alle Kleinbuchstaben).
- `\`: Maskiert Sonderzeichen (z. B. `\d` für Ziffern, `\D` für Nicht-Ziffern).
- `.`: Jedes Zeichen außer Zeilenumbruch.
- `^`: Beginnt mit (z. B. `^Hallo`).
- `$`: Endet mit (z. B. `Welt$`).
- `*`: Null oder mehr Male.
- `+`: Ein oder mehr Male.
- `?`: Null oder ein Mal (optional).
- `{n}`: Genau n Mal.
- `|`: Entweder oder (z. B. `Apfel|Birne`).
- `()`: Gruppierung.

---

## 💻 Übungen - Tag 18

### Level 1
1. Was ist das häufigste Wort im folgenden Absatz? (Nutze Regex zur Reinigung).
   `paragraph = 'I love teaching. If you do not love teaching what else can you love...'`
2. Extrahiere alle Zahlen aus folgendem Text und berechne die Distanz zwischen den beiden am weitesten entfernten Punkten auf einer x-Achse:
   `'Die Positionen der Teilchen sind -12, -4, -3, -1, 0, 4 und 8.'`

### Level 2
1. Schreibe ein Muster, das prüft, ob ein String ein gültiger Python-Variablenname ist (keine Zahlen am Anfang, nur Alphanumerik und Unterstriche).

### Level 3
1. Reinige den folgenden Text von Sonderzeichen (`%`, `$`, `@`, `&`, `#`) und finde danach die drei häufigsten Wörter:
   `sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;...'''`

🎉 HERZLICEN GLÜCKWUNSCH! 🎉

[<< Tag 17](./17_exception_handling_de.md) | [Tag 19 >>](./19_file_handling_de.md)
