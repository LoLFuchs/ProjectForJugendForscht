# Beispielaufruf
# Könnte passieren das der Trigger im System ausgeführt werden muss
import System
import time

if __name__ == '__main__':
    name = "Leon Entoch"
    role = "Schueler"
    klasse = "K8A"
    ha = None
    System.add_schueler(name, klasse)
    System.Trigger(name ,role, klasse, ha)
    time.sleep(2)
    System.LeftClick()

