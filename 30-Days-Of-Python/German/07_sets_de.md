<div align="center">
  <h1> 30 Tage Python: Tag 7 - Mengen (Sets)</h1>
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

[<< Tag 6](./06_tuples_de.md) | [Tag 8 >>](./08_dictionaries_de.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Tag 7](#-tag-7)
  - [Mengen (Sets)](#mengen-sets)
    - [Eine Menge erstellen](#eine-menge-erstellen)
    - [Länge einer Menge](#länge-einer-menge)
    - [Zugriff auf Elemente](#zugriff-auf-elemente)
    - [Prüfen auf Elemente](#prüfen-auf-elemente)
    - [Elemente hinzufügen](#elemente-hinzufügen)
    - [Elemente entfernen](#elemente-entfernen)
    - [Mengen leeren und löschen](#mengen-leeren-und-löschen)
    - [Liste in Menge umwandeln](#liste-in-menge-umwandeln)
    - [Mengen verbinden (Union & Update)](#mengen-verbinden-union--update)
    - [Schnittmenge finden (Intersection)](#schnittmenge-finden-intersection)
    - [Teilmengen und Obermengen prüfen](#teilmengen-und-obermengen-prüfen)
    - [Differenz zwischen Mengen finden](#differenz-zwischen-mengen-finden)
    - [Symmetrische Differenz](#symmetrische-differenz)
    - [Disjunkte Mengen](#disjunkte-mengen)
  - [💻 Übungen - Tag 7](#-übungen---tag-7)

# 📘 Tag 7

## Mengen (Sets)

Eine Menge (Set) ist eine Sammlung von Elementen. Erinnere dich an deinen Mathematikunterricht in der Schule – die Definition einer Menge lässt sich direkt auf Python übertragen. Ein Set ist eine ungeordnete und nicht indizierte Sammlung von **eindeutigen** Elementen. In Python werden Sets verwendet, um Duplikate zu vermeiden und mathematische Operationen wie *Vereinigung*, *Schnittmenge*, *Differenz* und *Teilmengen* durchzuführen.

### Eine Menge erstellen

Um eine leere Menge zu erstellen, nutzen wir die Funktion `set()`. Achtung: Leere geschweifte Klammern `{}` erstellen ein Dictionary, kein Set!

- Leere Menge erstellen:
```python
st = set()
```

- Menge mit Werten erstellen:
```python
fruits = {'Banane', 'Orange', 'Mango', 'Zitrone'}
```

### Länge einer Menge

Wie gewohnt mit `len()`:
```python
print(len(fruits)) # 4
```

### Zugriff auf Elemente

Da Sets ungeordnet sind, gibt es keinen Index-Zugriff (`st[0]` funktioniert nicht). Wir greifen auf Elemente meist über Schleifen zu (siehe Kapitel Schleifen).

### Prüfen auf Elemente

Mit dem `in` Operator:
```python
fruits = {'Banane', 'Orange', 'Mango'}
print('Mango' in fruits) # True
```

### Elemente hinzufügen

- `add(item)`: Fügt **ein** Element hinzu.
- `update(list)`: Fügt **mehrere** Elemente (z. B. aus einer Liste) hinzu.

```python
fruits.add('Limette')
fruits.update(['Apfel', 'Pfirsich'])
```

### Elemente entfernen

- `remove(item)`: Entfernt ein Element. Wirft einen Fehler, wenn das Element nicht existiert.
- `discard(item)`: Entfernt ein Element, wirft aber **keinen Fehler**, falls es fehlt.
- `pop()`: Entfernt ein **zufälliges** Element und gibt es zurück.

### Mengen leeren und löschen

- `clear()`: Macht die Menge leer (`set()`).
- `del st`: Löscht die Variable komplett.

### Liste in Menge umwandeln

Dies ist der schnellste Weg, um Duplikate aus einer Liste zu entfernen:
```python
lst = ['Apfel', 'Banane', 'Apfel']
st = set(lst) # {'Apfel', 'Banane'}
```

### Mengen verbinden (Union & Update)

- `union()`: Gibt eine **neue Menge** zurück, die alle Elemente beider Mengen enthält. (Symbol: `|`)
- `update()`: Fügt die Elemente einer anderen Menge zur **aktuellen Menge** hinzu.

### Schnittmenge finden (Intersection)

Gibt die Elemente zurück, die in **beiden** Mengen vorhanden sind. (Symbol: `&`)
```python
A = {1, 2, 3}
B = {2, 3, 4}
C = A.intersection(B) # {2, 3}
```

### Teilmengen und Obermengen prüfen

- `issubset()`: Ist A eine Teilmenge von B?
- `issuperset()`: Ist A eine Obermenge von B?

### Differenz zwischen Mengen finden

Gibt die Elemente zurück, die in A, aber **nicht** in B sind. (Symbol: `-`)
```python
A = {1, 2, 3}
B = {2, 3, 4}
diff = A.difference(B) # {1}
```

### Symmetrische Differenz

Gibt alle Elemente zurück, die in A oder B sind, aber **nicht in beiden**. (Symbol: `^`)
Mathematisch: (A \ B) ∪ (B \ A).

### Disjunkte Mengen

Zwei Mengen sind disjunkt, wenn sie **keine gemeinsamen Elemente** haben. Prüfung mit `isdisjoint()`.

---

## 💻 Übungen - Tag 7

```python
# Daten für die Übungen
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
```

### Level 1
1. Ermittle die Länge des Sets `it_companies`.
2. Füge 'Twitter' zu `it_companies` hinzu.
3. Füge mehrere IT-Unternehmen gleichzeitig hinzu.
4. Entferne eines der Unternehmen aus dem Set.
5. Was ist der Unterschied zwischen `remove` und `discard`?

### Level 2
1. Verbinde A und B (`union`).
2. Finde die Schnittmenge von A und B (`intersection`).
3. Ist A eine Teilmenge von B?
4. Sind A und B disjunkte Mengen?
5. Verbinde A mit B und B mit A.
6. Was ist die symmetrische Differenz zwischen A und B?
7. Lösche die Mengen A und B vollständig.

### Level 3
1. Wandle die Liste `age` in ein Set um und vergleiche die Länge der Liste mit der des Sets. Welche ist größer?
2. Erkläre den Unterschied zwischen: String, List, Tuple und Set.
3. "I am a teacher and I love to inspire and teach people." -> Wie viele einzigartige Wörter wurden in diesem Satz verwendet? Nutze `split` und `set`.

🎉 HERZLICHEN GLÜCKWUNSCH! 🎉

[<< Tag 6](./06_tuples_de.md) | [Tag 8 >>](./08_dictionaries_de.md)
