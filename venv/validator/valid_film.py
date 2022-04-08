from domeniu.entitati_film import film
from erori.exceptii import ValidError
class valid_film():
    #clasa care valideaza un film introdus
    def valideaza_film(self,film):
        """functie care valideaza un film introdus
        date de intrare:film
        date de iesire:-
        daca id-ul e invalid-programul afiseaza exceptia:id invalid!
        daca titlul e invalid-programul afiseaza exceptia:titlu invalid!
        daca descrierea e invalida-programul afiseaza exceptia:descriere invalid!
        daca genul invalid-programul afiseaza exceptia:gen invalid!"""
        erori=""
        if film.get_id()<1 and type(film.get_id)is not int:
            erori+="id invalid!\n"
        if film.get_titlu()=="":
            erori+="titlu invalid!\n"
        if film.get_gen()=="":
            erori+="gen invalid!\n"
        if film.get_descriere=="":
            erori+="descriere invalida!\n"
        if len(erori)>0:
            raise ValidError(erori)






