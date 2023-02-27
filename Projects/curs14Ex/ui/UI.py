'''
Created on Feb 23, 2023

@author: balut
'''

import colorama
from colorama.ansi import Fore


class Console(object):
    '''
    classdocs
    '''

    def __init__(self, srv):
        '''
        Constructor
        '''
        self.__srv = srv

    def __menu(self):
        print(Fore.MAGENTA + "Lista functionalitati: \n")
        print(Fore.GREEN + "1.Vizualizare lista studenti")
        print(Fore.GREEN + "2.Cauta student dupa id")
        print(Fore.GREEN + "3.Asignare laborator la un student")
        print(Fore.GREEN + "4.Vizualizeaza toate laboratoarele unui student")
        print(
            Fore.GREEN + "5.Vizualizeaza studenti si laboratoare asignate pentru un lab dat")
        print(Fore.GREEN + "0.Exit!")

    def __showStuds(self):
        self.__prettyPrinter(self.__srv.getAllStudenti())

    def __prettyPrinter(self, l):
        if len(l) == 0:
            print(Fore.LIGHTMAGENTA_EX + "Lista este goala!\n")
        else:
            print(Fore.WHITE + "Inceputul listei: \n")
            for e in l:
                print(Fore.LIGHTBLUE_EX + str(e))
            print(Fore.LIGHTMAGENTA_EX + "\nSfarsitul listei! \n")

    def run(self):
        while True:
            self.__menu()
            cmd = input("\nIntroduceti functionalitatea:")
            if cmd == '1':
                self.__showStuds()
            elif cmd == '0':
                return 0
            else:
                print(Fore.RED + "\n!!! COMANDA INVALIDA !!!\n")
