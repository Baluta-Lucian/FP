'''
Created on Jan 31, 2023

@author: balut
'''
from errors.Exceptions import ValidationError


class ValidatorSpectacol(object):
    '''
    classdocs
    '''

    def validate(self, s):
        '''
        Functie care valideaza un spectacol
        :param s[Spectacol]: spectacolul de validat
        @raises[ValidationError]: spectacolul nu este valid
        '''
        errors = ""
        if len(s.getTitlu()) == 0:
            errors += "!!!Titlul trebuie sa fie nevid!!!\n"
        if len(s.getArtist()) == 0:
            errors += "!!!Artistul trebuie sa fie nevid\n!!!"
        if s.getDurata() <= 0:
            errors += "!!!Durata trebuie sa fie intreg pozitiv!!!\n"
        gen = s.getGen()
        if gen != "Comedie" and gen != "Concert" and gen != "Balet" and gen != "Altele":
            errors += "!!!Genul trebuie sa fie: Comedie/Concert/Balet/Altele!!!\n"
        if len(errors) != 0:
            raise ValidationError(errors)
