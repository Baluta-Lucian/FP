'''
Created on Dec 13, 2022

@author: balut
'''
from fontTools.otlLib.builder import buildMultipleSubstSubtable


class Bicicleta(object):
    '''
    classdocs
    '''

    def __init__(self, id, tip, pret):
        '''
        Constructor
        '''
        self.__id = id
        self.__tip = tip
        self.__pret = pret

    def getID(self):
        return self.__id

    def setID(self, ot):
        self.__id = id

    def getTip(self):
        return self.__tip

    def setTip(self, ot):
        self.__tip = ot

    def getPret(self):
        return self.__pret

    def setPret(self, ot):
        self.__pret = ot

    def __str__(self):
        return str(self.__id) + ";" + self.__tip + ";" + str(self.__pret)
