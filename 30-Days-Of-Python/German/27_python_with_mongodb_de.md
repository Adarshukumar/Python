<div align="center">
  <h1> 30 Tage Python: Tag 27 - Python mit MongoDB</h1>
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

[<< Tag 26](./26_python_web_de.md) | [Tag 28 >>](./28_API_de.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Tag 27](#-tag-27)
  - [Python mit MongoDB](#python-mit-mongodb)
    - [SQL vs. NoSQL](#sql-vs-nosql)
    - [MongoDB Einrichtung](#mongodb-einrichtung)
    - [Verbindung mit PyMongo](#verbindung-mit-pymongo)
    - [Datenbank und Kollektion erstellen](#datenbank-und-kollektion-erstellen)
    - [CRUD-Operationen](#crud-operationen)
      - [Einfügen (Create)](#einfügen-create)
      - [Finden (Read)](#finden-read)
      - [Aktualisieren (Update)](#aktualisieren-update)
      - [Löschen (Delete)](#löschen-delete)
  - [💻 Übungen - Tag 27](#-übungen---tag-27)

# 📘 Tag 27

## Python mit MongoDB

Python wird oft als Backend-Technologie eingesetzt und kann mit verschiedenen Datenbanksystemen verbunden werden (SQL und NoSQL). In diesem Kapitel verbinden wir Python mit **MongoDB**, einer beliebten NoSQL-Datenbank.

### SQL vs. NoSQL

Während SQL-Datenbanken (wie MySQL oder PostgreSQL) Tabellen mit festen Schemata nutzen, speichert MongoDB Daten in Dokumenten (JSON-ähnlich). Dies macht MongoDB sehr flexibel und skalierbar.

### MongoDB Einrichtung

Wir nutzen **MongoDB Atlas**, die Cloud-Lösung von MongoDB.
1. Registriere dich auf [mongodb.com](https://www.mongodb.com/).
2. Erstelle einen kostenlosen Cluster (Shared Sandbox).
3. Erstelle einen Datenbank-Nutzer (Name & Passwort).
4. Erlaube den Zugriff von deiner IP-Adresse.
5. Kopiere den "Connection String" (URI).

### Verbindung mit PyMongo

Um MongoDB in Python zu nutzen, benötigen wir den Treiber `pymongo`.

```shell
pip install pymongo dnspython
```

**Verbindung herstellen:**
```python
import pymongo

# Ersetze <password> durch dein Passwort
uri = "mongodb+srv://user:<password>@cluster.mongodb.net/test?retryWrites=true&w=majority"
client = pymongo.MongoClient(uri)

# Datenbank und Kollektion auswählen
db = client.python_kurs
collection = db.studenten
```

### CRUD-Operationen

#### Einfügen (Create)
```python
student = {'name': 'Asabeneh', 'land': 'Finnland', 'alter': 250}
collection.insert_one(student) # Ein Dokument einfügen
```

#### Finden (Read)
```python
# Das erste Dokument finden
result = collection.find_one()

# Alle Dokumente finden
for s in collection.find():
    print(s)

# Mit Filter (z. B. alle aus Finnland)
for s in collection.find({'land': 'Finnland'}):
    print(s)
```

#### Aktualisieren (Update)
```python
query = {'name': 'Asabeneh'}
neue_werte = {'$set': {'alter': 38}}
collection.update_one(query, neue_werte)
```

#### Löschen (Delete)
```python
collection.delete_one({'name': 'Asabeneh'})
# collection.drop() # Löscht die gesamte Kollektion
```

---

## 💻 Übungen - Tag 27

1. Erstelle einen MongoDB Atlas Account und einen kostenlosen Cluster.
2. Verbinde dein Python-Skript mit der Cloud-Datenbank.
3. Erstelle eine Datenbank `schulverwaltung` und eine Kollektion `lehrer`.
4. Füge 5 Lehrer-Dokumente mit Name, Fach und Erfahrung (Jahre) ein.
5. Finde alle Lehrer, die mehr als 10 Jahre Erfahrung haben.
6. Aktualisiere das Fach eines Lehrers.
7. Lösche einen Lehrer aus der Datenbank.

🎉 HERZLICEN GLÜCKWUNSCH! 🎉

[<< Tag 26](./26_python_web_de.md) | [Tag 28 >>](./28_API_de.md)
