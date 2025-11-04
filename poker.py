import random

farben = ["Herz", "Karo", "Pik", "Kreuz"]
werte = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Bube", "Dame", "König", "Ass"]
deck = [(wert, farbe) for farbe in farben for wert in werte]


def gib_fuenf_karten():
    return random.sample(deck, 5)

def ist_flush(karten):
    farben = [f for (w, f) in karten]
    return len(set(farben)) == 1

def ist_strasse(karten):
    reihenfolge = ["2","3","4","5","6","7","8","9","10","Bube","Dame","König","Ass"]
    werte_index = sorted([reihenfolge.index(w) for (w, f) in karten])
    zaehler = 1
    for i in range(1, len(werte_index)):
        if werte_index[i] == werte_index[i-1] + 1:
            zaehler += 1
            if zaehler == 5:
                return True
        else:
            zaehler = 1
    return False

def kombination(karten):
    werte = [w for (w, f) in karten]
    gleiche = {}
    for w in werte:
        gleiche[w] = gleiche.get(w, 0) + 1
    anzahl = sorted(gleiche.values(), reverse=True)

    if ist_flush(karten) and ist_strasse(karten):
        return "Straight Flush"
    elif anzahl == [4,1]:
        return "Vierling"
    elif anzahl == [3,2]:
        return "Full House"
    elif ist_flush(karten):
        return "Flush"
    elif ist_strasse(karten):
        return "Straße"
    elif anzahl == [3,1,1]:
        return "Drilling"
    elif anzahl == [2,2,1]:
        return "Zwei Paare"
    elif anzahl == [2,1,1,1]:
        return "Paar"
    else:
        return "Hohe Karte"

def poker_simulation(spiele=100000):
    ergebnisse = {
        "Paar": 0,
        "Zwei Paare": 0,
        "Drilling": 0,
        "Straße": 0,
        "Flush": 0,
        "Full House": 0,
        "Vierling": 0,
        "Straight Flush": 0,
        "Hohe Karte": 0
    }

    for _ in range(spiele):
        hand = gib_fuenf_karten()
        erg = kombination(hand)
        ergebnisse[erg] += 1

    print("\nPoker Statistik bei 10000")
    for name, anzahl in ergebnisse.items():
        prozent = anzahl / spiele * 100
        print(f"{name:15}: {anzahl:8d} ({prozent:7.4f} %)")


def main():
    poker_simulation(100000)


if __name__ == "__main__":
    main()
