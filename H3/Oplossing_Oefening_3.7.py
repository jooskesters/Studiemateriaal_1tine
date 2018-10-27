#Oefening_3.7
examen_1 = int(input("De punten van examen 1:"))
examen_2 = int(input("De punten van examen 2:"))
examen_3 = int(input("De punten van examen 3:"))
examen_totaal = examen_1 + examen_2 + examen_3 / 60 * 100
if examen_totaal < 60:
    print('onvoldoende')
elif examen_totaal < 70:
    print('voldoende')
elif examen_totaal < 80:
    print('onderscheiding')
elif examen_totaal < 90:
    print('grote onderscheiding')
elif examen_totaal >= 90:
    print('grootste oderscheiding')

