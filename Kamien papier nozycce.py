import numpy as np

wynik = 0
wynik2 = 0
x=0
print(' "Papier, kamien, nozyce"')

while wynik!=3 or wynik2!=3:
    x+=1
    print("Runda numer ", x)
    print("Wybierz: \n1.Papier\n2.Kamien\n3.Nozyce")

    wybor = int(input())
    if(wybor == 1):
        print("Wybrales papier")

    elif(wybor == 2):
        print("Wybrales kamien")
    elif(wybor == 3):
        
        print("Wybrales nozyce")
    else:
        print("nie ma takiej opcji przegrales")
        exit()

    los = int(np.random.randint(3, size=1) + 1)
    if(los == 1):
        print("przeciwnik wybral papier")
    elif(los == 2):
        print("przeciwnik wybral kamien")
    elif(los == 3):
        print("przeciwnik wybral nozyce")
    else:
        print("przeciwnik jest glupi ;c")

    if(wybor == los):
        wynik2 += 1
        wynik += 1

    elif((wybor == 1 and los == 2) or (wybor == 2 and los == 3) or (wybor == 3 and los == 1)):
        wynik += 1
    else:
        wynik2 += 1

    print("Aktualny wynik: \nTy - ",wynik, "\nBot - ",wynik2, "\n\n\n")

    if(wynik == 3):
        print("GRATULACJE WYGRALES!")
        exit()

    elif(wynik2 == 3):
        print("Twój przeciwnik wygral !")
        exit()
