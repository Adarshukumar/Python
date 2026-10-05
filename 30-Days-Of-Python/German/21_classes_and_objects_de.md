<div align="center">
  <h1> 30 Tage Python: Tag 21 - Klassen und Objekte (OOP)</h1>
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

[<< Tag 20](./20_python_package_manager_de.md) | [Tag 22 >>](./22_web_scraping_de.md)

![30DaysOfPython](../images/30DaysOfPython_banner3@2x.png)

- [📘 Tag 21](#-tag-21)
  - [Klassen und Objekte](#klassen-und-objekte)
    - [Eine Klasse erstellen](#eine-klasse-erstellen)
    - [Ein Objekt erstellen](#ein-objekt-erstellen)
    - [Der Klassen-Konstruktor (__init__)](#der-klassen-konstruktor-init)
    - [Methoden eines Objekts](#methoden-eines-objekts)
    - [Standardwerte in Konstruktoren](#standardwerte-in-konstruktoren)
    - [Vererbung (Inheritance)](#vererbung-inheritance)
    - [Methoden überschreiben (Overriding)](#methoden-überschreiben-overriding)
  - [💻 Übungen - Tag 21](#-übungen---tag-21)

# 📘 Tag 21

## Klassen und Objekte

Python ist eine objektorientierte Programmiersprache (OOP). Alles in Python ist ein Objekt mit seinen Eigenschaften (Attributen) und Methoden. Eine Klasse ist wie ein "Bauplan" oder eine Konstruktionszeichnung zur Erstellung von Objekten. Wir instanziieren eine Klasse, um ein Objekt zu erzeugen.

### Eine Klasse erstellen

Wir nutzen das Schlüsselwort `class`. Klassennamen werden üblicherweise in **CamelCase** geschrieben.

```python
# Syntax
class ClassName:
    # Code hier
```

### Ein Objekt erstellen

```python
class Person:
    pass

p = Person() # Erstellt eine Instanz der Klasse Person
```

### Der Klassen-Konstruktor (__init__)

Die `__init__`-Methode ist eine spezielle Funktion, die automatisch aufgerufen wird, wenn ein neues Objekt erstellt wird. Sie initialisiert die Attribute des Objekts. Der Parameter `self` bezieht sich auf die aktuelle Instanz der Klasse.

```python
class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

p = Person('Asabeneh', 'Yetayeh')
print(p.firstname) # Asabeneh
```

### Methoden eines Objekts

Methoden sind Funktionen, die innerhalb einer Klasse definiert sind und auf das Objekt angewendet werden können.

```python
class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def info(self):
        return f'{self.firstname} ist {self.age} Jahre alt.'

p = Person('Asabeneh', 'Yetayeh', 250)
print(p.info())
```

### Vererbung (Inheritance)

Vererbung erlaubt es uns, eine Klasse zu definieren, die alle Methoden und Eigenschaften einer anderen Klasse (Elternklasse) übernimmt.

```python
class Student(Person): # Student erbt von Person
    def __init__(self, firstname, lastname, age, student_id):
        super().__init__(firstname, lastname, age) # Ruft den Konstruktor der Elternklasse auf
        self.student_id = student_id

s = Student('Eyob', 'Yetayeh', 30, 'S12345')
print(s.info()) # Nutzt die Methode von Person
```

---

## 💻 Übungen - Tag 21

### Level 1
1. Erstelle eine Klasse namens `Statistics`. Sie soll eine Liste von Zahlen entgegennehmen und Methoden für folgende statistische Berechnungen enthalten:
   - `count()`, `sum()`, `min()`, `max()`, `range()`, `mean()`, `median()`, `mode()`, `std()` (Standardabweichung), `var()` (Varianz).
   - Die Methode `describe()` soll eine Zusammenfassung aller Werte ausgeben.

### Level 2
1. Erstelle eine Klasse `PersonAccount`.
   - Eigenschaften: `firstname`, `lastname`, `incomes` (Menge aus Einkommen & Beschreibung), `expenses` (Menge aus Ausgaben & Beschreibung).
   - Methoden: `total_income()`, `total_expense()`, `account_info()`, `add_income()`, `add_expense()`, `account_balance()`.

🎉 HERZLICEN GLÜCKWUNSCH! 🎉

[<< Tag 20](./20_python_package_manager_de.md) | [Tag 22 >>](./22_web_scraping_de.md)
