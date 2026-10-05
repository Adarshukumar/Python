<div align="center">
  <h1> 30 Tage Python: Tag 25 - Pandas</h1>
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

[<< Tag 24](./24_statistics_de.md) | [Tag 26 >>](./26_python_web_de.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Tag 25](#-tag-25)
  - [Pandas](#pandas)
    - [Installation und Import](#installation-und-import)
    - [Pandas Series](#pandas-series)
    - [Pandas DataFrames](#pandas-dataframes)
  - [Datenexploration](#datenexploration)
  - [DataFrames modifizieren](#dataframes-modifizieren)
    - [Spalten hinzufügen](#spalten-hinzufügen)
    - [Werte berechnen](#werte-berechnen)
    - [Filtern (Boolean Indexing)](#filtern-boolean-indexing)
  - [💻 Übungen - Tag 25](#-übungen---tag-25)

# 📘 Tag 25

## Pandas

Pandas ist eine Open-Source-Bibliothek für Python, die leistungsstarke, einfach zu bedienende Datenstrukturen und Analysewerkzeuge bietet. Es ist das Standardwerkzeug für die Arbeit mit tabellarischen Daten (ähnlich wie Excel oder SQL-Tabellen).

### Installation und Import

```shell
pip install pandas
```

```python
import pandas as pd
import numpy as np
```

### Pandas Series

Eine **Series** ist eine einzelne Spalte von Daten. Sie kann aus einer Liste, einem Dictionary oder einem NumPy-Array erstellt werden.

```python
nums = [1, 2, 3, 4, 5]
s = pd.Series(nums)
print(s)
```

### Pandas DataFrames

Ein **DataFrame** ist eine zweidimensionale Tabelle (eine Sammlung von Series). Er ist das Herzstück von Pandas.

```python
data = {
    'Name': ['Asabeneh', 'David', 'John'],
    'Land': ['Finnland', 'UK', 'Schweden'],
    'Stadt': ['Helsinki', 'London', 'Stockholm']
}
df = pd.DataFrame(data)
```

## Datenexploration

Wenn du einen großen Datensatz hast (z. B. eine CSV-Datei), helfen dir diese Methoden:

- `df.head()`: Zeigt die ersten 5 Zeilen.
- `df.tail()`: Zeigt die letzten 5 Zeilen.
- `df.shape`: Zeigt die Anzahl der Zeilen und Spalten (Tupel).
- `df.info()`: Zeigt Datentypen und fehlende Werte.
- `df.describe()`: Berechnet statistische Kennzahlen (Mittelwert, Min, Max etc.).

## DataFrames modifizieren

### Spalten hinzufügen
```python
df['Gewicht'] = [74, 78, 69]
```

### Werte berechnen
Du kannst Spalten direkt miteinander verrechnen:
```python
# BMI berechnen (Gewicht / Größe in m^2)
df['BMI'] = df['Gewicht'] / (df['Größe'] ** 2)
```

### Filtern (Boolean Indexing)
Du kannst Daten basierend auf Bedingungen filtern:
```python
# Nur Personen über 30 Jahre anzeigen
print(df[df['Alter'] > 30])
```

---

## 💻 Übungen - Tag 25

1. Lies die Datei `hacker_news.csv` aus dem `data`-Ordner ein.
2. Zeige die ersten und letzten 5 Zeilen an.
3. Extrahiere die Spalte "title" als Series.
4. Zähle die Anzahl der Zeilen und Spalten.
5. Filtere alle Titel, die das Wort "python" enthalten.
6. Filtere alle Titel, die das Wort "JavaScript" enthalten.
7. Vergleiche, über welche Sprache öfter geschrieben wurde.

🎉 HERZLICEN GLÜCKWUNSCH! 🎉

[<< Tag 24](./24_statistics_de.md) | [Tag 26 >>](./26_python_web_de.md)
