<div align="center">
  <h1> 30 Tage Python: Tag 28 - API (Schnittstellen)</h1>
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

[<< Tag 27](./27_python_with_mongodb_de.md) | [Tag 29 >>](./29_building_API_de.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Tag 28](#-tag-28)
  - [Application Programming Interface (API)](#application-programming-interface-api)
    - [Was ist eine API?](#was-ist-eine-api)
    - [HTTP-Protokoll](#http-protokoll)
    - [Struktur von HTTP](#struktur-von-http)
    - [HTTP-Methoden](#http-methoden)
    - [Status-Codes](#status-codes)
  - [💻 Übungen - Tag 28](#-übungen---tag-28)

# 📘 Tag 28

## Application Programming Interface (API)

### Was ist eine API?

API steht für **Application Programming Interface** (Programmierschnittstelle). Eine Web-API ist eine definierte Schnittstelle, über die verschiedene Anwendungen miteinander kommunizieren können. Im Web-Kontext ist eine API oft eine Sammlung von Spezifikationen für HTTP-Anfragen, deren Antworten meist im **JSON**- oder XML-Format geliefert werden.

REST (Representational State Transfer) ist der heute am weitesten verbreitete Stil für Web-APIs.

### HTTP-Protokoll

HTTP (Hypertext Transfer Protocol) ist das Kommunikationsprotokoll zwischen einem **Client** (z. B. dein Browser) und einem **Server** (wo die Daten liegen).

### Struktur von HTTP

Jede Kommunikation folgt dem **Request-Response-Zyklus**:
1. Der Client sendet eine Anfrage (Request).
2. Der Server verarbeitet diese und sendet eine Antwort (Response).

Eine Nachricht besteht aus:
- Einer Startzeile (Methode/Pfad/Version).
- Header-Feldern (Metadaten wie `Content-Type`).
- Einem optionalen Body (die eigentlichen Daten, z. B. JSON).

### HTTP-Methoden

Um CRUD-Operationen (Erstellen, Lesen, Aktualisieren, Löschen) über eine API durchzuführen, nutzen wir:
1. **GET:** Daten abrufen/lesen.
2. **POST:** Neue Daten erstellen/senden.
3. **PUT:** Bestehende Daten aktualisieren/ersetzen.
4. **DELETE:** Daten löschen.

### Status-Codes

Der Server gibt immer einen Code zurück, der über den Erfolg informiert:
- **200 OK:** Alles hat geklappt.
- **201 Created:** Erfolgreich erstellt.
- **400 Bad Request:** Fehler in der Anfrage.
- **404 Not Found:** Ressource nicht gefunden.
- **500 Server Error:** Fehler auf dem Server.

---

## 💻 Übungen - Tag 28

1. Recherchiere und lies mehr über das HTTP-Protokoll und REST-APIs.
2. Suche nach drei öffentlichen APIs im Internet (z. B. Wetter, News, Pokémon) und schaue dir deren Dokumentation an.

🎉 HERZLICEN GLÜCKWUNSCH! 🎉

[<< Tag 27](./27_python_with_mongodb_de.md) | [Tag 29 >>](./29_building_API_de.md)
