from subject import Subject
from student import Student
def wykaz_ocen():
    print("----------+----------+-------+")
    print("Przedmiot | Studenci | Oceny |")
    print("----------+----------+-------+")
    with open('dane.txt', 'r') as file:
        for line in file:
            print(line.strip())

def dopisz_ocene():
    tab = []
    imie = []
    przedmiot = []
    ocena, ocena2 = [], []
    for i in range(len(wejscie)):
        tab.append(str(wejscie[i]))
    for i in range(len(tab)):
        if tab[i] != "+":
            imie += tab[i]
        else: 
            break
    for i in range(len(imie)+2, len(tab)):
        if tab[i] != "(":
            przedmiot.append(tab[i])
        else: 
            break
    for i in range(len(imie)+len(przedmiot)+3, len(tab)):
        if tab[i] != "," and tab[i] != ")":
            ocena += tab[i]
        else:
            break
    for i in range(len(imie)+len(przedmiot)+8, len(tab)):
        if tab[i] != ")":
            ocena2 += tab[i]
        else:
            break
    with open("dane.txt", "a") as file:
        file.write(''.join(przedmiot) + " ")
        file.write(''.join(imie) + " ")
        file.write(''.join(ocena))
        file.write("\n")

def usun_linie(plik, linia_do_usuniecia):
    with open(plik, 'r') as wejscie:
        lines = wejscie.readlines()

    with open(plik, 'w') as wyjscie:
        for line in lines:
            if line.strip() != linia_do_usuniecia:
                wyjscie.write(line)

def usun_ocene():
    tab, tab2 = [], []
    imie = []
    przedmiot, przedmiot2 = [], []
    ocena, ocena2 = [], []
    for i in range(len(wejscie)):
        tab.append(str(wejscie[i]))
    for i in range(len(tab)):
        if tab[i] != "-":
            imie += tab[i]
        else: 
            break
    for i in range(len(imie)+2, len(tab)):
        if tab[i] != "(":
            przedmiot.append(tab[i])
        else: 
            break
    for i in range(len(imie)+len(przedmiot)+3, len(tab)):
        if tab[i] != "," and tab[i] != ")":
            ocena += tab[i]
        else:
            break
    for i in range(len(imie)+len(przedmiot)+6, len(tab)):
        if tab[i] != "," and tab[i] != ")":
            ocena2 += tab[i]
        else:
            break
    if len(ocena) < 3:
        if ''.join(ocena) in ["2", "3", "4", "5"]:
            print(" " * 11 + f"{''.join(przedmiot)} - nie istnieje ocena o numerze {''.join(ocena)}")
    if "|" in tab:
        start_dane2 = tab.index("|")
        for i in range(start_dane2+1, len(tab)):
            tab2.append(tab[i])
        #print(tab2)
        for i in range(0, len(tab2)):
            if tab2[i] != "(":
                przedmiot2 += tab2[i]
            else:
                break
        for i in range(len(przedmiot2)+1, len(tab2)):
            if tab2[i] != "," and tab2[i] != ")":
                ocena += tab2[i]
    if len(ocena) < 3:
        if ''.join(ocena) in ["2", "3", "4", "5"]:
            print(" " * 11 + f"{''.join(przedmiot)} - nie istnieje ocena o numerze {''.join(ocena)}")
    if len(ocena2) > 0 and len(ocena2) < 3:
        if ''.join(ocena2) in ["2", "3", "4", "5"]:
            print(" " * 11 + f"{''.join(przedmiot)} - nie istnieje ocena o numerze {''.join(ocena2)}")
    if ''.join(przedmiot2) not in ["Matematyka", "Fizyka", ""]:
        print(" " * 11 + f"{''.join(przedmiot2)} - nie ma takiego przedmiotu")
    else:
        linia = ''.join(przedmiot)+ " " + ''.join(imie) + " " + ''.join(ocena)
        usun_linie("dane.txt", linia)





while True:
    wejscie = input("> ")
    if wejscie == "grades":
        wykaz_ocen()
    elif "+=" in wejscie:
        dopisz_ocene()
    elif "-=" in wejscie:
        usun_ocene()
    elif "+" in wejscie:
        print(" " * 11 + "Niepoprawny format komendy")
    elif wejscie == "print(list_of_subjects)":
        Subject.__str__
    elif wejscie == "print(list_of_students)":
        Student.__str__
    else:
        print(" " * 11 + "Nieznana komenda")