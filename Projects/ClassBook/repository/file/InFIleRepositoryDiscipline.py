'''
Created on Nov 25, 2022

@author: balut
'''

from domain.Entities import Disciplina
from repository.memory.InMemoryRepositoryDiscipline import InMemoryRepositoryDiscipline


class InFileRepositoryDiscipline(InMemoryRepositoryDiscipline):
    '''
    classdocs
    '''

    def __init__(self, fileName):
        '''
        Constructor
        '''
        InMemoryRepositoryDiscipline.__init__(self)
        self.__fileName = fileName
        self.__loadFromFile()

    def findOne(self, d):
        '''
        Functie care gaseste o disciplina in lista de discipline
        :param d[Disciplina]:Disciplina de cautat
        @return[Disciplina]: Disciplina din lista de discipline
        @raises[RepositoryException]: Disciplina nu a fost gasita
        '''
        return InMemoryRepositoryDiscipline.findOne(self, d)

    def exists(self, d):
        '''
        Functie care verifica daca o disciplina exista deja in lista de discipline
        :param d[Disciplina]: Disciplina de verificat
        @raises[RepositoryException]: Disciplina exista in lista de discipline
        '''
        InMemoryRepositoryDiscipline.exists(self, d)

    def delete(self, d):
        '''
        Functie care sterge o disciplina din lista de discipline
        :param d[Disciplina]:Disciplina de sters
        @return[Disciplina]: Disciplina stearsa din lista de discipline
        @raises[RepositoryException]: Disciplina nu exista in lista de discipline
        '''
        deleted = InMemoryRepositoryDiscipline.delete(self, d)
        self.__saveToFile()
        return deleted

    def store(self, d):
        '''
        Functie care adauga o disciplina in lista de discipline
        :param d[Disciplina]: Disciplina de adaugat
        @raises[RepositoryException]: Disciplina exista in lista de discipline
        @post: Lista de discipline creste cu 1
        '''
        InMemoryRepositoryDiscipline.store(self, d)
        self.__saveToFile()

    def modify(self, d, ot):
        '''
        Functie care modifica o disciplina din lista de discipline
        :param d[Disciplina]: Disciplina de modificat
        :param ot[Disciplina]: Noua valoare a disciplinei
        @raises[RepositoryException]: Disciplina de modificat nu exista in lista de discipline
        '''
        InMemoryRepositoryDiscipline.modify(self, d, ot)
        self.__saveToFile()

    def getAll(self):
        '''
        Functie care returneaza lista de discipline
        :param self:
        @return[list[Disciplina]]: Lista de discipline
        '''
        return InMemoryRepositoryDiscipline.getAll(self)

    def __loadFromFile(self):
        try:
            f = open(self.__fileName, "r")
        except IOError:
            return
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            line = line.split(";")
            d = Disciplina(int(line[0]), line[1], line[2])
            InMemoryRepositoryDiscipline.store(self, d)
        f.close()

    def __saveToFile(self):
        try:
            f = open(self.__fileName, "w")
        except IOError:
            return
        discipline = InMemoryRepositoryDiscipline.getAll(self)
        for d in discipline:
            df = str(d.getID()) + ";" + d.getDenumire() + ";" + d.getProfesor()
            df = df + "\n"
            f.write(df)
        f.close()
