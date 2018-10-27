teller = 1
GEWICHT = int(input("Geef het gewicht van de appel (in gram): "))
while teller < 101:
    gewicht = GEWICHT * teller
    print(str(teller) + "appel(s)"  + "= " + str(gewicht) + " gr.")
    teller += 1
