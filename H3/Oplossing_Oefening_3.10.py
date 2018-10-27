leeftijd = int(input("Hoe oud bent u:"))
aansluitingsjaar = int(input("Wanneer bent u gestart:"))
bijdrage = 100
reductie = 14.5
reductie_per_aangesloten_jaar = 2.5

if leeftijd < 21 or leeftijd > 60:
    bijdrage = bijdrage - reductie

bijdrage = bijdrage - 2.5 *(2018-aansluitingsjaar)

if bijdrage < 62.5:
   bijdrage = 62.5
print(bijdrage)
