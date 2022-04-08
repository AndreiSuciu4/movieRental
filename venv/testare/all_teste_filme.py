from domeniu.entitati_film import film
from validator.valid_film import valid_film
from erori.exceptii import ValidError,RepoError
from infrastructura.repo_film import repository_f,FileRepoFilm
from business.servicii_film import ServiceFilm
import unittest
class teste_filme(unittest.TestCase):
    def test_creare_film(self):
        #testeaza daca un film e corect construit
        id=2
        titlu="Titanic"
        descriere="un film bun"
        gen="film de dragoste"
        Film=film(id,titlu,descriere,gen)
        self.assertTrue(Film.get_id() == id)
        self.assertTrue(Film.get_titlu()==titlu)
        self.assertTrue (Film.get_descriere()==descriere)
        self.assertTrue (Film.get_gen()==gen)
        self.assertTrue(str(Film)=="2 titlu:Titanic descriere:un film bun gen:film de dragoste")
        alt_film=film(id,"A","un film rau","horror")
        self.assertTrue(Film == alt_film)

    def test_validare_film(self):
        # testeaza daca programul returneaza o eroare de tip ValidError in cazul in care este introdus un film cu atribuie incorecte
        #black-box testing
        Film=film(-1,"","aaaa","horror")
        self.assertRaises(ValidError,valid_film.valideaza_film,self,Film)


    def test_repo(self):
        #functie care testeaza functiile din clasa repository_f:adauga_film,cauta_dupa_id,modifica_film si stergere_film
        #daca datele introduse de utilizator sunt incorecte,programul returneaza una dintre erorile din clasa RepoError
        id = 2
        titlu = "Titanic"
        descriere = "un film bun"
        gen = "film de dragoste"
        Film = film(id, titlu, descriere, gen)
        self.repo=repository_f()
        self.assertTrue(len(self.repo)==0)
        #teste pentru adauga_film
        self.repo.adauga_film(Film)
        Filme=self.repo.get_all_film()
        self.assertTrue (len(Filme) == 1)
        self.assertTrue(Filme[0].get_id()==2)
        self.assertTrue(Filme[0].get_titlu() == titlu)
        self.assertTrue(Filme[0].get_descriere() == descriere)
        self.assertTrue(Filme[0].get_gen() == gen)
        self.assertRaises(RepoError,self.repo.adauga_film,Film)
        #teste pentru cauta_dupa_id_film
        fl=self.repo.cauta_dupa_id_film(id)
        self.assertTrue(fl.get_titlu()==titlu)
        self.assertTrue(fl.get_descriere() == descriere)
        self.assertTrue(fl.get_gen() == gen)
        self.assertRaises(RepoError,self.repo.cauta_dupa_id_film,5)
        film1 = film(4,"1917","primul razboi mondial","istorie")
        self.repo.adauga_film(film1)
        #teste pentru stergere_film
        self.repo.stergere_film(2)
        Filme = self.repo.get_all_film()
        self.assertTrue(len(Filme) == 1)
        self.assertTrue(Filme[0].get_id() == 4)
        self.assertTrue(Filme[0].get_titlu() == "1917")
        self.assertTrue(Filme[0].get_descriere() == "primul razboi mondial")
        self.assertTrue(Filme[0].get_gen() == "istorie")
        self.assertRaises(RepoError,self.repo.stergere_film,3)
        #teste pentru modifica_film
        self.repo.modifica_film(4,"Avatar","experimente","SF")
        Filme = self.repo.get_all_film()
        self.assertTrue(len(Filme) == 1)
        self.assertTrue(Filme[0].get_id() == 4)
        self.assertTrue(Filme[0].get_titlu() == "Avatar")
        self.assertTrue(Filme[0].get_descriere() == "experimente")
        self.assertTrue(Filme[0].get_gen() == "SF")
        self.assertRaises(RepoError,self.repo.modifica_film,5,"Home Alone","Craciun","comedie")
        #teste pentru incrementeaza_film
        self.repo.incrementeaza_film(4)
        Filme = self.repo.get_all_film()
        self.assertEqual(Filme[0].get_nr_inchirieri(), 1)
        #teste pentru decrementeaza film
        self.repo.decrementeaza_film(4)
        Filme = self.repo.get_all_film()
        self.assertEqual(Filme[0].get_nr_inchirieri(), 0)
    def test_service(self):
        #testeza functiile din clasa ServiceFilm:adauga_film,cauta_dupa_id,stergere_film.,modifica_film
        id = 2
        titlu = "Titanic"
        descriere = "un film bun"
        gen = "film de dragoste"
        valid=valid_film()
        repo=repository_f()
        self.srv=ServiceFilm(valid,repo)
        #teste pentru adauga_film
        self.srv.adauga_film(id,titlu,descriere,gen)
        Filme =self.srv.get_filme()
        self.assertTrue(len(Filme)==1)
        self.assertTrue(Filme[0].get_id()==2)
        self.assertTrue(Filme[0].get_titlu() == titlu)
        self.assertTrue(Filme[0].get_descriere() == descriere)
        self.assertTrue(Filme[0].get_gen() == gen)
        self.srv.adauga_film(1,"1917","primul razboi mondial","istorie")
        #teste pentru stergere_film
        self.srv.stergere_film(id)
        Filme = self.srv.get_filme()
        self.assertTrue(len(Filme) == 1)
        self.assertTrue(Filme[0].get_id() == 1)
        self.assertTrue(Filme[0].get_titlu() == "1917")
        self.assertTrue(Filme[0].get_descriere() =="primul razboi mondial" )
        self.assertTrue(Filme[0].get_gen() == "istorie")
        self.assertRaises(RepoError,self.srv.stergere_film,7)
        #test pentru cauta_dupa_id_film
        self.assertRaises(RepoError,self.srv.cauta_dupa_id_film,7)
        #teste pentru modifica_film
        self.srv.modifica_film(1,"Home Alone","Craciun","Comedie")
        Filme = self.srv.get_filme()
        self.assertTrue(len(Filme) == 1)
        self.assertTrue(Filme[0].get_id() == 1)
        self.assertTrue(Filme[0].get_titlu() == "Home Alone")
        self.assertTrue(Filme[0].get_descriere() == "Craciun")
        self.assertTrue(Filme[0].get_gen() == "Comedie")
        self.assertRaises(RepoError,self.srv.modifica_film,4,"Home Alone2","Craciun","Comedie")
    def ruleaza_teste(self):
        #functie care apeleaza toate functiile de testare
        self.test_creare_film()
        self.test_validare_film()
        self.test_repo()
        self.test_service()

class teste_FileRepoFilm(unittest.TestCase):
    def teste_file_repo_film(self):
        #testeaza functiile din clasa FileRepoFilm
        with open("teste_filme.txt","w") as f:
            f.write("")
        self.repo = FileRepoFilm("teste_filme.txt")
        id = 2
        titlu = "Titanic"
        descriere = "un film bun"
        gen = "film de dragoste"
        Film = film(id, titlu, descriere, gen)
        self.assertTrue(len(self.repo) == 0)
        #teste pentru adauga_film
        self.repo.adauga_film(Film)
        Filme = self.repo.get_all_film()
        self.assertTrue(len(Filme) == 1)
        self.assertTrue(Filme[0].get_id() == 2)
        self.assertTrue(Filme[0].get_titlu() == titlu)
        self.assertTrue(Filme[0].get_descriere() == descriere)
        self.assertTrue(Filme[0].get_gen() == gen)
        self.assertRaises(RepoError, self.repo.adauga_film, Film)
        #teste pentru cauta_dupa_id_film
        fl = self.repo.cauta_dupa_id_film(id)
        self.assertTrue(fl.get_titlu() == titlu)
        self.assertTrue(fl.get_descriere() == descriere)
        self.assertTrue(fl.get_gen() == gen)
        self.assertRaises(RepoError, self.repo.cauta_dupa_id_film, 5)
        film1 = film(4, "1917", "primul razboi mondial", "istorie")
        self.repo.adauga_film(film1)
        #teste pentru stergere_film
        self.repo.stergere_film(2)
        Filme = self.repo.get_all_film()
        self.assertTrue(len(Filme) == 1)
        self.assertTrue(Filme[0].get_id() == 4)
        self.assertTrue(Filme[0].get_titlu() == "1917")
        self.assertTrue(Filme[0].get_descriere() == "primul razboi mondial")
        self.assertTrue(Filme[0].get_gen() == "istorie")
        self.assertRaises(RepoError, self.repo.stergere_film, 3)
        #teste pentru modifica_film
        self.repo.modifica_film(4, "Avatar", "experimente", "SF")
        Filme = self.repo.get_all_film()
        self.assertTrue(len(Filme) == 1)
        self.assertTrue(Filme[0].get_id() == 4)
        self.assertTrue(Filme[0].get_titlu() == "Avatar")
        self.assertTrue(Filme[0].get_descriere() == "experimente")
        self.assertTrue(Filme[0].get_gen() == "SF")
        self.assertRaises(RepoError, self.repo.modifica_film, 5, "Home Alone", "Craciun", "comedie")
        # teste pentru incrementeaza_film
        self.repo.incrementeaza_film(4)
        Filme = self.repo.get_all_film()
        self.assertEqual(Filme[0].get_nr_inchirieri(), 1)
        # teste pentru decrementeaza film
        self.repo.decrementeaza_film(4)
        Filme = self.repo.get_all_film()
        self.assertEqual(Filme[0].get_nr_inchirieri(), 0)


