## YAML Database Library (yaml_db)
The YAML Database Library (yaml_db) is a Python library that allows you to create and manage a simple database based on YAML files. The library provides basic CRUD (Create, Read, Update, Delete) operations as well as functions for searching, filtering, and indexing records.

Installation
You can install the library using the Python package manager pip:

`` pip install yaml-db ``
Usage
To use the YAML Database Library in your Python project, you first need to import it:


`` from yaml_db import YamlDatabase ``
Initialization
To create a YAML database, create an instance of the YamlDatabase class and specify the filename of the YAML file to be used as the database:

`` db = YamlDatabase("database.yaml") ``
Record Operations
The YamlDatabase class provides the following methods for managing records:

insert_record(record): Adds a new record to the database.
update_record(index, new_record): Updates an existing record in the database.
delete_record(index): Deletes a record from the database.
get_record(index): Retrieves a record from the database.
get_all_records(): Retrieves all records from the database.
Searching and Filtering
The library also provides methods for searching and filtering records:

search_record(key, value): Searches for a record based on a specific key-value pair.
filter_records(key, value): Filters all records in the database based on a specific key-value pair.
Example
Here's a simple example demonstrating the usage of the YAML Database Library:


```python 
from yaml_db import YamlDatabase

# Initialize the database
db = YamlDatabase("database.yaml")

# Insert records
db.insert_record({"name": "John", "age": 30, "city": "New York"})
db.insert_record({"name": "Alice", "age": 25, "city": "Los Angeles"})
db.insert_record({"name": "Bob", "age": 35, "city": "New York"})

# Search for a record
search_result = db.search_record("name", "John")
if search_result:
    print("Search Result:", search_result)
else:
    print("Record not found.")

# Filter records
filtered_records = db.filter_records("city", "New York")
if filtered_records:
    print("Filtered Records:", filtered_records)
else:
    print("No records found for the filter criteria.")
```
This example demonstrates inserting records into the database, searching for a specific record, and filtering records based on a specific criterion.

That's the manual for the YAML Database Library. If you need further information or have any questions, feel free to consult the documentation or reach out to the developer.


---

German Version:

YAML-Datenbankbibliothek (yaml_db)
Die YAML-Datenbankbibliothek (yaml_db) ist eine Python-Bibliothek, die es ermöglicht, eine einfache Datenbank auf Basis von YAML-Dateien zu erstellen und zu verwalten. Die Bibliothek bietet grundlegende CRUD-Operationen (Create, Read, Update, Delete) sowie Funktionen zum Suchen, Filtern und Indizieren von Datensätzen.

Installation
Die Bibliothek kann mit dem Python-Paketmanager pip installiert werden:


`` pip install yaml-db ``
Verwendung
Um die YAML-Datenbankbibliothek in Ihrem Python-Projekt zu verwenden, müssen Sie sie zuerst importieren:


`` from yaml_db import YamlDatabase ``
Initialisierung
Um eine YAML-Datenbank zu erstellen, erstellen Sie zunächst eine Instanz der YamlDatabase-Klasse und geben Sie den Dateinamen der YAML-Datei an, die als Datenbank verwendet werden soll:


`` db = YamlDatabase("database.yaml") ``
Datensatzoperationen
Die YamlDatabase-Klasse bietet folgende Methoden zur Verwaltung von Datensätzen:

insert_record(record): Fügt einen neuen Datensatz zur Datenbank hinzu.
update_record(index, new_record): Aktualisiert einen vorhandenen Datensatz in der Datenbank.
delete_record(index): Löscht einen Datensatz aus der Datenbank.
get_record(index): Ruft einen Datensatz aus der Datenbank ab.
get_all_records(): Ruft alle Datensätze aus der Datenbank ab.
Suchen und Filtern
Die Bibliothek bietet auch Methoden zum Suchen und Filtern von Datensätzen:

search_record(key, value): Sucht nach einem Datensatz anhand eines bestimmten Schlüssel-Wert-Paares.
filter_records(key, value): Filtert alle Datensätze in der Datenbank basierend auf einem bestimmten Schlüssel-Wert-Paar.
Beispiel
Hier ist ein einfaches Beispiel für die Verwendung der YAML-Datenbankbibliothek:

```
from yaml_db import YamlDatabase

# Initialisierung der Datenbank
db = YamlDatabase("database.yaml")

# Einfügen von Datensätzen
db.insert_record({"name": "John", "age": 30, "city": "New York"})
db.insert_record({"name": "Alice", "age": 25, "city": "Los Angeles"})
db.insert_record({"name": "Bob", "age": 35, "city": "New York"})

# Suchen nach einem Datensatz
search_result = db.search_record("name", "John")
if search_result:
    print("Search Result:", search_result)
else:
    print("Record not found.")

# Filtern von Datensätzen
filtered_records = db.filter_records("city", "New York")
if filtered_records:
    print("Filtered Records:", filtered_records)
else:
    print("No records found for the filter criteria.")
```

Dieses Beispiel demonstriert das Einfügen von Datensätzen in die Datenbank, das Suchen nach einem bestimmten Datensatz und das Filtern von Datensätzen basierend auf einem bestimmten Kriterium.
