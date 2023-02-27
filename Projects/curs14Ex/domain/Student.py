'''
Created on Feb 23, 2023

@author: balut
'''


class Student(object):
    '''
    classdocs
    '''

    def __init__(self, id, name):
        '''
        Constructor
        '''
        self.__id = id
        self.__name = name

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def set_id(self, value):
        self.__id = value

    def set_name(self, value):
        self.__name = value

    def __str__(self):
        return "Student {" + str(self.__id) + ", " + self.__name + "}"
