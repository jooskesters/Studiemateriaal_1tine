#Oefening 2.3
PI = 3.14
INCH_TO_METER = 0.0254
diameter_fietswiel = float(input("Geef de gewenste diameter in inches:"))
af_te_leggen_afstand = float(input("Hoeveel meter wenst u af te leggen:"))

afgelegde_weg_per_omwenteling = diameter_fietswiel * PI * INCH_TO_METER
nodige_omwentelingen = af_te_leggen_afstand / afgelegde_weg_per_omwenteling

print(nodige_omwentelingen)


