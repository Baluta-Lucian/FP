'''
Created on Jan 31, 2023

@author: balut
'''
from errors.Exceptions import RepositeroryError, ValidationError


class Console(object):
    '''
    classdocs
    '''

    def __init__(self, srv):
        '''
        Constructor
        '''
        self.__srv = srv

    def __meniu(self):
        '''
        Functie privata pentru afisarea meniului de utilizator
        '''
        print("Lista de functionalitati:")
        print("\n1.Adauga Spectacol")
        print("2.Modifica Spectacol")
        print("3.Generate Spectacole")
        print("4.Export Spectacole")
        print("0.Exit!\n")

    def __uiAdauga(self):
        '''
        Functie privata pentru afisarea meniului de adaugare
        @raises[ValidationError]: Spectacol nevalid
        '''
        titlu = input("\nIntroduceti titlul: ")
        artist = input("Introduceti artist: ")
        gen = input("Introduceti genul(Comedie/Concert/Balet/Altele): ")
        durata = int(input("Introduceti durata(in secunde): "))
        try:
            self.__srv.addSpectacol(titlu, artist, gen, durata)
            print("\nSpectacol adaugat!\n")
        except ValidationError as ve:
            print(ve)

    def __uiModifica(self):
        '''
        Functie privata pentru afisarea meniului de modificare
        @raises[ValidationError]: Spectacol nevalid
        @raises[RepositoryError]: spectacolul nu exista in lista de spectacole
        '''
        titlu = input("\nIntroduceti titlul: ")
        artist = input("Introduceti artist: ")
        gen = input("Introduceti noul gen(Comedie/Concert/Balet/Altele): ")
        durata = int(input("Introduceti noua durata(in secunde): "))
        try:
            self.__srv.modifySpectacol(titlu, artist, gen, durata)
            print("\nSpectacol modificat!\n")
        except ValidationError as ve:
            print(ve)
        except RepositeroryError as re:
            print(re)

    def __uiGenerate(self):
        print("\n!!!Nu este inca implementat!!!\n")

    def __uiExport(self):
        '''
        Functie privata pentru afisarea meniului de export
        @post: spectacolele s-au adaugat in fisier
        '''
        fisier = input(
            "introduceti numele fisierului in care vreti sa exportati: ")
        self.__srv.exportSpectacole(fisier)

    def __printer(self, l):
        '''
        Functie privata pentru afisarea spectacolelor din lista de spectacole
        :param l:
        '''
        if len(l) == 0:
            print("!!!LISTA ESTE GOALA!!!")
        else:
            print("Inceputul listei:\n")
            for e in l:
                print(str(e))
            print("\nSfarsitul listei!")

    def run(self):
        '''
        Functie publica pentru pornirea aplicatiei
        :param self:
        '''
        while True:
            self.__meniu()
            cmd = input("\nIntroduceti functionalitatea:")

            if cmd == "0":
                return
            elif cmd == "1":
                self.__uiAdauga()
            elif cmd == "2":
                self.__uiModifica()
            elif cmd == "3":
                self.__uiGenerate()
            elif cmd == "4":
                self.__uiExport()
            elif cmd == "5":
                self.__printer(self.__srv.getSpectacole())
            else:
                print("!!!COMANDA INVALIDA!!!")
