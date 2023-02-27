'''
Created on Oct 26, 2022

@author: balut
'''
from math import sqrt


class Helpers(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Clasa speciala pentru deservirea GraspController-ului
        Constructor

        :param self:
        '''

    def prim(self, n):
        '''
        Functie care verifica daca un numar intreg este prim
        :param n[int]: -> numarul intreg de verificat
        @return[bool]: *True -> Daca numarul este prim
                       *False -> Daca numarul nu este prim
        '''
        if n <= 1:
            return False

        if n == 2 or n == 3:
            return True

        if n % 2 == 0 or n % 3 == 0:
            return False

        for i in range(5, int(sqrt(n) + 1), 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True

    def module(self, a, b):
        '''
        Functie care calculeaza modulul unui numar complex
        :param a[int]: -> partea reala a unui numar complex
        :param b[int]: -> partea imaginara a unui numar complex
        @return[int]: modulul numarului complex
        '''
        return int(sqrt(a**2 + b**2))
