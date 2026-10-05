<div align="center">
  <h1> 30 Tage Python: Tag 6 - Tupel (Tuples)</h1>
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

[<< Tag 5](./05_lists_de.md) | [Tag 7 >>](./07_sets_de.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [Tag 6:](#tag-6)
  - [Tupel (Tuples)](#tupel-tuples)
    - [Ein Tupel erstellen](#ein-tupel-erstellen)
    - [Länge eines Tupels](#länge-eines-tupels)
    - [Zugriff auf Tupel-Elemente](#zugriff-auf-tupel-elemente)
    - [Slicing (Teilstücke extrahieren)](#slicing-teilstücke-extrahieren)
    - [Tupel in Listen umwandeln](#tupel-in-listen-umwandeln)
    - [Prüfen auf Elemente](#prüfen-auf-elemente)
    - [Tupel verbinden](#tupel-verbinden)
    - [Tupel löschen](#tupel-löschen)
  - [💻 Übungen - Tag 6](#-übungen---tag-6)

# Tag 6:

## Tupel (Tuples)

Ein Tupel ist eine geordnete Sammlung verschiedener Datentypen, die **unveränderbar** (immutable) ist. Tupel werden mit runden Klammern `()` geschrieben. Sobald ein Tupel erstellt wurde, können wir seinen Inhalt nicht mehr ändern. Methoden wie `add`, `insert` oder `remove` funktionieren hier nicht. Im Gegensatz zu Listen haben Tupel nur sehr wenige Methoden:

- `tuple()`: Erstellt ein leeres Tupel.
- `count()`: Zählt das Vorkommen eines bestimmten Elements.
- `index()`: Findet den Index eines Elements.
- `+` Operator: Verbindet zwei oder mehr Tupel zu einem neuen Tupel.

### Ein Tupel erstellen

- Leeres Tupel:
  ```python
  empty_tpl = ()
  # oder mit dem Konstruktor
  empty_tpl = tuple()
  ```

- Tupel mit Werten:
  ```python
  fruits = ('Banane', 'Orange', 'Mango', 'Zitrone')
  ```

### Länge eines Tupels

Wie bei anderen Sequenzen nutzen wir `len()`:
```python
tpl = ('Element1', 'Element2', 'Element3')
print(len(tpl)) # 3
```

### Zugriff auf Tupel-Elemente

- **Positiver Index:** Beginnt bei 0.
- **Negativer Index:** Beginnt am Ende bei -1.

```python
fruits = ('Banane', 'Orange', 'Mango', 'Zitrone')
first_fruit = fruits[0] # Banane
last_fruit = fruits[-1] # Zitrone
```

### Slicing (Teilstücke extrahieren)

Wir können Teilstücke extrahieren, was ein **neues Tupel** zurückgibt:
```python
fruits = ('Banane', 'Orange', 'Mango', 'Zitrone')
orange_mango = fruits[1:3] # Index 1 bis 3 (ohne 3)
```

### Tupel in Listen umwandeln

Da Tupel unveränderbar sind, müssen wir sie in eine Liste umwandeln, wenn wir sie modifizieren wollen:
```python
fruits = ('Banane', 'Orange', 'Mango')
fruits_list = list(fruits)
fruits_list[0] = 'Apfel'
fruits = tuple(fruits_list)
print(fruits) # ('Apfel', 'Orange', 'Mango')
```

### Prüfen auf Elemente

Mit dem `in` Operator prüfen wir, ob ein Wert im Tupel existiert:
```python
fruits = ('Banane', 'Orange', 'Mango')
print('Orange' in fruits) # True
```

### Tupel verbinden

Wir können Tupel mit dem `+` Operator verknüpfen:
```python
fruits = ('Banane', 'Orange')
vegetables = ('Tomate', 'Kartoffel')
food = fruits + vegetables
```

### Tupel löschen

Es ist nicht möglich, einzelne Elemente zu entfernen, aber man kann das gesamte Tupel mit `del` löschen:
```python
fruits = ('Banane', 'Orange')
del fruits
```

---

## 💻 Übungen - Tag 6

### Level 1
1. Erstelle ein leeres Tupel.
2. Erstelle ein Tupel mit den Namen deiner Geschwister.
3. Verbinde die Tupel deiner Brüder und Schwestern zu einem `siblings` Tupel.
4. Wie viele Geschwister hast du? (Länge von `siblings`).
5. Füge die Namen deiner Eltern hinzu und erstelle ein neues Tupel `family_members`.

### Level 2
1. Entpacke (`Unpacking`) Geschwister und Eltern aus `family_members`.
2. Erstelle Tupel für Früchte, Gemüse und Tierprodukte. Verbinde sie zu `food_stuff_tp`.
3. Wandle `food_stuff_tp` in eine Liste `food_stuff_lt` um.
4. Schneide das mittlere Element (oder die mittleren zwei) aus.
5. Schneide die ersten drei und die letzten drei Elemente aus `food_stuff_lt` heraus.
6. Lösche das Tupel `food_stuff_tp` vollständig.
7. Prüfe, ob 'Island' ein nordisches Land ist:
   ```python
   nordic_countries = ('Dänemark', 'Finnland', 'Island', 'Norwegen', 'Schweden')
   ```

🎉 HERZLICEN GLÜCKWUNSCH! 🎉

[<< Tag 5](./05_lists_de.md) | [Tag 7 >>](./07_sets_de.md)
