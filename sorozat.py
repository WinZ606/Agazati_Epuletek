import random

def szamok():
    szamok = []
    for i in range(0,7,1):
        szamok.append(random.randint(0,1))
    return szamok

def fejek_szama(szamok):
    fejek = 0
    for i in range(0,7,1):
        if (szamok[i] == 1):
            fejek += 1
    return fejek

def konzol_kiir(szamok,fejek):
    print("II/A, B, C:")
    betuk = []
    for i in range(0,7,1):
        if (szamok[i] == 0):
            betuk.append("FEJ")
        else:
            betuk.append("ÍRÁS")
    print(*betuk,sep="-")
    print("II/D, E:")
    print(f"A fejek száma: {fejek}.")

def file_kiir(fejek):
    f = open("fejek.txt","a")
    f.write(f"A fejek száma: {fejek}.")