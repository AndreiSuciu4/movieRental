class client:
    def __init__(self,id,nume,CNP):
        #creeaza o noua instanta pentru clasa Client
        self.__id=id
        self.__nume=nume
        self.__CNP=CNP
        self.__nr_filme=0

    def get_id_c(self):
        """" returneaza id-ul unui client
        date de intrare:-
        date de iesire:id-int"""
        return self.__id
    def get_nume(self):
        """care returneaza numele unui client
        date de intrare:
        date de iesire:nume-str"""
        return self.__nume
    def get_CNP(self):
        """returneaza CNP-ul unui client
        date de intrare:
        date de iesire:CNP-str"""
        return self.__CNP
    def get_nr_filme(self):
        """returneaza numarul de filme inchiriate ale unui client
            date de intrare:
            date de iesire:nr_filme-int"""
        return self.__nr_filme
    def set_id_c(self,val):
        """atribuie id-ului o anumita valoare
        date de intrare:val-int
        date de iesire:-"""
        self.__id=val
    def set_nume(self,val):
        """"atribuie numelui o anumita valoare
        date de intrare:val-str
        date de iesire:-"""
        self.__nume=val
    def set_CNP(self,val):
        """atribuie CNP-ului o anumita valoare
        date de intrare:val-str
        date de iesire:-"""
        self.__CNP = val
    def set_nr_filme(self,val):
        """atribuie numarului de filme inchiriate o anumita valoare
        date de intrare:val-int
        date de iesire:-"""
        self.__nr_filme=val
    def __str__(self):
        return str(self.__id)+" Nume:"+self.__nume+" CNP:"+self.__CNP
    def __eq__(self,other):
        #returneaza daca doi clienti au acelasi id
        return self.__id==other.__id
