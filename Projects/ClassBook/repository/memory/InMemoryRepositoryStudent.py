'''
Created on Nov 10, 2022

@author: balut
'''
from errors.Exceptions import RepositoryException


class InMemoryRepositoryStudent(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.__studenti = []

    def store(self, s):
        self.exists(s)
        self.__studenti.append(s)

    def findOne(self, s):
        for student in self.__studenti:
            if student == s:
                return s
        raise RepositoryException("!!!Studentul nu exista in lista de studenti!!!")\


    def delete(self, s):
        deleted = self.findOne(s)
        self.__studenti.remove(s)
        return deleted

    def exists(self, s):
        for student in self.__studenti:
            if student.getID() == s.getID():
                raise RepositoryException(
                    "!!!ID-ul studentului exista deja in lista de studenti!!!")

    def modify(self, s, ot):
        self.findOne(s)
        self.exists(ot)
        i = self.__studenti.index(s)
        self.__studenti[i].setID(ot.getID())
        self.__studenti[i].setNume(ot.getNume())

    def getAll(self):
        return self.__studenti

# class InMemoryRepositoryStudent(object):
#     '''
#     classdocs
#     '''
#
#     def __init__(self):
#         '''
#         Constructor
#         '''
#         self.__studenti = {'0': []}
#
#     def store(self, s):
#         '''
#         Functie care adauga un student in lista de studenti
#         :param s[Student]: Stundetul de adaugat
#         @raises[RepositoryException]: Studentul de adaugat exista deja in lista de studenti
#         '''
#         self.exists(s)
#         self.__studenti['0'].append(s)
#
#     def findOne(self, s):
#         '''
#         Functie care cauta un student in lista de studenti
#         :param s[Student]: Student de cautat
#         @return[Student]: Studentul gasit in lista de studenti
#         @raises[RepositoryException]: Studentul nu exista in lista de studenti
#         '''
#         for student in self.__studenti['0']:
#             if student == s:
#                 return s
#         raise RepositoryException("!!!Studentul nu exista in lista de studenti!!!")\
#
#
#     def delete(self, s):
#         '''
#         Functie care sterge un student din lista de studenti
#         :param s[Student]: Studentul de sters
#         @return[Student]: Studentul sters din lista de studenti
#         @raises[RepositoryException]: Studentul nu exista in lista de studenti
#         '''
#         deleted = self.findOne(s)
#         self.__studenti['0'].remove(s)
#         return deleted
#
#     def exists(self, s):
#         '''
#         Functie care verifica daca un student exista in lista de studenti
#         :param s[Student]: Studentul de verificat
#         @raises[RepositoryException]: studentul exista deja in lista
#         '''
#         for student in self.__studenti['0']:
#             if student.getID() == s.getID():
#                 raise RepositoryException(
#                     "!!!ID-ul studentului exista deja in lista de studenti!!!")
#
#     def modify(self, s, ot):
#         '''
#         Functie care modifica un student din lista de studenti
#         :param s[Student]: Studentul de modificat
#         :param ot[Student]: Noile valori ale studentului
#         @raises[RepositoryException]: Studentul de modificat nu exista in lista de studenti
#         '''
#         self.findOne(s)
#         self.exists(ot)
#         i = self.__studenti['0'].index(s)
#         self.__studenti['0'][i].setID(ot.getID())
#         self.__studenti['0'][i].setNume(ot.getNume())
#
#     def getAll(self):
#         '''
#         Functie care returneaza lista de studenti
#         :param self:
#         @return[list[Student]]: Lista de studenti
#         '''
#         return self.__studenti['0']
