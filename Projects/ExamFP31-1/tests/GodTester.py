'''
Created on Jan 31, 2023

@author: balut
'''
import unittest
from domain.Entities import Spectacol
from repository.RepositoryInFileSpectacole import RepositorySpectacol
from errors.Exceptions import RepositeroryError, ValidationError
from validators.Validator import ValidatorSpectacol
from service.Service import ServiceSpectacole


class TestDomain(unittest.TestCase):

    def setUp(self):
        self.s1 = Spectacol("T1", "S1", "Concert", 1200)
        self.s2 = Spectacol("T2", "S2", "Concert", 1200)
        self.s1_copy = Spectacol("T1", "S1", "Concert", 1200)

    def testName(self):
        self.assertEqual(self.s1.getTitlu(), "T1")
        self.assertEqual(self.s1.getArtist(), "S1")
        self.assertEqual(self.s1.getGen(), "Concert")
        self.assertEqual(self.s1.getDurata(), 1200)
        self.assertEqual(self.s1, self.s1_copy)
        self.s1.setDurata(1000)
        self.s1.setGen("Altele")
        self.assertEqual(self.s1.getGen(), "Altele")
        self.assertEqual(self.s1.getDurata(), 1000)

    def tearDown(self):
        pass


class TestRepository(unittest.TestCase):
    def setUp(self):
        self.repo = RepositorySpectacol("uniTest.txt")

    def testLoadFromFile(self):
        self.assertEqual(len(self.repo.getAll()), 5)

    def testStoreModifySaveToFile(self):
        s1 = Spectacol("T1", "S1", "Concert", 1500)
        self.repo.store(s1)
        self.assertEqual(len(self.repo.getAll()), 6)
        self.repo.modify(Spectacol("T1", "S1", "Altele", 1000))
        s_modify = self.repo.findOne(Spectacol("T1", "S1", "Altele", 1000))
        self.assertEqual(s1, s_modify)
        self.assertEqual(s_modify.getDurata(), 1000)
        self.assertEqual(s_modify.getGen(), "Altele")
        with self.assertRaises(RepositeroryError):
            self.repo.findOne(Spectacol("t1", "a1", "Concert", 100))
            self.repo.findOne(Spectacol("t1", "a1", "Concert", 1000))
            self.repo.findOne(Spectacol("t1", "s1", "Altele", 1000))
            self.repo.findOne(Spectacol("t1", "S1", "Altele", 1000))
            self.repo.findOne(Spectacol("T1", "s1", "Altele", 1000))
            self.repo.modify(Spectacol("t1", "a1", "Concert", 100))
            self.repo.modify(Spectacol("t1", "s1", "Concert", 100))
            self.repo.modify(Spectacol("T1", "s1", "Concert", 100))
            self.repo.modify(Spectacol("t1", "S1", "Concert", 100))
        self.Curatare()

    def Curatare(self):
        with open("uniTest.txt", "w") as f:
            l = self.repo.getAll()
            for i in range(0, 5):
                sfile = ""
                sfile += l[i].getTitlu() + ";" + l[i].getArtist() + ";" + \
                    l[i].getGen() + ";" + str(l[i].getDurata()) + "\n"
                f.write(sfile)
            f.close()

    def tearDown(self):
        pass


class TestService(unittest.TestCase):
    def setUp(self):
        self.repo = RepositorySpectacol("uniTest.txt")
        self.val = ValidatorSpectacol()
        self.srv = ServiceSpectacole(self.repo, self.val)

    def testAddModifyGetSpectacol(self):
        self.assertEqual(len(self.repo.getAll()), 5)
        self.srv.addSpectacol("T1", "S30", "Comedie", 100)
        self.assertEqual(len(self.repo.getAll()), 6)
        with self.assertRaises(ValidationError):
            self.srv.addSpectacol("", "", "ADS", -1)
            self.srv.modifySpectacol("", "", "ADS", -1)
            self.srv.addSpectacol("T1", "", "ADS", -1)
            self.srv.modifySpectacol("T1", "", "ADS", -1)
            self.srv.addSpectacol("T1", "S1", "ADS", -1)
            self.srv.modifySpectacol("T1", "S1", "ADS", -1)
            self.srv.addSpectacol("T1", "S1", "Comedie", -1)
            self.srv.modifySpectacol("T1", "S1", "Comedie", -1)
            self.srv.addSpectacol("", "S1", "Comedie", 1)
            self.srv.modifySpectacol("", "S1", "Comedie", 1)
            self.srv.addSpectacol("T1", "", "Comedie", 1)
            self.srv.modifySpectacol("T1", "", "Comedie", 1)
            self.srv.addSpectacol("T1", "S1", "ASSD", 1)
            self.srv.modifySpectacol("T1", "S1", "ASSD", 1)
            self.srv.addSpectacol("T1", "S1", "Comedie", -301)
            self.srv.modifySpectacol("T1", "S1", "Comedie", -301)
        self.srv.modifySpectacol("T1", "S30", "Altele", 30000)
        with self.assertRaises(RepositeroryError):
            self.srv.modifySpectacol("t1", "S30", "Comedie", 1)
            self.srv.modifySpectacol("T1", "s30", "Comedie", 1)
        self.Curatare()

    def testExportSortSpectacole(self):
        self.srv.exportSpectacole("uniTestExport.txt")

    def Curatare(self):
        with open("uniTest.txt", "w") as f:
            l = self.repo.getAll()
            for i in range(0, 5):
                sfile = ""
                sfile += l[i].getTitlu() + ";" + l[i].getArtist() + ";" + \
                    l[i].getGen() + ";" + str(l[i].getDurata()) + "\n"
                f.write(sfile)
            f.close()

    def tearDown(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
