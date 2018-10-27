#Oefening 3.4
a = float(input("Geef een getal:"))
b = float(input("Geef nog een getal:"))
if a < b:
    c = a
    a = b
    b = c
print("het kleinste getal is", b)
print("kwadraat:", b ** 2)
if a != 0:
    print("deling: ", a / b)