def input_hoogte():
    heigth = float(input("Geef hier de hoogte van de poort: "))
    while heigth < 2 or heigth > 6.5:
        if heigth < 2:
            print("De opgegeven hoogte is te klein,", end=" ")
        elif heigth > 6.5:
            print("De opgegeven hoogte is te groot,", end=" ")
        heigth = float(input("Probeer het opnieuw: "))
    return heigth


def input_breedte():
    width = float(input("Geef hier de breedte van de poort: "))
    while width < 2 or width > 8:
        if width < 2:
            print("De opgegeven breedte is te klein,", end=" ")
        elif width > 8:
            print("De opgegeven breedte is te groot,", end=" ")
        width = float(input("Probeer het opnieuw: "))
    return width


def bereken_oppervlakte(hoogte, breedte):
    surface = hoogte * breedte
    return surface


def bereken_gewicht(oppervlakte):
    weight = oppervlakte * 11
    return weight


def bepaal_motor(gewicht):
    if gewicht < 150:
        engine = "A101"
    elif gewicht < 300:
        engine = "A105"
    else:
        engine = "X300"
    return engine


def bereken_prijs(oppervlakte, speciale_kleur, motor):
    motor_cost = 0
    if motor == "A101":
        motor_cost = 120
    elif motor == "A105":
        motor_cost = 220.5
    elif motor == "X300":
        motor_cost = 250.5

    total_price = oppervlakte * 113.5 + motor_cost
    if speciale_kleur:
        total_price = (total_price - motor_cost) * 1.10 + motor_cost
    return total_price


def genereer_offertenummer(naam_verkoper, prijs):
     return "{}_{}_{}".format("2018", str(naam_verkoper), str(round(prijs))[::-1])


naam_verkoper = input("Geef de naam van de verkoper: ")
hoogte = input_hoogte()
breedte = input_breedte()
speciale_kleur = input("Wilt u een speciale kleur? (j/n) ") == "j"
oppervlakte = bereken_oppervlakte(hoogte, breedte)
gewicht = bereken_gewicht(oppervlakte)
motor = bepaal_motor(gewicht)
prijs = bereken_prijs(oppervlakte, speciale_kleur, motor)
print(genereer_offertenummer(naam_verkoper, prijs))
print("Oppervlakte: {:.2f}".format(oppervlakte))
print("Gewicht: {:.2f}".format(gewicht))
print("Motor: {}".format(motor))
print("Prijs: {:.2f}".format(prijs))
