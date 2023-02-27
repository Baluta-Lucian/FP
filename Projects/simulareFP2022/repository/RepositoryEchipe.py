'''
Created on Dec 14, 2022

@author: balut
'''
from domain.entities import Echipa


class RepositoryEchipe(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.__echipe = []
        self.__populate()

    def get_all(self):
        '''
        Functie care returneaza lista de echipe
        :param self:
        @return[list[Echipa]]: lista de echipe
        '''
        return self.__echipe

    def __populate(self):
        '''
        Functie care populeaza lista de echipe
        :param self:
        @post: Lungimea listei creste cu 10
        '''
        e1 = Echipa("Dinamo", "Roi")
        self.__echipe.append(e1)
        self.__echipe.append(Echipa("Steaua", "Becali"))
        self.__echipe.append(Echipa("Pandurii", "Romanescu"))
        self.__echipe.append(Echipa("Bayern", "Roi"))
        self.__echipe.append(Echipa("Madrid", "Bil"))
        self.__echipe.append(Echipa("Lateral", "Rony"))
        self.__echipe.append(Echipa("Timisoara", "Balaci"))
        self.__echipe.append(Echipa("Napoli", "Pintili"))
        self.__echipe.append(Echipa("Arsenal", "Raul"))
        self.__echipe.append(Echipa("Izvoare", "Draghici"))
