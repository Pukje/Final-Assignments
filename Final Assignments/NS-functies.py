PrijsperKM = 0.8
Langeritprijs = 15.00
LangeritprijsKM = 0.6
LangeritAfstand = 50

def standaardprijs(afstandKM):
    prijs = 0

    if afstandKM > LangeritAfstand:
        prijs = (afstandKM * PrijsperKM) + Langeritprijs * (LangeritprijsKM * afstandKM)
    else:
        prijs = afstandKM * PrijsperKM
    return prijs

Werkdagkorting = 0.7
LeeftijdskortingWK = 0.65
Weekendkorting = 0.6
LeeftijdskortingMax = 12
LeeftijdskortingMin = 65

def ritprijs(leeftijd, weekendrit, afstandKM):
    Standaard = standaardprijs(afstandKM)
    Prijs = 0
    Leeftijdskorting = ((leeftijd < LeeftijdskortingMax) or (leeftijd >= LeeftijdskortingMin))
    if not weekendrit and Leeftijdskorting:
        Prijs = Standaard * Werkdagkorting
    elif weekendrit and Leeftijdskorting:
        Prijs = Standaard * LeeftijdskortingWK
    elif weekendrit:
        Prijs = Standaard * Weekendkorting
    else:
        prijs = Standaard
    return Prijs

tests = [
    [11, True,50],
    [12, False, 49],
    [64, True, 100],
    [65, False, 20],
    [41, False,  -124],
    [40, False, 140]
]

for test in tests:
    print('test: €' + str(format( ritprijs( test[0], test[1], test[2]),'.2f')) + '---standaard: €'+ str(standaardprijs(test[2])))
