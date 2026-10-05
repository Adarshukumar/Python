<div align="center">
  <h1> 30 Tage Python: Tag 5 - Listen (Lists)</h1>
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

[<< Tag 4](./04_strings_de.md) | [Tag 6 >>](./06_tuples_de.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [Tag 5](#tag-5)
  - [Listen (Lists)](#listen-lists)
    - [Wie man eine Liste erstellt](#wie-man-eine-liste-erstellt)
    - [Zugriff auf Listenelemente per Index](#zugriff-auf-listenelemente-per-index)
    - [Negativer Index](#negativer-index)
    - [Entpacken von Listenelementen (Unpacking)](#entpacken-von-listenelementen-unpacking)
    - [Slicing (Teilstücke extrahieren)](#slicing-teilstücke-extrahieren)
    - [Listen modifizieren](#listen-modifizieren)
    - [Elemente in einer Liste prüfen](#elemente-in-einer-liste-prüfen)
    - [Elemente hinzufügen (Append & Insert)](#elemente-hinzufügen-append--insert)
    - [Elemente entfernen (Remove, Pop, Del)](#elemente-entfernen-remove-pop-del)
    - [Listen kopieren](#listen-kopieren)
    - [Listen verbinden (Join)](#listen-verbinden-join)
    - [Sortieren von Listen](#sortieren-von-listen)
  - [💻 Übungen - Tag 5](#-übungen---tag-5)

# Tag 5

## Listen (Lists)

In Python gibt es vier primäre Datentypen für Sammlungen:
- **List (Liste):** Geordnet und veränderbar (mutable). Erlaubt doppelte Einträge.
- **Tuple (Tupel):** Geordnet und unveränderbar (immutable). Erlaubt doppelte Einträge.
- **Set (Menge):** Ungeordnet, nicht indiziert und unveränderbar (man kann jedoch neue Elemente hinzufügen). Keine doppelten Einträge erlaubt.
- **Dictionary (Wörterbuch):** Ungeordnet, veränderbar und indiziert (per Schlüssel). Keine doppelten Einträge.

Eine Liste ist eine geordnete Sammlung verschiedener Datentypen. Sie ist "mutable", was bedeutet, dass wir ihren Inhalt nach der Erstellung verändern können.

### Wie man eine Liste erstellt

In Python gibt es zwei Wege:
1. Mit der Funktion `list()`:
```python
lst = list()
```
2. Mit eckigen Klammern `[]`:
```python
lst = []
```

Beispiel für eine Liste mit Werten:
```python
fruits = ['Banane', 'Orange', 'Mango', 'Zitrone']
print('Früchte:', fruits)
print('Anzahl der Früchte:', len(fruits))
```

### Zugriff auf Listenelemente per Index

Der Index beginnt bei **0**.
```python
fruits = ['Banane', 'Orange', 'Mango', 'Zitrone']
first_fruit = fruits[0] # Banane
last_fruit = fruits[3]  # Zitrone
```

**Negativer Index:** Zählt von hinten rückwärts. `-1` ist das letzte Element.
```python
last_fruit = fruits[-1] # Zitrone
```

### Entpacken von Listenelementen (Unpacking)

```python
lst = ['Element1','Element2','Element3', 'Element4', 'Element5']
item1, item2, item3, *rest = lst
print(item1) # Element1
print(rest)  # ['Element4', 'Element5']
```

### Slicing (Teilstücke extrahieren)

Format: `liste[start:stop:step]`
```python
fruits = ['Banane', 'Orange', 'Mango', 'Zitrone']
all_fruits = fruits[0:4] # Alle Früchte
some_fruits = fruits[1:3] # ['Orange', 'Mango'] - Index 3 ist nicht dabei
```

### Listen modifizieren

Da Listen veränderbar sind, können wir Werte einfach überschreiben:
```python
fruits = ['Banane', 'Orange', 'Mango']
fruits[0] = 'Avocado'
print(fruits) # ['Avocado', 'Orange', 'Mango']
```

### Elemente hinzufügen

- `append(item)`: Fügt ein Element am **Ende** hinzu.
- `insert(index, item)`: Fügt ein Element an einer **bestimmten Stelle** ein. Alle nachfolgenden Elemente verschieben sich nach rechts.

```python
fruits.append('Apfel')
fruits.insert(1, 'Limette')
```

### Elemente entfernen

- `remove(item)`: Entfernt das **erste Vorkommen** eines bestimmten Wertes.
- `pop(index)`: Entfernt das Element am angegebenen Index (Standard: das letzte).
- `del liste[index]`: Löscht das Element am Index oder die ganze Liste.
- `clear()`: Leert die Liste komplett.

### Listen verbinden (Join)

- Mit dem `+` Operator: `list3 = list1 + list2`
- Mit der `extend()` Methode: `list1.extend(list2)`

### Sortieren von Listen

- `sort()`: Sortiert die **Original-Liste** (aufsteigend oder absteigend mit `reverse=True`).
- `sorted()`: Gibt eine **neue sortierte Liste** zurück, ohne das Original zu ändern.

---

## 💻 Übungen - Tag 5

### Level 1
1. Deklariere eine leere Liste.
2. Deklariere eine Liste mit mehr als 5 Elementen.
3. Ermittle die Länge der Liste.
4. Gib das erste, das mittlere und das letzte Element aus.
5. Erstelle eine Liste `it_companies` mit: Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon.
6. Gib die Liste und die Anzahl der Unternehmen aus.
7. Gib das erste, mittlere und letzte Unternehmen aus.
8. Ändere eines der Unternehmen in der Liste.
9. Füge ein neues IT-Unternehmen hinzu (`append`).
10. Füge ein IT-Unternehmen in der Mitte der Liste ein (`insert`).
11. Wandle eines der Unternehmen (außer IBM) in Großbuchstaben um.
12. Verbinde die Liste mit einem String '#;&nbsp; '.
13. Prüfe, ob ein bestimmtes Unternehmen in der Liste existiert (`in`).
14. Sortiere die Liste mit `sort()`.
15. Kehre die Liste um (`reverse()`).
16. Schneide die ersten 3 Unternehmen ab.
17. Schneide die letzten 3 Unternehmen ab.
18. Entferne das erste Unternehmen.
19. Entferne alle Unternehmen aus der Liste.

### Level 2
1. Gegeben ist eine Liste mit Alterswerten: `ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]`
   - Sortiere die Liste und finde das Minimum und Maximum.
   - Füge das Minimum und Maximum erneut zur Liste hinzu.
   - Finde den Median (den mittleren Wert).
   - Finde den Durchschnittswert.
   - Finde die Spannweite (Maximum minus Minimum).
2. Finde das mittlere Land/die mittleren Länder in der [Länderliste](https://github.com/Asabeneh/30-Days-Of-Python/tree/master/data/countries.py).
3. Teile die Länderliste in zwei hälften auf.
4. Entpacke die ersten drei Länder und den Rest als "skandinavische Länder".

🎉 HERZLICHEN GLÜCKWUNSCH! 🎉

[<< Tag 4](./04_strings_de.md) | [Tag 6 >>](./06_tuples_de.md)
