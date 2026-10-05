<div align="center">
  <h1> 30 Tage Python: Tag 19 - Dateiverarbeitung (File Handling)</h1>
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

[<< Tag 18](./18_regular_expressions_de.md) | [Tag 20 >>](./20_python_package_manager_de.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Tag 19](#-tag-19)
  - [Dateiverarbeitung](#dateiverarbeitung)
    - [Dateien zum Lesen öffnen](#dateien-zum-lesen-öffnen)
    - [Dateien zum Schreiben und Aktualisieren öffnen](#dateien-zum-schreiben-und-aktualisieren-öffnen)
    - [Dateien löschen](#dateien-löschen)
  - [Dateitypen](#dateitypen)
    - [TXT-Dateien](#txt-dateien)
    - [JSON-Dateien](#json-dateien)
    - [CSV-Dateien](#csv-dateien)
    - [XML-Dateien](#xml-dateien)
  - [💻 Übungen - Tag 19](#-übungen---tag-19)

# 📘 Tag 19

## Dateiverarbeitung

Bisher haben wir Daten nur im Arbeitsspeicher gehalten. Um Daten dauerhaft zu speichern, nutzen wir Dateien. Python bietet die eingebaute Funktion `open()`, um Dateien zu erstellen, zu lesen, zu aktualisieren und zu löschen.

```python
# Syntax
open('dateiname', modus)
```

**Die verschiedenen Modi:**
- `"r"` (Read): Standardwert. Öffnet zum Lesen. Fehler, wenn Datei fehlt.
- `"a"` (Append): Fügt am Ende hinzu. Erstellt Datei, falls nötig.
- `"w"` (Write): Überschreibt den Inhalt. Erstellt Datei, falls nötig.
- `"x"` (Create): Erstellt neue Datei. Fehler, wenn Datei bereits existiert.
- `"t"` (Text): Standardwert (Textmodus).
- `"b"` (Binary): Binärmodus (z. B. für Bilder).

### Dateien zum Lesen öffnen

Es wird empfohlen, das `with`-Statement zu nutzen, da es die Datei automatisch schließt.

```python
with open('./files/beispiel.txt') as f:
    inhalt = f.read()
    print(inhalt)
```

**Methoden zum Lesen:**
- `read()`: Liest die gesamte Datei als String.
- `readline()`: Liest nur die erste Zeile.
- `readlines()`: Liest alle Zeilen und gibt eine Liste zurück.

### Dateien zum Schreiben und Aktualisieren öffnen

```python
# Hinzufügen (Append)
with open('./files/beispiel.txt', 'a') as f:
    f.write('\nDieser Text wird hinten angehängt.')

# Überschreiben (Write)
with open('./files/neu.txt', 'w') as f:
    f.write('Dies ist eine neue Datei.')
```

### Dateien löschen

Hierfür nutzen wir das `os`-Modul:
```python
import os
if os.path.exists('test.txt'):
    os.remove('test.txt')
```

## Dateitypen

### JSON-Dateien
JSON (JavaScript Object Notation) ist das Standardformat für den Datenaustausch im Web. In Python entspricht es fast exakt einem Dictionary.

- `json.loads(json_string)`: Wandelt JSON in ein Python-Dictionary um.
- `json.dumps(dictionary)`: Wandelt ein Dictionary in einen JSON-String um.
- `json.dump(data, file)`: Speichert Daten direkt in eine JSON-Datei.

### CSV-Dateien
CSV (Comma Separated Values) speichert tabellarische Daten. Python hat dafür das `csv`-Modul.

### XML-Dateien
XML ist ein strukturiertes Format (ähnlich wie HTML). Wir nutzen `xml.etree.ElementTree`, um XML zu verarbeiten.

---

## 💻 Übungen - Tag 19

### Level 1
1. Schreibe eine Funktion, die Zeilen und Wörter in einem Text zählt. Teste sie mit den Reden von Obama, Michelle Obama, Donald Trump und Melina Trump (Dateien im `data`-Ordner).
2. Finde die 10 am häufigsten gesprochenen Sprachen aus der `countries_data.json`.
3. Finde die 10 bevölkerungsreichsten Länder aus der `countries_data.json`.

### Level 2
1. Extrahiere alle E-Mail-Adressen aus der Datei `email_exchange_big.txt` als Liste.
2. Finde die häufigsten Wörter in der englischen Sprache basierend auf einer Textdatei.
3. Vergleiche die Reden von Michelle Obama und Melina Trump auf Ähnlichkeit. (Tipp: Berechne die Worthäufigkeiten und vergleiche sie).

🎉 HERZLICEN GLÜCKWUNSCH! 🎉

[<< Tag 18](./18_regular_expressions_de.md) | [Tag 20 >>](./20_python_package_manager_de.md)
