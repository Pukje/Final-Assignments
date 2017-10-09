maxkluizen = 12
listofFileLines = list()
kluisnummerlijst = list()


def readfile():
    del listofFileLines[:]
    with open('Kluizen.txt') as f:
        for line in f:
            listofFileLines.append(line)
        f.close()


def aantalkluizenvrij():
    readfile()
    return maxkluizen - len(listofFileLines)


def nieuwekluis():
    if aantalkluizenvrij() == 0:
        print('Alle kluizen zitten vol.')
        return False
    else:
        code = input('Uw code voor de kluis? (Minimaal 4 tekens.) ')
        if len(code) < 4:
            nieuwekluis()
        for line in listofFileLines:
            kluisli = line.split(';')
            kluisnummerlijst.append(int(kluisli[0]))
        print(kluisnummerlijst)
        kluisnummer = nieuwkluisnummer(1, kluisnummerlijst);

        file = open('kluizen.txt', 'w')
        for line in listofFileLines:
            file.write(line)
        file.write('\n' + str(kluisnummer) + ';' + code)
        file.close()
        print('Uw kluisnummer is:' + str(kluisnummer))
        readfile()


def kluis_openen():
    readfile()
    code = input('Uw code voor de kluis?')
    nummer = int(input('Uw Kluisnummer?'))
    if (str(nummer) + ';' + code) in listofFileLines:
        print('Uw kluis is open.')
    else:
        print('De code klopt niet, probeer het nog eens.')
        kluis_openen()


def kluis_teruggeven():
    readfile()
    code = input('Uw code voor de kluis? ')
    nummer = int(input('Uw Kluisnummer? '))
    if (str(nummer) + ';' + code) not in listofFileLines:
        print('Probeer het niet')
    elif (str(nummer) + ';' + code) in listofFileLines:
        file = open("kluizen.txt", 'w')
        for line in listofFileLines:
            if line == (str(nummer) + ';' + code):
                continue
            file.write(line)
        file.close()
        print('Kluis is weer beschikbaar')


def nieuwkluisnummer(nummer, kluislistarg):
    if nummer in kluisnummerlijst:
        nummer = nummer + 1
        return nieuwkluisnummer(nummer, kluislistarg)
    else:
        return nummer


print('1: Hoeveel kluizen zijn nog vrij.?')
print('2: Nieuwe kluis.')
print('3: Iets uit de kluis halen.')
print('4: Kluis teruggeven.')


menuchoice = int(input('Wat wilt u doen? '))


if not isinstance(menuchoice, int):
    print('Error terminating program')
    exit()


if menuchoice == 1:
    print(aantalkluizenvrij())
elif menuchoice == 2:
    nieuwekluis()
elif menuchoice == 3:
    kluis_openen()
elif menuchoice == 4:
    kluis_teruggeven()
