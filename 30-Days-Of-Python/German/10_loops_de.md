<div align="center">
  <h1> 30 Tage Python: Tag 10 - Schleifen (Loops)</h1>
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

[<< Tag 9](./09_conditionals_de.md) | [Tag 11 >>](./11_functions_de.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Tag 10](#-tag-10)
  - [Schleifen (Loops)](#schleifen-loops)
    - [While-Schleife](#while-schleife)
    - [Break und Continue](#break-und-continue)
    - [For-Schleife](#for-schleife)
    - [Die Range-Funktion](#die-range-funktion)
    - [Verschachtelte Schleifen](#verschachtelte-schleifen)
    - [For-Else und Pass](#for-else-und-pass)
  - [💻 Übungen - Tag 10](#-übungen---tag-10)

# 📘 Tag 10

## Schleifen (Loops)

Das Leben ist voll von Routinen. Auch in der Programmierung müssen wir oft Aufgaben wiederholen. Um solche repetitiven Aufgaben effizient zu bewältigen, nutzen wir Schleifen. Python bietet zwei Hauptarten von Schleifen:

1. **while** Schleife
2. **for** Schleife

### While-Schleife

Das Schlüsselwort `while` wird verwendet, um einen Codeblock so lange zu wiederholen, wie eine bestimmte Bedingung wahr (`True`) ist.

```python
# Syntax
while bedingung:
    code
```

**Beispiel:**
```python
count = 0
while count < 5:
    print(count)
    count = count + 1
# Gibt 0 bis 4 aus
```

### Break und Continue

- **Break:** Bricht die Schleife sofort ab.
- **Continue:** Überspringt den aktuellen Durchlauf und macht mit dem nächsten weiter.

```python
count = 0
while count < 5:
    if count == 3:
        break # Stoppt bei 3
    print(count)
    count += 1
```

### For-Schleife

Das Schlüsselwort `for` wird verwendet, um über eine Sequenz (Liste, Tupel, Dictionary, Set oder String) zu iterieren.

- **Über eine Liste:**
```python
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:
    print(number)
```

- **Über ein Dictionary:**
Iterieren über ein Dictionary gibt standardmäßig die **Schlüssel** zurück. Mit `.items()` erhält man Schlüssel und Werte.
```python
person = {'name': 'Asabeneh', 'country': 'Finnland'}
for key, value in person.items():
    print(key, value)
```

### Die Range-Funktion

Die Funktion `range(start, stop, step)` erzeugt eine Sequenz von Zahlen. Standardmäßig startet sie bei 0.
```python
for i in range(11):
    print(i) # 0 bis 10
```

### Verschachtelte Schleifen (Nested Loops)

Man kann Schleifen innerhalb anderer Schleifen verwenden. Dies ist nützlich für komplexe Datenstrukturen oder Muster.

### For-Else und Pass

- **For-Else:** Der `else`-Block wird ausgeführt, wenn die Schleife regulär beendet wurde (ohne `break`).
- **Pass:** Ein Platzhalter, wenn syntaktisch ein Codeblock erforderlich ist, man aber noch keinen Code schreiben möchte.

---

## 💻 Übungen - Tag 10

### Level 1
1. Iteriere von 0 bis 10 mit einer `for`-Schleife und dann mit einer `while`-Schleife.
2. Iteriere von 10 bis 0.
3. Schreibe eine Schleife, die folgendes Muster ausgibt:
   ```
   #
   ##
   ###
   ####
   #####
   ######
   #######
   ```
4. Nutze verschachtelte Schleifen, um ein 8x8 Gitter aus `#` zu erzeugen.
5. Gib das Einmaleins (0 bis 10) in folgendem Format aus: `0 x 0 = 0`, `1 x 1 = 1`, etc.
6. Iteriere durch die Liste `['Python', 'Numpy', 'Pandas', 'Django', 'Flask']` und gib die Elemente aus.
7. Gib alle geraden Zahlen von 0 bis 100 aus.

### Level 2
1. Berechne die Summe aller Zahlen von 0 bis 100.
2. Berechne separat die Summe aller geraden und aller ungeraden Zahlen von 0 bis 100.

### Level 3
1. Gehe zur `countries.py` Datei und gib alle Länder aus, die das Wort "land" enthalten.
2. Kehre die Liste `['banana', 'orange', 'mango', 'lemon']` mit einer Schleife um.
3. Nutze die `countries_data.py` Datei:
   - Wie viele Sprachen gibt es insgesamt?
   - Finde die 10 am häufigsten gesprochenen Sprachen.
   - Finde die 10 bevölkerungsreichsten Länder.

🎉 HERZLICEN GLÜCKWUNSCH! 🎉

[<< Tag 9](./09_conditionals_de.md) | [Tag 11 >>](./11_functions_de.md)
