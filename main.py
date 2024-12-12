import bevezetes
import sorozat
from Epuletek import Epuletek

"""print("I/A:")
bevezetes.bevezetes()
sorozat.konzol_kiir(sorozat.szamok(),sorozat.fejek_szama(sorozat.szamok()))
sorozat.file_kiir(sorozat.fejek_szama(sorozat.szamok()))"""
epuletek_lista = Epuletek.fajlbeolvas()
print(epuletek_lista)