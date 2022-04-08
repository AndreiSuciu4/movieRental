from infrastructura.repo_inchirieri import repository_i
from infrastructura.repo_clienti import repository_c
from infrastructura.repo_film import repository_f
from validator.valid_inchiriere import valid_inchirieri
from domeniu.entitati_inchiriere import inchiriere,InchirieriDTO,Ordonare_numar_filmeDTO,Cele_mai_inchiriate_filmeDTO
from domeniu.entitati_film import film
from domeniu.entitati_clienti import client

class ServiceInchiriere:



    def __init__(self,repo,valid_i,repo_c,repo_f):
        # creeaza o noua instanta pentru clasa ServiceFilm
        self.__repo=repo
        self.__valid_i=valid_i
        self.__repo_c=repo_c
        self.__repo_f=repo_f

    def adauga_inchirieri(self,id_i,id_c,id_f,zi_r,luna_r,an_r):
        """verifica daca o inchiriere este valida si o adauga in lista de inchirieri
        date de intrare:id_i-int
                        id_c-int
                        id_f-int
                        zi_r-int
                        luna_r-int
                        an_r-int
        date de iesire:-"""
        nume=self.__repo_c.cauta_dupa_id_client(id_c)
        titlu=self.__repo_f.cauta_dupa_id_film(id_f)
        Inchiriere=inchiriere(id_i,nume,titlu,zi_r,luna_r,an_r)
        self.__valid_i.valideaza_inchiriere(Inchiriere)
        self.__repo.adauga_inchiriere(Inchiriere)
        self.__repo_c.incrementeaza_clienti(id_c)
        self.__repo_f.incrementeaza_film(id_f)

    def get_all_inchirieri(self):
        """returneaza toate inchirierile din lista
        date de intrare:-
        date de iesire:-inchirierile  din lista"""
        Inchirieri=self.__repo.get_all_inchirieri()
        aux=[]
        for i in Inchirieri:
            id_i=i.get_id()
            nume_client = i.get_client().get_nume()
            titlu_film=i.get_film().get_titlu()
            zi_r=i.get_zi_r()
            luna_r=i.get_luna_r()
            an_r=i.get_an_r()
            Inchiriere1=InchirieriDTO(id_i,nume_client,titlu_film,zi_r,luna_r,an_r)
            aux.append(Inchiriere1)
        return aux

    def stergere_inchiriere(self,id):
        """sterge o anumita inchiriere din lista
        date de intrare:id-int
        date de iesire:-"""
        id_c=self.__repo.cauta_dupa_id_inchiriere(id).get_client().get_id_c()
        id_f = self.__repo.cauta_dupa_id_inchiriere(id).get_film().get_id()
        self.__repo.stergere_inchiriere(id)
        self.__repo_c.decrementeaza_clienti(id_c)
        self.__repo_f.decrementeaza_film(id_f)


    def cauta_dupa_id_inchiriere(self,id):
        """cauta o inchiriere dupa un id dat
        date de intrare:id-int
        date de iesire:inchirierea cu id-ul respectiv"""
        aux=self.__repo.cauta_dupa_id_inchiriere(id)
        id_i = aux.get_id()
        nume_client = aux.get_client().get_nume()
        titlu_film = aux.get_film().get_titlu()
        zi_r = aux.get_zi_r()
        luna_r=aux.get_luna_r()
        an_r=aux.get_an_r()
        Inchiriere1 = InchirieriDTO(id_i, nume_client, titlu_film, zi_r,luna_r,an_r)
        print((Inchiriere1))

    def modifica_inchiriere(self,id_i,id_c,id_f,zi_r,luna_r,an_r):
        """modifica datele uunei anumite inchirieri
        date de intrare:id_i-int
                        id_c-int
                        id_f-int
                        zi_r-int
                        luna_r-int
                        an_r-int
        date de iesire:-"""
        nume = self.__repo_c.cauta_dupa_id_client(id_c)
        titlu = self.__repo_f.cauta_dupa_id_film(id_f)
        id_c1 = self.__repo.cauta_dupa_id_inchiriere(id_i).get_client().get_id_c()
        id_f1 = self.__repo.cauta_dupa_id_inchiriere(id_i).get_film().get_id()
        self.__repo.modifica_inchiriere(id_i, nume, titlu, zi_r, luna_r, an_r)
        self.__repo_c.decrementeaza_clienti(id_c1)
        self.__repo_f.decrementeaza_film(id_f1)
        self.__repo_f.incrementeaza_film(id_f)
        self.__repo_c.incrementeaza_clienti(id_c)

    def ordonare_dupa_nume_client(self):
        """" ordoneaza clientii in functie de nume
        date de intrare:-
        date de iesire:Clienti-list"""
        inchirieri=self.__repo.get_all_inchirieri()
        if len(inchirieri)<1:
            print("nu avem inchirieri")
            return
        clienti = []
        Clienti=[]
        clienti=self.__repo_c.get_all_clienti()
        for el in clienti:
            if el.get_nr_filme()>0:
                Clienti.append(el)
        Clienti.sort(key = lambda x: x.get_nume())
        return Clienti
    def ordonare_numar_filme(self):
        """"ordoneaza clientii in functie de numarul filmelor inchiriate
        date de intrare:-
        date de iesire:-"""
        inchirieri = self.__repo.get_all_inchirieri()
        if len(inchirieri)<0:
            print("nu avem inchirieri\n")
        clienti_str=[]
        clienti=self.__repo_c.get_all_clienti()
        clienti.sort(key=lambda x: x.get_nr_filme(), reverse=True)
        for el in clienti:
            if el.get_nr_filme()>0:
                clienti_str.append(Ordonare_numar_filmeDTO(el.get_nume(),el.get_nr_filme()))
        return clienti_str
    def cele_mai_inchiriate_filme(self):
        """"cele mai inchiriate filme
        date de intrare:-
        date de iesire:filme_str-list"""
        inchirieri = self.__repo.get_all_inchirieri()
        if len(inchirieri)<1:
            print("nu avem inchirieri")
            return
        filme = self.__repo_f.get_all_film()
        nr_inchirieri = []
        filme_str=[]
        filme.sort(key=lambda x: x.get_nr_inchirieri(), reverse=True)
        max=filme[0]
        for el in filme:
            if el.get_nr_inchirieri() == max.get_nr_inchirieri() :
                filme_str.append(Cele_mai_inchiriate_filmeDTO(el.get_titlu(),el.get_nr_inchirieri()))
        return filme_str

    def primii_clienti(self):
        """" primii 30% clienti cu cele mai multe filme (nume client și numărul de filme închiriate)
        date de intrare:-
        date de iesire:-client_str-list"""
        inchirieri = self.__repo.get_all_inchirieri()
        Clienti=[]
        clienti=[]
        if len(inchirieri)<1:
            print("nu avem inchirieri")
            return
        clienti=self.__repo_c.get_all_clienti()
        client_str=[]
        clienti.sort(key=lambda x: x.get_nr_filme(), reverse=True)
        for el in clienti:
            if el.get_nr_filme()>0:
                Clienti.append(el)
        lungime=len(Clienti)
        if lungime<4:
            client_str.append(Ordonare_numar_filmeDTO(Clienti[0].get_nume(),Clienti[0].get_nr_filme()))
        else:
            for el in range(int(3*lungime/10)):
                client_str.append(Ordonare_numar_filmeDTO(Clienti[el].get_nume(),Clienti[el].get_nr_filme()))
        return client_str

    def rap2(self,litera):
        """"returneaza toti clientii cu inchirieri care incep cu oanumita litera citita de la tastatura
        date de intrare:-litera-str
        date de iesire:clienti_rap-list"""
        inchirieri = self.__repo.get_all_inchirieri()
        if len(inchirieri) < 1:
            print("nu avem inchirieri")
            return
        clienti_rap=[]
        clienti = []
        clienti=self.__repo_c.get_all_clienti()
        clienti.sort(key=lambda x: x.get_nume())
        for el in clienti:
            if(el.get_nume()[0]==litera and el.get_nr_filme()>0):
                clienti_rap.append(el)
        return clienti_rap






