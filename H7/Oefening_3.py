positieve_getallen = []
negatieve_getallen = []
kleinste_getal = -1
for a in range(10):
    getal = int(input("Geef hier een getal in: "))
    if getal > -1:
        positieve_getallen.append(getal)
    else:
        negatieve_getallen.append(getal)
        if getal < kleinste_getal:
            kleinste_getal = getal


print("De lengte van de positieve getallenlijst is = ",len(positieve_getallen) , ", Dit zijn de positieve getallen: ", positieve_getallen)
print("De lengte van de negatieve getallenlijst is = ",len(negatieve_getallen), ", Dit zijn de negatieve getallen: ",negatieve_getallen)
print("Het kleinste getal is: ", kleinste_getal)