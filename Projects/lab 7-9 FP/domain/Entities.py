'''
Created on Nov 10, 2022

@author: balut
'''
from fontTools.unicodedata import ot_tag_to_script


class Student(object):
    '''
    classdocs
    '''

    def __init__(self, id, nume):
        '''
        Constructor
        '''
        self.__id = id
        self.__nume = nume

    def getID(self):
        '''
        Functie care returneaza id-ul unui student
        :param self:
        @return[int]: id-ul studentului
        '''
        return self.__id

    def setID(self, ot):
        '''
        Functie care seteaza id-ul unui student
        :param ot[int]: noul id al studentului
        @post: -> id-ul studentului se modifica
        '''
        self.__id = ot

    def getNume(self):
        '''
        Functie care returneaza numele studentului
        :param self:
        @return[string]: numele studentului
        '''
        return self.__nume

    def setNume(self, ot):
        '''
        Functie care seteaza numele studentului
        :param ot[string]: noul nume al studentului
        @post: -> numele studentului este modificat
        '''
        self.__nume = ot

    def __str__(self):
        '''
        Functie care suprascrie modul de afisare a entitatii Student
        :param self:
        @return[string]: modul de afisare al studentului
        '''
        return "Student{ ID: " + str(self.__id) + ", Nume: " + str(self.__nume) + " };"

    def __eq__(self, ot):
        '''
        Functie care suprascrie modul de egalitate intre doua obiecte de tip Student
        :param ot[Student]: studentul cu care se compara
        @return: -> True: daca stundetii sunt aceeasi
                    False: altfel
        '''
        return self.__id == ot.__id and self.__nume == ot.__nume


class Disciplina(object):
    def __init__(self, id, denumire, profesor):
        self.__id = id
        self.__denumire = denumire
        self.__profesor = profesor

    def getID(self):
        '''
        Functie care returneaza id-ul unei discipline
        :param self:
        @return[int]: id-ul disciplinei
        '''
        return self.__id

    def setID(self, ot):
        '''
        Functie care seteaza id-ul unei discipline
        :param ot[int]: noul id al disciplinei
        @post: id-ul disciplinei este modificat
        '''
        self.__id = ot

    def getDenumire(self):
        '''
        Functie care returneaza denumirea unei discipline
        :param self:
        @return[string]: denumirea disciplinei
        '''
        return self.__denumire

    def setDenumire(self, ot):
        '''
        Functie care seteaza denumirea unei disciplinei
        :param ot[string]: noua denumire a disciplinei
        @post: denumirea disciplinei este modificata
        '''
        self.__denumire = ot

    def getProfesor(self):
        '''
        Functie care returneaza profesorul disciplinei
        :param self:
        @return[string]: profesorul disciplinei
        '''
        return self.__profesor

    def setProfesor(self, ot):
        '''
        Functie care seteaza profesorul disciplinei
        :param ot[string]: profesorul disciplinei
        @post: profesorul disciplinei este modificat
        '''
        self.__profesor = ot

    def __str__(self):
        '''
        Functie care suprascrie afisarea unei entitati de tip Disciplina
        :param self:
        @return[string]: Afisarea unei entitati de tip Disciplina
        '''
        return "Disciplina{ ID: " + str(self.__id) + ", Denumire: " + str(self.__denumire) + ", Profesor: " + str(self.__profesor) + " };"

    def __eq__(self, ot):
        '''
        Functie care suprascrie modul de egalitate intre doua obiecte de tip Disciplina
        :param ot[Disciplina]: Disciplina cu care se compara
        @return:    ->True: daca disciplinele sunt egale
                    ->False: altfel
        '''
        return self.__id == ot.__id and self.__denumire == ot.__denumire and self.__profesor == ot.__profesor


class Statistica(object):
    def __init__(self, s, d, note):
        self.__s = s
        self.__d = d
        self.__note = note

    def getS(self):
        '''
        Functie care returneaza stundetul unei statistici
        :param self:
        @return[Student]: Studentul statisticii
        '''
        return self.__s

    def getD(self):
        '''
        Functie care returneaza disciplina unei statistici
        :param self:
        @return[Disciplina]: Disciplina statisticii
        '''
        return self.__d

    def getNote(self):
        '''
        Functie care returneaza notele unui student la o disciplina
        :param self:
        @return[list[int]]:Notele unui student la o disciplina
        '''
        return self.__note

    def getMedie(self):
        '''
        Functie care returneaza media notelor unui student la o disciplina
        :param self:
        @return[float]: media notelor unui student la o disciplina
        '''
        n = 0
        suma = 0
        for i in self.__note:
            suma += i
            n += 1
        return suma / n

    def __str__(self):
        '''
        Functie care suprascrie modul de afisare a unei statistici
        :param self:
        @return[string]: Modul de afisare a unei statistici
        '''
        return "Student: " + self.__s.getNume() + "; Materie: " + self.__d.getDenumire() + "; Note: " + str(self.__note)

    def __eq__(self, ot):
        '''
        Functie care suprascrie relatia de egalitate dintre doua statistici
        :param ot[Statistica]:Statistica de comparat
        @return[bool] :     ->True: Daca statisticile sunt egale
                            ->False: Altfel
        '''
        return self.__s == ot.getS() and self.__d == ot.getD() and self.__note == ot.getNote()


class Situatie(object):
    def __init__(self, s, medie):
        self.__s = s
        self.__medie = medie

    def getMedieGenerala(self):
        '''
        Functie care afiseaza media generala a unui student
        :param self:
        @return[int]: Media generala a unui student
        '''
        return self.__medie

    def __str__(self):
        '''
        Functie care suprascrie modul de afisare a unei situatii
        :param self:
        @return[string]: Modul de afisare a unei situatii
        '''
        return "Student: " + self.__s.getNume() + "; Medie: " + str(self.__medie)

    def __eq__(self, ot):
        '''
        Functie care suprascrie relatia de egalitate dintre doua entitati de tip Situatie
        :param ot[Situatie]:Situatia de comparat
        @return[bool]:    ->True: Daca situatiile sunt egale
                          ->False: Altfel
        '''
        return self.__s == ot.__s and self.__medie == ot.__medie
