bedrag = float(input("Geef de gewenste hoeveelheid centen:"))
twee_euro = bedrag // 200
bedrag = bedrag % 200
een_euro = bedrag // 100
bedrag = bedrag % 100
vijftig_cent = bedrag // 50
bedrag = bedrag % 50
twintig_cent = bedrag // 20
bedrag = bedrag % 20
tien_cent = bedrag // 10
bedrag = bedrag % 10
vijf_cent = bedrag // 5
bedrag = bedrag % 5
twee_cent = bedrag // 2
bedrag = bedrag % 2
een_cent = bedrag // 1
bedrag = bedrag % 1

print("Volgende munten vormen", bedrag)
print("twee euro\'s:",(twee_euro))
print("een euro\'s:",(een_euro))
print("vijftig cent\'s:",(vijftig_cent))
print("twintig cent\'s:",(twintig_cent))
print("tien cent\'s:",(tien_cent))
print("vijf cent\'s:",(vijf_cent))
print("twee cent\'s:",(twee_cent))
print("een cent\'s:",(een_cent))
