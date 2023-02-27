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

    def __meniu(self):
        '''
        Functie care tipareste meniul principal
        :param self:
        '''
        print("Lista de functionalitati: \n")
        print("1.Cautare de echipe pe baza sponsorului")
        print("2.Clasament")
        print("0.Exit")

    def __uiCautare(self):
        '''
        Functie ajutatoare pentru cautarea echipelor cu un sponsor ales de utilizator
        :param self:
        '''
        sponsor = input("Introduceti sponsorul: ")
        self.__print(self.__srv.cautareEcipe(sponsor))

    def __print(self, l):
        '''
        Functie ajutatoare de printare a unei liste
        :param l[list[Object]: lista de printat
        '''
        if len(l) == 0:
            print("\nLista este goala!\n")
        else:
            print("\nInceputul listei: ")
            for i in l:
                print(str(i))
            print("Sfarsitul listei!\n")

    def run(self):
        '''
        Functie de pornire a programului de tip consola
        :param self:
        '''
        while True:
            self.__meniu()
            cmd = input("Introduceti functionalitatea: ")
            if cmd == '1':
                self.__uiCautare()
            elif cmd == '2':
                self.__print(self.__srv.clasamentEchipe())
            elif cmd == 'afisareEchipe':
                self.__print(self.__srv.getAllEchipe())
            elif cmd == 'afisareMeciuri':
                self.__print(self.__srv.getAllMeciuri())
            elif cmd == '0':
                break
            else:
                print("!!!COMANDA INVALIDA!!!")
