'''
Created on Feb 23, 2023

@author: balut
'''
import unittest
from domain.Jucator import Jucator
from repository.RepositoryFileJucatori import RepositoryJucatori
from errors.Exception import RepositoryException, ValidationException
from validator.Validator import Validator
from service.Service import Service


class TestDomain(unittest.TestCase):

    def setUp(self):
        self.j = Jucator("Baluta", "Iustinian", 180, "Fundas")

    def testGetters(self):
        self.assertEqual(self.j.get_nume(), "Baluta")
        self.assertEqual(self.j.get_prenume(), "Iustinian")
        self.assertEqual(self.j.get_inaltime(), 180)
        self.assertEqual(self.j.get_post(), "Fundas")

    def testSetters(self):
        self.j.set_inaltime(160)
        self.assertEqual(self.j.get_inaltime(), 160)

    def tearDown(self):
        pass


class TestRepositoryServiceValidator(unittest.TestCase):
    def setUp(self):
        self.repoTest = RepositoryJucatori("test.txt")
        self.iSize = len(self.repoTest.getAll())
        self.val = Validator()
        self.srv = Service(self.repoTest, self.val)

    def testGetSaveModifyEchipa(self):
        # test Echipa
        echipa = self.srv.echipaMax()
        self.assertEqual(echipa[0].get_nume(), "Nikolic")
        self.assertEqual(echipa[1].get_nume(), "Graham")
        self.assertEqual(echipa[2].get_nume(), "Dragusin")
        self.assertEqual(echipa[3].get_nume(), "Navickas")
        self.assertEqual(echipa[4].get_nume(), "Dumitrescu")

        # Teste Repo
        self.assertEqual(len(self.repoTest.getAll()), self.iSize)
        self.repoTest.save(Jucator("Mihai", "Schintee", 190, "Fundas"))
        currentSize = self.iSize + 1
        self.assertEqual(len(self.repoTest.getAll()), currentSize)
        with self.assertRaises(RepositoryException):
            self.repoTest.save(Jucator("Mihai", "Schintee", 200, "Fundas"))
        self.assertEqual(len(self.repoTest.getAll()), currentSize)
        jucator = Jucator("Mihai", "Schintee", 190, "Fundas")
        self.repoTest.modifyByH(10)
        self.assertEqual(self.repoTest.getAll()[
                         currentSize - 1].get_inaltime(), jucator.get_inaltime() + 10)

        # Teste Service + Validator
        self.assertEqual(len(self.srv.getAllJucatori()), currentSize)
        self.srv.modificaInaltime(10)
        self.assertEqual(self.srv.getAllJucatori()[
                         currentSize - 1].get_inaltime(), jucator.get_inaltime() + 20)
        # testSave
        self.srv.addJucator("Horia", "Raduletu", 160, "Fundas")
        currentSize = currentSize + 1
        self.assertEqual(len(self.srv.getAllJucatori()), currentSize)
        # testValidator
        with self.assertRaises(ValidationException):
            self.srv.addJucator("Horia", "Raduletu", 130, "Fundas")
            self.srv.addJucator("", "Raduletu", 150, "Fundas")
            self.srv.addJucator("Horia", "", 150, "Fundas")
            self.srv.addJucator("Horia", "Raduletu", 150, "ROL")
        with self.assertRaises(RepositoryException):
            self.srv.addJucator("Horia", "Raduletu", 160, "Fundas")

    def tearDown(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
