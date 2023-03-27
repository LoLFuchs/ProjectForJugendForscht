import sqlite3
import time 
import Datenbank

# Verbindung zur SQLite-Datenbank herstellen
conn = sqlite3.connect('Datenbank.db')

# Tabelle 'schueler' erstellen, falls sie noch nicht existiert
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS schueler
             (name timport sqlite3
import time 
import Datenbank


menu = 0 # menu = 1 (Main Menu)

# Verbindung zur SQLite-Datenbank herstellen
conn = sqlite3.connect('Datenbank.db')

# Tabelle 'schueler' erstellen, falls sie noch nicht existiert
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS schueler
             (name text PRIMARY KEY, punkte integer, klasse text)''')
conn.commit()

def add_schueler(name, klasse): # neuen Schüler hinzufügen
    conn = sqlite3.connect('Datenbank.db')
    c = conn.cursor()
    c.execute("SELECT * FROM schueler WHERE name=?", (name,))
    result = c.fetchone()
    if result is None:
        c.execute("INSERT INTO schueler (name, punkte, klasse) VALUES (?, 0, ?)", (name, klasse))
        conn.commit()
        print("Herzlich Willkommen im " + Datenbank.NameSchule)
        time.sleep(4)
    conn.close()


def add_punkte(name, punkte): # add Punkte zu dem Schueler / Hausaufgaben fertig
    conn = sqlite3.connect('Datenbank.db')
    c = conn.cursor()
    c.execute("UPDATE schueler SET punkte = punkte + ? WHERE name=?", (punkte, name))
    conn.commit()
    print("added points to " + name)
    conn.close()
    
def get_punkte(name): #return Punkte des Schueler / later: left click on button to show on LCD in System.py
    conn = sqlite3.connect('Datenbank.db')
    c = conn.cursor()
    c.execute("SELECT punkte FROM schueler WHERE name=?", (name,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else 0

##########################################################################################################################
# Teacher or Student 

def Trigger(name, role, klasse, value): 
    #Save the parameter for later
    Sname = name
    Srole = role 
    Sklasse = klasse 
    Svalue = value 

    # Verbindung zur SQLite-Datenbank herstellen
    with sqlite3.connect('Datenbank.db') as conn:
        c = conn.cursor()

        # Platzhalter-Zeichen für den Tabellennamen im SQL-Befehl
        query = '''CREATE TABLE IF NOT EXISTS {} (name text PRIMARY KEY, punkte integer)'''.format(klasse)
        c.execute(query)

    if menu == 1: # MENU 1 FOR EVERYONE

        if role == "Lehrer":
            query = '''INSERT INTO {} VALUES (?, ?)'''.format(klasse)
            c.execute(query, (value, 1))

            print(f"{value} zu Klasse {klasse} hinzugefügt.")
       


        elif role == "Schueler":
            print(f"Guten Tag {name} =)")
            query = '''SELECT name FROM {}'''.format(klasse)
            c.execute(query)
            results = c.fetchall()

            if len(results) > 0:
                 class_list = [result[0] for result in results]
                 print(f"Die Hausaufgaben für {klasse} sind: {', '.join(class_list)}")
            else:
                 print(f"Keine Hausaufgaben für {klasse} gefunden.")

    elif menu == 0:
        if role == "Lehrer":
            print("nix")
        
        elif role == "Schueler":
            
            print(f"Du hast: {get_punkte(name)} Punkte")


    conn.commit()
    conn.close

def LeftClick(menu = menu):
    if Sname != "a":
        if menu > -1:  
            menu = menu - 1
            #Trigger(Sname,Srole,Sklasse,Svalue)
        
            print("Debug: " + str(menu))
        else: 
            print("Lege erst eine Karte ein")

def RightClick(menu = menu):
    if Sname != None:
        if menu < 3:  
             menu = menu + 1
        
        print("Debug: " + str(menu))
    else: 
        print("Lege erst eine Karte ein")

ext PRIMARY KEY, punkte integer, klasse text)''')
conn.commit()

def add_schueler(name, klasse): # neuen Schüler hinzufügen
    conn = sqlite3.connect('Datenbank.db')
    c = conn.cursor()
    c.execute("SELECT * FROM schueler WHERE name=?", (name,))
    result = c.fetchone()
    if result is None:
        c.execute("INSERT INTO schueler (name, punkte, klasse) VALUES (?, 0, ?)", (name, klasse))
        conn.commit()
        print("Herzlich Willkommen im " + Datenbank.NameSchule)
        time.sleep(4)
    conn.close()


def add_punkte(name, punkte): # add Punkte zu dem Schueler / Hausaufgaben fertig
    conn = sqlite3.connect('Datenbank.db')
    c = conn.cursor()
    c.execute("UPDATE schueler SET punkte = punkte + ? WHERE name=?", (punkte, name))
    conn.commit()
    print("added points to " + name)
    conn.close()
    
def get_punkte(name): #return Punkte des Schueler / later: left click on button to show on LCD in System.py
    conn = sqlite3.connect('Datenbank.db')
    c = conn.cursor()
    c.execute("SELECT punkte FROM schueler WHERE name=?", (name,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else 0

##########################################################################################################################
# Teacher or Student 

def Trigger(role, klasse, value): 
    # Verbindung zur SQLite-Datenbank herstellen
    with sqlite3.connect('Datenbank.db') as conn:
        c = conn.cursor()

        # Platzhalter-Zeichen für den Tabellennamen im SQL-Befehl
        query = '''CREATE TABLE IF NOT EXISTS {} (name text PRIMARY KEY, punkte integer)'''.format(klasse)
        c.execute(query)



        if role == "Lehrer":
            query = '''INSERT INTO {} VALUES (?, ?)'''.format(klasse)
            c.execute(query, (value, 1))

            print(f"{value} zu Klasse {klasse} hinzugefügt.")
       


        elif role == "Schueler":
            query = '''SELECT name FROM {}'''.format(klasse)
            c.execute(query)
            results = c.fetchall()

            if len(results) > 0:
                 class_list = [result[0] for result in results]
                 print(f"Die Hausaufgaben für {klasse} sind: {', '.join(class_list)}")
            else:
                 print(f"Keine Hausaufgaben für {klasse} gefunden.")
        conn.commit()
        conn.close


