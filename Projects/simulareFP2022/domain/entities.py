'''
Created on Dec 14, 2022

@author: balut
'''


class Echipa(object):
    '''
    classdocs
    '''

    def __init__(self, denumire, sponsor):
        '''
        Constructor
        '''
        self.__denumire = denumire
        self.__sponsor = sponsor

    def getEchipa(self):
        '''
        Functie care returneaza denumirea echipei
        :param self:
        @return[str]: denumirea echipei
        '''
        return self.__denumire

    def getSponsor(self):
        '''
        Functie care returneaza numele sponsorului
        :param self:
        @return[str]: numele sponsorului
        '''
        return self.__sponsor

    def setDenumire(self, ot):
        '''
        Functie care actualizeaza denumirea echipei
        :param ot[str]: denumirea de actualizat
        '''
        self.__denumire = ot

    def setSponsor(self, ot):
        '''
        Functie care actualizeaza numele sponsorului
        :param ot[str]: numele de actualizat
        '''
        self.__sponsor = ot

    def __str__(self):
        '''
        Functie care suprascrie modul de afisare a unei entitati de tip Echipa
        :param self:
        @return[str]: Modul de afisare a unei Echipe
        '''
        return "Echipa: " + self.__denumire + "; Sponsor: " + self.__sponsor

    def __eq__(self, ot):
        return self.__denumire == ot.getDenumire() and self.__sponsor == ot.getSponsor()


class Meci(object):
    def __init__(self, e1, e2, g1, g2):
        self.__e1 = e1
        self.__e2 = e2
        self.__g1 = g1
        self.__g2 = g2

    def getE1(self):
        '''
        Functie care returneaza numele primei echipe
        :param self:
        @return[str]: numele primei echipe
        '''
        return self.__e1

    def getE2(self):
        '''
        Functie care returneaza numele la echipa nr 2
        :param self:
        @return[str]: numele echipei nr 2
        '''
        return self.__e2

    def getG1(self):
        '''
        Functie care returneaza golurile marcate de echipa 1
        :param self:
        @return[int]: golurile marcate de echipa 1
        '''
        return self.__g1

    def getG2(self):
        '''
        Functie care returneaza golurile marcate de echipa 2
        :param self:
        @return[int]: golurile marcate de echipa 2
        '''
        return self.__g2
    #
    # def setE1(self, ot):
    #     '''
    #     Functie care actualizeaza numele echipei 1
    #     :param ot[str]:
    #     '''
    #     self.__e1 = ot
    #
    # def setE2(self, ot):
    #     self.__e2 = ot
    #
    # def setG1(self, ot):
    #     self.__g1 = ot
    #
    # def setG2(self, ot):
    #     self.__g2 = ot

    def __str__(self):
        '''
        Functie care suprascrie modul de afisare al unui meci
        :param self:
        @return[str]: modul de afisare al unui meci
        '''
        return "Meci: " + self.__e1 + " - " + self.__e2 + " ; " + str(self.__g1) + " - " + str(self.__g2)
