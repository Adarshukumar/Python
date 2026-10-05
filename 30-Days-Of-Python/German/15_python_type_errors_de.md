<div align="center">
  <h1> 30 Tage Python: Tag 15 - Python Fehlertypen</h1>
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

[<< Tag 14](./14_higher_order_functions_de.md) | [Tag 16 >>](./16_python_datetime_de.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Tag 15](#-tag-15)
  - [Python Fehlertypen](#python-fehlertypen)
    - [SyntaxError](#syntaxerror)
    - [NameError](#nameerror)
    - [IndexError](#indexerror)
    - [ModuleNotFoundError](#modulenotfounderror)
    - [AttributeError](#attributeerror)
    - [KeyError](#keyerror)
    - [TypeError](#typeerror)
    - [ImportError](#importerror)
    - [ValueError](#valueerror)
    - [ZeroDivisionError](#zerodivisionerror)
  - [💻 Übungen - Tag 15](#-übungen---tag-15)

# 📘 Tag 15

## Python Fehlertypen

Beim Programmieren ist es völlig normal, Fehler zu machen – sei es ein Tippfehler oder ein logischer Fehler. Wenn dein Code nicht läuft, zeigt Python eine Fehlermeldung an. Diese enthält Informationen darüber, wo das Problem aufgetreten ist und um welche Art von Fehler es sich handelt. Das Verständnis dieser Fehlermeldungen hilft dir, deinen Code schnell zu "debuggen" (Fehler zu beheben).

### SyntaxError
Tritt auf, wenn Python den Code aufgrund falscher Grammatik nicht lesen kann (z. B. fehlende Klammern).
```python
# Fehler
print 'Hallo Welt' # SyntaxError: Missing parentheses
# Lösung
print('Hallo Welt')
```

### NameError
Tritt auf, wenn du eine Variable verwendest, die noch nicht definiert wurde.
```python
# Fehler
print(alter) # NameError: name 'age' is not defined
# Lösung
alter = 25
print(alter)
```

### IndexError
Tritt auf, wenn du auf einen Index in einer Liste zugreifst, der nicht existiert.
```python
lst = [1, 2, 3]
print(lst[5]) # IndexError: list index out of range
```

### ModuleNotFoundError
Tritt auf, wenn du ein Modul importieren möchtest, das nicht installiert oder falsch geschrieben ist.
```python
import maths # ModuleNotFoundError: No module named 'maths' (es heißt 'math')
```

### AttributeError
Tritt auf, wenn du auf eine Eigenschaft oder Methode eines Objekts zugreifst, die dieses nicht besitzt.
```python
import math
math.PI # AttributeError: module 'math' has no attribute 'PI' (es heißt 'pi')
```

### KeyError
Tritt auf, wenn du in einem Dictionary auf einen Schlüssel zugreifst, der nicht existiert.
```python
user = {'name': 'Asab'}
print(user['alter']) # KeyError: 'alter'
```

### TypeError
Tritt auf, wenn eine Operation auf einen Datentyp angewendet wird, der dafür nicht geeignet ist (z. B. Zahl + String).
```python
print(4 + '3') # TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

### ImportError
Tritt auf, wenn ein Import fehlschlägt, z. B. weil die Funktion im Modul nicht existiert.
```python
from math import power # ImportError: cannot import name 'power' (es heißt 'pow')
```

### ValueError
Tritt auf, wenn eine Funktion ein Argument mit dem richtigen Typ, aber einem ungültigen Wert erhält.
```python
int('12a') # ValueError: invalid literal for int()
```

### ZeroDivisionError
Tritt auf, wenn du versuchst, eine Zahl durch Null zu teilen.
```python
print(1/0) # ZeroDivisionError: division by zero
```

Das Verständnis dieser Fehler macht dich zu einem effizienteren Programmierer. Nutze die Fehlermeldungen als Wegweiser zur Lösung!

---

## 💻 Übungen - Tag 15

1. Öffne die interaktive Python-Shell und provoziere absichtlich jeden der oben genannten Fehler, um die Meldungen selbst zu sehen. Fixe sie anschließend.

🎉 HERZLICEN GLÜCKWUNSCH! 🎉

[<< Tag 14](./14_higher_order_functions_de.md) | [Tag 16 >>](./16_python_datetime_de.md)
