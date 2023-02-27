'''
Created on Jan 31, 2023

@author: balut
'''


class Spectacol(object):
    '''
    classdocs
    '''

    def __init__(self, titlu, artist, gen, durata):
        '''
        Constructor
        '''
        self.__titlu = titlu
        self.__artist = artist
        self.__gen = gen
        self.__durata = durata

    def getTitlu(self):
        '''
        Functie care returneaza titlul unui spectacol
        @return[string]: Titlul spectacolului
        '''
        return self.__titlu

    def getArtist(self):
        '''
        Functie care returneaza artistul spectacolului
        @return[string]: Artistul spectacolului
        '''
        return self.__artist

    def getGen(self):
        '''
        Functie care returneaza genul spectacolului
        @return[string]: Genul spectacolului
        '''
        return self.__gen

    def getDurata(self):
        '''
        Functie care returneaza durata spectacolului
        @return[int]: Durata spectacolului
        '''
        return self.__durata

    def setGen(self, ot):
        '''
        Functie care seteaza genul spectacolului
        :param ot[string]: noul gen
        @post: genul s-a modificat
        '''
        self.__gen = ot

    def setDurata(self, ot):
        '''
        Functie care seteaza durata spectacolului
        :param ot[int]: noua durata
        @post: durata s-a modificat
        '''
        self.__durata = ot

    def __str__(self):
        '''
        Functie care suprascrie modul de afisare al unui obiect de tip Spectacol
        @return[string]: Modul de afisare al obiectului de tip Spectacol
        '''
        string = ""
        string += "Spectacol: {" + self.__titlu + " ; " + self.__artist + \
            " ; " + self.__gen + " ; " + str(self.__durata) + "}"
        return string

    def __eq__(self, ot):
        '''
        Functie care suprascrie modul in care doua spectacole sunt egale
        :param ot:
        '''
        return self.__titlu == ot.getTitlu() and self.__artist == ot.getArtist()
