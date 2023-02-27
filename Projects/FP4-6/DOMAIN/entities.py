'''
Created on Oct 26, 2022

@author: balut
'''


class ComplexNumber(object):
    '''
    classdocs
    '''

    def __init__(self, real, imaginar):
        '''
        Constructor

        :param real[int]: -> partea reala a unui numar complex
        :param imaginar[int]: -> partea imaginara a unui numar complex
        '''
        self.__real = real
        self.__imaginar = imaginar

    def getReal(self):
        '''
        Functie care returneaza partea reala a unui numar complex
        :param self:
        @return[int]: -> partea reala a unui nr real
        '''
        return self.__real

    def setReal(self, ot):
        '''
        Functie care seteaza partea reala a unui numar complex cu alta valoare
        :param ot[int]: valoarea dorita
        '''
        self.__real = ot

    def getImaginar(self):
        '''
        Funcite care returneaza partea imaginara a unui numar complex
        :param self:
        @return[int]: -> partea imaginara a unui numnar complex
        '''
        return self.__imaginar

    def setImaginar(self, ot):
        '''
        Functie care seteaza partea imaginara a unui numar complex cu alta valoare
        :param ot[int]: valoarea dorita
        '''
        self.__imaginar = ot

    def __str__(self):
        '''
        Functie care supraincarca operatorul str al obiectului
        :param self:
        @return[str]: Obiectul in formatul dorit de afisat
        '''
        if self.__imaginar >= 0:
            return str(self.__real) + " + " + str(self.__imaginar) + "i"
        else:
            t = self.__imaginar
            t = t * (-1)
            return str(self.__real) + " - " + str(t) + "i"

    def __eq__(self, ot):
        '''
        Functie care supraincarca operatorul eq pentru a vedea daca doua obiecte sunt de acelasi tip
        :param ot:
        @return[bool]: *True -> Daca obiectele sunt egale
                       *False -> Altfel
        '''
        return self.__real == ot.__real and self.__imaginar == ot.__imaginar
