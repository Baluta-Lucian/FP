'''
Created on Feb 23, 2023

@author: balut
'''
from errors.Exceptions import ValidationException
from numpy.core.defchararray import isnumeric


class Validator(object):
    '''
    classdocs
    '''

    def validateS(self, s):
        errors = ""
        if len(s.get_name()) == 0:
            errors += "!!! NUMELE NU TREBUIE SA FIE NULL !!!\n"

        if len(errors) != 0:
            raise ValidationException(errors)

    def validateL(self, lab):
        errors = ""
        if isnumeric(lab.get_problem_number()) == False:
            errors += "!!! NUMARUL PROBLEMEI LABORATORULUI TREBUIE SA FIE FORMAT DIN CIFRE !!!\n"

        if lab.get_lab_number() < 0:
            errors += "!!! NUMARUL LABORATORULUI TREBUIE SA FIE POZITIV !!!\n"

        if len(errors) != 0:
            raise ValidationException(errors)
