# Beispielaufruf
# Könnte passieren das der Trigger im System ausgeführt werden muss
import System

if __name__ == '__main__':
    name = "Max Mustermann"
    role = "Schueler"
    klasse = "K8A"
    ha = None
    System.add_schueler(name)
    System.Trigger(role, klasse, ha)

