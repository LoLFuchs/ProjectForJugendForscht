# Dies dient zur veranschaulichung des Systems welches am Ende den Scanner darstellen wird um Hausaufgaben Hoch bzw. zu lesen

import Datenbank


# KS = Klasse Schüler 
# KL = Klasse Lehrer



def Trigger(Rolle, KL, value):

    if Rolle == "Lehrer":
        class_list = "Datenbank." + KL
        exec(f"{class_list}.append('{value}')")
        print(Datenbank.K8A)

    elif Rolle == "Schueler": 
          print("Deine Hausaufgaben sind:")
    
#Trigger(Input, "Hausaufgaben") # Triggern der Founktion // Entweder auf der NFC Card speichern / oder im System.py ausfühern

