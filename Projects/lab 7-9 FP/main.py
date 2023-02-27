'''
Created on Nov 10, 2022

@author: balut
'''
from domain.Entities import Student
from validation.Validator import Validator
from errors.Exceptions import ValidationException
from repository.memory.InMemoryRepositoryStudent import InMemoryRepositoryStudent
from repository.memory.InMemoryRepositoryDiscipline import InMemoryRepositoryDiscipline
from repository.memory.InMemoryRepositoryCatalog import InMemoryRepositoryCatalog
from service.Service import ServiceCatalog
from ui.Ui import Console
from colorama import Fore
from repository.file.InFIleRepositoryStudent import InFileRepositoryStudent
from repository.file.InFIleRepositoryDiscipline import InFileRepositoryDiscipline
from repository.file.InFileRepositoryCatalog import InFileRepositoryCatalog
from tkinter import *


if __name__ == '__main__':
    """
    BACKTRACKING PROBLEMA 2
    BACKTRACKING PROBLEMA 2
    BACKTRACKING PROBLEMA 2
    BACKTRACKING PROBLEMA 2
    BACKTRACKING PROBLEMA 2
    BACKTRACKING PROBLEMA 2
    BACKTRACKING PROBLEMA 2
    BACKTRACKING PROBLEMA 2
    BACKTRACKING PROBLEMA 2
    with open(self.__numeF, "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            line = line.split()
            var1 = line[1]
            var2 = int(line[2])
            Entity(var1, var2)
            self.__store(Entity)
        f.close()
        
    with open(self.__numeF, "w") as f:
        l = self.__getall()
        for e in l:
            eString = str(e.getVar1()) + ";" + str(e.getVar2()) + "\n"
            f.write(eString)
        f.close()
    """
    while True:
        print(Fore.WHITE + "Modurile de gestionare a datelor: ")
        print(Fore.GREEN + "1.In memorie")
        print(Fore.GREEN + "2.In fisier")
        cmd = input(Fore.LIGHTGREEN_EX +
                    "Introduceti functionalitatea: >>>")
        if cmd == "1":
            val = Validator()
            repoS = InMemoryRepositoryStudent()
            repoD = InMemoryRepositoryDiscipline()
            repoC = InMemoryRepositoryCatalog()
            srv = ServiceCatalog(repoS, repoD, repoC, val)
            ui = Console(srv)
            break
        elif cmd == "2":
            val = Validator()
            repoS = InFileRepositoryStudent("stundeti.txt")
            repoD = InFileRepositoryDiscipline("discipline.txt")
            repoC = InFileRepositoryCatalog("catalog.txt")
            srv = ServiceCatalog(repoS, repoD, repoC, val)
            ui = Console(srv)
            break
        else:
            print(Fore.RED + "\n!!!COMANDA INVALIDA!!!")

    ui.run()

    print("RETURNED 0")

    # # testing some gui
    # root = Tk()
    #
    # # Creating a label widget
    # myLabel1 = Label(root, text="Hello World!")
    # myLabel2 = Label(root, text="Baluta pe zona!")
    # # showing it into the screen
    # myLabel1.grid(row=0, column=0)
    # myLabel2.grid(row=1, column=0)
    #
    # buttonsFrame = Frame(root, relief='solid', bd=2)
    # buttonsFrame.grid(row=2, column=0, padx=10, pady=10, sticky="ne")
    #
    # # buttons
    # inMemoryButton = Button(buttonsFrame, text="In memory", padx=10)
    # inFileButton = Button(buttonsFrame, text="In file", padx=10)
    #
    # # show them
    # inMemoryButton.grid(row=0, column=0, padx=10, pady=5)
    # inFileButton.grid(row=1, column=0, padx=10, pady=5)
    #
    # root.mainloop()
