from testare.all_teste_filme import *
from testare.all_teste_clienti import *
from testare.all_tests_inchirieri import *
from coordonare.app_coord import App_coordinator

if __name__ == '__main__':
    Teste_filme = teste_filme()
    Teste_filme.ruleaza_teste()
    Teste_file_repo_film=teste_FileRepoFilm()
    Teste_file_repo_film.teste_file_repo_film()
    Teste_clienti=teste_clienti()
    Teste_clienti.ruleaza_teste_clienti()
    Teste_file_repo_clienti=teste_FileRepoClienti()
    Teste_file_repo_clienti.teste_file_repo_clienti()
    Teste_inchiriere=teste_inchirieri()
    Teste_inchiriere.ruleaza_teste_inchiriere()
    Teste_file_repo_inchiriere=teste_FileRepoInchiriere()
    Teste_file_repo_inchiriere.test_repo_inchiriere_cu_fisiere()
    app_coord=App_coordinator()
    app_coord.ruleaza()


