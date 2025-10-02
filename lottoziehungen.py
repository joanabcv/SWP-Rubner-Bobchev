import random

def lottoziehung():
    gezogene_zahlen = []

    for i in range(6):
        zahl = random.randint(1,45)
        while zahl in gezogene_zahlen:
            zahl = random.randint(1,45)
        gezogene_zahlen.append(zahl)

    gezogene_zahlen.sort()
    return gezogene_zahlen
    
def statistik(ziehungen=1000):
    zaehler = {}        #Dictionary
    for zahl in range(1,46):
        zaehler[zahl] = 0  #Anfangswert 0

    for j in range(ziehungen):
        aktuelle_ziehung = lottoziehung()

        for zahl in aktuelle_ziehung:
            zaehler[zahl] =zaehler[zahl] + 1  #bei jeder Ziehung +1
    return zaehler

print("Lottoziehung:", lottoziehung())
print("Statistik (1000 Ziehungen):", statistik(1000))
