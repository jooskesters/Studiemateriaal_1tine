from random import(randint,random,seed)

a = randint(1,10)
b = int(input("Geef hier het getal in:"))
while b != a:
    if  b > a:
        print("Lager")
    elif b < a:
        print("Hoger")
    b = int(input("Geef hier een getal in:"))
print("Proficiat")
