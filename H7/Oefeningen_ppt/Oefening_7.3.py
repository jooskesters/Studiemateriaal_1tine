getal = int(input("Geef hier een getal in: "))
getallenlijst = []
while getal != 0:
    if getal in getallenlijst:
        getallenlijst.remove(getal)
    else:
        getallenlijst.append(getal)
    print(getallenlijst)
    getal = int(input("Geef hier nog een getal in: "))

