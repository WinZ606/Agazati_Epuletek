import bevezetes
import sorozat
import epuletek_beolvasasa
from Epuletek import Epulet

"""print("I/A:")
bevezetes.bevezetes()
sorozat.konzol_kiir(sorozat.szamok(),sorozat.fejek_szama(sorozat.szamok()))
sorozat.file_kiir(sorozat.fejek_szama(sorozat.szamok()))"""
lista = epuletek_beolvasasa.fajlbeolvas()
epuletek_beolvasasa.epuletek(lista)
epuletek_beolvasasa.magassag(lista)
epuletek_beolvasasa.legoregebb(lista)