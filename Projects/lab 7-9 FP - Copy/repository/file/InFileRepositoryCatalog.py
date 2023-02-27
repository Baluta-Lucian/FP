'''
Created on Nov 25, 2022

@author: balut
'''

from domain.Entities import Statistica, Student, Disciplina
from repository.memory.InMemoryRepositoryCatalog import InMemoryRepositoryCatalog


class InFileRepositoryCatalog(InMemoryRepositoryCatalog):
    '''
    classdocs
    '''

    def __init__(self, fileName):
        '''
        Constructor
        '''
        InMemoryRepositoryCatalog.__init__(self)
        self.__fileName = fileName
        self.__loadFromFile()

    def exists(self, statistica):
        '''
        Functie care verifica daca o statistica exista deja in catalog
        :param statistica[Statistica]:Statistica de verificat
        @raises[RepositoryException]: Statistica existenta
        '''
        InMemoryRepositoryCatalog.exists(self, statistica)

    def findOne(self, statistica):
        '''
        Functie care returneaza daca o statistica se afla in catalog
        :param statistica[Statistica]: Statistica de cautat
        @return[Statistica]: Statistica din catalog
        @raises[RepositoryException]: Statistica inexistenta in catalog
        '''
        return InMemoryRepositoryCatalog.findOne(self, statistica)

    def store(self, statistica):
        '''
        Functie care adauca o statistica in catalog
        :param statistica[Statistica]: Statistica de adaugat in catalog
        @raises[RepositoryException]: Statistica existenta in catalog
        '''
        InMemoryRepositoryCatalog.store(self, statistica)
        self.__saveToFile()

    def deleteByStudent(self, s):
        '''
        Functie care sterge o statisticile din catalog ale unui student
        :param s[Student]: Studentul de la care vrem sa stergem statisticile
        '''
        InMemoryRepositoryCatalog.deleteByStudent(self, s)
        self.__saveToFile()

    def deleteByDisciplina(self, d):
        '''
        Functie care sterge o statisticile din catalog ale unei discipline
        :param d[Disciplina]: Disciplina de la care vrem sa stergem statisticile
        '''
        InMemoryRepositoryCatalog.deleteByDisciplina(self, d)
        self.__saveToFile()

    def getAll(self):
        '''
        Functie care returneaza catalogul
        :param self:
        @return[List[Statistici]]: Catalogul
        '''
        return InMemoryRepositoryCatalog.getAll(self)

    def __loadFromFile(self):
        try:
            f = open(self.__fileName, "r")
        except IOError:
            return
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            line = line.split(";")
            s = Student(int(line[0]), line[1])
            d = Disciplina(int(line[2]), line[3], line[4])
            note = line[5]
            # print(note)
            note = note.strip(", [ ]")
            note = note.split(", ")
            # print(note)
            note = [int(x) for x in note]
            stat = Statistica(s, d, note)
            InMemoryRepositoryCatalog.store(self, stat)
        f.close()

    def __saveToFile(self):
        try:
            f = open(self.__fileName, "w")
        except IOError:
            return
        statistici = InMemoryRepositoryCatalog.getAll(self)
        for stat in statistici:
            s = stat.getS()
            d = stat.getD()
            statf = str(s.getID()) + ";" + s.getNume() + ";" + str(d.getID()) + ";" + \
                d.getDenumire() + ";" + d.getProfesor() + ";" + str(stat.getNote())
            statf = statf + "\n"
            f.write(statf)
        f.close()
