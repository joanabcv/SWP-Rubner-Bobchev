def SetComp():
    noten = [1, 2, 3, 4, 5, 1, 2, 5]
    positive_Noten = {note for note in noten if note <= 4}
    return positive_Noten

def DicComp():
    personen = {"Annabell": 18, "Eva": 20, "Hans": 15}
    status = {
        name: ("Erwachsen" if alter >= 18 else "Kind")
        for name, alter in personen.items()
    }
    return status

def ListComp():
    namen = ["Annabell", "Eva", "Joana"]
    begruessung = ["Hallo "+name for name in namen]
    return begruessung

if __name__ == "__main__":
    print("\nSet Comprehention:")
    print(SetComp())

    print("\nDic Comprehention:")
    print(DicComp())

    print("\nList Comprehention:")
    print(ListComp())

