def exercise1():
    nbr = int(input("Entrez un nombre de depart: "))
    for x in range(0,10):
        nbr += 1
        print(nbr)

def exercise2():
    nbr = int(input("Entrez un nombre de depart: "))
    for x in range(1,11):
        print(nbr," x ",x," = ",nbr * x)

def exercise3():
    list = []
    biggerlist = [0]
    atraiter = int(input("Combien de nombres désirez-vous traiter? "))
    for x in range(0,atraiter):
        print("Entrez le nombre ",x+1,": ")
        nbr = int(input())
        list.append(nbr)
    for i in range(0, len(list)):
        a = list[i]
        b = biggerlist[0]
        if a < b:
            biggerlist[0] = b
        elif b<a:
            biggerlist[0]= a
        else:
            biggerlist[0] = a
    print("Le plus grand de ces nombres est : ",biggerlist[0])
    print(list.index(biggerlist[0])+1)
def exercise1S2():
    password = input("Entrez le mot de passe: ")
    while password != "wow":
        print("Le mot de passe est invalide")
        password = input("Entrez le mot de passe: ")
    print("Bienvenue")

def exercise3S2a():
    nbr = int(input("Entrez le nombres de colonne d'etoiles: "))
    for i in range(1, nbr+1):
        n = 0
        while n != i:
            print("*", end = " ")
            n+=1
        print("")

def exercise3S2b():
    nbr = int(input("Entrez le nombres de colonne d'etoiles: "))
    for i in range(nbr, 0, -1):
        n = 0
        while n != i:
            print("*", end = " ")
            n+=1
        print("")

def exercise3S2c():
    nbretoiles = int(input("Entrez le nombres de colonne d'etoiles: "))
    for i in range(0,nbretoiles):
        n = 0
        for n in range(0, i):
            print("_", end = " ")

        x=0
        while x != nbretoiles-i:
            print("*", end = " ")
            x+=1

        print("")

def exercise3S2d():
    nbretoiles = int(input("Entrez le nombres de colonne d'etoiles: "))
    for i in range(0,nbretoiles):
        x = 0
        for x in range(0,nbretoiles - i-1):
            print("_", end=" ")
            x += 1
        n = 0
        for n in range(0, i+1):
            print("*", end = " ")

        print("")

