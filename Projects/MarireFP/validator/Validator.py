'''
Created on Feb 23, 2023

@author: balut
'''
from errors.Exception import ValidationException


class Validator(object):
    '''
    classdocs
    '''

    def validateJucator(self, j):
        '''
        Functie care valideaza un obiect de tip jucator
        :param j[Jucator]: jucatorul de validat
        @raises[ValidationException]:jucatorul este invalid
        '''
        errors = ""
        posturi = ["Fundas", "Pivot", "Extrema"]
        if len(j.get_nume()) == 0:
            errors += "!!! Numele jucatorului nu poate fi vid !!!\n"
        if len(j.get_prenume()) == 0:
            errors += "!!! Prenumele jucatorului nu poate fi vid !!!\n"
        if j.get_inaltime() <= 140:
            errors += "!!! Inaltimea unui jucator nu poate fi mai mica sau egala cu 140 !!!\n"
        if j.get_post() not in posturi:
            errors += "!!! Postul jucatorului poate fi doar (Fundas, Pivot, Extrema) !!!\n"

        if len(errors) != 0:
            raise ValidationException(errors)
