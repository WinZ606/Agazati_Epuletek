class Epuletek:
    def __init__(self, neve:str, varosa:str, orszaga:str, magassag:str, emelet:int, epites_eve:int):
        self.neve = neve
        self.varosa = varosa
        self.orszaga = orszaga
        self.magassag = magassag
        self.emelet = emelet
        self.epites_eve = epites_eve

    def fajlbeolvas():
        epulet_lista = []
        
        f = open("epulet.txt", "r", encoding="utf-8")
        f.readline().strip()
        sorok = f.readlines()
        f.close()
        
        i = 0
        while i < len(sorok):
            adatok = sorok[i].strip().split('$')
            nev, varos, orszag, magassag, emelet, ev = adatok
            epulet = Epuletek(
                nev.strip(),
                varos.strip(),
                orszag.strip(),
                float(magassag.strip()),
                int(emelet.strip()),
                int(ev.strip())
            )
            epulet_lista.append(epulet)
            i += 1
        
        return epulet_lista

    def __str__(self):
        return (f"Épület neve: {self.neve}\n"
                f"Város: {self.varosa}\n"
                f"Ország: {self.orszaga}\n"
                f"Magasság: {self.magassag} m\n"
                f"Emeletek száma: {self.emelet}\n"
                f"Építés éve: {self.epites_eve}")