import xml.etree.ElementTree as ET
tree = ET.parse('Stations.xml')
root = tree.getroot()

dictionary = dict()

print('Dit zijn de codes en types van de 4 stations: ')
for station in root:
        try:
            dictionary[station[0].text] = station
            print(str(station[0].text) + " - " + str(station[1].text))
        except:
            IndexError

print('\nDit zijn alle stations met een of meer synoniemen: ')
for key, station in dictionary.items():
    try:
        for synoniem in station[4]:
            print(key + ' - ' + synoniem.text)
    except:
        IndexError

print('\nDit is de lange naam van elk station:')
for key, station in dictionary.items():
    print(key + ' - ' + station[2][2].text)
