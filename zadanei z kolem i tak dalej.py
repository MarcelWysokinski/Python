szescian = lambda a:a*a*a

prost = lambda a,b,c:a*b*c

kula = lambda r:(4/3)*(3.14)*(r*r*r)

opcja = int(input("Wybierz co chcesz obliczyc?\n 1. Objetosc sześcianu\n 2. Objetosc prastopadloscianu\n 3. Objetosc kuli\n"))

if(opcja == 1):
    a = int(input("Podaj  odcinka a: "))
    print("Objetosc szescianu o boku: ",a," = ",szescian(a))

elif(opcja == 2):
    a = int(input("Podaj odcinek a: "))
    b = int(input("Podaj odcinek b: "))
    c = int(input("Podaj odcinek c: "))

    print("Objetosc prostopadloscianu o bokach: ",a,", ",b,", ",c," = ",prost(a,b,c))
elif(opcja == 3):

    r = int(input("Podaj promien: "))
    print("Objetosc kulki o promieni: ",r," = ",kula(r))

else:
    print("Nie klam, ta liczba jest poza zakresem")