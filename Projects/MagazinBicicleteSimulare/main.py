'''
Created on Dec 13, 2022

@author: balut
'''
from repository.InFileRepositoryBiciclete import InFileRepositoryBiciclete
from validator.Validator import Validator
from service.ServiceBiciclete import ServiceProduse
from ui.UI import Console

if __name__ == '__main__':
    repo = InFileRepositoryBiciclete("produse.txt")
    val = Validator()
    srv = ServiceProduse(repo, val)
    ui = Console(srv)

    ui.run()

    print("Returned 0!")
