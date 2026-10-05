<div align="center">
  <h1> 30 Tage Python: Tag 23 - Virtuelle Umgebungen</h1>
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

[<< Tag 22](./22_web_scraping_de.md) | [Tag 24 >>](./24_statistics_de.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Tag 23](#-tag-23)
  - [Virtuelle Umgebungen einrichten](#virtuelle-umgebungen-einrichten)
    - [Warum eine virtuelle Umgebung?](#warum-eine-virtuelle-umgebung)
    - [Erstellung und Aktivierung](#erstellung-und-aktivierung)
  - [💻 Übungen - Tag 23](#-übungen---tag-23)

# 📘 Tag 23

## Virtuelle Umgebungen einrichten

Bevor du mit einem neuen Projekt beginnst, ist es ratsam, eine **virtuelle Umgebung (Virtual Environment)** zu erstellen. Diese hilft dir dabei, ein isoliertes System für jedes Projekt zu schaffen. Ohne virtuelle Umgebung würden sich die Pakete verschiedener Projekte gegenseitig stören oder Konflikte verursachen.

### Warum eine virtuelle Umgebung?
Wenn du `pip freeze` in deinem normalen Terminal eingibst, siehst du alle Pakete, die global auf deinem Computer installiert sind. In einer virtuellen Umgebung siehst du nur die Pakete, die du **explizit für dieses eine Projekt** installiert hast.

### Erstellung und Aktivierung

1. **Erstellen:**
   Gehe in deinen Projektordner und gib folgenden Befehl ein:

   - **Windows:** `python -m venv venv`
   - **Mac/Linux:** `python3 -m venv venv`

2. **Aktivieren:**
   Nach der Erstellung musst du die Umgebung aktivieren:

   - **Windows (PowerShell):** `.\venv\Scripts\Activate.ps1`
   - **Windows (Git Bash/CMD):** `source venv/Scripts/activate`
   - **Mac/Linux:** `source venv/bin/activate`

Sobald die Umgebung aktiviert ist, erscheint ein `(venv)` vor deiner Eingabeaufforderung im Terminal.

**Beispiel:**
```shell
(venv) user@computer:~/mein_projekt$ pip install Flask
```
Jetzt ist `Flask` nur in diesem Projekt verfügbar.

3. **Deaktivieren:**
   Wenn du fertig bist, kannst du die Umgebung mit dem Befehl `deactivate` verlassen.

**Wichtig:** Du solltest den Ordner `venv/` niemals in dein GitHub-Repository hochladen. Füge ihn stattdessen zu deiner `.gitignore` Datei hinzu.

---

## 💻 Übungen - Tag 23

1. Erstelle einen neuen Ordner für ein Projekt (z. B. `mein_test_projekt`).
2. Erstelle darin eine virtuelle Umgebung.
3. Aktiviere sie und installiere ein beliebiges Paket (z. B. `requests`).
4. Prüfe mit `pip freeze`, ob das Paket installiert ist.
5. Deaktiviere die Umgebung wieder.

🎉 HERZLICEN GLÜCKWUNSCH! 🎉

[<< Tag 22](./22_web_scraping_de.md) | [Tag 24 >>](./24_statistics_de.md)
