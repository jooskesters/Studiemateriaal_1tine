from random import (randint)
tekst = input("Geef hier de tekst in die geëncrypteerd moet worden: ")

def genereer_nummer():
    getal = randint(2, 24)
    if getal % 2 == 1:
        getal += 1
    return getal
random_nummer = genereer_nummer()
print(genereer_nummer())

for i in tekst:
    waarde = ord(i)
    waarde += random_nummer
    print(chr(waarde), end=" ")