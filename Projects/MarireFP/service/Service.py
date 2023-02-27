'''
Created on Feb 23, 2023

@author: balut
'''
from domain.Jucator import Jucator
import random
from errors.Exception import RepositoryException, ValidationException


class Service(object):
    '''
    classdocs
    '''

    def __init__(self, repo, val):
        '''
        Constructor
        '''
        self.__repo = repo
        self.__val = val

    def addJucator(self, nume, prenume, inaltime, post):
        '''
        Functie care creeaza si salveaza un obiect de tip Jucator in lista de jucatori
        :param nume[String]: numele jucatorului
        :param prenume[String]: prenumele jucatorului
        :param inaltime[int]: inaltimea jucatorului
        :param post[String]: postul jucatorului
        @raises: [RepositoryException] : jucator existent
                 [ValidationException] : jucator invalid
        '''
        j = Jucator(nume, prenume, inaltime, post)
        self.__val.validateJucator(j)
        self.__repo.save(j)

    def modificaInaltime(self, inaltime):
        '''
        Functie care modifica toti jucatorii dupa o anumita inaltime data
        :param inaltime[int]: inaltimea cu care modificam
        '''
        self.__repo.modifyByH(inaltime)

    def importa(self, fileName):
        '''
        Functie care importa si genereaza jucatori dintr-un fisier dat
        :param fileName[String]: fisierul din care importam
        @return[int]: numarul de jucatori adaugati in lista de jucatori
        '''
        n = 0
        m = 0
        pozitii = ["Fundas", "Pivot", "Extrema"]
        with open(fileName, "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                line = line.split(";")
                nume = line[0]
                prenume = line[1]
                inaltime = random.randint(0, 220)
                post = random.choice(pozitii)
                j = Jucator(nume, prenume, inaltime, post)
                try:
                    self.__val.validateJucator(j)
                    self.__repo.save(j)
                    n = n + 1
                except RepositoryException as re:
                    m = m + 1
                except ValidationException as ve:
                    m = m + 1
            f.close()
        return n

    # def __inaltimeMedie(self, fundasi, extreme, pivoti, inaltimeMedie):
    #     n = 0
    #     sumInaltime = 0
    #     echipa = []
    #
    #     if len(fundasi) < 2:
    #         return False
    #     if len(extreme) < 2:
    #         return False
    #     if len(pivoti) < 1:
    #         return False
    #
    #     for i in range(0, 2):
    #         echipa.append(fundasi[i])
    #         n = n + 1
    #         sumInaltime = sumInaltime + fundasi[i].get_inaltime()
    #         echipa.append(extreme[i])
    #         n = n + 1
    #         sumInaltime = sumInaltime + extreme[i].get_inaltime()
    #         if i == 0:
    #             echipa.append(pivoti[i])
    #             n = n + 1
    #             sumInaltime = sumInaltime + pivoti[i].get_inaltime()
    #
    #     fundasi.pop(0)
    #     fundasi.pop(0)
    #     extreme.pop(0)
    #     extreme.pop(0)
    #     pivoti.pop(0)
    #
    #     currentMedie = sumInaltime / n
    #     if currentMedie < inaltimeMedie:
    #         return False
    #     else:
    #         return True

    def echipaMax(self):
        '''
        Functie care returneaza o echipa formata din 2 Fundasi, 2 Extreme si 1 Pivot
        cu inaltimea medie maxima
        :param self:
        @return[list[Jucator]]: echipa ceruta
        '''
        jucatori = self.__repo.getAll()
        fundasi = []
        extreme = []
        pivoti = []
        for j in jucatori:
            if j.get_post() == "Fundas":
                fundasi.append(j)
            elif j.get_post() == "Extrema":
                extreme.append(j)
            else:
                pivoti.append(j)

        fundasi.sort(key=lambda x: x.get_inaltime(), reverse=True)
        extreme.sort(key=lambda x: x.get_inaltime(), reverse=True)
        pivoti.sort(key=lambda x: x.get_inaltime(), reverse=True)

        echipa = []
        sumInaltime = 0
        n = 0
        if len(fundasi) < 2:
            return []
        if len(extreme) < 2:
            return []
        if len(pivoti) < 1:
            return []

        for i in range(0, 2):
            echipa.append(fundasi[i])
            n = n + 1
            sumInaltime = sumInaltime + fundasi[i].get_inaltime()
            echipa.append(extreme[i])
            n = n + 1
            sumInaltime = sumInaltime + extreme[i].get_inaltime()
            if i == 0:
                echipa.append(pivoti[i])
                n = n + 1
                sumInaltime = sumInaltime + pivoti[i].get_inaltime()

        fundasi.pop(0)
        fundasi.pop(0)
        extreme.pop(0)
        extreme.pop(0)
        pivoti.pop(0)

        inaltimeMedie = sumInaltime / n

        return echipa

    def getAllJucatori(self):
        '''
        Functie care returneaza toti jucatorii din lista de jucatori
        :param self:
        @return[list[Jucator]]: Lista de jucatori
        '''
        return self.__repo.getAll()
