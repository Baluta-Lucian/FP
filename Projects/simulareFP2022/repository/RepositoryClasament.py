'''
Created on Dec 14, 2022

@author: balut
'''

from domain.entities import Meci


class RepositoryMeciuri(object):
    '''
    classdocs
    '''

    def __init__(self, repoE):
        '''
        Constructor
        '''
        self.__repoE = repoE
        self.__meciuri = []
        self.__populate()

    def get_all(self):
        '''
        Functie care returneaza lista de meciuri
        :param self:
        @return[list[Meci]]: lista de meciuri
        '''
        return self.__meciuri

    def __populate(self):
        '''
        Functie care populeaza lista de meciuri
        :param self:
        @post: Lungimea listei creste cu 10
        '''
        self.__meciuri.append(Meci("Steaua", "Pandurii", 3, 4))
        self.__meciuri.append(Meci("Bayern", "Arsenal", 3, 2))
        self.__meciuri.append(Meci("Napoli", "Izvoare", 2, 1))
        self.__meciuri.append(Meci("Timisoara", "Lateral", 0, 0))
        self.__meciuri.append(Meci("Madrid", "Pandurii", 2, 0))
        self.__meciuri.append(Meci("Dinamo", "Lateral", 5, 0))
        self.__meciuri.append(Meci("Bayern", "Lateral", 7, 0))
        self.__meciuri.append(Meci("Madrid", "Bayern", 2, 2))
        self.__meciuri.append(Meci("Arsenal", "Pandurii", 1, 0))
        self.__meciuri.append(Meci("Lateral", "Dinamo", 0, 0))
