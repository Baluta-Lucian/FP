'''
Created on Dec 14, 2022

@author: balut
'''
from repository.InFileRepositoryCafenea import InFileRepositoryCafenea
from service.ServiceCafenea import ServiceCafenea
from ui.UI import Console

if __name__ == '__main__':
    repo = InFileRepositoryCafenea("produseCaf.txt")
    srv = ServiceCafenea(repo)
    ui = Console(srv)

    ui.run()

    print("Returned 0!")
