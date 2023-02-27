'''
Created on Dec 14, 2022

@author: balut
'''
from repository.RepositoryEchipe import RepositoryEchipe
from repository.RepositoryClasament import RepositoryMeciuri
from service.Service import ServiceClasament
from ui.UI import Console

if __name__ == '__main__':
    repoE = RepositoryEchipe()
    repoM = RepositoryMeciuri(repoE)
    srv = ServiceClasament(repoE, repoM)
    ui = Console(srv)

    ui.run()
    print("Returned 0!")
