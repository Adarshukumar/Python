<div align="center">
  <h1> 30 Tage Python: Tag 22 - Web Scraping</h1>
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

[<< Tag 21](./21_classes_and_objects_de.md) | [Tag 23 >>](./23_virtual_environment_de.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Tag 22](#-tag-22)
  - [Python Web Scraping](#python-web-scraping)
    - [Was ist Web Scraping?](#was-ist-web-scraping)
    - [Werkzeuge: BeautifulSoup und Requests](#werkzeuge-beautifulsoup-und-requests)
  - [💻 Übungen - Tag 22](#-übungen---tag-22)

# 📘 Tag 22

## Python Web Scraping

### Was ist Web Scraping?

Das Internet ist voll von riesigen Datenmengen, die für verschiedene Zwecke genutzt werden können. Um diese Daten automatisiert zu sammeln, nutzen wir Web Scraping. **Web Scraping** ist der Prozess, bei dem Daten von Webseiten extrahiert, gesammelt und auf dem lokalen Computer oder in einer Datenbank gespeichert werden.

### Werkzeuge: BeautifulSoup und Requests

Um mit dem Scraping zu beginnen, benötigen wir zwei Pakete:
1. **Requests:** Um die Webseite herunterzuladen.
2. **BeautifulSoup4:** Um den HTML-Code der Seite zu analysieren und die gewünschten Informationen zu finden.

```shell
pip install requests
pip install beautifulsoup4
```

Um erfolgreich zu scrapen, ist ein Grundverständnis von HTML-Tags (wie `<table>`, `<tr>`, `<td>`, `<a>`) und CSS-Selektoren (Klassen und IDs) hilfreich.

**Beispiel:**
```python
import requests
from bs4 import BeautifulSoup

url = 'https://archive.ics.uci.edu/ml/datasets.php'
response = requests.get(url)
content = response.content # HTML-Inhalt der Seite

soup = BeautifulSoup(content, 'html.parser')
print(soup.title.get_text()) # Gibt den Titel der Webseite aus

# Tabellen finden
tables = soup.find_all('table', {'cellpadding': '3'})
table = tables[0]
for tr in table.find_all('tr'):
    tds = tr.find_all('td')
    for td in tds:
        print(td.text)
```

---

## 💻 Übungen - Tag 22

1. Scrape die folgende Webseite und speichere die Daten als JSON-Datei: `http://www.bu.edu/president/boston-university-facts-stats/`.
2. Extrahiere die Tabelle aus dieser URL: `https://archive.ics.uci.edu/ml/datasets.php` und wandle sie in eine JSON-Datei um.
3. Scrape die Tabelle der US-Präsidenten von Wikipedia und speichere sie als JSON: `https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States`. (Hinweis: Dies ist eine fortgeschrittene Aufgabe, da Wikipedia-Tabellen oft komplex strukturiert sind).

🎉 HERZLICEN GLÜCKWUNSCH! 🎉

[<< Tag 21](./21_classes_and_objects_de.md) | [Tag 23 >>](./23_virtual_environment_de.md)
