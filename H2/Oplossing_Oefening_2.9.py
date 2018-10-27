bedrag = float(input("Geef de gewenste hoeveelheid centen:"))
twee_euro = bedrag//2
een_euro = (bedrag % 2) // 1
vijftig_cent = (bedrag % 2 % 1) // 0.5
twintig_cent = (bedrag % 2 % 1 % 0.5) // 0.2
tien_cent = (bedrag % 2 % 1 % 0.5 % 0.2) // 0.1
vijf_cent = (bedrag % 2 % 1 % 0.5 % 0.2 % 0.1) // 0.05
twee_cent = (bedrag % 2 % 1 % 0.5 % 0.2 % 0.1 % 0.05) // 0.02
een_cent = (bedrag % 2 % 1 % 0.5 % 0.2 % 0.1 % 0.05 % 0.02) // 0.01

print("Volgende munten vormen", bedrag)
print("twee euro\'s:",(twee_euro))
print("een euro\'s:",(een_euro))
print("vijftig cent\'s:",(vijftig_cent))
print("twintig cent\'s:",(twintig_cent))
print("tien cent\'s:",(tien_cent))
print("vijf cent\'s:",(vijf_cent))
print("twee cent\'s:",(twee_cent))
print("een cent\'s:",(een_cent))
