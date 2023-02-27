'''
Created on Dec 13, 2022

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
        print("Lista de functionalitati:")
        print("1.Sterge tip\n")
        print("2.Sterge max\n")
        print("0.Exit\n")

    def __uiStergeTip(self):
        tip = input("Introduceti tipul: ")
        self.__srv.stergeTip(tip)

    def __uiStergeMax(self):
        self.__srv.stergeMax()

    def __uiPrint(self, l):
        for c in l:
            print(str(c) + "\n")

    def run(self):
        while(True):
            self.meniu()
            cmd = input("Introduceti functionalitatea: ")
            if cmd == '1':
                self.__uiStergeTip()
            elif cmd == '2':
                self.__uiStergeMax()
            elif cmd == '0':
                break

            elif cmd == '3':
                self.__uiPrint(self.__srv.getAll())
            else:
                print("!!!FUNCTIONALITATE INVALIDA!!!")
