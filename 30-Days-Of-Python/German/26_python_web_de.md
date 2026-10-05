<div align="center">
  <h1> 30 Tage Python: Tag 26 - Python im Web (Flask)</h1>
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

[<< Tag 25](./25_pandas_de.md) | [Tag 27 >>](./27_python_with_mongodb_de.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Tag 26](#-tag-26)
  - [Python für das Web](#python-für-das-web)
    - [Flask Framework](#flask-framework)
    - [Projektstruktur](#projektstruktur)
    - [Routen erstellen](#routen-erstellen)
    - [Templates verwenden](#templates-verwenden)
    - [Layouts und Vererbung](#layouts-und-vererbung)
    - [Statische Dateien (CSS)](#statische-dateien-css)
    - [Deployment (Veröffentlichung)](#deployment-veröffentlichung)
  - [💻 Übungen - Tag 26](#-übungen---tag-26)

# 📘 Tag 26

## Python für das Web

Python ist eine vielseitige Sprache, die auch in der Web-Entwicklung eine große Rolle spielt. Die beiden populärsten Frameworks sind **Django** (umfangreich) und **Flask** (leichtgewichtig). In diesem Kapitel lernen wir, wie man Flask verwendet.

### Flask Framework

Flask ist ein Micro-Web-Framework. Es ist einfach zu erlernen und bietet dennoch alle Werkzeuge, um moderne Webanwendungen zu bauen. Flask nutzt die **Jinja2** Template-Engine, um dynamische HTML-Seiten zu erzeugen.

### Projektstruktur

Ein typisches Flask-Projekt sieht so aus:
```
├── app.py           # Die Hauptanwendung
├── static/          # Bilder, CSS, JavaScript
│   └── css/
│       └── main.css
└── templates/       # HTML-Dateien
    ├── home.html
    └── layout.html
```

### Routen erstellen

Eine "Route" bestimmt, was passiert, wenn ein Nutzer eine bestimmte URL aufruft.

```python
from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/') # Die Startseite
def home():
    return '<h1>Willkommen auf der Startseite!</h1>'

@app.route('/about') # Die Über-uns-Seite
def about():
    return '<h1>Über uns</h1>'

if __name__ == '__main__':
    app.run(debug=True)
```

### Templates verwenden

Anstatt Text direkt im Python-Code zu schreiben, nutzen wir HTML-Dateien im Ordner `templates/`.

```python
@app.route('/')
def home():
    return render_template('home.html', title='Startseite')
```

### Layouts und Vererbung

Um Code-Wiederholungen zu vermeiden (z. B. Navigation auf jeder Seite), nutzen wir ein Basis-Layout (`layout.html`), das von anderen Seiten erweitert wird.

**layout.html:**
```html
<html>
  <head><title>{{ title }}</title></head>
  <body>
    <nav>...</nav>
    {% block content %}{% endblock %}
  </body>
</html>
```

**home.html:**
```html
{% extends 'layout.html' %}
{% block content %}
  <h1>Willkommen!</h1>
{% endblock %}
```

### Deployment (Veröffentlichung)

Damit deine Seite für alle erreichbar ist, musst du sie auf einem Server veröffentlichen. Beliebte Dienste sind Heroku, PythonAnywhere oder digitale Ozeane (DigitalOcean). Dafür brauchst du eine `requirements.txt` und oft ein `Procfile`.

---

## 💻 Übungen - Tag 26

1. Erstelle eine kleine Flask-Anwendung mit mindestens drei Seiten (Home, Über uns, Kontakt).
2. Nutze ein gemeinsames Layout für alle Seiten.
3. Erstelle eine Seite "Text-Analysator", die einen Text entgegennimmt (Formular) und die Anzahl der Wörter zählt.

🎉 HERZLICEN GLÜCKWUNSCH! 🎉

[<< Tag 25](./25_pandas_de.md) | [Tag 27 >>](./27_python_with_mongodb_de.md)
