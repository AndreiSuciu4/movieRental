from validator.valid_film import valid_film
from validator.valid_clienti import valid_clienti
from validator.valid_inchiriere import valid_inchirieri
from infrastructura.repo_film import repository_f,FileRepoFilm
from infrastructura.repo_clienti import repository_c,FileRepoClienti
from infrastructura.repo_inchirieri import repository_i,FileRepoInchiriere
from business.servicii_film import ServiceFilm
from business.servicii_clienti import ServiceClient
from business.servicii_inchiriere import ServiceInchiriere
from prezentare.consola import UI
class App_coordinator:
    def ruleaza(self):
        #alege modul dupa care functioneaza aplicatia(cu date salvate in memorie sau date salvate in fisier)
        while True:
            metoda=input("dati metoda:fisier sau memorie: ")
            if metoda=="fisier":
                repo_f = FileRepoFilm("filme.txt")
                repo_c = FileRepoClienti("clienti.txt")
                repo_i = FileRepoInchiriere("inchirieri.txt")
            elif metoda=="memorie":
                repo_f = repository_f()
                repo_c = repository_c()
                repo_i = repository_i()
            else:
                print("metoda incorecta")
                return
            valid_f = valid_film()
            valid_c = valid_clienti()
            valid_i = valid_inchirieri()
            srv_f = ServiceFilm(valid_f, repo_f)
            srv_c = ServiceClient(valid_c, repo_c)
            srv_i = ServiceInchiriere(repo_i, valid_i, repo_c, repo_f)
            cons = UI(srv_i, srv_c, srv_f)
            cons.run()
