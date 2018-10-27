vertrektijd_uren = int(input("Welk uur is het momenteel?"))
vertrektijd_minuten = int(input("Hoeveel minuten zijn er al voorbij in dit uur?"))
duur = int(input("Hoelang duurt de vlucht (in minuten)?"))

vertrektijd_uren = vertrektijd_uren + duur // 60
vertrektijd_minuten = vertrektijd_minuten + duur % 60
print("het aankomstuur wordt", vertrektijd_uren)
print("de aankomstminuut wordt", vertrektijd_minuten)


