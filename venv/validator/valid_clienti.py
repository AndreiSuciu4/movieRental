from domeniu.entitati_clienti import client
from erori.exceptii import ValidError
class valid_clienti():
    def valideaza_clienti(self,client):
        """functie care valideaza un client introdus
               date de intrare:client
               date de iesire:-
               daca id_c-ul e invalid-programul afiseaza exceptia:id invalid!
               daca numele e invalid-programul afiseaza exceptia:nume invalid!
               daca CNP-ul e invalid-programul afiseaza exceptia:CNP invalid!
               """
        erori=""
        if client.get_id_c()<0:
            erori+="id invalid!\n"
        if client.get_nume()=="":
            erori+="nume invalid!\n"
        if len(client.get_CNP())!=13:
            erori+="CNP invalid!\n"
        if len(erori)>0:
            raise ValidError(erori)