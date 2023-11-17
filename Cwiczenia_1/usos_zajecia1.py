import sys

oceny = {}

przedmioty = {'Matematyka': 2, "Fizyka": 3}

def dodaj_ocene(przedmiot, student, ocena):
    if przedmiot in przedmioty:
        if przedmiot not in oceny:
            oceny[przedmiot] = {}
        if student in oceny[przedmiot]:
            oceny[przedmiot][student].append(ocena)
        else:
            oceny[przedmiot][student] = [ocena]
    else:
        print(f"Przedmiot '{przedmiot}' nie istnieje.")

def wykaz_ocen():
    a = 1
    print("----------+----------+-------+")
    print("Przedmiot | Studenci | Oceny |")
    print("----------+----------+-------+")
    for przedmiot, max_studentow in przedmioty.items():
        print(przedmiot,)
        if przedmiot in oceny:
            for student, oceny_studenta in oceny[przedmiot].items():
                print(" " * 11, a, student, " " * (10 - len(student)), " ".join(oceny_studenta))
                a += 1
            if przedmiot[a-1] != przedmiot[a]:
                   a = 1
        else:
            for a in range(max_studentow):
                
                print(" " * 11, a+1)
    

if len(sys.argv) > 1:
    if sys.argv[1] == "--wykaz_ocen":
        wykaz_ocen()
    else:
        for i in range(1, len(sys.argv), 3):
            przedmiot = sys.argv[i]
            student = sys.argv[i + 1]
            ocena = sys.argv[i + 2]
            dodaj_ocene(przedmiot, student, ocena)
        wykaz_ocen()
    
else:
    print("Parametry:")
    print("  • Nazwa_przedmiotu1 Nazwa_studenta Ocena  Nazwa_przedmiotu2 Nazwa_studenta Ocena ...")
    print("  • --wykaz_ocen")
