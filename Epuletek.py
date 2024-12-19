class Epulet:
    def __init__(self, neve:str, varosa:str, orszaga:str, magassag:str, emelet:int, epites_eve:int):
        self.neve = neve
        self.varosa = varosa
        self.orszaga = orszaga
        self.magassag = magassag
        self.emelet = emelet
        self.epites_eve = epites_eve

    def __str__(self):
        return (f"Épület neve: {self.neve}\n"
                f"Város: {self.varosa}\n"
                f"Ország: {self.orszaga}\n"
                f"Magasság: {self.magassag} m\n"
                f"Emeletek száma: {self.emelet}\n"
                f"Építés éve: {self.epites_eve}")