from random import randint

def rekenlijst():
    for i in range(1,6):
        print("reeks", i)
        for j in range(5):
            a = randint(1,20)
            b = randint(1,20)
            c = 0
            bewerking = a - b
            if bewerking < 0:
                c = a
                a = b
                b = c
            print("trek volgende getallen van elkaar af:", a, "-", b, "=")
        print()
print(rekenlijst())
print("klaar")