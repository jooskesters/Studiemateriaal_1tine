def hotel_kosten(nachten):
    return nachten - (nachten // 3) * 140.50


def vliegtuig_kosten(stad):
    if stad == "Barcelona":
        return 183
    elif stad == "Rome":
        return 220
    elif stad == "Berlijn":
        return 125
    else:
        return 400


def huurauto_kosten(aantal_dagen):
    vast_auto = aantal_dagen * 40
    if aantal_dagen > 7:
        auto = vast_auto - 50
        return auto
    elif aantal_dagen < 7 and aantal_dagen > 3:
        auto = vast_auto - 20
        return auto
    else:
        auto = vast_auto
        return auto

def reis_kosten(stad, aantal_dagen):
    if stad !="Barcelona" and stad !="Rome" and stad !="Berlijn" and stad!="Oslo":
        print("foutboodschap")
    else:
         hotel_kosten(nachten)+ huurauto_kosten(aantal_dagen) + vliegtuig_kosten(stad)


a = int(input("Geef hier het aantal nachten in:"))
b = str(input("Geef hier de verblijfplaats in"))
c = a + 1 #aantal dagen

print(reis_kosten(b,c))
print(hotel_kosten(a))