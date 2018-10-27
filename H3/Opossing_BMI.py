#Oefening BMI
lengte = float(input("Wat is uw lengte:"))
gewicht = float(input("Hoeveel weegt u (in kg):"))
BMI = gewicht/(lengte*lengte)
if BMI < 18:
    print("U heeft ondergewicht.")
elif BMI < 25:
    print("Ok.")
elif BMI < 30:
    print("Overgewicht")
elif BMI < 40:
    print("Obesitas")
else:
    print("ziekelijk overgewicht")