'''
Created on Jan 31, 2023

@author: balut
'''
from domain.Entities import Spectacol
from repository.RepositoryInFileSpectacole import RepositorySpectacol
from service.Service import ServiceSpectacole
from UI.ui import Console
from validators.Validator import ValidatorSpectacol

if __name__ == '__main__':
    repo = RepositorySpectacol("spectacole.txt")
    val = ValidatorSpectacol()

    srv = ServiceSpectacole(repo, val)

    ui = Console(srv)

    ui.run()

    print("Returned 0!")
