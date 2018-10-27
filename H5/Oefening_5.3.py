def lidgeld_tennisclub(leeftijd, aantal_kinderen_ten_laste, inkomen, aansluitingsjaar):
    normaal_aanvangsgeld = int(100)
    if leeftijd > 60:
        normaal_aanvangsgeld -= 15
    if aantal_kinderen_ten_laste > 0:
        max(aantal_kinderen_ten_laste, 4)
        kindervermindering = aantal_kinderen_ten_laste * 7.5
        normaal_aanvangsgeld -= (aantal_kinderen_ten_laste*7.5)
    if 2018 - aansluitingsjaar > 20:
        normaal_aanvangsgeld -= 12.5
    if inkomen < 7500:
        normaal_aanvangsgeld -= 25
    min(normaal_aanvangsgeld, 50)
    return normaal_aanvangsgeld

naam = input("Geef hier uw naam in:")
while naam != "x" and naam != "X":
    a = int(input("Geef hier uw leeftijd in:"))
    b = int(input("Geef hier het aantal kinderen in:"))
    c = int(input("Geef hier uw jaarlijkse inkomen in:"))
    d = int(input("Geef hier het jaar dat u lid bent geworden:"))
    print(lidgeld_tennisclub(a,b,c,d))
    naam = input("Geef hier uw naam in:")