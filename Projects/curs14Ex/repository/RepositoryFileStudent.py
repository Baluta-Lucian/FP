'''
Created on Feb 23, 2023

@author: balut
'''
from domain.Student import Student


class RepositoryStudenti(object):
    '''
    classdocs
    '''

    def __init__(self, fileName):
        '''
        Constructor
        '''
        self.__fileName = fileName
        self.__studenti = []
        self.__loadFromFile()

    def save(self, s):
        self.__studenti.append(s)
        self.__saveToFile()

    def getAll(self):
        return self.__studenti

    def __loadFromFile(self):
        with open(self.__fileName, "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                line = line.split(';')
                id = int(line[0])
                name = line[1]
                student = Student(id, name)
                self.save(student)
            f.close()

    def __saveToFile(self):
        with open(self.__fileName, "w") as f:
            l = self.getAll()
            for s in l:
                idFile = str(s.get_id())
                studentFile = idFile + ";" + s.get_name() + "\n"
                f.write(studentFile)
            f.close()
