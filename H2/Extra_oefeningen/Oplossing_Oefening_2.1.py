kosten_per_begonnen_minuut_buitenland = float(input("Geef het aantal gebelde minuten naar het buitenland"))
aantal_belgische_gesprekken = int(input("Geef het aantal gesprekken binnen Beglië"))
tweemaandelijkse_vaste_kosten = float(20.0/2)
INCL_BTW = 1.21

kosten_bellen_naar_buitenland = kosten_per_begonnen_minuut_buitenland * 0.50 * INCL_BTW
kosten_belgische_gesprekken = aantal_belgische_gesprekken * 0.12 * INCL_BTW
totale_kost = kosten_bellen_naar_buitenland + kosten_belgische_gesprekken + tweemaandelijkse_vaste_kosten

print(totale_kost)
