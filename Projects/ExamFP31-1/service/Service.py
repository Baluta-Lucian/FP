'''
Created on Jan 31, 2023

@author: balut
'''
import random
import string

from domain.Entities import Spectacol
from repository.RepositoryInFileSpectacole import RepositorySpectacol
from validators.Validator import ValidatorSpectacol
from prettytable import PrettyTable


class ServiceSpectacole(object):
    '''
    classdocs
    '''
 
    def __init__(self, repo, val):
        '''
        Constructor
        '''
        self.__repo = repo
        self.__val = val
        

    def addSpectacol(self, titlu, artist, gen, durata):
        '''
        Functie care adauga un spectacol la lista de spectacole
        :param titlu[string]: titlul spectacolului
        :param artist[string]: artistul spectacolului
        :param gen[string]: genul spectacolului
        :param durata[int]: durata spectacolului
        @raises[ValidationError]: spectacolul nu este valid
        @post: lista de spectacole creste cu 1
        '''
        s = Spectacol(titlu, artist, gen, durata)
        self.__val.validate(s)
        self.__repo.store(s)

    def modifySpectacol(self, titlu, artist, gen, durata):
        '''
        Functie care modifica un spectacol din lista de spectacole
        :param titlu[string]: titlul spectacolului
        :param artist[string]: artistul spectacolului
        :param gen[string]: noul gen al spectacolului
        :param durata[int]: noua durata a spectacolului
        @raises[ValidationError]: spectacolul nu este valid
                [RepositoryError]: spectacolul nu exista in lista de spectacole
        '''
        s = Spectacol(titlu, artist, gen, durata)
        self.__val.validate(s)
        self.__repo.modify(s)

    def exportSpectacole(self, fileName):
        '''
        Functie care exporta spectacolele intr-un fisier ales de utilizator
        :param fileName[string]: numele fisierului
        '''
        with open(fileName, "w") as f:
            spectacole = self.getSpectacole()
            self.__sorter(spectacole)
            for s in spectacole:
                sfile = ""
                sfile += s.getTitlu() + "," + s.getArtist() + "," + \
                    str(s.getDurata()) + "," + s.getGen() + "\n"
                f.write(sfile)
            f.close()

    def randomGenerator(self, nr):
        '''
        Functie care creeaza nr entitati de tip studenti/discipline
        :param nr[int]: numarul de entitati de generat
            @post: Lista de studenti si de discipline creste cu nr(daca nr>0)
        '''
        genuri = ["Comedie", "Concert", "Balet", "Altele"]
        for _ in range(0, nr):
            # for i in range(9,13):
            ra = int(random.uniform(9, 12))
            consoane = ['a', 'b', 'c', 'd', 'e']
            for i in range(0, ra):
                if i % 2 == 0:
                    letter = 6
            titlu = ''.join(random.choice(string.ascii_letters)

                            for _ in range(0, 12))
            durata = int(''.join(random.choice(string.digits)
                                 for _ in range(7)))
            gen = genuri[int(random.uniform(0, 4))]
            # s = Spectacol(titlu, artist, gen, durata)
            # self.__val.validate(s)
            # self.__repo.store(s)
            print(titlu)
            print(durata)
            print(gen)

            

    def __sorter(self, l):
        '''
        Functie privata care sorteaza o lista de spectacole crescator dupa artist si titlu
        :param l:
        '''
        for i in range(0, len(l) - 1):
            for j in range(i + 1, len(l)):
                if l[j].getArtist() < l[i].getArtist():
                    l[i], l[j] = l[j], l[i]
                elif l[j].getArtist() == l[i].getArtist():
                    if l[j].getTitlu() < l[i].getTitlu():
                        l[i], l[j] = l[j], l[i]

    def getSpectacole(self):
        '''
        Functie care returneaza o copie a listei de spectacole
        :param self:
        '''
        return self.__repo.getAll()
