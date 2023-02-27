'''
Created on Dec 14, 2022

@author: balut
'''
import unittest
from domain.entities import Echipa, Meci
from repository.RepositoryEchipe import RepositoryEchipe
from repository.RepositoryClasament import RepositoryMeciuri
from service.Service import ServiceClasament


class TestEntities(unittest.TestCase):
    '''
    classdocs
    '''

    def setUp(self):
        self.e1 = Echipa("Steaua", "Becali")
        self.e2 = Echipa("Dinamo", "Roi")
        self.e1_copy = Echipa("Steaua", "Becali")
        self.m1 = Meci("Steaua", "Dinamo", 3, 2)
        self.m2 = Meci("Dinamo", "Steaua", 1, 1)

    def test_getEchipa(self):
        self.assertEqual(self.e1.getEchipa(), "Steaua")
        self.assertEqual(self.e2.getEchipa(), "Dinamo")

    def test_getSponsor(self):
        self.assertEqual(self.e1.getSponsor(), "Becali")
        self.assertEqual(self.e2.getSponsor(), "Roi")

    def test_getE1E2(self):
        self.assertEqual(self.m1.getE1(), "Steaua")
        self.assertEqual(self.m1.getE2(), "Dinamo")
        self.assertEqual(self.m2.getE1(), "Dinamo")
        self.assertEqual(self.m2.getE2(), "Steaua")

    def test_getG1G2(self):
        self.assertEqual(self.m1.getG1(), 3)
        self.assertEqual(self.m1.getG2(), 2)
        self.assertEqual(self.m2.getG1(), 1)
        self.assertEqual(self.m2.getG2(), 1)

    def tearDown(self):
        pass


class TestRepoEchipe(unittest.TestCase):
    def setUp(self):
        self.repoTest = RepositoryEchipe()

    def test_PopulateGetAll(self):
        self.assertEqual(len(self.repoTest.get_all()), 10)


class TestRepoClasament(unittest.TestCase):
    def setUp(self):
        self.repoETest = RepositoryEchipe()
        self.__repoTest = RepositoryMeciuri(self.repoETest)

    def test_PopulateGetAll(self):
        self.assertEqual(len(self.__repoTest.get_all()), 10)


class TestService(unittest.TestCase):
    def setUp(self):
        self.repoETest = RepositoryEchipe()
        self.repoMTest = RepositoryMeciuri(self.repoETest)
        self.__srv = ServiceClasament(self.repoETest, self.repoMTest)

    def test_getAllEchipe(self):
        self.assertEqual(len(self.__srv.getAllEchipe()), 10)

    def test_getAllMeciuri(self):
        self.assertEqual(len(self.__srv.getAllMeciuri()), 10)

    def test_cautareEchipe(self):
        self.assertEqual(len(self.__srv.cautareEcipe("Roi")), 2)
        self.assertEqual(len(self.__srv.cautareEcipe("Becali")), 1)
        self.assertEqual(len(self.__srv.cautareEcipe("Baluta")), 0)

    def test_clasamentEchipe(self):
        clasament = self.__srv.clasamentEchipe()
        self.assertEqual(clasament[0].getEchipa(), "Bayern")
        self.assertEqual(clasament[1].getEchipa(), "Dinamo")
        self.assertEqual(clasament[2].getEchipa(), "Madrid")
        self.assertEqual(clasament[3].getEchipa(), "Pandurii")
        self.assertEqual(clasament[4].getEchipa(), "Arsenal")
        self.assertEqual(clasament[5].getEchipa(), "Napoli")
        self.assertEqual(clasament[6].getEchipa(), "Steaua")
        self.assertEqual(clasament[7].getEchipa(), "Izvoare")
        self.assertEqual(clasament[8].getEchipa(), "Lateral")
        self.assertEqual(clasament[9].getEchipa(), "Timisoara")
