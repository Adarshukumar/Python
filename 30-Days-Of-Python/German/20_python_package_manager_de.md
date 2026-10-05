<div align="center">
  <h1> 30 Tage Python: Tag 20 - PIP & Paket-Manager</h1>
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

[<< Tag 19](./19_file_handling_de.md) | [Tag 21 >>](./21_classes_and_objects_de.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Tag 20](#-tag-20)
  - [Python PIP - Der Paket-Manager](#python-pip---der-paket-manager)
    - [Was ist PIP?](#was-ist-pip)
    - [Pakete installieren](#pakete-installieren)
    - [Pakete deinstallieren und auflisten](#pakete-deinstallieren-und-auflisten)
    - [PIP Freeze & requirements.txt](#pip-freeze--requirementstxt)
    - [Lesen von URLs (Requests)](#lesen-von-urls-requests)
    - [Ein eigenes Paket erstellen](#ein-eigenes-paket-erstellen)
  - [Beliebte Python Pakete](#beliebte-python-pakete)
  - [💻 Übungen - Tag 20](#-übungen---tag-20)

# 📘 Tag 20

## Python PIP - Der Paket-Manager

### Was ist PIP?
PIP steht für "Preferred Installer Program". Wir nutzen `pip`, um zusätzliche Python-Pakete zu installieren. Ein **Paket** ist eine Sammlung von Modulen. In der Programmierung müssen wir das Rad nicht neu erfinden – wir nutzen Pakete, die andere bereits für uns geschrieben haben.

### Pakete installieren

Um ein Paket (z. B. `numpy` für Mathematik oder `requests` für das Web) zu installieren, nutzt du dein Terminal:
```shell
pip install numpy
pip install requests
```

### Pakete deinstallieren und auflisten

- Deinstallieren: `pip uninstall paketname`
- Auflisten: `pip list`
- Details anzeigen: `pip show paketname`

### PIP Freeze & requirements.txt

Wenn du ein Projekt veröffentlichst, möchtest du anderen mitteilen, welche Pakete sie brauchen.
```shell
pip freeze > requirements.txt
```
Die Datei `requirements.txt` enthält alle installierten Pakete und deren Versionen.

### Lesen von URLs (Requests)

Um Daten aus dem Internet oder von einer API zu laden, nutzen wir das Paket `requests`.

```python
import requests
url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt'
response = requests.get(url)
print(response.status_code) # 200 bedeutet Erfolg
print(response.text) # Zeigt den Text der Webseite an
```

### Ein eigenes Paket erstellen

Ein Paket ist einfach ein Ordner, der eine spezielle Datei namens `__init__.py` enthält. Diese Datei sagt Python: "Dieser Ordner ist ein Paket".

Struktur:
```
mypackage/
    ├── __init__.py
    ├── arithmetic.py
    └── greet.py
```

## Beliebte Python Pakete

- **Datenanalyse:** `numpy`, `pandas`, `matplotlib`
- **Web-Entwicklung:** `Django`, `Flask`
- **Web Scraping:** `BeautifulSoup`, `requests`
- **Machine Learning:** `TensorFlow`, `scikit-learn`, `PyTorch`
- **Datenbanken:** `SQLAlchemy`

---

## 💻 Übungen - Tag 20

1. Lies eine Textdatei von einer URL (z. B. Romeo & Julia von Projekt Gutenberg) und finde die 10 häufigsten Wörter.
2. Nutze die [Cats API](https://api.thecatapi.com/v1/breeds):
   - Berechne Minimum, Maximum und Durchschnittsgewicht der Katzenrassen.
   - Berechne die durchschnittliche Lebenserwartung.
   - Erstelle eine Tabelle, welche Rassen aus welchen Ländern kommen.
3. Nutze die [Countries API](https://restcountries.com/v2/all) (Hinweis: URL kann variieren):
   - Finde die 10 größten Länder.
   - Finde die 10 meistgesprochenen Sprachen.
   - Zähle die Gesamtzahl aller Sprachen.
4. Versuche, die UCI Machine Learning Repository Webseite mit `BeautifulSoup` zu analysieren (Bonusaufgabe).

🎉 HERZLICEN GLÜCKWUNSCH! 🎉

[<< Tag 19](./19_file_handling_de.md) | [Tag 21 >>](./21_classes_and_objects_de.md)
