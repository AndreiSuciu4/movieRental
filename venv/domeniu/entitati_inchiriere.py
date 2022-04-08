from datetime import datetime
class inchiriere:
    def __init__(self,id,client,film,zi_r,luna_r,an_r):
        # creeaza o noua instanta pentru clasa inchiriere
        self.__id=id
        self.__client=client
        self.__film = film
        self.__zi_r=zi_r
        self.__luna_r=luna_r
        self.__an_r=an_r

    def get_id(self):
        """returneaza id_ul unei inchirieri
        date de intrare:-
        date de iesire:id-int"""
        return self.__id
    def get_client(self):
        """returneaza clintul unei inchirieri
        date de intrare:-
        date de iesire:client"""
        return self.__client
    def get_film(self):
        """returneaza filmul unei inchirieri
        date de intrare:-
        date de iesire:film"""
        return self.__film
    def get_zi_r(self):
        """returneaza ziua returnarii unei inchirieri
        date de intrare:-
        date de iesiere:zi_r-int"""
        return self.__zi_r
    def get_luna_r(self):
        """returneaza luna returnarii unei inchirieri
        date de intrare:-
        date de iesiere:luna_r-int"""
        return self.__luna_r
    def get_an_r(self):
        """returneaza anul returnarii unei inchirieri
        date de intrare:-
        date de iesiere:an_r-int"""
        return self.__an_r
    def set_id(self,val):
        """atribuie id-ului o anumita valoare
        date de intrare:val-int
        date de iesire:-"""
        self.__id=val
    def set_film(self,val):
        """atribuie filmului o anumita valoare
        date de intrare:val
        date de iesire:-"""
        self.__film=val
    def set_client(self,val):
        """atribuie clientului o anumita valoare
        date de intrare:val
        date de iesire:-"""
        self.__client=val
    def set_zi_r(self, val):
        """atribuie zilei de returnare o anumita valoare
        date de intrare:val
        date de iesire:-"""
        self.__zi_r = val
    def set_luna_r(self,val):
        """atribuie lunii de returnare o anumita valoare
        date de intrare:val
        date de iesire:-"""
        self.__luna_r=val
    def set_an_r(self,val):
        """atribuie anului de returnare o anumita valoare
        date de intrare:val
        date de iesire:-"""
        self.__an_r=val
    def __eq__(self,other):
        #verifica daca doua filme au acelasi id
        return self.__id == other.__id

class InchirieriDTO():
    def __init__(self,id,nume_client,titlu_film,zi_r,luna_r,an_r):
        # creeaza o noua instanta pentru clasa InchirieriDTO
        self.__id=id
        self.__nume_client=nume_client
        self.__titlu_film=titlu_film
        self.__zi_r = zi_r
        self.__luna_r = luna_r
        self.__an_r = an_r
    def get_id(self):
        """returneaza id_ul unei inchirieri
        date de intrare:-
        date de iesire:id-int"""
        return self.__id
    def get_nume(self):
        """returneaza numele unui client
        date de intrare:-
        date de iesire:nume-str"""
        return self.__nume_client
    def get_titlu(self):
        """returneaza titlul unui film inchiriat
        date de intrare:-
        date de iesire:titlu-str"""
        return self.__titlu_film
    def get_zi_r(self):
        """"returneaza ziua returnarii unei inchirieri
        date de intrare:-
        date de iesiere:zi_r-int"""
        return self.__zi_r
    def get_luna_r(self):
        """returneaza luna returnarii unei inchirieri
        date de intrare:-
        date de iesiere:luna_r-int"""
        return self.__luna_r
    def get_an_r(self):
        """returneaza anul returnarii unei inchirieri
        date de intrare:-
        date de iesiere:an_r-int"""
        return self.__an_r


    def __str__(self):
        data=datetime(self.__an_r,self.__luna_r,self.__zi_r)
        aux=data.strftime("%d-%b-%Y")
        return str(self.__id)+":clientul "+self.__nume_client+" a inchiriat filmul "+self.__titlu_film+" si trebuie sa il returneze la data de "+aux

class Ordonare_numar_filmeDTO():
    def __init__(self,nume,filme_inchiriate):
        # creeaza o noua instanta pentru clasa Ordonare_numar_filmeDTO
        self.__nume=nume
        self.__filme_inchiriate=filme_inchiriate
    def get_nume(self):
        """returneaza numele unui client
        date de intrare:-
        date de iesire:nume-str"""
        return self.__nume
    def get_filme_inchiriate(self):
        """returneaza numarul de filme inchiriate ale unui client
        date de intrare:-
        date de iesire:filme_inchiriate-int"""
        return self.__filme_inchiriate
    def __str__(self):
        return self.__nume + " a inchiriat " + str(self.__filme_inchiriate) +" filme"

class Cele_mai_inchiriate_filmeDTO():
    # creeaza o noua instanta pentru clasa Cele_mai_inchiriate_filmeDTO
    def __init__(self,titlu,nr_inchirieri):
        self.__titlu=titlu
        self.__nr_inchirieri=nr_inchirieri
    def get_titlu(self):
        """returneaza titlul unui film inchiriat
        date de intrare:-
        date de iesire:titlu-str"""
        return self.__titlu
    def get_nr_inchirieri(self):
        """returneaza numarul de inchirieri ale unui film inchiriat
        date de intrare:-
        date de iesire:nr_inchirieri-int"""
        return self.__nr_inchirieri
    def __str__(self):
        return "filmul:"+self.__titlu+" cu "+str(self.__nr_inchirieri)+" inchirieri"

