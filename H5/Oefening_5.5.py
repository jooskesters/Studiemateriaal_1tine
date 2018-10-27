from random import(randint,random,seed)

def neem_getal(nummer, index):
    for i in range(7 - index):
        nummer /= 10
    return int(nummer % 10)

a = int(input("Geef hier uw lidnummer"))

getal2 = neem_getal(a, 2)
getal4 = neem_getal(a, 4)
print(getal2)
print(getal4)
print(a % 10)
if getal2 *10 + getal4 == a % 100:
    print("Gratis")
else:
    print("Niet gratis")


