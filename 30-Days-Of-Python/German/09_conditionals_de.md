<div align="center">
  <h1> 30 Tage Python: Tag 9 - Bedingte Anweisungen (Conditionals)</h1>
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

[<< Tag 8](./08_dictionaries_de.md) | [Tag 10 >>](./10_loops_de.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Tag 9](#-tag-9)
  - [Bedingte Anweisungen](#bedingte-anweisungen)
    - [If Bedingung](#if-bedingung)
    - [If Else](#if-else)
    - [If Elif Else](#if-elif-else)
    - [Kurzschreibweise (Short Hand)](#kurzschreibweise-short-hand)
    - [Verschachtelte Bedingungen](#verschachtelte-bedingungen)
    - [Logische Operatoren in Bedingungen](#logische-operatoren-in-bedingungen)
  - [💻 Übungen - Tag 9](#-übungen---tag-9)

# 📘 Tag 9

## Bedingte Anweisungen

Standardmäßig werden Anweisungen in einem Python-Skript nacheinander von oben nach unten ausgeführt. Wenn die Logik es erfordert, kann dieser sequentielle Fluss auf zwei Arten geändert werden:

- **Bedingte Ausführung:** Ein Codeblock wird nur ausgeführt, wenn eine bestimmte Bedingung wahr (True) ist.
- **Wiederholte Ausführung:** Ein Codeblock wird wiederholt ausgeführt, solange eine Bedingung wahr ist (siehe Kapitel Schleifen).

In diesem Abschnitt behandeln wir `if`, `else` und `elif`. Die Vergleichs- und Logikoperatoren aus den vorherigen Kapiteln sind hierbei sehr nützlich.

### If Bedingung

Das Schlüsselwort `if` wird verwendet, um eine Bedingung zu prüfen. Beachte unbedingt die **Einrückung** nach dem Doppelpunkt.

```python
# Syntax
if bedingung:
    dieser Teil läuft, wenn die Bedingung wahr ist
```

**Beispiel:**
```python
a = 3
if a > 0:
    print('A ist eine positive Zahl')
```

### If Else

Wenn die Bedingung wahr ist, wird der erste Block ausgeführt, andernfalls der `else`-Block.

```python
a = 3
if a < 0:
    print('A ist eine negative Zahl')
else:
    print('A ist eine positive Zahl')
```

### If Elif Else

Im Alltag treffen wir Entscheidungen oft basierend auf vielen verschiedenen Bedingungen. In Python nutzen wir dafür `elif` (short for "else if").

```python
a = 0
if a > 0:
    print('A ist positiv')
elif a < 0:
    print('A ist negativ')
else:
    print('A ist Null')
```

### Kurzschreibweise (Short Hand)

Für sehr einfache Bedingungen gibt es den Ternary Operator:
```python
a = 3
print('Positiv') if a > 0 else print('Negativ')
```

### Verschachtelte Bedingungen (Nested)

Du kannst Bedingungen innerhalb anderer Bedingungen platzieren:
```python
a = 0
if a > 0:
    if a % 2 == 0:
        print('A ist positiv und gerade')
    else:
        print('A ist positiv und ungerade')
elif a == 0:
    print('A ist Null')
else:
    print('A ist negativ')
```

### Logische Operatoren in Bedingungen

Verschachtelte Bedingungen lassen sich oft durch `and` oder `or` vermeiden:
```python
if a > 0 and a % 2 == 0:
    print('A ist eine positive gerade Zahl')
```

---

## 💻 Übungen - Tag 9

### Level 1
1. Frage den Nutzer nach seinem Alter (`input`). Wenn er 18 oder älter ist: "Du bist alt genug zum Autofahren." Wenn jünger: "Du musst noch X Jahre warten."
2. Vergleiche dein Alter mit dem eines Nutzers. Wer ist älter? Berücksichtige auch den Fall, dass beide gleich alt sind.
3. Frage nach zwei Zahlen (a und b). Gib aus, ob a größer, kleiner oder gleich b ist.

### Level 2
1. Schreibe ein Programm, das Noten (Grades) basierend auf Punktzahlen vergibt:
   - 90-100: A
   - 80-89: B
   - 70-79: C
   - 60-69: D
   - 0-59: F
2. Frage nach einem Monat und gib die Jahreszeit aus (Herbst, Winter, Frühling, Sommer).
3. Gegeben ist eine Liste: `fruits = ['banana', 'orange', 'mango', 'lemon']`. Frage den Nutzer nach einer Frucht. Wenn sie nicht in der Liste ist, füge sie hinzu. Wenn sie existiert, gib eine entsprechende Meldung aus.

### Level 3
1. Gegeben ist ein `person` Dictionary (siehe Original-Aufgabe).
   - Prüfe, ob die Person Fähigkeiten (`skills`) hat und gib die mittlere Fähigkeit aus.
   - Prüfe, ob die Person die Fähigkeit 'Python' besitzt.
   - Erstelle eine Logik, die die Person als "Frontend-Entwickler", "Backend-Entwickler" oder "Fullstack-Entwickler" einstuft, basierend auf ihren Skills.
   - Wenn die Person verheiratet ist und in Finnland lebt, gib die Infos in einem schönen Satz aus.

🎉 HERZLICEN GLÜCKWUNSCH! 🎉

[<< Tag 8](./08_dictionaries_de.md) | [Tag 10 >>](./10_loops_de.md)
