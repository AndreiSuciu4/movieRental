from domeniu.entitati_inchiriere import inchiriere
from domeniu.entitati_film import film
from domeniu.entitati_clienti import client
from validator.valid_inchiriere import valid_inchirieri
from erori.exceptii import ValidError,RepoError
from infrastructura.repo_inchirieri import repository_i,FileRepoInchiriere
from infrastructura.repo_clienti import repository_c,FileRepoClienti
from infrastructura.repo_film import repository_f,FileRepoFilm
from business.servicii_inchiriere import ServiceInchiriere
import unittest
class teste_inchirieri(unittest.TestCase):
    def test_creare_inchiriere(self):
        #testeaza daca o inchiriere e corect construita
        id=2
        Film=film(1,"1917","razboi","istorie")
        Client=client(1,"Andrei","5141445632201")
        zi_r=1
        luna_r=1
        an_r=2021
        Inchiriere=inchiriere(id,Client,Film,zi_r,luna_r,an_r)
        self.assertTrue(Inchiriere.get_id() == id)
        self.assertTrue(Inchiriere.get_client()==Client)
        self.assertTrue(Inchiriere.get_film()==Film)
        self.assertTrue(Inchiriere.get_zi_r()==zi_r)
        self.assertTrue(Inchiriere.get_luna_r()==luna_r)
        self.assertTrue(Inchiriere.get_an_r()==an_r)
        Inchiriere1=inchiriere(id,Client,Film,zi_r,luna_r,an_r)
        self.assertTrue(Inchiriere == Inchiriere1)

    def test_validare_inchiriere(self):
        # testeaza daca programul returneaza o eroare de tip ValidError in cazul in care este introdus un film cu atribuie incorecte
        valid=valid_inchirieri()
        id = 2
        Film = film(1, "1917", "razboi", "istorie")
        Client = client(1, "Andrei", "5141445632201")
        zi_r = 1
        luna_r = 10
        an_r = 2020
        Inchiriere = inchiriere(id, Client, Film, zi_r, luna_r, an_r)
        self.assertRaises(ValidError,valid.valideaza_inchiriere,Inchiriere)
    def test_repo(self):
        # functie care testeaza functiile din clasa repository_i:adauga_inchiriere,cauta_dupa_id,modifica_inchiriere si stergere_inchiriere
        # daca datele introduse de utilizator sunt incorecte,programul returneaza una dintre erorile din clasa RepoError
        id = 2
        Film = film(1, "1917", "razboi", "istorie")
        Client = client(1, "Marius", "5141445632201")
        zi_r = 1
        luna_r = 12
        an_r = 2021
        Inchiriere = inchiriere(id, Client, Film, zi_r,luna_r,an_r)
        self.repo=repository_i()
        Inchirieri=self.repo.get_all_inchirieri()
        self.assertTrue(len(Inchirieri)==0)
        #teste pentru adauga_inchiriere
        self.repo.adauga_inchiriere(Inchiriere)
        Inchirieri = self.repo.get_all_inchirieri()
        self.assertTrue(len(Inchirieri) == 1)
        self.assertTrue(Inchirieri[0].get_id() == id)
        self.assertTrue(Inchirieri[0].get_client() == Client)
        self.assertTrue(Inchirieri[0].get_film() == Film)
        self.assertTrue(Inchirieri[0].get_zi_r() == zi_r)
        self.assertTrue(Inchirieri[0].get_luna_r() == luna_r)
        self.assertTrue(Inchirieri[0].get_an_r() == an_r)
        self.assertRaises(RepoError,self.repo.adauga_inchiriere,Inchiriere)
        #teste pentru cauta_dupa_id_inchiriere
        inc=self.repo.cauta_dupa_id_inchiriere(id)
        self.assertTrue(inc.get_client()==Client)
        self.assertTrue(inc.get_film() == Film)
        self.assertTrue(inc.get_zi_r() == zi_r)
        self.assertTrue(inc.get_luna_r() == luna_r)
        self.assertTrue(inc.get_an_r() == an_r)
        self.assertRaises(RepoError,self.repo.cauta_dupa_id_inchiriere,7)
        id1 = 3
        Film1 = film(2, "Avatar", "Experiment", "SF")
        Client1 = client(2, "Marian", "5141445201401")
        zi_r1 = 2
        luna_r1 = 2
        an_r1 = 2021
        Inchiriere1 = inchiriere(id1, Client1, Film1, zi_r1,luna_r1,an_r1)
        self.repo.adauga_inchiriere(Inchiriere1)
        #teste pentru stergere_inchiriere
        self.repo.stergere_inchiriere(id)
        Inchirieri = self.repo.get_all_inchirieri()
        self.assertTrue(len(Inchirieri) == 1)
        self.assertTrue(Inchirieri[0].get_id() == id1)
        self.assertTrue(Inchirieri[0].get_client() == Client1)
        self.assertTrue(Inchirieri[0].get_film() == Film1)
        self.assertTrue(Inchirieri[0].get_zi_r() == zi_r1)
        self.assertTrue(Inchirieri[0].get_luna_r() == luna_r1)
        self.assertTrue(Inchirieri[0].get_an_r() == an_r1)
        self.assertRaises(RepoError,self.repo.stergere_inchiriere,4)
        #teste pentru modifica_inchiriere
        self.repo.modifica_inchiriere(id1,Client,Film,zi_r,luna_r,an_r)
        Inchirieri = self.repo.get_all_inchirieri()
        self.assertTrue(len(Inchirieri) == 1)
        self.assertTrue(Inchirieri[0].get_id() == id1)
        self.assertTrue(Inchirieri[0].get_client() == Client)
        self.assertTrue(Inchirieri[0].get_film() == Film)
        self.assertTrue(Inchirieri[0].get_zi_r() == zi_r)
        self.assertTrue(Inchirieri[0].get_luna_r() == luna_r)
        self.assertTrue(Inchirieri[0].get_an_r() == an_r)
        self.assertRaises(RepoError,self.repo.modifica_inchiriere,5,Client,Film,zi_r,luna_r,an_r)
    def test_service(self):
        #functie care testeza functiile din clasa ServiceInchiriere
        id = 2
        Film = film(1, "1917", "razboi", "istorie")
        Client = client(4, "Andrei", "5141445632201")
        zi_r = 1
        luna_r = 1
        an_r = 2021
        valid=valid_inchirieri()
        repo_i=repository_i()
        repo_c=repository_c()
        repo_f=repository_f()
        repo_f.adauga_film(Film)
        repo_c.adauga_client(Client)
        self.srv=ServiceInchiriere(repo_i,valid,repo_c,repo_f)
        #teste pentru adauga_inchiriere
        self.srv.adauga_inchirieri(id,4,1,zi_r,luna_r,an_r)
        Inchirieri =self.srv.get_all_inchirieri()
        self.assertTrue(len(Inchirieri) == 1)
        self.assertTrue(Inchirieri[0].get_id()==id)
        self.assertTrue(Inchirieri[0].get_nume() == "Andrei")
        self.assertTrue(Inchirieri[0].get_titlu() == "1917")
        self.assertTrue(Inchirieri[0].get_zi_r() == zi_r)
        self.assertTrue(Inchirieri[0].get_luna_r() == luna_r)
        self.assertTrue(Inchirieri[0].get_an_r() == an_r)
        id1 = 1
        Film1 = film(2, "Titanic", "film bun", "dragoste")
        repo_f.adauga_film(Film1)
        Client1 = client(2, "Gabi", "5021254500101")
        repo_c.adauga_client(Client1)
        zi_r1 = 1
        luna_r1 = 1
        an_r1 = 2021
        self.srv.adauga_inchirieri(id1,2,2,zi_r1,luna_r1,an_r1)
        #teste pentru stergere_inchiriere
        self.srv.stergere_inchiriere(id)
        Inchirieri = self.srv.get_all_inchirieri()
        self.assertTrue(len(Inchirieri) == 1)
        self.assertTrue(Inchirieri[0].get_id() == 1)
        self.assertTrue(Inchirieri[0].get_nume() == "Gabi")
        self.assertTrue(Inchirieri[0].get_titlu() == "Titanic")
        self.assertTrue(Inchirieri[0].get_zi_r() == zi_r1)
        self.assertTrue(Inchirieri[0].get_luna_r() == luna_r1)
        self.assertTrue(Inchirieri[0].get_an_r() == an_r1)
        self.assertRaises(RepoError,self.srv.stergere_inchiriere,10)
        #test pentru cauta_dupa_id_inchiriere
        self.assertRaises(RepoError,self.srv.cauta_dupa_id_inchiriere,7)
        #teste pentru modifica_inchiriere
        Film2 = film(3, "Avatar", "experiment", "SF")
        repo_f.adauga_film(Film2)
        Client2 = client(3, "Gabitzu", "5021252142101")
        repo_c.adauga_client(Client2)
        zi_r2 = 1
        luna_r2 = 1
        an_r2 = 2021
        self.srv.modifica_inchiriere(id1,3,3,zi_r2,luna_r2,an_r2)
        Inchirieri = self.srv.get_all_inchirieri()
        self.assertTrue(len(Inchirieri) == 1)
        self.assertTrue(Inchirieri[0].get_id() == id1)
        self.assertTrue(Inchirieri[0].get_nume() == "Gabitzu")
        self.assertTrue(Inchirieri[0].get_titlu() == "Avatar")
        self.assertTrue(Inchirieri[0].get_zi_r() == zi_r2)
        self.assertTrue(Inchirieri[0].get_luna_r() == luna_r2)
        self.assertTrue(Inchirieri[0].get_an_r() == an_r2)
        self.assertRaises(RepoError,self.srv.modifica_inchiriere,9,3,3,zi_r2,luna_r2,an_r2)
        #teste pentru ordonare_dupa_nume_client
        Film10 = film(10, "Home Alone", "craciun", "comedie")
        Client10 = client(10, "Andreea", "5141445632201")
        repo_f.adauga_film(Film10)
        repo_c.adauga_client(Client10)
        self.srv.adauga_inchirieri(10,10,10,2,2,2022)
        Client11 = client(11, "Ana", "5100125632201")
        repo_c.adauga_client(Client11)
        self.srv.adauga_inchirieri(11,11,10, 1, 1, 2021)
        nume =self.srv.ordonare_dupa_nume_client()
        self.assertTrue (len(nume)==3)
        self.assertTrue (nume[0] == Client11)
        self.assertTrue (nume[1] == Client10)
        self.assertTrue (nume[2]==Client2)
        #teste pentru ordonare_numar_filme
        Film11 = film(11, "Pistruiatul", "aventurile unui baiat", "comedie")
        repo_f.adauga_film(Film11)
        self.srv.adauga_inchirieri(12,10,11,1,1,2021)
        clienti_filme = self.srv.ordonare_numar_filme()
        self.assertTrue(len(clienti_filme) == 3)
        self.assertTrue(clienti_filme[0].get_nume()=="Andreea")
        self.assertTrue(clienti_filme[0].get_filme_inchiriate() == 2)
        #teste pentru cele_mai_inchiriate_filme
        cele_mai_inchiriate_filme =self.srv.cele_mai_inchiriate_filme()
        self.assertTrue(len(cele_mai_inchiriate_filme) == 1)
        self.assertTrue(cele_mai_inchiriate_filme[0].get_titlu()=="Home Alone")
        self.assertTrue(cele_mai_inchiriate_filme[0].get_nr_inchirieri()==2)
        #teste pentru primii_clienti
        Client12 = client(12, "Malina", "51007452632201")
        repo_c.adauga_client(Client12)
        self.srv.adauga_inchirieri(13,12,10,1,1,2021)
        Client13 = client(13, "Kazi", "5100125263221")
        repo_c.adauga_client(Client13)
        self.srv.adauga_inchirieri(14,13,10,1,1,2021)
        primii_clienti =self.srv.primii_clienti()
        self.assertTrue(len(primii_clienti) == 1)
        self.assertTrue(primii_clienti[0].get_nume()=="Andreea")
        self.assertTrue(primii_clienti[0].get_filme_inchiriate()==2)
        #teste pentru rap2
        rap2=self.srv.rap2("A")
        self.assertTrue(len(rap2)==2)
        self.assertTrue(rap2[0]==Client11)
        self.assertTrue(rap2[1] == Client10)
    def ruleaza_teste_inchiriere(self):
        self.test_creare_inchiriere()
        self.test_repo()
        self.test_validare_inchiriere()
        self.test_service()
class teste_FileRepoInchiriere(unittest.TestCase):
    def test_repo_inchiriere_cu_fisiere(self):
        #testeaza functiile din clasa FileRepoInchiriere
        with open("teste_inchiriere.txt","w") as f:
            f.write("")
        self.repo = FileRepoInchiriere("teste_inchiriere.txt")
        id = 2
        Film = film(1, "1917", "razboi", "istorie")
        Client = client(1, "Marius", "5141445632201")
        zi_r = 1
        luna_r = 12
        an_r = 2021
        Inchiriere = inchiriere(id, Client, Film, zi_r, luna_r, an_r)
        Inchirieri = self.repo.get_all_inchirieri()
        self.assertTrue(len(Inchirieri) == 0)
        #teste pentru adauga_inchiriere
        self.repo.adauga_inchiriere(Inchiriere)
        Inchirieri = self.repo.get_all_inchirieri()
        self.assertTrue(len(Inchirieri) == 1)
        self.assertTrue(Inchirieri[0].get_id() == id)
        self.assertTrue(Inchirieri[0].get_client() == Client)
        self.assertTrue(Inchirieri[0].get_film() == Film)
        self.assertTrue(Inchirieri[0].get_zi_r() == zi_r)
        self.assertTrue(Inchirieri[0].get_luna_r() == luna_r)
        self.assertTrue(Inchirieri[0].get_an_r() == an_r)
        self.assertRaises(RepoError, self.repo.adauga_inchiriere, Inchiriere)
        #teste pentru cauta_dupa_id_inchiriere
        inc = self.repo.cauta_dupa_id_inchiriere(id)
        self.assertTrue(inc.get_client() == Client)
        self.assertTrue(inc.get_film() == Film)
        self.assertTrue(inc.get_zi_r() == zi_r)
        self.assertTrue(inc.get_luna_r() == luna_r)
        self.assertTrue(inc.get_an_r() == an_r)
        self.assertRaises(RepoError, self.repo.cauta_dupa_id_inchiriere, 7)
        id1 = 3
        Film1 = film(2, "Avatar", "Experiment", "SF")
        Client1 = client(2, "Marian", "5141445201401")
        zi_r1 = 2
        luna_r1 = 2
        an_r1 = 2021
        Inchiriere1 = inchiriere(id1, Client1, Film1, zi_r1, luna_r1, an_r1)
        self.repo.adauga_inchiriere(Inchiriere1)
        #teste pentru stergere_inchiriere
        self.repo.stergere_inchiriere(id)
        Inchirieri = self.repo.get_all_inchirieri()
        self.assertTrue(len(Inchirieri) == 1)
        self.assertTrue(Inchirieri[0].get_id() == id1)
        self.assertTrue(Inchirieri[0].get_client() == Client1)
        self.assertTrue(Inchirieri[0].get_film() == Film1)
        self.assertTrue(Inchirieri[0].get_zi_r() == zi_r1)
        self.assertTrue(Inchirieri[0].get_luna_r() == luna_r1)
        self.assertTrue(Inchirieri[0].get_an_r() == an_r1)
        self.assertRaises(RepoError, self.repo.stergere_inchiriere, 4)
        #teste pentru modifica_inchiriere
        self.repo.modifica_inchiriere(id1, Client, Film, zi_r, luna_r, an_r)
        Inchirieri = self.repo.get_all_inchirieri()
        self.assertTrue(len(Inchirieri) == 1)
        self.assertTrue(Inchirieri[0].get_id() == id1)
        self.assertTrue(Inchirieri[0].get_client() == Client)
        self.assertTrue(Inchirieri[0].get_film() == Film)
        self.assertTrue(Inchirieri[0].get_zi_r() == zi_r)
        self.assertTrue(Inchirieri[0].get_luna_r() == luna_r)
        self.assertTrue(Inchirieri[0].get_an_r() == an_r)
        self.assertRaises(RepoError, self.repo.modifica_inchiriere, 5, Client, Film, zi_r, luna_r, an_r)


