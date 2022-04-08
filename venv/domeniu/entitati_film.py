class film:
    def __init__(self,id,titlu,descriere,gen):
        # creeaza o noua instanta pentru clasa film
        self.__id=id
        self.__titlu=titlu
        self.__descriere=descriere
        self.__gen=gen
        self.__nr_inchirieri=0
    def get_id(self):
        """returneaza id_ul unui film
        date de intrare:-
        date de ieisre:id-int"""
        return self.__id
    def get_titlu(self):
        """returneaza titlul unui film
        date de intrare:
        date de iesire:titlu-str"""
        return self.__titlu
    def get_descriere(self):
        """returneaza descrierea unui film
        date de intrare:
        date de iesire:descriere-str"""
        return self.__descriere
    def get_gen(self):
        """returneaza genul unui film
        date de intrare:
        date de iesire:gen-str"""
        return self.__gen
    def get_nr_inchirieri(self):
        """returneaza nr de inchirieri ale unui film
        date de intrare:-
        date de iesire:nr_inchirieri-int"""
        return self.__nr_inchirieri

    def set_id(self,val):
        """atribuie id-ului o anumita valoare
        date de intrare:val-int
        date de iesire:-"""
        self.__id=val
    def set_titlu(self,val):
        """atribuie titlului o anumita valoare
        date de intrare:val-str
        date de iesire:-"""
        self.__titlu=val
    def set_descriere(self,val):
        """atribuie descrierii o anumita valoare
        date de intrare:val-str
        date de iesire:-"""
        self.__descriere=val
    def set_gen(self,val):
        """atribuie genului o anumita valoare
        date de intrare:val-str
        date de iesire:-"""
        self.__gen=val
    def set_nr_inchirieri(self,val):
        """atribuie numarului de inchirieri o anumita valoare
        date de intrare:val-int
        date de iesire:-"""
        self.__nr_inchirieri=val
    def __str__(self):
        return str(self.__id)+" titlu:"+self.__titlu+" descriere:"+self.__descriere+" gen:"+self.__gen
    def __eq__(self,other):
        #verifica daca doua filme au acelasi id
        return self.__id == other.__id



