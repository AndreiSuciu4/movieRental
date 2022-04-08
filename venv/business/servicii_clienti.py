from infrastructura.repo_clienti import repository_c
from domeniu.entitati_clienti import client
class ServiceClient:
    def __init__(self,valid_c,repo_c):
        # creeaza o noua instanta pentru clasa ServiceClient
        self.__valid_c=valid_c
        self.__repo_c=repo_c

    def adauga_client(self,id_c,nume,CNP):
        """verifica daca un client este valid si il adauga in lista de clienti
        date de intrare:id_c-int
                        nume-str
                        CNP-str
        date de iesire:-"""
        Client=client(id_c,nume,CNP)
        self.__valid_c.valideaza_clienti(Client)
        self.__repo_c.adauga_client(Client)

    def get_client(self):
         """returneaza toti clientii din lista
        date de intrare:-
        date de iesire:-clientii din lista"""
         return self.__repo_c.get_all_clienti()
    def cauta_dupa_id_client(self,id):
        """cauta un client dupa un id dat
        date de intrare:id-int
        date de iesire:clientul cu id-ul respectiv"""
        aux=self.__repo_c.cauta_dupa_id_client(id)
        print(aux)

    def stergere_client(self,id_c):
        """sterge un anumit client din lista
        date de intrare:id_c-int
        date de iesire:-"""
        self.__repo_c.stergere_client(id_c)

    def modifica_client(self,id,nume,CNP):
        """modifica datele unui anumit client
        date de intrare:id-int
                        nume-str
                        CNP-str
        date de iesire:-"""
        self.__repo_c.modifica_client(id,nume,CNP)

