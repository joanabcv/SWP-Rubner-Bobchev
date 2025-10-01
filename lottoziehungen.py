import random

def lottoziehung():
    zahlen = range(1, 46)
    ziehung = random.sample(zahlen, 6)
    ziehung.sort()
    return ziehung

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
print("Statistik - 1000 Ziehungen:", statistik(1000))
