totaal_premie = 0
personal_premie = 0
hoogste_premie = 0
familienaam = input("Geef hier uw familienaam:")
while familienaam != "/":
    voornaam = input("Geef hier uw voornaam in:")
    aantal_dienstjaren = int(input("Geef het aantal gewerkte jaren:"))
    if aantal_dienstjaren < 5:
        personal_premie = 0
        print("geen premie")
    else:
        personal_premie = aantal_dienstjaren * 25
        if personal_premie > hoogste_premie:
            hoogste_premie = personal_premie
        totaal_premie += personal_premie
        print(familienaam, voornaam, "\n", "Het aantal jaren in dienst:", aantal_dienstjaren, "\n", "Uw premie bedraagt", personal_premie, "euro")
    familienaam = input("Geef hier uw familienaam:")
if familienaam == "/":
    print("De hoogste te betalen premie is:", hoogste_premie)
    print("De totaal te betalen premies bedragen:", totaal_premie)
