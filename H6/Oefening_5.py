"""Imports"""
import string
from random import *


def random_string_generator():
    min_char = 2
    max_char = 2
    allchar = string.ascii_letters.upper()
    Hotelcode = "".join(choice(allchar) for x in range(randint(min_char, max_char)))
    return Hotelcode



def random_number_generator():
    min_num = 4
    max_num = 4
    allnum = string.digits
    numbers = "".join(choice(allnum) for i in range(randint(min_num, max_num)))
    print(numbers)


def prijs_voor_volwassenen(aantal_sterren):
    qsterren = aantal_sterren * (str("*"))
    while aantal_sterren != 0 and aantal_sterren < 6:
        if aantal_sterren > 3:
            prijs = 60
        elif aantal_sterren == 3:
            if random_string_generator() == "BR" or random_string_generator() == "AN":
                prijs = 60
            else:
                prijs = 56
        else:
            prijs = 48
        if random_string_generator() == "HI":
            prijs = 70
        print(qsterren)
        return prijs


def prijs_per_kind(kindercode):
    kinder_prijs = prijs_voor_volwassenen(aantal_sterren) / 2
    if kindercode == "A":
        kinder_prijs = 0
    return kinder_prijs

aantal_sterren = int(input("Geef hier het aantal sterren"))
aantal_volwassenen = int(input("Geef hier het aantal volwassenen)"))
kindercode = input("Geef hier een letter van A tot Z, namelijk de kindercode")
aantal_kinderen = int(input("Geef hier het aantal kinderen"))
print(random_string_generator(), random_number_generator(), (prijs_voor_volwassenen(aantal_sterren) * aantal_volwassenen), (prijs_per_kind(kindercode) * aantal_kinderen))

