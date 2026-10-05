<div align="center">
  <h1> 30 Tage Python: Tag 16 - Python Datum und Zeit</h1>
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

[<< Tag 15](./15_python_type_errors_de.md) | [Tag 17 >>](./17_exception_handling_de.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Tag 16](#-tag-16)
  - [Python datetime](#python-datetime)
    - [Aktuelle Zeit abrufen](#aktuelle-zeit-abrufen)
    - [Datum formatieren mit strftime](#datum-formatieren-mit-strftime)
    - [Strings in Zeit umwandeln mit strptime](#strings-in-zeit-umwandeln-mit-strptime)
    - [Datumsobjekte (date)](#datumsobjekte-date)
    - [Zeitobjekte (time)](#zeitobjekte-time)
    - [Zeitdifferenzen (Timedelta)](#zeitdifferenzen-timedelta)
  - [💻 Übungen - Tag 16](#-übungen---tag-16)

# 📘 Tag 16

## Python datetime

Python nutzt das Modul `datetime`, um mit Datum und Uhrzeit zu arbeiten.

```python
import datetime
print(dir(datetime)) # Listet alle verfügbaren Funktionen auf
```

Wir konzentrieren uns auf die wichtigsten Klassen: `date`, `datetime`, `time` und `timedelta`.

### Aktuelle Zeit abrufen

```python
from datetime import datetime
now = datetime.now()
print(now) # 2021-07-08 07:34:46.549883
day = now.day
month = now.month
year = now.year
timestamp = now.timestamp() # Unix-Zeitstempel (Sekunden seit 1.1.1970)
```

### Datum formatieren mit strftime

Mit `strftime` kannst du bestimmen, wie ein Datum als Text dargestellt wird. Die Symbole (wie `%d`, `%m`, `%Y`) findest du auf [strftime.org](https://strftime.org/).

```python
from datetime import datetime
now = datetime.now()
formatted = now.strftime("%d.%m.%Y, %H:%M:%S")
print(formatted) # 08.07.2021, 07:34:46
```

### Strings in Zeit umwandeln mit strptime

Wenn du ein Datum als Text hast, kannst du es in ein Python-Objekt umwandeln:
```python
from datetime import datetime
date_string = "5 December, 2019"
date_obj = datetime.strptime(date_string, "%d %B, %Y")
print(date_obj) # 2019-12-05 00:00:00
```

### Datumsobjekte (date)

Wenn du nur das Datum ohne Uhrzeit brauchst:
```python
from datetime import date
today = date.today()
print(today.year, today.month, today.day)
```

### Zeitobjekte (time)

Wenn du nur die Uhrzeit brauchst:
```python
from datetime import time
t = time(10, 30, 50)
print(t) # 10:30:50
```

### Zeitdifferenzen (Timedelta)

Du kannst Zeiträume addieren oder subtrahieren:
```python
from datetime import datetime, timedelta
now = datetime.now()
in_one_week = now + timedelta(weeks=1)
print(in_one_week)
```

Berechnung der Differenz zwischen zwei Zeitpunkten:
```python
t1 = datetime(2020, 1, 1)
t2 = datetime.now()
diff = t2 - t1
print(f"Seit Neujahr 2020 sind {diff.days} Tage vergangen.")
```

---

## 💻 Übungen - Tag 16

1. Rufe den aktuellen Tag, Monat, Jahr, Stunde, Minute und den Zeitstempel ab.
2. Formatiere das aktuelle Datum im Format: `"%m/%d/%Y, %H:%M:%S"`.
3. Wandle den String "5 December, 2019" in ein Zeitobjekt um.
4. Berechne die verbleibende Zeit bis zum nächsten Neujahr.
5. Berechne die Differenz zwischen dem 1. Januar 1970 und dem heutigen Tag.
6. Überlege: Wofür braucht man das `datetime` Modul im echten Leben? (Beispiele: Blog-Posts, Logs, Zeitreihenanalyse).

🎉 HERZLICEN GLÜCKWUNSCH! 🎉

[<< Tag 15](./15_python_type_errors_de.md) | [Tag 17 >>](./17_exception_handling_de.md)
