from domeniu.entitati_clienti import client
from validator.valid_clienti import valid_clienti
from erori.exceptii import ValidError,RepoError
from infrastructura.repo_clienti import repository_c,FileRepoClienti
from business.servicii_clienti import ServiceClient
import unittest
class teste_clienti(unittest.TestCase):
    def test_creare_client(self):
        #testeaza daca un client este construit corect
        id=2
        nume="Andrei"
        CNP="5012453629874"
        Client=client(id,nume,CNP)
        self.assertEqual(Client.get_id_c(),id)
        self.assertEqual(Client.get_nume(),nume)
        self.assertEqual(Client.get_CNP(),CNP)
        self.assertEqual(str(Client),"2 Nume:Andrei CNP:5012453629874")
        alt_client=client(id,"Adi","5014257584693")
        self.assertEqual(Client,alt_client)

    def test_validare_clienti(self):
        #testeaza daca programul returneaza o eroare de tip ValidError in cazul in care este introdus un client cu atribuie incorecte
        Client=client(1,"","")
        self.assertRaises(ValidError,valid_clienti.valideaza_clienti,self,Client)
        Client1=client(1,"Andrei","")
        self.assertRaises(ValidError, valid_clienti.valideaza_clienti, self, Client1)
        Client2=client(-1,"","5214125214125")
        self.assertRaises(ValidError, valid_clienti.valideaza_clienti, self, Client2)
        Client3=client(-3,"","5214120201201")
        self.assertRaises(ValidError, valid_clienti.valideaza_clienti, self, Client3)
    def test_repo(self):
        #testeaza functiile din clasa repository_c
        # daca datele introduse de utilizator sunt incorecte,programul returneaza una dintre erorile din clasa RepoError
        self.repo=repository_c()
        id =1
        nume="Andrei"
        CNP="5012453629874"
        Client = client(id, nume, CNP)
        Clienti=self.repo.get_all_clienti()
        self.assertEqual(len(Clienti),0)
        #teste pentru adauga_client
        self.repo.adauga_client(Client)
        Clienti = self.repo.get_all_clienti()
        self.assertEqual(Clienti[0].get_id_c(),1)
        self.assertEqual(Clienti[0].get_nume(), nume)
        self.assertEqual(Clienti[0].get_CNP(), CNP)
        self.assertRaises(RepoError,self.repo.adauga_client,client(1,"Marian","5214123201202"))
        #teste prntru cauta_dupa_id_client
        cl=self.repo.cauta_dupa_id_client(id)
        self.assertEqual(cl.get_nume(),nume)
        self.assertEqual(cl.get_CNP() , CNP)
        self.assertRaises(RepoError,self.repo.cauta_dupa_id_client,4)
        self.repo.adauga_client(client(2,"Hagi","5111245287441"))
        #teste pentru stergere_client
        self.repo.stergere_client(id)
        Clienti = self.repo.get_all_clienti()
        self.assertEqual(Clienti[0].get_id_c(), 2)
        self.assertEqual(Clienti[0].get_nume(), "Hagi")
        self.assertEqual(Clienti[0].get_CNP(),"5111245287441")
        self.assertEqual(len(self.repo),1)
        self.assertRaises(RepoError,self.repo.stergere_client,5)
        #teste pentru modifica_client
        self.repo.modifica_client(2,"Marius","5014257584693")
        Clienti = self.repo.get_all_clienti()
        self.assertEqual(Clienti[0].get_id_c(), 2)
        self.assertEqual(Clienti[0].get_nume(), "Marius")
        self.assertEqual(Clienti[0].get_CNP(), "5014257584693")
        self.assertEqual(len(self.repo),1)
        self.assertRaises(RepoError,self.repo.modifica_client,5,"Dica","1204536744121")
        #teste pentru incrementeaza_clienti
        self.repo.incrementeaza_clienti(2)
        Clienti = self.repo.get_all_clienti()
        self.assertEqual(Clienti[0].get_nr_filme(),1)
        #teste pentru decrementeaza_client
        self.repo.decrementeaza_clienti(2)
        Clienti = self.repo.get_all_clienti()
        self.assertEqual(Clienti[0].get_nr_filme(),0)

    def test_service(self):
        #functie care testeza functiile din clasa ServiceFilm:adauga_film,cauta_dupa_id,stergere_client.,modifica_client
        id = 2
        nume = "Andrei"
        CNP = "5012453629874"
        valid=valid_clienti()
        repo=repository_c()
        self.srv=ServiceClient(valid,repo)
        #teste pentru adauga_client
        self.srv.adauga_client(id,nume,CNP)
        Clienti =self.srv.get_client()
        self.assertTrue(len(Clienti)==1)
        self.assertEqual(Clienti[0].get_id_c(),2)
        self.assertEqual(Clienti[0].get_nume(), "Andrei")
        self.assertEqual(Clienti[0].get_CNP(), CNP)
        self.assertRaises(RepoError,self.srv.adauga_client,2,"Diana","5214020120214")
        self.srv.adauga_client(1,"Malina","5111245287441")
        #teste pentru stergere_client
        self.srv.stergere_client(id)
        Clienti = self.srv.get_client()
        self.assertEqual(len(Clienti),1)
        self.assertEqual(Clienti[0].get_id_c(), 1)
        self.assertEqual(Clienti[0].get_nume(), "Malina")
        self.assertEqual(Clienti[0].get_CNP(),"5111245287441")
        self.assertRaises(RepoError,self.srv.stergere_client,id)
        #test pentru cauta_dupa_id_client
        self.assertRaises(RepoError,self.srv.cauta_dupa_id_client,7)
        #teste pentru modifica_client
        self.srv.modifica_client(1,"Adi","5000148566905")
        Clienti = self.srv.get_client()
        self.assertTrue(len(Clienti) == 1)
        self.assertEqual(Clienti[0].get_id_c(), 1)
        self.assertEqual(Clienti[0].get_nume(), "Adi")
        self.assertEqual(Clienti[0].get_CNP(),"5000148566905")
        self.assertRaises(RepoError,self.srv.modifica_client,4,"Teo","5000142536561")

    def ruleaza_teste_clienti(self):
        self.test_creare_client()
        self.test_validare_clienti()
        self.test_repo()
        self.test_service()
class teste_FileRepoClienti(unittest.TestCase):
    def teste_file_repo_clienti(self):
        #testeaza functiile din clasa FileRepoClienti
        with open("teste_clienti.txt","w") as f:
            f.write("")
        self.repo =FileRepoClienti("teste_clienti.txt")
        id = 1
        nume = "Andrei"
        CNP = "5012453629874"
        Client = client(id, nume, CNP)
        Clienti = self.repo.get_all_clienti()
        self.assertEqual(len(Clienti), 0)
        #teste pentru adauga_client
        self.repo.adauga_client(Client)
        Clienti = self.repo.get_all_clienti()
        self.assertEqual(Clienti[0].get_id_c(), 1)
        self.assertEqual(Clienti[0].get_nume(), nume)
        self.assertEqual(Clienti[0].get_CNP(), CNP)
        self.assertRaises(RepoError, self.repo.adauga_client, client(1, "Marian", "5214123201202"))
        #teste pentru cauta_dupa_id_client
        cl = self.repo.cauta_dupa_id_client(id)
        self.assertEqual(cl.get_nume(), nume)
        self.assertEqual(cl.get_CNP(), CNP)
        self.assertRaises(RepoError, self.repo.cauta_dupa_id_client, 4)
        self.repo.adauga_client(client(2, "Hagi", "5111245287441"))
        #teste pentru stergere_client
        self.repo.stergere_client(id)
        Clienti = self.repo.get_all_clienti()
        self.assertEqual(Clienti[0].get_id_c(), 2)
        self.assertEqual(Clienti[0].get_nume(), "Hagi")
        self.assertEqual(Clienti[0].get_CNP(), "5111245287441")
        self.assertEqual(len(self.repo), 1)
        self.assertRaises(RepoError, self.repo.stergere_client, 5)
        #teste pentru modifica_client
        self.repo.modifica_client(2, "Marius", "5014257584693")
        Clienti = self.repo.get_all_clienti()
        self.assertEqual(Clienti[0].get_id_c(), 2)
        self.assertEqual(Clienti[0].get_nume(), "Marius")
        self.assertEqual(Clienti[0].get_CNP(), "5014257584693")
        self.assertEqual(len(self.repo), 1)
        self.assertRaises(RepoError, self.repo.modifica_client, 5, "Dica", "1204536744121")
        #teste pentru incrementeaza_client
        self.repo.incrementeaza_clienti(2)
        Clienti = self.repo.get_all_clienti()
        self.assertEqual(Clienti[0].get_nr_filme(), 1)
        #teste pentru decrementeaza_client
        self.repo.decrementeaza_clienti(2)
        Clienti = self.repo.get_all_clienti()
        self.assertEqual(Clienti[0].get_nr_filme(), 0)
