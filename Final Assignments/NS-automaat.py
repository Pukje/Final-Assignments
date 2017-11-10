stations = [
    'Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk',
    'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', 's-Hertogenbosch',
    'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht'
]


def inlezen_beginstation(stations):
    stationsnaam = input('Het beginstation: ')
    if stationsnaam == "Maastricht":
        print('Dit is het eindstation, je kan hier niet beginnen')
        stationsnaam = ''
    elif stationsnaam in stations:
        print(stationsnaam + ' zit in het traject')
    else:
        print('Dit Station bestaat niet/Zit niet in het traject, probeer het nog eens.')
        stationsnaam = ''
    return stationsnaam


def inlezen_eindstation(stations, beginstation):
    stationsnaam = input("Uw Eindstation: ")
    if stationsnaam not in stations or stations.index(beginstation) >= stations.index(stationsnaam):
        print("Probeer het opnieuw, dit station bestaat niet of is niet bereikbaar vanaf uw beginstation")
        stationsnaam = ''
    return stationsnaam


def omroepen_reis(stations, beginsation, eindstation):
    beginnummerstation = stations.index(beginsation) + 1
    eindnummerstation = stations.index(eindstation) + 1
    stationsafstand = stations.index(eindstation) - stations.index(beginsation)

    print('Het beginsation ' + beginsation + 'is het ' + str(beginnummerstation) + 'e station in het traject')
    print('Het eindstation ' + eindstation + 'is het ' + str(eindnummerstation) + 'e station in het traject')
    if beginnummerstation + 1 is not eindnummerstation:
        print('De afstand is ' + str(stationsafstand) + ' Station(s).')
    print('De prijs van het kaartje is ' + str(stationsafstand * 5) + 'euro.')
    print('Je stapt in de trein op ' + beginsation)
    for idx, station in enumerate(stations):
        if idx + 1 > beginnummerstation and idx + 1 < eindnummerstation:
            print('     - ' + station)
    print('Je stapt uit de trein in: ' + eindstation)


beginstation = inlezen_beginstation(stations)

while beginstation == '':
    beginstation = inlezen_beginstation(stations)

eindStation = inlezen_eindstation(stations, beginstation)

while eindStation == '':
    eindStation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindStation)

print('Dit is het eindstation, je kan hier niet beginnen')
