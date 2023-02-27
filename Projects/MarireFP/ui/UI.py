'''
Created on Feb 23, 2023

@author: balut
'''
from colorama.ansi import Fore
from errors.Exception import RepositoryException, ValidationException


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
        print(Fore.LIGHTMAGENTA_EX + "Lista functionalitati: ")
        print(Fore.GREEN + "1.Adauga jucator")
        print(Fore.GREEN + "2.Modificare inaltime")
        print(Fore.GREEN + "3.Construieste echipa inaltime max")
        print(Fore.GREEN + "4.Importa jucatori din fisier")
        print(Fore.GREEN + "0.Exit!")

    def __ui_adauga_jucator(self):
        try:
            nume = input(Fore.MAGENTA + "Introduceti numele jucatorului: ")
            prenume = input(
                Fore.MAGENTA + "Introduceti prenumele jucatorului: ")
            inaltime = int(input(Fore.LIGHTMAGENTA_EX +
                                 "Introduceti inaltimea jucatorului: "))
            post = input(Fore.MAGENTA + "Introduceti postul jucatorului: ")
            self.__srv.addJucator(nume, prenume, inaltime, post)
            print(Fore.GREEN + "\nJucator adaugat cu succes!\n")
        except RepositoryException as re:
            print(Fore.RED + "\n" + str(re) + "\n")
        except ValidationException as ve:
            print(Fore.RED + "\n" + str(ve) + "\n")
        except ValueError as te:
            print(Fore.RED + "\n" + str(te) + "\n")

    def __ui_modifica_jucatori(self):
        try:
            inaltime = int(
                input(Fore.MAGENTA + "Inaltimea cu care modificam jucatorii:"))
            self.__srv.modificaInaltime(inaltime)
            print(Fore.GREEN + "\nJucatori modificati cu succes!\n")
        except ValueError as te:
            print(Fore.RED + "\n" + str(te) + "\n")

    def __ui_import(self):
        try:
            fisier = input(
                Fore.MAGENTA + "Introduceti numele fisierului din care importam: ")
            jucatoriAdaugati = self.__srv.importa(fisier)
            print(Fore.LIGHTBLUE_EX + "\nJucatori adaugati: " +
                  str(jucatoriAdaugati) + "\n")
        except FileNotFoundError as fne:
            print(Fore.RED + "\n" + str(fne) + "\n")

    def __ui_tipareste_echipa(self):
        self.__prettyPrinter(self.__srv.echipaMax())

    def __prettyPrinter(self, l):
        if len(l) == 0:
            print(Fore.WHITE + "Lista este goala!\n")
        else:
            print(Fore.MAGENTA + "Inceputul listei:\n")
            for j in l:
                print(Fore.LIGHTBLUE_EX + str(j))
            print(Fore.MAGENTA + "\nSfarsitul listei!\n")

    def run(self):
        while True:
            self.__menu()
            cmd = input(Fore.WHITE + "\nIntroduceti functionalitatea: ")
            if cmd == '1':
                self.__ui_adauga_jucator()
            elif cmd == '2':
                self.__ui_modifica_jucatori()
            elif cmd == '3':
                self.__ui_tipareste_echipa()

            elif cmd == '4':
                self.__ui_import()
            elif cmd == '5':
                self.__prettyPrinter(self.__srv.getAllJucatori())
            elif cmd == '0':
                return 0
            else:
                print(Fore.RED + "\n!!! COMANDA INVALIDA !!!\n")
