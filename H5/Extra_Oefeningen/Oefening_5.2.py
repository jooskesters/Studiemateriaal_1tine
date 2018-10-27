def binnen(uur, minuten):
    binnenkomst = (uur,"u",minuten)
    return binnenkomst

def buiten(uur, minuten):
    verlaten = (uur,"u",minuten)
    return verlaten

a = int(input("Geef hier het uur vanbinnenkomst"))
b = int(input("Geef hier de minuten"))

print()