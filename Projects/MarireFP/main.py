'''
Created on Feb 23, 2023

@author: balut
'''
from repository.RepositoryFileJucatori import RepositoryJucatori
from validator.Validator import Validator
from service.Service import Service
from ui.UI import Console
from colorama.ansi import Fore

if __name__ == '__main__':
    repo = RepositoryJucatori("jucatori.txt")
    val = Validator()

    srv = Service(repo, val)

    ui = Console(srv)

    ui.run()

    print(Fore.GREEN + "\nReturned 0!\n")
