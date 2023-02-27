'''
Created on Dec 13, 2022

@author: balut
'''
from domain.entities import Bicicleta
from erorrs.Errors import ValidationException


class Validator(object):
    '''
    classdocs
    '''

    def validate(self, b: Bicicleta):
        errors = ""
        if type(b.getID()) != int:
            errors += "Type-ul id-ului trebuie sa fie int!\n"
        if b.getTip() == "":
            errors += "Tipul nu trebuie sa fie gol!\n"
        if type(b.getPret()) != float:
            errors += "Type-ul pretului trebuie sa fie de tip float!\n"

        if len(errors) != 0:
            raise ValidationException(errors)
