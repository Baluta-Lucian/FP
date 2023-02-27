'''
Created on Feb 23, 2023

@author: balut
'''
from errors.Exception import RepositoryException
from domain.Jucator import Jucator


class RepositoryJucatori(object):
    '''
    classdocs
    '''

    def __init__(self, fileName):
        '''
        Constructor
        '''
        self.__fileName = fileName
        self.__jucatori = []
        self.__loadFromFile()

    def save(self, jucator):
        '''
        Functie care salveaza un obiect de tip Jucator
        :param jucator[Jucator]: jucatorul de salvat
        @raises[RepositoryException]: Jucatorul deja exista
        @post: lista se mareste cu 1
        '''
        for j in self.__jucatori:
            if j == jucator:
                raise RepositoryException(
                    "!!! Jucatorii trebuie sa aiba nume si prenume diferiti !!!")
        self.__jucatori.append(jucator)
        self.__saveToFile()

    def getAll(self):
        '''
        Functie care returneaza lista de jucatori
        :param self:
        @return[list[Jucator]]: lista de jucatori
        '''
        return self.__jucatori

    def modifyByH(self, inaltime):
        '''
        Functie care modifica toti jucatorii dupa o anumita inaltime data
        :param inaltime[int]: inaltimea cu care modificam
        @post: toti jucatorii sunt modificati
        '''
        for j in self.__jucatori:
            j.set_inaltime(j.get_inaltime() + inaltime)
        self.__saveToFile()
        # lungime = len(self.__jucatori)
        # l = []
        # for j in self.getAll():
        #     print(j.get_inaltime)
        #     modInaltime = j.get_inaltime() + inaltime
        #     print(modInaltime)
        #     jucator = Jucator(j.get_nume(), j.get_prenume(),
        #                       modInaltime, j.get_post())
        #
        #     l.append(jucator)
        #
        # self.__jucatori.clear()
        # for j in l:
        #     self.save(j)

    def __loadFromFile(self):
        '''
        Functie privata care ne ajuta la citirea din fisier
        :param self:
        '''
        with open(self.__fileName, "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                line = line.split(";")
                nume = line[0]
                prenume = line[1]
                inaltime = int(line[2])
                post = line[3]

                jucator = Jucator(nume, prenume, inaltime, post)

                self.save(jucator)

            f.close()

    def __saveToFile(self):
        '''
        Functie privata care ne ajuta la salvarea listei de jucatori in fisier
        :param self:
        '''
        with open(self.__fileName, "w") as f:
            l = self.getAll()
            for j in l:
                jFile = j.get_nume() + ";" + j.get_prenume() + ";" + \
                    str(j.get_inaltime()) + ";" + j.get_post() + "\n"
                f.write(jFile)

            f.close()
