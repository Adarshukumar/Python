<div align="center">
  <h1> 30 Tage Python: Tag 8 - Wörterbücher (Dictionaries)</h1>
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

[<< Tag 7](./07_sets_de.md) | [Tag 9 >>](./09_conditionals_de.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Tag 8](#-tag-8)
  - [Wörterbücher (Dictionaries)](#wörterbücher-dictionaries)
    - [Ein Dictionary erstellen](#ein-dictionary-erstellen)
    - [Länge eines Dictionaries](#länge-eines-dictionaries)
    - [Zugriff auf Elemente](#zugriff-auf-elemente)
    - [Elemente hinzufügen](#elemente-hinzufügen)
    - [Elemente modifizieren](#elemente-modifizieren)
    - [Schlüssel prüfen](#schlüssel-prüfen)
    - [Elemente entfernen](#elemente-entfernen)
    - [Dictionary in eine Liste umwandeln](#dictionary-in-eine-liste-umwandeln)
    - [Dictionary leeren und löschen](#dictionary-leeren-und-löschen)
    - [Dictionary kopieren](#dictionary-kopieren)
    - [Schlüssel und Werte als Listen abrufen](#schlüssel-und-werte-als-listen-abrufen)
  - [💻 Übungen - Tag 8](#-übungen---tag-8)

# 📘 Tag 8

## Wörterbücher (Dictionaries)

Ein Dictionary ist eine ungeordnete, veränderbare (mutable) Sammlung von Daten, die in **Schlüssel-Wert-Paaren** (key: value) organisiert sind.

### Ein Dictionary erstellen

Wir nutzen geschweifte Klammern `{}` oder die Funktion `dict()`.

- Leeres Dictionary:
```python
empty_dict = {}
# Dictionary mit Daten
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3'}
```

**Beispiel:**
```python
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finnland',
    'is_married':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Weltraumstraße',
        'zipcode':'02210'
    }
}
```
Ein Wert kann jeder Datentyp sein: String, Zahl, Liste, Tupel oder sogar ein weiteres Dictionary.

### Länge eines Dictionaries

Gibt die Anzahl der Schlüssel-Wert-Paare zurück:
```python
print(len(person)) # 7
```

### Zugriff auf Elemente

Wir greifen über den **Schlüsselnamen** auf die Werte zu.
```python
print(person['first_name']) # Asabeneh
print(person['skills'][0])  # JavaScript
```
Achtung: Wenn ein Schlüssel nicht existiert, stürzt das Programm ab. Sicherer ist die Methode `get()`:
```python
print(person.get('city')) # Gibt None zurück, statt abzustürzen
```

### Elemente hinzufügen

```python
person['job_title'] = 'Dozent'
person['skills'].append('HTML')
```

### Elemente modifizieren

```python
person['first_name'] = 'Eyob'
person['age'] = 252
```

### Schlüssel prüfen

Mit dem `in` Operator prüfen wir, ob ein Schlüssel existiert:
```python
print('country' in person) # True
```

### Elemente entfernen

- `pop(key)`: Entfernt das Element mit dem angegebenen Schlüssel.
- `popitem()`: Entfernt das letzte Element.
- `del dct[key]`: Löscht das Element mit dem Schlüssel.

### Dictionary in eine Liste umwandeln

Die Methode `items()` wandelt das Dictionary in eine Liste von Tupeln um:
```python
print(person.items()) # [('first_name', 'Eyob'), ...]
```

### Dictionary leeren und löschen

- `clear()`: Entfernt alle Elemente.
- `del dct`: Löscht das gesamte Dictionary-Objekt.

### Dictionary kopieren

Nutze `copy()`, um eine unabhängige Kopie zu erstellen und das Original nicht versehentlich zu verändern.

### Schlüssel und Werte als Listen abrufen

- `keys()`: Gibt alle Schlüssel zurück.
- `values()`: Gibt alle Werte zurück.

---

## 💻 Übungen - Tag 8

1. Erstelle ein leeres Dictionary namens `dog`.
2. Füge Name, Farbe, Rasse, Beine und Alter zum `dog` Dictionary hinzu.
3. Erstelle ein `student` Dictionary mit: Vorname, Nachname, Geschlecht, Alter, Familienstand, Fähigkeiten (Skills), Land, Stadt und Adresse.
4. Ermittle die Länge des `student` Dictionaries.
5. Rufe den Wert von `skills` ab und prüfe den Datentyp (es sollte eine Liste sein).
6. Modifiziere die `skills`, indem du ein oder zwei neue Fähigkeiten hinzufügst.
7. Rufe alle Schlüssel des Dictionaries als Liste ab.
8. Rufe alle Werte des Dictionaries als Liste ab.
9. Wandle das Dictionary mit `items()` in eine Liste von Tupeln um.
10. Lösche eines der Elemente im Dictionary.
11. Lösche eines der Dictionaries komplett.

🎉 HERZLICHEN GLÜCKWUNSCH! 🎉

[<< Tag 7](./07_sets_de.md) | [Tag 9 >>](./09_conditionals_de.md)
