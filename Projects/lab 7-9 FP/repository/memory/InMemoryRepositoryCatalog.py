'''
Created on Nov 14, 2022

@author: balut
'''
from errors.Exceptions import RepositoryException


# class InMemoryRepositoryCatalog(object):
#     '''
#     classdocs
#     '''
#
#     def __init__(self):
#         '''
#         Constructor
#         '''
#         self.__catalog = []
#
#     def exists(self, statistica):
#         for stat in self.__catalog:
#             if stat == statistica:
#                 raise RepositoryException("!!!Statistica existenta!!!")
#
#     def findOne(self, statistica):
#         for stat in self.__catalog:
#             if stat == statistica:
#                 return stat
#         raise RepositoryException("!!!Statistica nu existenta in catalog!!!")
#
#     def store(self, statistica):
#         self.exists(statistica)
#         self.__catalog.append(statistica)
#
#     def deleteByStudent(self, s):
#         for stat in self.__catalog:
#             if stat.getS() == s:
#                 self.__catalog.remove(stat)
#
#     def deleteByDisciplina(self, d):
#         for stat in self.__catalog:
#             if stat.getD() == d:
#                 self.__catalog.remove(stat)
#
#     def getAll(self):
#         return self.__catalog

class InMemoryRepositoryCatalog(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.__catalog = {'0': []}

    def exists(self, statistica):
        '''
        Functie care verifica daca o statistica exista deja in catalog
        :param statistica[Statistica]:Statistica de verificat
        @raises[RepositoryException]: Statistica existenta
        '''
        for stat in self.__catalog['0']:
            if stat == statistica:
                raise RepositoryException("!!!Statistica existenta!!!")

    def findOne(self, statistica):
        '''
        Functie care returneaza daca o statistica se afla in catalog
        :param statistica[Statistica]: Statistica de cautat
        @return[Statistica]: Statistica din catalog
        @raises[RepositoryException]: Statistica inexistenta in catalog
        '''
        for stat in self.__catalog['0']:
            if stat == statistica:
                return stat
        raise RepositoryException("!!!Statistica nu existenta in catalog!!!")

    def store(self, statistica):
        '''
        Functie care adauca o statistica in catalog
        :param statistica[Statistica]: Statistica de adaugat in catalog
        @raises[RepositoryException]: Statistica existenta in catalog
        '''
        self.exists(statistica)
        self.__catalog['0'].append(statistica)

    def deleteByStudent(self, s):
        '''
        Functie care sterge o statisticile din catalog ale unui student
        :param s[Student]: Studentul de la care vrem sa stergem statisticile
        '''
        for stat in self.__catalog['0']:
            if stat.getS() == s:
                self.__catalog['0'].remove(stat)

    def deleteByDisciplina(self, d):
        '''
        Functie care sterge o statisticile din catalog ale unei discipline
        :param d[Disciplina]: Disciplina de la care vrem sa stergem statisticile
        '''
        for stat in self.__catalog['0']:
            if stat.getD() == d:
                self.__catalog['0'].remove(stat)

    def getAll(self):
        '''
        Functie care returneaza catalogul
        :param self:
        @return[List[Statistici]]: Catalogul
        '''
        return self.__catalog['0']
