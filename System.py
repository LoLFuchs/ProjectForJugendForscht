import sqlite3
import time 
import Datenbank

# Verbindung zur SQLite-Datenbank herstellen
conn = sqlite3.connect('Datenbank.db')

# Cursor-Objekt erstellen
c = conn.cursor()

# Tabelle 'schueler' erstellen, falls sie noch nicht existiert
c.execute('''CREATE TABLE IF NOT EXISTS schueler
             (name text PRIMARY KEY, punkte integer)''')

def add_schueler(name): # add schüeler if name != Datenbank
    c.execute("SELECT * FROM schueler WHERE name=?", (name,))
    result = c.fetchone()
    if result is None:
        c.execute("INSERT INTO schueler VALUES (?,?)", (name, 0))
        conn.commit()
        print("Herzlich Willkommen im " + Datenbank.NameSchule)
        time.sleep(4)
    
def add_punkte(name, punkte): # add Punkte zu dem Schueler / in System.py
    c.execute("UPDATE schueler SET punkte = punkte + ? WHERE name=?", (punkte, name))
    conn.commit()
    print("added points to " + name)
    
def get_punkte(name): #return Punkte des Schueler / later: click on button to show on LCD in System.py
    c.execute("SELECT punkte FROM schueler WHERE name=?", (name,))
    result = c.fetchone()
    return result[0] if result else 0

def Trigger(role, klasse, value): # Teacher or Student 
    class_list = getattr(Datenbank, klasse, None)

    if class_list is None:
        print(f"Klasse {klasse} nicht gefunden!")
        return

    if role == "Lehrer": #if role is lehrer do: 
        class_list.append(value)
        print(f"{value} zu Klasse {klasse} hinzugefügt.")
    elif role == "Schueler":
        if len(class_list) > 0:
            print(f"Deine Hausaufgaben für {klasse} sind: {', '.join(class_list)}")
        else:
            print(f"Keine Hausaufgaben für {klasse} gefunden.")
# Verbindung zur Datenbank schließen
conn.close()
