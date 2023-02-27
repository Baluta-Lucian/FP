'''
Created on Nov 10, 2022

@author: balut
'''

from errors.Exceptions import RepositoryException


# class InMemoryRepositoryDiscipline(object):
#     '''
#     classdocs
#     '''
#
#     def __init__(self):
#         '''
#         Constructor
#         '''
#         self.__discipline = []
#
#     def findOne(self, d):
#         for disciplina in self.__discipline:
#             if disciplina == d:
#                 return d
#         raise RepositoryException("!!!Disciplina nu exista in lista de discipline!!!")\
#
#
#     def exists(self, d):
#         for disciplina in self.__discipline:
#             if disciplina.getID() == d.getID():
#                 raise RepositoryException(
#                     "!!!ID-ul disciplinei exista deja in lista de discipline!!!")
#
#     def delete(self, d):
#         deleted = self.findOne(d)
#         self.__discipline.remove(d)
#         return deleted
#
#     def store(self, d):
#         self.exists(d)
#         self.__discipline.append(d)
#
#     def modify(self, d, ot):
#         self.findOne(d)
#         self.exists(ot)
#         i = self.__discipline.index(d)
#         self.__discipline[i].setID(ot.getID())
#         self.__discipline[i].setDenumire(ot.getDenumire())
#         self.__discipline[i].setProfesor(ot.getProfesor())
#
#     def getAll(self):
#         return self.__discipline
#

class InMemoryRepositoryDiscipline(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.__discipline = {'0': []}

    def findOne(self, d):
        '''
        Functie care gaseste o disciplina in lista de discipline
        :param d[Disciplina]:Disciplina de cautat
        @return[Disciplina]: Disciplina din lista de discipline
        @raises[RepositoryException]: Disciplina nu a fost gasita
        '''
        for disciplina in self.__discipline['0']:
            if disciplina == d:
                return d
        raise RepositoryException("!!!Disciplina nu exista in lista de discipline!!!")\


    def exists(self, d):
        '''
        Functie care verifica daca o disciplina exista deja in lista de discipline
        :param d[Disciplina]: Disciplina de verificat
        @raises[RepositoryException]: Disciplina exista in lista de discipline
        '''
        for disciplina in self.__discipline['0']:
            if disciplina.getID() == d.getID():
                raise RepositoryException(
                    "!!!ID-ul disciplinei exista deja in lista de discipline!!!")

    def delete(self, d):
        '''
        Functie care sterge o disciplina din lista de discipline
        :param d[Disciplina]:Disciplina de sters
        @return[Disciplina]: Disciplina stearsa din lista de discipline
        @raises[RepositoryException]: Disciplina nu exista in lista de discipline
        '''
        deleted = self.findOne(d)
        self.__discipline['0'].remove(d)
        return deleted

    def store(self, d):
        '''
        Functie care adauga o disciplina in lista de discipline
        :param d[Disciplina]: Disciplina de adaugat
        @raises[RepositoryException]: Disciplina exista in lista de discipline
        @post: Lista de discipline creste cu 1
        '''
        self.exists(d)
        self.__discipline['0'].append(d)

    def modify(self, d, ot):
        '''
        Functie care modifica o disciplina din lista de discipline
        :param d[Disciplina]: Disciplina de modificat
        :param ot[Disciplina]: Noua valoare a disciplinei
        @raises[RepositoryException]: Disciplina de modificat nu exista in lista de discipline
        '''
        self.findOne(d)
        self.exists(ot)
        i = self.__discipline['0'].index(d)
        self.__discipline['0'][i].setID(ot.getID())
        self.__discipline['0'][i].setDenumire(ot.getDenumire())
        self.__discipline['0'][i].setProfesor(ot.getProfesor())

    def getAll(self):
        '''
        Functie care returneaza lista de discipline
        :param self:
        @return[list[Disciplina]]: Lista de discipline
        '''
        return self.__discipline['0']
