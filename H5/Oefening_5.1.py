def reken_om_naar_dollar(koers, bedrag):
    return koers * bedrag

waarde_dollar = float(input("Geef de waarde van de dollar ten opzichte van de euro:"))
euro = float(input("Geef hier het aantal euro's:"))
while euro != 0:
    bedrag_dollar = reken_om_naar_dollar(waarde_dollar, euro)
    print("€", euro, "= $", bedrag_dollar)
    euro = float(input("Geef een bedrag in euro: "))