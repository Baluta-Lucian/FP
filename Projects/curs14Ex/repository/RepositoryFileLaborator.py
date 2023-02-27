'''
Created on Feb 23, 2023

@author: balut
'''
from domain.Laborator import Laborator


class RepositoryLaboratoare(object):
    '''
    classdocs
    '''

    def __init__(self, fileName):
        '''
        Constructor
        '''
        self.__fileName = fileName
        self.__laboratoare = []
        self.__loadFromFile()

    def save(self, lab):
        self.__laboratoare.append(lab)
        self.__saveToFile()

    def getAll(self):
        return self.__laboratoare

    def __loadFromFile(self):
        with open(self.__fileName, "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                line = line.split(";")
                sId = int(line[0])
                labNumber = int(line[1])
                problemNumber = line[2]
                laborator = Laborator(sId, labNumber, problemNumber)
                self.save(laborator)
            f.close()

    def __saveToFile(self):
        with open(self.__fileName, "w") as f:
            l = self.getAll()
            for s in l:
                sIdFile = str(s.get_student_id())
                labNumberFile = str(s.get_lab_number())
                problemNumber = s.get_problem_number()
                labFile = sIdFile + ";" + labNumberFile + ";" + problemNumber + "\n"
                f.write(labFile)
            f.close()
