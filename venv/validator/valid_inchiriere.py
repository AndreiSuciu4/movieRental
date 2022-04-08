from domeniu.entitati_inchiriere import inchiriere
from erori.exceptii import ValidError
from datetime import datetime
class valid_inchirieri():
    def valideaza_inchiriere(self,inchiriere):
        """" functie care valideaza o inchiriere introdusa
        date de intrare:inchiriere
        date de iesire:-
        daca data inchirierii e mai mare decat data curent programul returneaza eroarea:data returnarii trebuie sa fie mai mare decat data actuala"""
        erori=""
        azi=datetime.now()
        data=datetime(inchiriere.get_an_r(),inchiriere.get_luna_r(),inchiriere.get_zi_r())
        if data<azi:
            erori+="data returnarii trebuie sa fie mai mare decat data actuala"
        if len(erori)>0:
            raise ValidError(erori)
