from infrastructura.repo_film import repository_f
from domeniu.entitati_film import film
class ServiceFilm:
    def __init__(self,valid,repo):
        # creeaza o noua instanta pentru clasa ServiceFilm
        self.__valid=valid
        self.__repo=repo

    def adauga_film(self,id_f,titlu,descriere,gen):
        """verifica daca un film este valid si il adauga in lista de filme
                date de intrare:id_f-int
                                titlu-str
                                descriere-str
                                gen-str
                date de iesire:-"""
        Film=film(id_f,titlu,descriere,gen)
        self.__valid.valideaza_film(Film)
        self.__repo.adauga_film(Film)
    def cauta_dupa_id_film(self,id):
        """cauta un film dupa un id dat
        date de intrare:id-int
        date de iesire:filmul cu id-ul respectiv"""

        aux=self.__repo.cauta_dupa_id_film(id)
        print(aux)

    def get_filme(self):
        """returneaza toate filmele din lista
        date de intrare:-
        date de iesire:-filmele din lista"""
        return self.__repo.get_all_film()

    def stergere_film(self,id_f):
        """sterge un anumit film din lista
        date de intrare:id_f-int
        date de iesire:-"""
        self.__repo.stergere_film(id_f)


    def modifica_film(self,id,titlu,descriere,gen):
        """modifica datele unui anumit film
        date de intrare:id-int
                        titlu-str
                        descriere-str
                        gen-str
        date de iesire:-"""
        self.__repo.modifica_film(id,titlu,descriere,gen)









