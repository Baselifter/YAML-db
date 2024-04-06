#               ██████╗░░░██╗██╗███████╗███╗░░██╗
#               ██╔══██╗░██╔╝██║╚════██║████╗░██║
#               ██████╔╝██╔╝░██║░░░░██╔╝██╔██╗██║
#               ██╔═══╝░███████║░░░██╔╝░██║╚████║
#               ██║░░░░░╚════██║░░██╔╝░░██║░╚███║
#               ╚═╝░░░░░░░░░░╚═╝░░╚═╝░░░╚═╝░░╚══╝
# ======================================================================
#	Code by:	Baselifter		Date:   06.04.2024
#	Version: 	1.0				Mail:	project.northstorm@gmail.com
#----------------------------------------------------------------------
#	License: DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#                    Version 2, December 2004
#
# 				  Copyright (C) 2004 Sam Hocevar
#  			  14 rue de Plaisance, 75014 Paris, France
# Everyone is permitted to copy and distribute verbatim or modified
# copies of this license document, and changing it is allowed as long
# 					  as the name is changed.
#
#            DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
#   TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION
#
#  				0. You just DO WHAT THE FUCK YOU WANT TO.
#----------------------------------------------------------------------

import yaml

class YamlDatabase:
    def __init__(self, filename):
        """
        Initialisiert die YAML-Datenbank mit dem angegebenen Dateinamen.
        :param filename: Der Dateiname der YAML-Datenbank.
        """
        self.filename = filename

    def insert_record(self, record):
        """
        Fügt einen neuen Datensatz zur YAML-Datenbank hinzu.
        :param record: Der Datensatz, der hinzugefügt werden soll.
        """
        with open(self.filename, 'a') as file:
            yaml.dump(record, file, default_flow_style=False)
            file.write('\n')

    def update_record(self, index, new_record):
        """
        Aktualisiert einen vorhandenen Datensatz in der YAML-Datenbank.
        :param index: Der Index des zu aktualisierenden Datensatzes.
        :param new_record: Der neue Datensatz, der anstelle des alten Datensatzes gespeichert werden soll.
        """
        records = self.get_all_records()
        if 0 <= index < len(records):
            records[index] = new_record
            with open(self.filename, 'w') as file:
                yaml.dump_all(records, file, default_flow_style=False)

    def delete_record(self, index):
        """
        Löscht einen Datensatz aus der YAML-Datenbank.
        :param index: Der Index des zu löschenden Datensatzes.
        """
        records = self.get_all_records()
        if 0 <= index < len(records):
            del records[index]
            with open(self.filename, 'w') as file:
                yaml.dump_all(records, file, default_flow_style=False)

    def get_record(self, index):
        """
        Ruft einen Datensatz aus der YAML-Datenbank ab.
        :param index: Der Index des abzurufenden Datensatzes.
        :return: Der abgerufene Datensatz oder None, wenn kein Datensatz gefunden wurde.
        """
        records = self.get_all_records()
        if 0 <= index < len(records):
            return records[index]
        else:
            return None

    def get_all_records(self):
        """
        Ruft alle Datensätze aus der YAML-Datenbank ab.
        :return: Eine Liste aller Datensätze in der YAML-Datenbank.
        """
        try:
            with open(self.filename, 'r') as file:
                records = list(yaml.safe_load_all(file))
                return records if records else []
        except FileNotFoundError:
            return []

    def search_record(self, key, value):
        """
        Sucht nach einem Datensatz in der YAML-Datenbank anhand eines bestimmten Schlüssel-Wert-Paares.
        :param key: Der Schlüssel, nach dem gesucht werden soll.
        :param value: Der Wert, nach dem gesucht werden soll.
        :return: Der gefundene Datensatz oder None, wenn kein Datensatz gefunden wurde.
        """
        records = self.get_all_records()
        for record in records:
            if record.get(key) == value:
                return record
        return None

    def filter_records(self, key, value):
        """
        Filtert alle Datensätze in der YAML-Datenbank basierend auf einem bestimmten Schlüssel-Wert-Paar.
        :param key: Der Schlüssel, nach dem gefiltert werden soll.
        :param value: Der Wert, nach dem gefiltert werden soll.
        :return: Eine Liste von Datensätzen, die dem Filterkriterium entsprechen.
        """
        records = self.get_all_records()
        filtered_records = []
        for record in records:
            if record.get(key) == value:
                filtered_records.append(record)
        return filtered_records

# Beispiel zur Verwendung der Bibliothek
if __name__ == "__main__":
    db = YamlDatabase("database.yaml")

    # Beispiel für das Einfügen eines Datensatzes
    db.insert_record({"name": "John", "age": 30, "city": "New York"})
    db.insert_record({"name": "Alice", "age": 25, "city": "Los Angeles"})
    db.insert_record({"name": "Bob", "age": 35, "city": "New York"})

    # Beispiel für das Suchen eines Datensatzes
    search_result = db.search_record("name", "John")
    if search_result:
        print("Search Result:", search_result)
    else:
        print("Record not found.")

    # Beispiel für das Filtern von Datensätzen
    filtered_records = db.filter_records("city", "New York")
    if filtered_records:
        print("Filtered Records:", filtered_records)
    else:
        print("No records found for the filter criteria.")
