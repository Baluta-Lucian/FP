'''
Created on Dec 14, 2022

@author: balut
'''


class Console(object):
    '''
    classdocs
    '''

    def __init__(self, srv):
        '''
        Constructor
        '''
        self.__srv = srv

    def meniu(self):
        print("Lista de functionalitati: ")
        print("1.Filtrare\n")
        print("2.Sort\n")
        print("x.Exit\n")

    def __uiFiltrare(self):
        tara = input("Introduceti tara: ")
        pret = float(input("Introduceti pret: "))
        self.__printer(self.__srv.filter(tara, pret))

    def __meniuSort(self):
        print("Lista de functionalitati: ")
        print("1.Sort by tara")
        print("2.Sort by tara/pret")
        print("0.Exit")

    def __sort1(self):
        self.__printer(self.__srv.sortByTara())

    def __sort2(self):
        self.__printer(self.__srv.sortByPret(self.__srv.sortByTara()))

    def __uiSort(self):
        while True:
            self.__meniuSort()
            cmd = input("Introduceti functionalitatea: ")
            if cmd == '1':
                self.__sort1()
            elif cmd == '2':
                self.__sort2()
            elif cmd == '0':
                break
            else:
                print("!!!COMANDA INVALIDA!!!")

    def __printer(self, l):
        if len(l) == 0:
            print("Lista este goala!")
        else:
            print("Inceputul listei:\n")
            for i in l:
                print(str(i))
            print("\nSfarsitul listei!!!\n")

    def run(self):
        while True:
            self.meniu()
            cmd = input("Introduceti functionalitatea: ")
            if cmd == '1':
                self.__uiFiltrare()
            elif cmd == '2':
                self.__uiSort()
            elif cmd == '3':
                self.__printer(self.__srv.getAll())
            elif cmd == 'x':
                break
            else:
                print("!!!COMANDA INVALIDA!!!")
