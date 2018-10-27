spreuk = "abracadabra"
spreuk = spreuk.replace("a", "o")
print(spreuk)
teller_o = 0
for karakter in spreuk:
    if karakter == "o":
        teller_o += 1
print("Aantal o's: ", teller_o)
print("Aantal o's: ", spreuk.count("o"))
