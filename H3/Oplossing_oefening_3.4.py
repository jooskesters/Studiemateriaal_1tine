#Oefening 3.8
a = float(input("Geef een getal:"))
b = float(input("Geef nog een getal:"))
if a < b:
    small = a
    large = b
else:
    small = b
    large = a
print("het kleinste getal is", small)
print("kwadraat:", small ** 2)
if small != 0:
    print("deling: ", large / small)