'''
Created on Nov 10, 2022

@author: balut
'''

from errors.Exceptions import ValidationException
from domain.Entities import Student, Disciplina, Statistica
from pickle import FALSE


class Validator:
    def validateS(self, student: Student):
        '''
        Functie care valideaza un student
        :param student[Student]: Studentul de validat
        @raises[ValidationException]: Studentul este invalid
        '''
        errors = ""
        nume = student.getNume()
        if student.getID() < 0:
            errors += "!!!ID INVALID!!!\n"
        # for i in range(0, len(nume)-1):
        #     x = i + 1
        #     if i == 0:
        #         if nume[i].isupper() == False:
        #             errors += "!!!NUMELE UNUI STUDENT TREBUIE SA INCEAPA CU LITERA MARE!!!\n"
        #     if x != len(nume) - 1 and nume[i].isupper() == False:
        #         pass
        if len(nume) == 0:
            errors += "!!!STUDENTUL TREBUIE SA AIBA UN NUME\n"
        result = self.checkName(nume, 0, "")
        errors += result
        if len(errors) != 0:
            raise ValidationException(errors)

    def validateD(self, disciplina: Disciplina):
        '''
        Functie care verifica daca o disciplina este valida
        :param disciplina[Disciplina]: Disciplina de verificat
        @raises[ValidationException]: Disciplina invalida
        '''
        errors = ""
        nume = disciplina.getProfesor()
        if disciplina.getID() < 0:
            errors += "!!!ID INVALID!!!\n"
        if disciplina.getDenumire() == "":
            errors += "!!!DENUMIRE INVALIDA!!!\n"
        if len(nume) == 0:
            errors += "!!!PROFESORUL TREBUIE SA AIBA UN NUME\n"
        result = self.checkName(nume, 0, "")
        errors += result
        if len(errors) != 0:
            raise ValidationException(errors)

    def validateStat(self, stat: Statistica):
        '''
        Functie care valideaza o statistica
        :param stat[Statistica]: Statistica de validat
        @raises[ValidationException]: Statistica este invalida
        '''
        self.validateS(stat.getS())
        self.validateD(stat.getD())
        errors = ""
        noteErr = "!!!Notele trebuie sa fie intre 1-10!!!\n"
        l = stat.getNote()
        if len(l) == 0:
            errors += "!!!Studentul trebuie sa aiba note la aceasta disciplina!!!\n"
        for el in l:
            if el < 1 or el > 10:
                if noteErr not in errors:
                    errors += noteErr
        if len(errors) != 0:
            raise ValidationException(errors)

    def checkName(self, name, lng, errors: str):
        '''
        Functie care verifica daca un nume incepe cu litera mare, este
        separat prin spatiu sau - de prenume 
        :param name:
        :param lng:
        :param errors:
        '''
        mare = "!!!NUMELE TREBUIE SA INCEAPA CU LITERA MARE!!!\n"
        spatiu = "!!!NUMELE SI PRENUMELE SUNT SEPARATE DE SPATIU!!!\n"
        mici = "!!!NUMELE INCEPE CU LITERA MARE SI CONTINUA CU LITERE MICI!!!\n"
        if len(name) == 0:
            return str(errors)
        if lng == 0 and name[0].isupper() == False:
            if "!!!NUMELE TREBUIE SA INCEAPA CU LITERA MARE!!!\n" not in errors:
                errors += mare
            return self.checkName(name[1:], lng + 1, errors)
        elif name[0] == " " or name[0] == "-":
            return self.checkName(name[1:], 0, errors)
        elif name[0].isupper() and lng == 0:
            return self.checkName(name[1:], lng + 1, errors)
        elif name[0].islower() == False:
            if "!!!NUMELE SI PRENUMELE SUNT SEPARATE DE SPATIU!!!\n" not in errors:
                errors += mici
            if spatiu not in errors:
                errors += spatiu
            return self.checkName(name[1:], lng + 1, errors)
        else:
            return self.checkName(name[1:], lng + 1, errors)
