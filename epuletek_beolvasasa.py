from Epuletek import Epulet

def fajlbeolvas():
        epulet_lista = []
        
        f = open("epulet.txt", "r", encoding="utf-8")
        f.readline().strip()
        sorok = f.readlines()
        f.close()
        
        i = 0
        while i < len(sorok):
            adatok = sorok[i].strip().split('$')
            nev, varos, orszaga, magassag, emelet, ev = adatok
            epulet = Epulet(
                nev.strip(),
                varos.strip(),
                orszaga.strip(),
                float(magassag.strip().replace(",",".")),
                int(emelet.strip()),
                int(ev.strip())
            )
            epulet_lista.append(epulet)
            i += 1
        return epulet_lista

def epuletek(sorok):
    print(f"III/A, B:\nAz épületek száma: {len(sorok)}")

def magassag(sorok):
    i = 0
    magas = 0
    labmeter = (555 / 3.280839895)
    while (i < len(sorok)):
        if (sorok[i].magassag >= labmeter):
            magas += 1
        i += 1
    print(f"III/C:\nAz 555 lábnál magasabb épületek száma: {magas}.")

def legoregebb(sorok):
    maxmagas = 0
    melyik = ""
    for i in range(0,len(sorok),1):
        if (sorok[i].magassag > maxmagas):
            melyik = sorok[i].orszaga
    print(f"III/D:\nA legöregebb épület országa: {melyik}")