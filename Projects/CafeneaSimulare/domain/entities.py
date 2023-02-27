'''
Created on Dec 14, 2022

@author: balut
'''


class Cafenea(object):
    '''
    classdocs
    '''

    def __init__(self, nume, tara_de_origine, pret):
        '''
        Constructor
        '''
        self.__nume = nume
        self.__tara_de_origine = tara_de_origine
        self.__pret = pret

    def getNume(self):
        return self.__nume

    def getTara(self):
        return self.__tara_de_origine

    def getPret(self):
        return self.__pret

    def __str__(self):
        return self.__nume + "," + self.__tara_de_origine + "," + str(self.__pret)
