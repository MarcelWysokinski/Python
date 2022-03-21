from random import seed

from random import randint

a = open("jd.txt", "x")
a.write("")
a.close()

a = open("jd.txt", "r")
print(a.read())
a.close()

a = open("jd.txt", "a")
for x in range(10):
    a.write("\nXD")
a.close()

a = open("jd.txt", "r")
print(a.read())
a.close()

a = open("jd.txt", "r")
files = a.read()
print("Liter w pliku:", len(files))
a.close()


los = ["Lechia","napastnik","gdyby","aby","lecz","michal","ola","jolo","jola","fifa","marciniak","marian","pazdzioch","mistrz","aktorstwa","slon","rozejm","lech","przegral","mecz","noby","instruktor","myszka","klawiatura","kosmos","a","yyy","yhym","malpa","pogchamp"]
seed(1)

a = open("jd.txt", "a")
y = int(input())
a.write("\n")
for x in range(y):

    liczba = randint(0, 29)
    a.write(los[liczba])
    a.write(" ")

    if(x % 10 == 0 and x != 0):
        a.write("\n")


a.close()