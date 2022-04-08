from domeniu.entitati_inchiriere import inchiriere
from domeniu.entitati_film import film
from domeniu.entitati_clienti import client
from erori.exceptii import RepoError

class repository_i():
    def __init__(self):
        # creeaza o noua instanta pentru clasa repository_i
        self._inchirieri = []
    def adauga_inchiriere(self,inchiriere):
        """"adauga o inchiriere in lista de inchirieri
        date de intrare:inchiriere
        date de iesire:-
        daca id-ul inchirierii  este deja prezent in lista de inchirieri atunci programul afiseaza eroarea:id deja utitlizat"""
        if inchiriere in self._inchirieri:
            raise RepoError("id deja utilizat\n")
            return
        self._inchirieri.append(inchiriere)

    def get_all_inchirieri(self):
        """returneaza toate inchirierile din lista
        date de intrare:-
        date de iesire:lista de inchirieri"""
        return self._inchirieri[:]
    def __len__(self):
        """returneaza lungimea listei de inchirieri
        date de intrare:-
        date de iesire:lungimea listei"""
        return len(self._inchirieri)

    def stergere_inchiriere(self,id):
        """sterge din lista o inchiriere cu un anumit id
        date de intrare:id-tip int
        date de iesire:lista modificata
        daca utilizatorul introduce un id inexistent programul returneaza eroarea:inchiriere inexistenta"""
        for i in range (len(self._inchirieri)):
            if self._inchirieri[i].get_id()==id:
                self._inchirieri.remove(self._inchirieri[i])
                return
        raise RepoError("inchiriere inexistenta\n")

    def cauta_dupa_id_inchiriere(self,id):
        """"cauta o inchiriere in lista  care are un anumit id
        date de intrare:id-tip int
        date de iesire:inchiriere
        daca id-ul introdus nu se afla  in lista,programul returneaza eroarea:inchiriere inexistenta!"""
        for i in range(len(self._inchirieri)):
            if self._inchirieri[i].get_id() == id:
                return self._inchirieri[i]
        raise RepoError("inchiriere inexistenta!\n")
        return

    def modifica_inchiriere(self,id_i,client,film,zi_r,luna_r,an_r):
        """"modifica datele unuei inchirieri
        date de intrare:id_i-int
                        client
                        film
                        zi_r-int
                        luna_r-int
                        an_r-int
        date de iesire:lista modificata
        daca utilizatorul introduce un id care nu e in lista programul returneaza eroarea:film inexistent"""
        for i in range(len(self._inchirieri)):
            if self._inchirieri[i].get_id()==id_i:
                self._inchirieri[i].set_client(client)
                self._inchirieri[i].set_film(film)
                self._inchirieri[i].set_zi_r(zi_r)
                self._inchirieri[i].set_luna_r(luna_r)
                self._inchirieri[i].set_an_r(an_r)
                return
        raise RepoError("id inexistent!\n")

class FileRepoInchiriere(repository_i):
    def __init__(self, text):
        self.__text = text
        repository_i.__init__(self)

    def __citeste_inchiriere_din_fisier(self):
        """"functie care citeste inchirieri din fisier
            date de intrare:-
            date de iesire:-"""
        with open(self.__text, "r") as f:
            self._inchirieri = []
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line != "":
                    parts = line.split(",")
                    Client=client(int(parts[1]),parts[2],parts[3])
                    Film=film(int(parts[4]),parts[5],parts[6],parts[7])
                    Inchiriere=inchiriere(int(parts[0]),Client,Film,int(parts[8]),int(parts[9]),int(parts[10]))
                    self._inchirieri.append(Inchiriere)

    def __append_inchiriere(self, Inchiriere):
        """"functie care adauga o inchiriere in fisier
            date de intrare:-
            date de iesire:-"""
        with open(self.__text, "a") as f:
            f.write(str(Inchiriere.get_id())+","+str(Inchiriere.get_client().get_id_c())+","+Inchiriere.get_client().get_nume()+","+Inchiriere.get_client().get_CNP()+","+str(Inchiriere.get_film().get_id())+","+Inchiriere.get_film().get_titlu()+","+Inchiriere.get_film().get_descriere()+","+Inchiriere.get_film().get_gen()+","+str(Inchiriere.get_zi_r())+","+str(Inchiriere.get_luna_r())+","+str(Inchiriere.get_an_r())+"\n")

    def __scrie_tot_in_fisier(self):
        """"functie care scrie in fisier toate inchirierile din memorie
            date de intrare:-
            date de iesire:-"""
        with open(self.__text, "w") as f:
            for Inchiriere in self._inchirieri:
                f.write(str(Inchiriere.get_id()) + "," + str(Inchiriere.get_client().get_id_c()) + "," + Inchiriere.get_client().get_nume() + "," + Inchiriere.get_client().get_CNP()+ "," + str(Inchiriere.get_film().get_id()) + "," + Inchiriere.get_film().get_titlu() + "," + Inchiriere.get_film().get_descriere() + "," + Inchiriere.get_film().get_gen()  + "," + str(Inchiriere.get_zi_r()) + "," + str(Inchiriere.get_luna_r()) + "," + str(Inchiriere.get_an_r()) + "\n")

    def adauga_inchiriere(self,Inchiriere):
        """"adauga o inchiriere in fisier
                date de intrare:inchiriere
                date de iesire:-
                daca id-ul inchirierii  este deja prezent in fisier atunci programul afiseaza eroarea:id deja utitlizat"""
        self.__citeste_inchiriere_din_fisier()
        repository_i.adauga_inchiriere(self,Inchiriere)
        self.__append_inchiriere(Inchiriere)

    def cauta_dupa_id_inchiriere(self,id):
        """"cauta o inchiriere in fisier  care are un anumit id
                date de intrare:id-tip int
                date de iesire:inchiriere
                daca id-ul introdus nu se afla in fisier,programul returneaza eroarea:inchiriere inexistenta!"""
        self.__citeste_inchiriere_din_fisier()
        return repository_i.cauta_dupa_id_inchiriere(self,id)

    def __len__(self):
        """returneaza numarul de inchirieri din fisier
            date de intrare:-
            date de iesire:numarul de inchirieri"""
        self.__citeste_inchiriere_din_fisier()
        return repository_i.__len__(self)

    def get_all_inchirieri(self):
        """returneaza toate inchirierile din fisier
        date de intrare:-
        date de iesire:lista de inchirieri"""
        self.__citeste_inchiriere_din_fisier()
        return repository_i.get_all_inchirieri(self)

    def stergere_inchiriere(self,id):
        """sterge din fisier o inchiriere cu un anumit id
        date de intrare:id-tip int
        date de iesire:-
        daca utilizatorul introduce un id inexistent programul returneaza eroarea:inchiriere inexistenta"""
        self.__citeste_inchiriere_din_fisier()
        repository_i.stergere_inchiriere(self,id)
        self.__scrie_tot_in_fisier()

    def modifica_inchiriere(self,id_i,client,film,zi_r,luna_r,an_r):
        """"modifica datele unuei inchirieri
            date de intrare:id_i-int
                        client
                        film
                        zi_r-int
                        luna_r-int
                        an_r-int
            date de iesire:-
            daca utilizatorul introduce un id care nu e in fisier programul returneaza eroarea:film inexistent"""
        self.__citeste_inchiriere_din_fisier()
        repository_i.modifica_inchiriere(self,id_i,client,film,zi_r,luna_r,an_r)
        self.__scrie_tot_in_fisier()



