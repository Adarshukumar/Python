<div align="center">
  <h1> 30 Tage Python: Tag 29 - API Erstellen (Building API)</h1>
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

[<< Tag 28](./28_API_de.md) | [Tag 30 >>](./30_conclusions_de.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Tag 29](#-tag-29)
  - [API Erstellen](#api-erstellen)
    - [Struktur einer API](#struktur-einer-api)
    - [Daten abrufen (GET)](#daten-abrufen-get)
    - [Daten per ID finden](#daten-per-id-finden)
    - [Daten erstellen (POST)](#daten-erstellen-post)
    - [Daten aktualisieren (PUT)](#daten-aktualisieren-put)
    - [Daten löschen (DELETE)](#daten-löschen-delete)
  - [💻 Übungen - Tag 29](#-übungen---tag-29)

# 📘 Tag 29

## API Erstellen

In diesem Abschnitt bauen wir eine echte **RESTful API**, die alle HTTP-Methoden (GET, POST, PUT, DELETE) nutzt, um Daten zu verarbeiten. Wir kombinieren dafür unser Wissen über Python, Flask und MongoDB.

Da ein Browser standardmäßig nur GET-Anfragen einfach darstellen kann, benötigen wir ein Werkzeug wie **Postman** oder **Insomnia**, um unsere API-Endpunkte professionell zu testen.

### Struktur einer API

Ein API-Endpunkt ist eine URL, über die eine Ressource erreicht wird.
Beispiel: `http://localhost:5000/api/v1.0/students`

### Daten abrufen (GET)

Zuerst erstellen wir einen Endpunkt, der uns eine Liste von Studenten als JSON zurückgibt.

```python
from flask import Flask, Response
import json

app = Flask(__name__)

@app.route('/api/v1.0/students', methods=['GET'])
def get_students():
    student_list = [
        {'name': 'Asabeneh', 'country': 'Finland'},
        {'name': 'David', 'country': 'UK'}
    ]
    return Response(json.dumps(student_list), mimetype='application/json')
```

### Daten erstellen (POST)

Mit der POST-Methode können wir neue Daten an den Server senden und in der Datenbank speichern.

```python
@app.route('/api/v1.0/students', methods=['POST'])
def create_student():
    name = request.form['name']
    country = request.form['country']
    # Logik zum Speichern in MongoDB...
    return Response(json.dumps({'result': 'Erfolgreich erstellt'}), mimetype='application/json')
```

### Daten aktualisieren (PUT)

PUT wird verwendet, um einen bestehenden Datensatz komplett zu ersetzen oder zu aktualisieren. Wir identifizieren den Datensatz meist über eine eindeutige ID.

### Daten löschen (DELETE)

Der DELETE-Endpunkt entfernt eine Ressource aus der Datenbank.

```python
@app.route('/api/v1.0/students/<id>', methods=['DELETE'])
def delete_student(id):
    db.students.delete_one({'_id': ObjectId(id)})
    return Response(json.dumps({'result': 'Gelöscht'}), mimetype='application/json')
```

---

## 💻 Übungen - Tag 29

1. Implementiere das Beispiel aus diesem Kapitel und erstelle eine voll funktionsfähige API für eine Studentenverwaltung.
2. Teste alle Endpunkte (GET, POST, PUT, DELETE) mit Postman.
3. (Bonus): Füge Validierungen hinzu, sodass ein Student nicht ohne Namen gespeichert werden kann.

🎉 HERZLICEN GLÜCKWUNSCH! 🎉

[<< Tag 28](./28_API_de.md) | [Tag 30 >>](./30_conclusions_de.md)
