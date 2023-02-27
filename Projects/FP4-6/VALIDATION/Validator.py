'''
Created on Oct 26, 2022

@author: balut
'''
from numpy import integer


class Validator(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Clasa de validatori
        Constructor
        '''

    def validate(self, cn):
        '''
        Functie care verifica daca datele de intrare ale unui numar complex sunt valide
        :param cn:
        @exception[ValueError]: Date invalide
        '''
        errors = ""
        if isinstance(cn.getReal(), int) == False:
            errors += "!!!The real part can only be integer!!!\n"
        if isinstance(cn.getImaginar(), int) == False:
            errors += "!!!The imaginary part can only be integer!!!"
        if len(errors) > 0:
            raise ValueError(errors)
