'''
Created on Nov 25, 2022

@author: balut
'''
from domain.Entities import Student
from repository.memory.InMemoryRepositoryStudent import InMemoryRepositoryStudent


class InFileRepositoryStudent(InMemoryRepositoryStudent):
    '''
    classdocs
    '''

    def __init__(self, fileName):
        '''
        Constructor
        '''
        InMemoryRepositoryStudent.__init__(self)
        self.__fileName = fileName
        self.__loadFromFile()

    def store(self, s):
        '''
        Functie care adauga un student in lista de studenti
        :param s[Student]: Stundetul de adaugat
        @raises[RepositoryException]: Studentul de adaugat exista deja in lista de studenti
         '''
        self.__loadFromFile()
        InMemoryRepositoryStudent.store(self, s)
        self.__saveToFile()

    # def findOne(self, s):
    #     '''
    #     Functie care cauta un student in lista de studenti
    #     :param s[Student]: Student de cautat
    #     @return[Student]: Studentul gasit in lista de studenti
    #     @raises[RepositoryException]: Studentul nu exista in lista de studenti
    #     '''
    #     InMemoryRepositoryStudent.findOne(self, s)

    def delete(self, s):
        '''
        Functie care sterge un student din lista de studenti
        :param s[Student]: Studentul de sters
        @return[Student]: Studentul sters din lista de studenti
        @raises[RepositoryException]: Studentul nu exista in lista de studenti
        '''
        deleted = InMemoryRepositoryStudent.delete(self, s)
        self.__saveToFile()
        return deleted

    # def exists(self, s):
    #     '''
    #     Functie care verifica daca un student exista in lista de studenti
    #     :param s[Student]: Studentul de verificat
    #     @raises[RepositoryException]: studentul exista deja in lista
    #     '''
    #     InMemoryRepositoryStudent.exists(self, s)

    def modify(self, s, ot):
        '''
        Functie care modifica un student din lista de studenti
        :param s[Student]: Studentul de modificat
        :param ot[Student]: Noile valori ale studentului
        @raises[RepositoryException]: Studentul de modificat nu exista in lista de studenti
        '''
        InMemoryRepositoryStudent.modify(self, s, ot)
        self.__saveToFile()

    def getAll(self):
        '''
        Functie care returneaza lista de studenti
        :param self:
        @return[list[Student]]: Lista de studenti
        '''
        return InMemoryRepositoryStudent.getAll(self)

    def __loadFromFile(self):
        with open(self.__fileName, "r") as f:
            InMemoryRepositoryStudent.__init__(self)
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                line = line.split(";")
                s = Student(int(line[0]), line[1])
                InMemoryRepositoryStudent.store(self, s)
            f.close()

    def __saveToFile(self):
        with open(self.__fileName, "w") as f:
            students = InMemoryRepositoryStudent.getAll(self)
            for s in students:
                sf = str(s.getID()) + ";" + s.getNume()
                sf = sf + "\n"
                f.write(sf)
            f.close()
