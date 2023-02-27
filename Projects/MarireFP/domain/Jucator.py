'''
Created on Feb 23, 2023

@author: balut
'''


class Jucator(object):
    '''
    classdocs
    '''

    def __init__(self, nume, prenume, inaltime, post):
        '''
        Constructor
        '''
        self.__nume = nume
        self.__prenume = prenume
        self.__inaltime = inaltime
        self.__post = post

    def get_nume(self):
        '''
        Functie care returneaza numele unui jucator
        :param self:
        @return[String]: numele jucatorului
        '''
        return self.__nume

    def get_prenume(self):
        '''
        Functie care returneaza prenumele unui jucator
        :param self:
        @return[String]: prenumele jucatorului
        '''
        return self.__prenume

    def get_inaltime(self):
        '''
        Functie care returneaza inaltimea unui jucator
        :param self:
        @return[int]: inaltimea jucatorului
        '''
        return self.__inaltime

    def get_post(self):
        '''
        Functie care returneaza postul unui jucator
        :param self:
        @return[String]: postul jucatorului
        '''
        return self.__post

    def set_inaltime(self, value):
        '''
        Functie care modifica inaltimea jucatorului
        :param value[int]: inaltimea noua
        '''
        self.__inaltime = value

    def __str__(self):
        '''
        Suprascrierea functiei de afisare a unui obiect de tip Jucator
        :param self:
        @return[String]: Modul de afisare al jucatorului
        '''
        return "Jucator{ " + self.__nume + ", " + self.__prenume + ", " + str(self.__inaltime) + ", " + self.__post + "}"

    def __eq__(self, ot):
        '''
        Suprascrierea functiei de egalitate intre doua obiecte de tip Jucator
        :param ot[Jucator]: jucatorul de comparat
        @return[Boolean]:    True -> Daca sunt egale
                             False -> Altfel
        '''
        return ot.get_nume() == self.get_nume() and ot.get_prenume() == self.get_prenume()
