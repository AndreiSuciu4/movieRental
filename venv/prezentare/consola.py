from datetime import datetime
from business.servicii_film import ServiceFilm
from business.servicii_clienti import ServiceClient
from business.servicii_inchiriere import ServiceInchiriere
from erori.exceptii import ValidError,RepoError
from infrastructura.repo_film import repository_f
from infrastructura.repo_clienti import repository_c
from infrastructura.repo_inchirieri import repository_i
from domeniu.entitati_inchiriere import inchiriere
from domeniu.entitati_film import film
from domeniu.entitati_clienti import client
import random
import string
class UI():
    #clasa UI
    def __init__(self,srv_i,srv_c,srv_f):
        self.__srv_i=srv_i
        self.__srv_c = srv_c
        self.__srv_f=srv_f
        self.__comenzi={"adauga_film":self.__ui_adauga_film,
                        "print_filme":self.__ui_print_film,
                        "stergere_film":self.__ui_stergere_film,
                        "modifica_film":self.__ui_modifica_film,
                        "cauta_film":self.__ui_cauta_dupa_id_film,
                        "adauga_client":self.__ui_adauga_client,
                        "print_clienti":self.__ui_print_clienti,
                        "stergere_client":self.__ui_stergere_client,
                        "modifica_client":self.__ui_modifica_client,
                        "cauta_client":self.__ui_cauta_dupa_id_client,
                        "adauga_inchiriere":self.__ui_adauga_inchirieri,
                        "print_inchiriere":self.__ui_print_inchirieri,
                        "stergere_inchiriere":self.__ui_stergere_inchiriere,
                        "cauta_inchiriere":self.__ui_cauta_dupa_id_inchiriere,
                        "modifica_inchiriere":self.__ui_modifica_inchiriere,
                        "random":self.__ui_random_film,
                        "ordonare_nume":self.__ui_ordoneaza_dupa_nume,
                        "ordonare_dupa_filme":self.__ui_ordoneaza_dupa_filme,
                        "cele_mai_inchiriate_filme":self.__ui_cele_mai_inchiriate_filme,
                        "primii_clienti":self.__ui_primii_clienti,
                        "rap2":self.__ui_raport2}



        
    def __ui_adauga_film(self,params):
        if len(params)!=4:
            print("numar incorect de parametrii")
            return
        id_f = int(params[0])
        titlu = params[1]
        descriere = params[2]
        #exemplu:Prezinta_batalia_de_la_Verdun
        gen = params[3]
        self.__srv_f.adauga_film(id_f,titlu,descriere,gen)
    def __process_comand(self,cmd):
        cmd = cmd.strip()
        parts=cmd.split(";")
        n=0
        cmd1=[]
        params=[]
        parts1=[]
        aux=[]
        skipp_next=0
        for el in range(len(parts)):
            parts1=parts[el].split(",")
            if len(parts1)>1:
                cmd1.append(parts1[0])
                for i in range(1,len(parts1)):
                    aux.append(parts1[i])
            else:
                cmd1.append(parts1[0])
            params.append(list(aux))
            aux.clear()
        return cmd1,params

    def __ui_random_film(self,params):
        lengh=int(params[0])
        for i in range (int(lengh)):
            id_f=random.randint(1,1000)
            titlu=''.join(random.choice(string.ascii_lowercase) for i in range(10))
            descriere=''.join(random.choice(string.ascii_lowercase) for i in range(10))
            gen= ''.join(random.choice(string.ascii_lowercase) for i in range(10))
            self.__srv_f.adauga_film(id_f, titlu, descriere, gen)

    def __ui_print_film(self,params):
        Filme=[]
        Filme=self.__srv_f.get_filme()
        if len(Filme)==0:
            print("lista goala")
            return
        for i in Filme:
            print(i)
    def __ui_stergere_film(self,params):
        if len(params)!=1:
            print("numar incorect de parametrii")
            return
        id_f=int(params[0])
        self.__srv_f.stergere_film(id_f)
    def __ui_modifica_film(self,params):
        if len(params)<4:
            print("prea putini parametrii")
            return
        id_f = int(params[0])
        titlu = params[1]
        descriere = params[2]
        gen = params[3]
        self.__srv_f.modifica_film(id_f,titlu,descriere,gen)
    def __ui_cauta_dupa_id_film(self,params):
        if len(params)!=1:
            print("numar incorect de parametrii")
            return
        id_f = int(params[0])
        self.__srv_f.cauta_dupa_id_film(id_f)

    def __ui_adauga_client(self,params):
        if len(params)!=3:
            print("numar incorect de parametrii")
            return
        id_c = int(params[0])
        nume = params[1]
        CNP = params[2]
        self.__srv_c.adauga_client(id_c,nume,CNP)

    def __ui_print_clienti(self,params):
        Clienti = []
        Clienti = self.__srv_c.get_client()
        if len(Clienti) == 0:
            print("lista goala")
            return
        for i in Clienti:
            print(i)

    def __ui_stergere_client(self,params):
        if len(params)!=1:
            print("numar incorect de parametrii")
            return
        id_c=int(params[0])
        self.__srv_c.stergere_client(id_c)

    def __ui_modifica_client(self,params):
        if len(params)!=3:
            print("numar incorect de parametrii")
            return
        id_c = int(params[0])
        nume = params[1]
        CNP = params[2]
        self.__srv_c.modifica_client(id_c,nume,CNP)

    def __ui_cauta_dupa_id_client(self,params):
        if len(params)!=1:
            print("numar incorect de parametrii")
            return
        id_c = int(params[0])
        self.__srv_c.cauta_dupa_id_client(id_c)

    def __ui_adauga_inchirieri(self,params):
        if len(params)!=6:
            print("numar incorect de parametrii")
            return
        id_i=int(params[0])
        id_f=int(params[1])
        id_c=int(params[2])
        zi=int(params[3])
        luna=int(params[4])
        an=int(params[5])
        self.__srv_i.adauga_inchirieri(id_i,id_c,id_f,zi,luna,an)

    def __ui_print_inchirieri(self,params):
        Inchiriere = []
        Inchiriere = self.__srv_i.get_all_inchirieri()
        if len(Inchiriere) == 0:
            print("lista goala")
            return
        for i in Inchiriere:
            print(i)

    def __ui_stergere_inchiriere(self,params):
        if len(params)!=1:
            print("numar incorect de parametrii")
            return
        id_i = int(params[0])
        self.__srv_i.stergere_inchiriere(id_i)

    def __ui_cauta_dupa_id_inchiriere(self,params):
        if len(params)!=1:
            print("numar incorect de parametrii")
            return
        id_i = int(params[0])
        self.__srv_i.cauta_dupa_id_inchiriere(id_i)

    def __ui_modifica_inchiriere(self,params):
        if len(params)!=6:
            print("numar incorect de parametrii")
            return
        id_i = int(params[0])
        id_c = int(params[1])
        id_f = int(params[2])
        zi = int(params[3])
        luna = int(params[4])
        an = int(params[5])
        self.__srv_i.modifica_inchiriere(id_i,id_c,id_f,zi,luna,an)

    def __ui_ordoneaza_dupa_nume(self,params):
        clienti=self.__srv_i.ordonare_dupa_nume_client()
        for el in clienti:
            print(el)
    def __ui_ordoneaza_dupa_filme(self,params):
        clienti=self.__srv_i.ordonare_numar_filme()
        for el in clienti:
            print(el)
    def __ui_cele_mai_inchiriate_filme(self,params):
        filme=self.__srv_i.cele_mai_inchiriate_filme()
        for el in filme:
            print(el)
    def __ui_primii_clienti(self,params):
        clienti=self.__srv_i.primii_clienti()
        for el in clienti:
            print(el)
    def __ui_raport2(self,params):
        if len(params)<1:
            print("prea putini parametrii")
            return
        litera=params[0]
        clienti=self.__srv_i.rap2(litera)
        for el in clienti:
            print(el)


    def run(self):
        #functia run
        while True:
            print("Meniu:\n"
                  "1.Filme:adauga_film, "
                  "print_filme, "
                   "stergere_film, "
                    "modifica_film, "
                    "random, "
                    "cauta_film\n"
                    "2.Clienti:adauga_client, "
                    "print_clienti, "
                    "stergere_client, "
                    "modifica_client, "
                    "cauta_client\n"
                    "3.Inchiriere:adauga_inchiriere, "
                    "print_inchiriere, "
                    "stergere_inchiriere, "
                    "cauta_inchiriere, "
                    "modifica_inchiriere\n"
                    "4.Rapoarte:ordonare_nume, "
                    "ordonare_dupa_filme, "
                    "cele_mai_inchiriate_filme, "
                    "primii_clienti ")

            cmd = input(">>>")
            if cmd == "exit":
                print(" bye")
                return
            cmd_name,params=self.__process_comand(cmd)
            for el in range(len(cmd_name)):
                if cmd_name[el] in self.__comenzi:
                    try:
                        self.__comenzi[cmd_name[el]](params[el])
                    except ValueError:
                         print("Valoare invalida")
                    except ValidError as ve:
                         print(ve)
                    except RepoError as re:
                        print(re)
                else:
                    print("comanda invalida!")

