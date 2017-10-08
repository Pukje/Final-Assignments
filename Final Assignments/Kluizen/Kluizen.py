MaxKluizen = 12
ListofFileLines = list()
KluisNummerLijst = list()

def readFile():
    del ListofFileLines[:]
    with open("C:\Users\steve\PycharmProjects\lessen\Final Assignments\Kluizen\kluizen.txt") as f:
        for line in f:
            ListofFileLines.append(line)
        f.close()

def AantalKluizenVrij():
    readFile()
    return MaxKluizen - len(ListofFileLines)

def NieuweKluis():
    if AantalKluizenVrij() == 0:
        print('Alle kluizen zitten vol.')
        return False
    else:
        Code = input('Uw code voor de kluis? (Minimaal 4 tekens.) ')
        if len(Code) < 4:
            NieuweKluis()
        for line in ListofFileLines:
            Kluisli = line.split(';')
            KluisNummerLijst.append(int(Kluisli[0]))
        print(KluisNummerLijst)
        Kluisnummer = NieuwKluisNummer(1, KluisNummerLijst);

        file = open('C:\Users\steve\PycharmProjects\lessen\Final Assignments\Kluizen\kluizen.txt', 'w')
        for line in ListofFileLines:
            file.write(line)
        file.write('\n' + str(Kluisnummer) + ';' + Code)
        file.close()
        print('Uw kluisnummer is:' + str(Kluisnummer))
        readFile()

def Kluis_openen():
    readFile()
    Code = input('Uw code voor de kluis?')
    Number = int(input('Uw Kluisnummer?'))
    if (str(Number) + ';' + Code) in ListofFileLines:
        print('Uw kluis is open.')
    else:
        print('De code klopt niet, probeer het nog eens.')
        Kluis_openen()

def Kluis_teruggeven():
    readFile()
    Code = input('Uw code voor de kluis? ')
    Nummer = int(input('Uw Kluisnummer? '))
    if (str(Nummer) + ';' + Code) not in ListofFileLines:
        print('Probeer het niet')
    elif (str(Nummer) + ';' + Code) in ListofFileLines:
        file = open("C:\Users\steve\PycharmProjects\lessen\Final Assignments\Kluizen\kluizen.txt", 'w')
        for line in list:
            if line == (str(Nummer) + ';' + Code):
                continue
            file.write(line)
        file.close()
        print('Kluis is weer beschikbaar')

def NieuwKluisNummer(Nummer, KluisListArg):
    if Nummer in KluisNummerLijst:
        Nummer = Nummer + 1
        return NieuwKluisNummer(Nummer, KluisListArg)
    else:
        return Nummer

print('1: Hoeveel kluizen zijn nog vrij.?')
print('2: Nieuwe kluis.')
print('3: Iets uit de kluis halen.')
print('4: Kluis teruggeven.')
MenuChoice = int(input('Wat wilt u doen? '))

if not isinstance(MenuChoice, int):
    print('Error terminating program')
    exit()

if MenuChoice == 1:
    print(AantalKluizenVrij())
elif MenuChoice == 2:
    NieuweKluis()
elif MenuChoice == 3:
    Kluis_openen()
elif MenuChoice == 4:
    Kluis_teruggeven()
