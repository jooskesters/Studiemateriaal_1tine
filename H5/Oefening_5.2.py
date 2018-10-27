
def bereken(jaartal):
    if jaartal % 4 == 0 and jaartal % 100 != 0 or jaartal % 400 == 0:
        return True
    else:
        return False

x = int(input("Geef het jaartal:"))

print(bereken(x))