from domeniu.entitati_clienti import client
from erori.exceptii import RepoError

class repository_c:
    def __init__(self):
        # creeaza o noua instanta pentru clasa repository_c
        self._elem_clienti = []
    def adauga_client(self,client):
        """"adauga un client in lista de clienti
            date de intrare:client
            date de iesire:-
            daca id-ul clientului  este deja prezent in lista de clienti atunci programul afiseaza eroarea:client deja adaugat"""
        if client in self._elem_clienti:
            raise RepoError("client deja adaugat\n")
        self._elem_clienti.append(client)
    def cauta_dupa_id_client(self,id):
        """"cauta un client in lista de clienti care are un anumit id
            date de intrare:id_c-tip int
            date de iesire:clientul cu id-ul respectiv
            daca id-ul nu e introdus nu se afla in lista programul returneaza eroarea:client inexistent!
                """
        for i in range(len(self._elem_clienti)):
            if self._elem_clienti[i].get_id_c() == id:
                return self._elem_clienti[i]
        raise RepoError("client inexistent!\n")
    def get_all_clienti(self):
        """returneaza toti clientii din lista
        date de intare:-
        date de iesire:elementele listei"""
        return self._elem_clienti[:]
    def __len__(self):
        """returneaza lungimea listei de clienti
        date de intrare:-
        date de iesire:lungimea listei"""
        return len(self._elem_clienti)
    def modifica_client(self,id_c,nume,CNP):
        """modifica datele unui client
            date de intrare:id-int
                            nume-str
                            CNP-str
            date de iesire:lista modificata
            daca utilizatorul introduce un ID care nu e in lista programul returneaza eroarea:client inexistent"""
        for i in range(len(self._elem_clienti)):
            if self._elem_clienti[i].get_id_c() == id_c:
                self._elem_clienti[i].set_nume(nume)
                self._elem_clienti[i].set_CNP(CNP)
                return
        raise RepoError("client inexistent!\n")
    def stergere_client(self,id):
        """"sterge din lista un client cu un anumit id
                date de intrare:id-tip int
                date de iesire:lista modificata
                daca utilizatorul introduce un id inexistent programul returneaza eroarea:client inexistent"""
        for i in range (len(self._elem_clienti)):

            if self._elem_clienti[i].get_id_c()==id:
                self._elem_clienti.remove(self._elem_clienti[i])
                return
        raise RepoError("client inexistent!\n")
    def incrementeaza_clienti(self,id):
        """"incrementeaza numarul de filme inchiriate ale unui client
        date de intrare:id-int
        date de iesire:-"""
        for i in self._elem_clienti:
            if i.get_id_c()==id:
                nr=i.get_nr_filme()
                i.set_nr_filme(nr+1)

    def decrementeaza_clienti(self,id):
        """"decrementeaza numarul de filme inchiriate ale unui client
            date de intrare:id-int
            date de iesire:-"""
        for i in self._elem_clienti:
            if i.get_id_c()==id:
                nr=i.get_nr_filme()
                i.set_nr_filme(nr-1)

class FileRepoClienti(repository_c):
    def __init__(self,text):
        self.__text=text
        repository_c.__init__(self)
    def __citeste_clienti_din_fisier(self):
        """"functie care citeste clientii din fisier
        date de intrare:-
        date de iesire:-"""
        parts=[]
        with open(self.__text,"r") as f:
            self._elem_clienti=[]
            lines=f.readlines()
            for line in lines:
                line=line.strip()
                if line !="":
                    parts=line.split(",")
                    Client=client(int(parts[0]),parts[1],parts[2])
                    Client.set_nr_filme(int(parts[3]))
                    self._elem_clienti.append(Client)
    def __append_client(self,Client):
        """"functie care adauga un client in fisier
        date de intrare:-
        date de iesire:-"""
        with open(self.__text,"a") as f:
            f.write(str(Client.get_id_c())+","+Client.get_nume()+","+Client.get_CNP()+","+str(Client.get_nr_filme())+"\n")

    def __scrie_tot_in_fisier(self):
        """"functie care scrie in fisier toti clientii din memorie
        date de intrare:-
        date de iesire:-"""
        with open(self.__text,"w") as f:
            for Client in self._elem_clienti:
                f.write(str(Client.get_id_c()) + "," + Client.get_nume() + "," + Client.get_CNP()+","+str(Client.get_nr_filme())+"\n")

    def adauga_client(self,Client):
        """"adauga un client fisier
            date de intrare:client
            date de iesire:-
            daca id-ul clientului  este deja prezent in fisier de clienti atunci programul afiseaza eroarea:client deja adaugat"""
        self.__citeste_clienti_din_fisier()
        repository_c.adauga_client(self,Client)
        self.__append_client(Client)

    def incrementeaza_clienti(self,id):
        """"incrementeaza numarul de filme inchiriate ale unui client
        date de intrare:id-int
        date de iesire:-"""
        self.__citeste_clienti_din_fisier()
        repository_c.incrementeaza_clienti(self,id)
        self.__scrie_tot_in_fisier()

    def decrementeaza_clienti(self,id):
        """"decrementeaza numarul de filme inchiriate ale unui client
            date de intrare:id-int
            date de iesire:-"""
        self.__citeste_clienti_din_fisier()
        repository_c.decrementeaza_clienti(self,id)
        self.__scrie_tot_in_fisier()

    def cauta_dupa_id_client(self,id):
        """"cauta un client in fisier care are un anumit id
            date de intrare:id_c-tip int
            date de iesire:clientul cu id-ul respectiv
            daca id-ul nu e introdus nu se afla in fisier programul returneaza eroarea:client inexistent!
                        """
        self.__citeste_clienti_din_fisier()
        return repository_c.cauta_dupa_id_client(self,id)

    def __len__(self):
        """returneaza numarul de clienti din fisier
            date de intrare:-
            date de iesire:numarul de clienti din fisier"""
        self.__citeste_clienti_din_fisier()
        return repository_c.__len__(self)

    def get_all_clienti(self):
        """returneaza toti clientii din fisier
        date de intare:-
        date de iesire:elementele listei"""
        self.__citeste_clienti_din_fisier()
        return repository_c.get_all_clienti(self)

    def stergere_client(self,id):
        """"sterge din fisier un client cu un anumit id
        date de intrare:id-tip int
        date de iesire:lista modificata
        daca utilizatorul introduce un id inexistent programul returneaza eroarea:client inexistent"""
        self.__citeste_clienti_din_fisier()
        repository_c.stergere_client(self,id)
        self.__scrie_tot_in_fisier()

    def modifica_client(self,id_c,nume,CNP):
        """modifica datele unui client
           date de intrare:id-int
                            nume-str
                            CNP-str
           date de iesire:-
           daca utilizatorul introduce un ID care nu e in fisier programul returneaza eroarea:client inexistent"""
        self.__citeste_clienti_din_fisier()
        repository_c.modifica_client(self,id_c,nume,CNP)
        self.__scrie_tot_in_fisier()








