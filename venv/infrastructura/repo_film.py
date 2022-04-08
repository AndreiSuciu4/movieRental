from domeniu.entitati_film import film
from erori.exceptii import RepoError


class repository_f():
    def __init__(self):
        # creeaza o noua instanta pentru clasa repository_f
        self._elem_film = []
    def adauga_film(self,film):
        """"adauga un film in lista de filme
            date de intrare:film
            date de iesire:-
            daca id-ul filmului este deja prezent in lista de filme atunci programul afiseaza eroarea:film deja adaugat"""
        if film in self._elem_film:
            raise RepoError("film deja adaugat\n")
        self._elem_film.append(film)
    def cauta_dupa_id_film(self,id):
        """"cauta un film in lista de filme care are un anumit id
        date de intrare:id-tip int
        date de iesire:film
        daca id-ul introdus nu se afla  in lista programul returneaza eroarea:film inexistent!"""
        for i in range(len(self._elem_film)):
            if self._elem_film[i].get_id() == id:
                return self._elem_film[i]
        raise RepoError("film inexistent!\n")
    def __len__(self):
        """returneaza lungimea listei de filme
        date de intrare:-
        date de iesire:lungimea listei"""
        return len(self._elem_film)
    def get_all_film(self):
        """returneaza toate filmele din lista
        date de intrare:-
        date de iesire:-elementele listei"""
        return self._elem_film[:]
    def modifica_film(self,id,titlu,descriere,gen):
        """"modifica datele unui film
        date de intrare:id-int
                        -titlu-str
                        -descriere-str
                        -gen-str
        date de iesire:lista modificata
        daca utilizatorul introduce un id care nu e in lista programul returneaza eroarea:film inexistent"""
        for i in range(len(self._elem_film)):
            if self._elem_film[i].get_id() == id:
                self._elem_film[i].set_titlu(titlu)
                self._elem_film[i].set_descriere(descriere)
                self._elem_film[i].set_gen(gen)
                return
        raise RepoError("film inexistent!\n")


    def stergere_film(self,id):
        """"functie care sterge din lista un film cu un anumit id
        date de intrare:id-tip int
        date de iesire:lista modificata
        daca utilizatorul introduce un id inexistent programul returneaza eroarea:film inexistent"""
        for i in range (len(self._elem_film)):
            if self._elem_film[i].get_id()==id:
                self._elem_film.remove(self._elem_film[i])
                #print("stergere efectuata cu succes pentru filmul cu Id-ul:" + str(id))
                return
        raise RepoError("film inexistent\n")
    def incrementeaza_film(self,id):
        """"incrementeaza numarul de inchirieri ale unui film
                date de intrare:id-int
                date de iesire:-"""
        for i in self._elem_film:
            if i.get_id()==id:
                nr=i.get_nr_inchirieri()
                i.set_nr_inchirieri(nr+1)

    def decrementeaza_film(self,id):
        """"decrementeaza numarul de inchirieri ale unui film
                    date de intrare:id-int
                    date de iesire:-"""
        for i in self._elem_film:
            if i.get_id()==id:
                nr=i.get_nr_inchirieri()
                i.set_nr_inchirieri(nr-1)



class FileRepoFilm(repository_f):
    def __init__(self, text):
        self.__text = text
        repository_f.__init__(self)

    def __citeste_filme_din_fisier(self):
        """"functie care citeste filme din fisier
            date de intrare:-
            date de iesire:-"""
        parts=[]
        with open(self.__text, "r") as f:
            self._elem_film = []
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line != "":
                    parts = line.split(",")
                    Film = film(int(parts[0]), parts[1], parts[2] , parts[3])
                    Film.set_nr_inchirieri(int(parts[4]))
                    self._elem_film.append(Film)

    def __append_film(self, Film):
        """"functie care adauga un film in fisier
                date de intrare:-
                date de iesire:-"""
        with open(self.__text, "a") as f:
            f.write(str(Film.get_id()) + "," + Film.get_titlu()+ "," + Film.get_descriere()+","+Film.get_gen()+","+str(Film.get_nr_inchirieri())+"\n")

    def __scrie_tot_in_fisier(self):
        """"functie care scrie in fisier toate filmele din memorie
                date de intrare:-
                date de iesire:-"""
        with open(self.__text, "w") as f:
            for Film in self._elem_film:
                f.write(str(Film.get_id()) + "," + Film.get_titlu() + "," + Film.get_descriere() + "," + Film.get_gen()+","+str(Film.get_nr_inchirieri())+"\n")

    def adauga_film(self,Film):
        """"adauga un film in fisier
                date de intrare:film
                date de iesire:-
                daca id-ul filmului este deja prezent in fisier atunci programul afiseaza eroarea:film deja adaugat"""
        self.__citeste_filme_din_fisier()
        repository_f.adauga_film(self, Film)
        self.__append_film(Film)

    def incrementeaza_film(self,id):
        """"incrementeaza numarul de inchirieri ale unui film
            date de intrare:id-int
            date de iesire:-"""
        self.__citeste_filme_din_fisier()
        repository_f.incrementeaza_film(self,id)
        self.__scrie_tot_in_fisier()

    def decrementeaza_film(self,id):
        """"decrementeaza numarul de inchirieri ale unui film
            date de intrare:id-int
            date de iesire:-"""
        self.__citeste_filme_din_fisier()
        repository_f.decrementeaza_film(self,id)
        self.__scrie_tot_in_fisier()

    def cauta_dupa_id_film(self,id):
        """"cauta un film in fisier care are un anumit id
            date de intrare:id-tip int
            date de iesire:film
            daca id-ul introdus nu se afla  in fisier programul returneaza eroarea:film inexistent!"""
        self.__citeste_filme_din_fisier()
        return repository_f.cauta_dupa_id_film(self, id)

    def __len__(self):
        """returneaza numarul filmelor din fisier
        date de intrare:-
        date de iesire:numarul filmelor"""
        self.__citeste_filme_din_fisier()
        return repository_f.__len__(self)

    def get_all_film(self):
        """returneaza toate filmele fisier
        date de intrare:-
        date de iesire:-filmele din fisier"""
        self.__citeste_filme_din_fisier()
        return repository_f.get_all_film(self)

    def stergere_film(self,id):
        """"functie care sterge din fisier un film cu un anumit id
        date de intrare:id-tip int
        date de iesire:-
        daca utilizatorul introduce un id inexistent programul returneaza eroarea:film inexistent"""
        self.__citeste_filme_din_fisier()
        repository_f.stergere_film(self,id)
        self.__scrie_tot_in_fisier()

    def modifica_film(self,id,titlu,descriere,gen):
        """"modifica datele unui film
            date de intrare:id-int
                -titlu-str
                -descriere-str
                -gen-str
            date de iesire:-
            daca utilizatorul introduce un id care nu e in fisier programul returneaza eroarea:film inexistent"""
        self.__citeste_filme_din_fisier()
        repository_f.modifica_film(self,id,titlu,descriere,gen)
        self.__scrie_tot_in_fisier()



