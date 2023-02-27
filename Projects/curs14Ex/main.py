'''
Created on Feb 23, 2023

@author: balut
'''
from repository.RepositoryFileStudent import RepositoryStudenti
from repository.RepositoryFileLaborator import RepositoryLaboratoare
from validators.Validator import Validator
from service.Service import Service
from ui.UI import Console
from colorama.ansi import Fore

if __name__ == '__main__':
    repoStudenti = RepositoryStudenti("studenti.txt")
    repoLaboratoare = RepositoryLaboratoare("laboratoare.txt")
    val = Validator()

    srv = Service(repoStudenti, repoLaboratoare, val)

    ui = Console(srv)

    ui.run()

    print(Fore.GREEN + "Returned 0!")
