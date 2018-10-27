def bereken_kost(oppervlakte):
    return round(oppervlakte / 160) * 12.5 #round voor de uitbreiding

def bereken_aantal_personen(oppervlakte):
    uren = oppervlakte / 160
    aantal8 = uren // 8
    rest = uren - aantal8 * 8
    if aantal8 != 0:
        if aantal8 == 1:
            print("1 persoon werkt 8 uur")
        else:
            print(aantal8, "personen werken 8 uur")
    if rest != 0:
        print("1 persoon werkt ", round(rest, 1), "uren")

m2 = float(input("Geef het aantal m2 dat gekuist moet worden "))

while m2 != 0:
    kost = bereken_kost(m2)
    print("het kuisen van deze oppervlakte kost", kost, "euro")
    bereken_aantal_personen(m2)
    m2 = float(input("Geef het aantal m2 dat gekuist moet worden "))

























