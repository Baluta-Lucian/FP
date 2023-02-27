'''
Created on Dec 13, 2022

@author: balut
'''
from erorrs.Errors import RepositoryException
from domain.entities import Bicicleta


class InFileRepositoryBiciclete(object):
    '''
    classdocs
    '''

    def __init__(self, fileName):
        '''
        Constructor
        '''

        self.__produse = []
        self.__fileName = fileName
        self.__loadFromFile()

    def __exists(self, b):
        for p in self.__produse:
            if p.getID() == b.getID():
                raise RepositoryException(
                    "!!!Bicicleta exista deja in lista de produse!!!\n")

    def __store(self, b):
        self.__exists(b)
        self.__produse.append(b)

    def __loadFromFile(self):
        with open(self.__fileName, "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                line = line.split(";")
                id = int(line[0])
                tip = line[1]
                pret = float(line[2])
                b = Bicicleta(id, tip, pret)
                self.__store(b)
            f.close()

    def __saveToFile(self):
        with open(self.__fileName, "w") as f:
            for b in self.__produse:
                strB = str(b.getID()) + ";" + b.getTip() + \
                    ";" + str(b.getPret()) + "\n"
                f.write(strB)
            f.close()

    def __findOne(self, id):
        for b in self.__produse:
            if b.getID() == id:
                return b
        raise RepositoryException(
            "!!!Bicicleta nu exista in lista de produse!!!")

    def get_all(self):
        return self.__produse

    def deleteByTip(self, tip):
        self.__produse = [x for x in self.__produse if x.getTip() != tip]
        self.__saveToFile()

    def deleteByMax(self, maxx):
        self.__produse = [x for x in self.__produse if x.getPret() != maxx]
        self.__saveToFile()

    def delete(self, id):
        deleted = self.__findOne(id)
        self.__produse.remove(deleted)
        self.__saveToFile()
        return deleted
