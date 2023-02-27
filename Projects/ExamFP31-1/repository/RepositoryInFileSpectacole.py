'''
Created on Jan 31, 2023

@author: balut
'''

from domain.Entities import Spectacol
from errors.Exceptions import RepositeroryError


class RepositorySpectacol(object):
    '''
    classdocs
    '''

    def __init__(self, fileName):
        '''
        Constructor
        '''
        self.__fileName = fileName
        self.__spectacole = []
        self.__loadFromFile()

    def store(self, spectacol):
        '''
        functie care adauga un spectacol in lista de spectacole
        :param spectacol[Spectacol]: spectacolul de adaugat
        @post: Lista creste cu 1
        '''
        self.__spectacole.append(spectacol)
        self.__saveToFile()

    def findOne(self, spectacol):
        '''
        Functie care verifica daca un spectacol se afla in lista de spectacole
        :param spectacol[Spectacol]: spectacolul de verificat
        @return[Spectacolul]: spectacolul gasit
        @raises[RepositoryError]: spectacolul nu exista in lista de spectacole
        '''
        for s in self.__spectacole:
            if s == spectacol:
                return s
        raise RepositeroryError(
            "!!!Spectacolul nu exista in lista de spectacole")

    def modify(self, spectacol):
        '''
        Functie care modifica genul si durata unui spectacol
        :param spectacol[Spectacol]: spectacolul cu care se modifica
        @raises[RepositoryError]: spectacolul nu exista in lista de spectacole
        @post: Spectacolul s-a modificat
        '''
        self.findOne(spectacol)
        for s in self.__spectacole:
            if s == spectacol:
                s.setGen(spectacol.getGen())
                s.setDurata(spectacol.getDurata())
        self.__saveToFile()

    def getAll(self):
        '''
        Functie care returneaza lista de spectacole
             @return[list[Spectacol]]: lista de spectacole
        '''
        return self.__spectacole

    def __loadFromFile(self):
        '''
        Functie privata care adauga informatiile dintr-un fisier in lista de spectacole
        @post: Lista creste cu nr de spectacole din fisier
        '''
        with open(self.__fileName, "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                line = line.split(";")
                t = line[0]
                a = line[1]
                g = line[2]
                d = int(line[3])
                s = Spectacol(t, a, g, d)
                self.store(s)
            f.close()

    def __saveToFile(self):
        '''
        Functie privata care salveaza spectacolele din lista de spectacole in fisier
        @post: Fisierul are toate spectacolele din lista de spectacole
        '''
        with open(self.__fileName, "w") as f:
            l = self.getAll()
            for s in l:
                sfile = ""
                sfile += s.getTitlu() + ";" + s.getArtist() + ";" + \
                    s.getGen() + ";" + str(s.getDurata()) + "\n"
                f.write(sfile)
            f.close()
