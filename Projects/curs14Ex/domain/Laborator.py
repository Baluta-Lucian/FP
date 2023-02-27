'''
Created on Feb 23, 2023

@author: balut
'''


class Laborator(object):
    '''
    classdocs
    '''

    def __init__(self, studentId, labNumber, problemNumber):
        '''
        Constructor
        '''
        self.__studentId = studentId
        self.__labNumber = labNumber
        self.__problemNumber = problemNumber

    def get_student_id(self):
        return self.__studentId

    def get_lab_number(self):
        return self.__labNumber

    def get_problem_number(self):
        return self.__problemNumber

    def set_student_id(self, value):
        self.__studentId = value

    def set_lab_number(self, value):
        self.__labNumber = value

    def set_problem_number(self, value):
        self.__problemNumber = value
