<div align="center">
  <h1> 30 Tage Python: Tag 24 - Statistik & NumPy</h1>
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

[<< Tag 23](./23_virtual_environment_de.md) | [Tag 25 >>](./25_pandas_de.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Tag 24](#-tag-24)
  - [Statistik in Python](#statistik-in-python)
  - [NumPy (Numerical Python)](#numpy-numerical-python)
    - [Einführung in NumPy](#einführung-in-numpy)
    - [NumPy Arrays erstellen](#numpy-arrays-erstellen)
    - [Mathematische Operationen mit NumPy](#mathematische-operationen-mit-numpy)
    - [Mehrdimensionale Arrays](#mehrdimensionale-arrays)
    - [Zufallszahlen generieren](#zufallszahlen-generieren)
  - [Zusammenfassung](#zusammenfassung)
  - [💻 Übungen - Tag 24](#-übungen---tag-24)

# 📘 Tag 24

## Statistik in Python

Statistik ist die Disziplin, die sich mit der Sammlung, Organisation, Analyse und Präsentation von Daten befasst. Für Data Science und Machine Learning ist ein Grundverständnis der Statistik unerlässlich.

## NumPy (Numerical Python)

Während Python-Listen flexibel sind, sind sie für große mathematische Berechnungen langsam. **NumPy** ist die Kernbibliothek für wissenschaftliches Rechnen in Python. Sie bietet leistungsstarke mehrdimensionale Arrays und Werkzeuge, um effizient damit zu arbeiten.

### Einführung in NumPy

Installation:
```shell
pip install numpy
```

Importieren:
```python
import numpy as np
print(np.__version__)
```

### NumPy Arrays erstellen

NumPy Arrays (ndarrays) sind schneller und speichereffizienter als normale Listen.

- **Aus einer Liste:**
```python
lst = [1, 2, 3, 4, 5]
np_arr = np.array(lst)
```

- **Mit Datentyp (Float):**
```python
np_float = np.array([1, 2, 3], dtype=float) # [1., 2., 3.]
```

### Mathematische Operationen mit NumPy

Einer der größten Vorteile von NumPy ist die **Vektorisierung**. Du kannst mathematische Operationen auf das gesamte Array anwenden, ohne eine Schleife zu schreiben.

```python
nums = np.array([1, 2, 3, 4])
print(nums + 10) # [11, 12, 13, 14]
print(nums * 2)  # [2, 4, 6, 8]
print(nums ** 2) # [1, 4, 9, 16]
```

### Mehrdimensionale Arrays

```python
matrix = np.array([[1, 2], [3, 4], [5, 6]])
print(matrix.shape) # (3, 2) - 3 Zeilen, 2 Spalten
```

### Zufallszahlen generieren

```python
# Zufällige Zahl zwischen 0 und 1
rand = np.random.random()

# 5 Zufallszahlen
rand_arr = np.random.random(5)

# Zufällige Ganzzahlen zwischen 0 und 10
rand_int = np.random.randint(0, 11)
```

## Zusammenfassung

Unterschiede zu normalen Listen:
1. Arrays unterstützen **vektorisierte Operationen**.
2. Die Größe eines Arrays ist nach der Erstellung **fest**.
3. Alle Elemente in einem Array müssen den **gleichen Datentyp** haben.
4. NumPy Arrays verbrauchen deutlich **weniger Speicher**.

---

## 💻 Übungen - Tag 24

1. Wiederhole alle Code-Beispiele aus diesem Kapitel in deiner eigenen Entwicklungsumgebung (oder im Jupyter Notebook).
2. Erstelle ein 3x3 Array mit Zufallswerten und berechne den Mittelwert jeder Spalte.

🎉 HERZLICEN GLÜCKWUNSCH! 🎉

[<< Tag 23](./23_virtual_environment_de.md) | [Tag 25 >>](./25_pandas_de.md)
