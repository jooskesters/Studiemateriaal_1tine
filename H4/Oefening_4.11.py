personeelsnummer = int(input("Geef hier uw personeelsnummer:"))
aantal_mannen_crit = 0
aantal_vrouwen_crit = 0
brutoloon = 0
while personeelsnummer != 0:
    geslacht = int(input("Als u een vrouw bent kiest u 0, als u een man bent kiest u 1:"))
    leeftijd = int (input("Geef hier uw leeftijd:"))
    if geslacht == 1:
        if leeftijd > 34:
            aantal_mannen_crit += 1
        elif leeftijd < 34:
            brutoloon = int(input("Geef hier uw brutoloon:"))
            if brutoloon >= 1800:
                aantal_mannen_crit += 1
    elif geslacht == 0:
        if leeftijd < 25:
            aantal_vrouwen_crit =+ 1
    personeelsnummer = int(input("Geef hier uw personeelsnummer:"))
print(aantal_mannen_crit)
print(aantal_vrouwen_crit)
