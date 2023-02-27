'''
Created on Dec 14, 2022

@author: balut
'''

from domain.entities import Cafenea


class InFileRepositoryCafenea(object):
    '''
    classdocs
    '''

    def __init__(self, fileName):
        '''
        Constructor
        '''
        self.__cafenele = []
        self.__fileName = fileName
        self.__loadFromFile()

    def get_all(self):
        return self.__cafenele

    def __loadFromFile(self):
        with open(self.__fileName, "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.split(",")
                nume = line[0]
                tara = line[1].strip()
                pret = float(line[2].strip())
                c = Cafenea(nume, tara, pret)
                self.__cafenele.append(c)
            f.close()

    def __saveToFile(self):
        with open(self.__fileName, "w") as f:
            for c in self.__cafenele:
                cstr = c.getNume() + "," + c.getTara() + "," + str(c.getPret()) + "\n"
                f.write(cstr)
            f.close()
