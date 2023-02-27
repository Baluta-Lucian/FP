'''
Created on Nov 16, 2022

@author: balut
'''

import unittest
from domain.Entities import Student


class TestStudent(unittest.TestCase):
    '''
    classdocs
    '''

    def setUp(self):
        self.s1 = Student(1, "Baluta Iustinian-Lucian")
        self.s2 = Student(2, "Raduletu Petre-Horia")
        self.copy = Student(1, "Baluta Iustinian-Lucian")

    def tearDown(self):
        pass

    def test_getID(self):
        self.assertEqual(self.s1.getID(), 1)
        self.assertEqual(self.s2.getID(), 2)

    def test_setID(self):
        self.s1.setID(2)
        self.assertEqual(self.s1.getID(), 2)

    def test_setNume(self):
        self.s1.setNume("Schintee Mihai")
        self.assertEqual(self.s1.getNume(), "Schintee Mihai")

    def test_getNume(self):
        self.assertEqual(self.s1.getNume(), "Baluta Iustinian-Lucian")
        self.assertEqual(self.s2.getNume(), "Raduletu Petre-Horia")

    def test_str(self):
        self.assertEqual(
            str(self.s1), "Student{ ID: 1, Nume: Baluta Iustinian-Lucian };")
        self.assertEqual(
            str(self.s2), "Student{ ID: 2, Nume: Raduletu Petre-Horia };")

    def test_eq(self):
        self.assertEqual(self.copy == self.s1, True)
        self.assertEqual(self.s1 == self.s2, False)


from domain.Entities import Disciplina


class TestDisciplina(unittest.TestCase):
    def setUp(self):
        self.d1 = Disciplina(1, "Informatica", "Eugenia Maria-Ohota")
        self.d2 = Disciplina(2, "Chimie", "Talaba Ioan")
        self.copy = Disciplina(1, "Informatica", "Eugenia Maria-Ohota")

    def tearDown(self):
        pass

    def test_getID(self):
        self.assertEqual(self.d1.getID(), 1)
        self.assertEqual(self.d2.getID(), 2)

    def test_setID(self):
        self.d1.setID(2)
        self.assertEqual(self.d1.getID(), 2)

    def test_getDenumire(self):
        self.assertEqual(self.d1.getDenumire(), "Informatica")
        self.assertEqual(self.d2.getDenumire(), "Chimie")

    def test_setDenumire(self):
        self.d1.setDenumire("Matematica")
        self.assertEqual(self.d1.getDenumire(), "Matematica")

    def test_getProfesor(self):
        self.assertEqual(self.d1.getProfesor(), "Eugenia Maria-Ohota")
        self.assertEqual(self.d2.getProfesor(), "Talaba Ioan")

    def test_setProfesor(self):
        self.d1.setProfesor("Nanu")
        self.assertEqual(self.d1.getProfesor(), "Nanu")

    def test_str(self):
        self.assertEqual(str(
            self.d1), "Disciplina{ ID: 1, Denumire: Informatica, Profesor: Eugenia Maria-Ohota };")
        self.assertEqual(str(
            self.d2), "Disciplina{ ID: 2, Denumire: Chimie, Profesor: Talaba Ioan };")

    def test_eq(self):
        self.assertEqual(self.d1 == self.d2, False)
        self.assertEqual(self.d1 == self.copy, True)


from domain.Entities import Statistica


class TestStatistica(unittest.TestCase):
    def setUp(self):
        self.s1 = Student(1, "Baluta Iustinian-Lucian")
        self.s2 = Student(2, "Raduletu Petre-Horia")
        self.d1 = Disciplina(1, "Informatica", "Eugenia Maria-Ohota")
        self.d2 = Disciplina(2, "Chimie", "Talaba Ioan")
        self.note1 = [10, 10, 10]
        self.note2 = [8, 8, 8]
        self.stat1 = Statistica(self.s1, self.d1, self.note1)
        self.stat3 = Statistica(self.s1, self.d2, self.note2)
        self.stat2 = Statistica(self.s2, self.d1, self.note2)
        self.stat4 = Statistica(self.s2, self.d2, self.note2)
        self.copy = Statistica(self.s1, self.d1, self.note1)

    def tearDown(self):
        pass

    def test_getS(self):
        self.assertEqual(self.stat1.getS(), self.s1)
        self.assertEqual(self.stat2.getS(), self.s2)

    def test_getD(self):
        self.assertEqual(self.stat1.getD(), self.d1)
        self.assertEqual(self.stat2.getD(), self.d1)
        self.assertEqual(self.stat3.getD(), self.d2)
        self.assertEqual(self.stat4.getD(), self.d2)

    def test_getMedie(self):
        self.assertEqual(self.stat1.getMedie(), 10)
        self.assertEqual(self.stat2.getMedie(), 8)

    def test_str(self):
        self.assertEqual(str(
            self.stat1), "Student: Baluta Iustinian-Lucian; Materie: Informatica; Note: [10, 10, 10]")
        self.assertEqual(str(
            self.stat2), "Student: Raduletu Petre-Horia; Materie: Informatica; Note: [8, 8, 8]")

    def test_eq(self):
        self.assertEqual(self.stat1 == self.copy, True)
        self.assertEqual(self.stat1 == self.stat2, False)
        self.assertEqual(self.stat1 == self.stat3, False)


from domain.Entities import Situatie


# 19
class TestSituatie(unittest.TestCase):
    def setUp(self):
        self.s1 = Student(1, "Baluta Iustinian-Lucian")
        self.s2 = Student(2, "Raduletu Petre-Horia")
        self.d1 = Disciplina(1, "Informatica", "Eugenia Maria-Ohota")
        self.d2 = Disciplina(2, "Chimie", "Talaba Ioan")
        self.note1 = [10, 10, 10]
        self.note2 = [8, 8, 8]
        self.stat1 = Statistica(self.s1, self.d1, self.note1)
        self.stat3 = Statistica(self.s1, self.d2, self.note2)
        self.stat2 = Statistica(self.s2, self.d1, self.note2)
        self.stat4 = Statistica(self.s2, self.d2, self.note2)
        self.sit1 = Situatie(self.s1, self.stat1.getMedie())
        self.sit2 = Situatie(self.s2, self.stat2.getMedie())
        self.copy = Situatie(self.s1, self.stat1.getMedie())

    def tearDown(self):
        pass

    def test_getMedieGenerala(self):
        self.assertEqual(self.sit1.getMedieGenerala(), 10)
        self.assertEqual(self.sit2.getMedieGenerala(), 8)

    def test_str(self):
        self.assertEqual(
            str(self.sit1), "Student: Baluta Iustinian-Lucian; Medie: 10.0")
        self.assertEqual(
            str(self.sit2), "Student: Raduletu Petre-Horia; Medie: 8.0")

    def test_eq(self):
        self.assertEqual(self.sit1 == self.copy, True)
        self.assertEqual(self.sit1 == self.sit2, False)


from repository.memory.InMemoryRepositoryStudent import InMemoryRepositoryStudent
from errors.Exceptions import RepositoryException
# 12


class TestInMemoryRepoStudent(unittest.TestCase):
    def setUp(self):
        self.s1 = Student(1, "Baluta Iustinian-Lucian")
        self.s2 = Student(2, "Raduletu Petre-Horia")
        self.copys = Student(1, "Baluta Iustinian-Lucian")
        self.repo = InMemoryRepositoryStudent()

    def tearDown(self):
        pass

    def test_StoreExistsLen(self):
        self.assertEqual(len(self.repo.getAll()), 0)
        self.repo.store(self.s1)
        self.assertEqual(len(self.repo.getAll()), 1)
        self.repo.store(self.s2)
        self.assertEqual(len(self.repo.getAll()), 2)
        with self.assertRaises(RepositoryException):
            self.repo.store(self.copys)
            self.repo.exists(self.copys)
        self.assertEqual(len(self.repo.getAll()), 2)

    def test_findOne(self):
        self.repo.store(self.s1)
        with self.assertRaises(RepositoryException):
            self.repo.findOne(self.s2)
        self.assertEqual(self.repo.findOne(self.s1), self.s1)

    def test_delete(self):
        self.repo.store(self.s1)
        with self.assertRaises(RepositoryException):
            self.repo.delete(self.s2)
        self.assertEqual(len(self.repo.getAll()), 1)
        self.assertEqual(self.repo.delete(self.s1), self.s1)
        self.assertEqual(len(self.repo.getAll()), 0)

    def test_modify(self):
        self.repo.store(self.s1)
        with self.assertRaises(RepositoryException):
            self.repo.modify(self.s1, self.s1)
            self.repo.modify(self.s2, self.s1)
        self.repo.modify(self.s1, self.s2)
        self.assertEqual(self.repo.findOne(self.s2), self.s2)


from repository.memory.InMemoryRepositoryDiscipline import InMemoryRepositoryDiscipline


# 26
class TestInMemoryRepoDisciplie(unittest.TestCase):
    def setUp(self):
        self.d1 = Disciplina(1, "Informatica", "Eugenia Maria-Ohota")
        self.d2 = Disciplina(2, "Chimie", "Talaba Ioan")
        self.copy = Disciplina(1, "Informatica", "Eugenia Maria-Ohota")
        self.repo = InMemoryRepositoryDiscipline()

    def tearDown(self):
        pass

    def test_StoreExistsLen(self):
        self.assertEqual(len(self.repo.getAll()), 0)
        self.repo.store(self.d1)
        self.assertEqual(len(self.repo.getAll()), 1)
        self.repo.store(self.d2)
        self.assertEqual(len(self.repo.getAll()), 2)
        with self.assertRaises(RepositoryException):
            self.repo.store(self.copy)
            self.repo.exists(self.copy)
        self.assertEqual(len(self.repo.getAll()), 2)

    def test_findOne(self):
        self.repo.store(self.d1)
        with self.assertRaises(RepositoryException):
            self.repo.findOne(self.d2)
        self.assertEqual(self.repo.findOne(self.d1), self.d1)

    def test_delete(self):
        self.repo.store(self.d1)
        with self.assertRaises(RepositoryException):
            self.repo.delete(self.d2)
        self.assertEqual(len(self.repo.getAll()), 1)
        self.assertEqual(self.repo.delete(self.d1), self.d1)
        self.assertEqual(len(self.repo.getAll()), 0)

    def test_modify(self):
        self.repo.store(self.d1)
        with self.assertRaises(RepositoryException):
            self.repo.modify(self.d1, self.d1)
            self.repo.modify(self.d2, self.d1)
        self.repo.modify(self.d1, self.d2)
        self.assertEqual(self.repo.findOne(self.d2), self.d2)


from repository.memory.InMemoryRepositoryCatalog import InMemoryRepositoryCatalog

# 30


class TestInMemoryRepoCatalog(unittest.TestCase):
    def setUp(self):
        self.ss1 = Student(1, "Baluta Iustinian-Lucian")
        self.ss2 = Student(2, "Raduletu Petre-Horia")
        self.d1 = Disciplina(1, "Informatica", "Eugenia Maria-Ohota")
        self.d2 = Disciplina(2, "Chimie", "Talaba Ioan")
        self.note1 = [10, 10, 10]
        self.note2 = [8, 8, 8]
        self.s1 = Statistica(self.ss1, self.d1, self.note1)
        self.s3 = Statistica(self.ss1, self.d2, self.note2)
        self.s2 = Statistica(self.ss2, self.d1, self.note2)
        self.s4 = Statistica(self.ss2, self.d2, self.note2)
        self.copy = Statistica(self.ss1, self.d1, self.note1)
        self.repo = InMemoryRepositoryCatalog()

    def tearDown(self):
        pass

    def test_StoreExistsLen(self):
        self.assertEqual(len(self.repo.getAll()), 0)
        self.repo.store(self.s1)
        self.assertEqual(len(self.repo.getAll()), 1)
        self.repo.store(self.s2)
        self.assertEqual(len(self.repo.getAll()), 2)
        with self.assertRaises(RepositoryException):
            self.repo.store(self.copy)
            self.repo.exists(self.copy)
        self.assertEqual(len(self.repo.getAll()), 2)

    def test_findOne(self):
        self.repo.store(self.s1)
        with self.assertRaises(RepositoryException):
            self.repo.findOne(self.s2)
        self.assertEqual(self.repo.findOne(self.s1), self.s1)

    # def test_delete(self):
    #     self.repo.store(self.s1)
    #     with self.assertRaises(RepositoryException):
    #         self.repo.delete(self.s2)
    #     self.assertEqual(len(self.repo.getAll()), 1)
    #     self.assertEqual(self.repo.delete(self.s1), self.s1)
    #     self.assertEqual(len(self.repo.getAll()), 0)

    def test_deleteByStudent(self):
        self.repo.store(self.s1)
        self.repo.deleteByStudent(self.ss2)
        self.assertEqual(len(self.repo.getAll()), 1)
        self.repo.deleteByStudent(self.ss1)
        self.assertEqual(len(self.repo.getAll()), 0)

    def test_deleteByDisciplina(self):
        self.repo.store(self.s1)
        self.repo.deleteByDisciplina(self.d2)
        self.assertEqual(len(self.repo.getAll()), 1)
        self.repo.deleteByDisciplina(self.d1)
        self.assertEqual(len(self.repo.getAll()), 0)


from validation.Validator import Validator
from errors.Exceptions import ValidationException
# 34


class TestValidator(unittest.TestCase):
    def setUp(self):
        self.s1 = Student(1, "Baluta Iustinian-Lucian")
        self.s2 = Student(1, "Baluta Iustinian Lucian")
        self.s3 = Student(1, "Baluta Iustinian")
        self.s4 = Student(1, "Baluta")
        self.s1w = Student(-1, "Baluta")
        self.s2w = Student(1, "BalutA")
        self.s3w = Student(1, "Bal-uta")
        self.s4w = Student(1, "")
        self.s5w = Student(1, "Baluta iustinian")
        self.s6w = Student(1, "Baluta iustinianLucian")
        self.s7w = Student(1, "Baluta IustinianLucian")

        self.d1 = Disciplina(1, "Informatica", "Eugenia Maria-Ohota")
        self.d2 = Disciplina(2, "Info", "Eugenia Maria Ohota")
        self.d3 = Disciplina(2, "Info", "Eugenia Maria")
        self.d4 = Disciplina(2, "Info", "Eugenia")
        self.d5 = Disciplina(2, "Info", "Eugenia-Maria")
        self.d1w = Disciplina(-1, "Informatica", "Eugenia Maria-Ohota")
        self.d2w = Disciplina(1, "", "Eugenia Maria-Ohota")
        self.d3w = Disciplina(1, "", "Eugenia MariaOhota")
        self.d4w = Disciplina(1, "", "Eugenia mariaOhota")
        self.d5w = Disciplina(1, "", "Eugenia Maria-ohota")
        self.d6w = Disciplina(1, "", "EugeniA")
        self.d7w = Disciplina(1, "", "Eugeni-A")
        self.d8w = Disciplina(1, "", "eugenia")
        self.d9w = Disciplina(1, "", "64")
        self.d10w = Disciplina(1, "", "")

        self.note1 = [10, 10, 10]
        self.note2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.note1w = [0]
        self.note2w = [-1, -2]
        self.note3w = []

        self.stat1 = Statistica(self.s1, self.d1, self.note1)
        self.stat2 = Statistica(self.s1, self.d1, self.note2)

        self.stat1w = Statistica(self.s1, self.d1, self.note1w)
        self.stat2w = Statistica(self.s1w, self.d1, self.note1)
        self.stat3w = Statistica(self.s1, self.d1w, self.note1)
        self.stat4w = Statistica(self.s1w, self.d1w, self.note1)
        self.stat5w = Statistica(self.s1, self.d1w, self.note1w)
        self.stat6w = Statistica(self.s1w, self.d1w, self.note1w)
        self.stat7w = Statistica(self.s1, self.d1, self.note2w)
        self.stat8w = Statistica(self.s1, self.d1, self.note3w)

        self.val = Validator()

    def tearDown(self):
        pass

    def test_validateS(self):
        self.val.validateS(self.s1)
        self.val.validateS(self.s2)
        self.val.validateS(self.s3)
        self.val.validateS(self.s4)
        with self.assertRaises(ValidationException):
            self.val.validateS(self.s1w)
            self.val.validateS(self.s2w)
            self.val.validateS(self.s3w)
            self.val.validateS(self.s4w)
            self.val.validateS(self.s5w)
            self.val.validateS(self.s6w)
            self.val.validateS(self.s7w)

    def test_validateD(self):
        self.val.validateD(self.d1)
        self.val.validateD(self.d2)
        self.val.validateD(self.d3)
        self.val.validateD(self.d4)
        self.val.validateD(self.d5)
        with self.assertRaises(ValidationException):
            self.val.validateD(self.d1w)
            self.val.validateD(self.d2w)
            self.val.validateD(self.d3w)
            self.val.validateD(self.d4w)
            self.val.validateD(self.d5w)
            self.val.validateD(self.d6w)
            self.val.validateD(self.d7w)
            self.val.validateD(self.d8w)
            self.val.validateD(self.d9w)
            self.val.validateD(self.d10w)

    def test_validateStat(self):
        self.val.validateStat(self.stat1)
        self.val.validateStat(self.stat2)
        with self.assertRaises(ValidationException):
            self.val.validateStat(self.stat1w)
            self.val.validateStat(self.stat2w)
            self.val.validateStat(self.stat3w)
            self.val.validateStat(self.stat4w)
            self.val.validateStat(self.stat5w)
            self.val.validateStat(self.stat6w)
            self.val.validateStat(self.stat7w)
            self.val.validateStat(self.stat8w)


from service.Service import ServiceCatalog


# 37
class TestServiceCatalog(unittest.TestCase):
    def setUp(self):
        self.repoS = InMemoryRepositoryStudent()
        self.repoD = InMemoryRepositoryDiscipline()
        self.repoC = InMemoryRepositoryCatalog()
        self.val = Validator()
        self.srv = ServiceCatalog(self.repoS, self.repoD, self.repoC, self.val)

        self.__repoS1 = InMemoryRepositoryStudent()
        self.__repoD1 = InMemoryRepositoryDiscipline()
        self.__repoC1 = InMemoryRepositoryCatalog()
        self.val1 = Validator()
        self.srv1 = ServiceCatalog(
            self.__repoS1, self.__repoD1, self.__repoC1, self.val1)

        self.s1 = Student(1, "Baluta Iustinian-Lucian")
        self.s2 = Student(1, "Baluta Iustinian Lucian")
        self.s3 = Student(1, "Baluta Iustinian")
        self.s4 = Student(1, "Baluta")
        self.s1w = Student(-1, "Baluta")
        self.s2w = Student(1, "BalutA")
        self.s3w = Student(1, "Bal-uta")
        self.s4w = Student(1, "")
        self.s5w = Student(1, "Baluta iustinian")
        self.s6w = Student(1, "Baluta iustinianLucian")
        self.s7w = Student(1, "Baluta IustinianLucian")

        self.d1 = Disciplina(1, "Informatica", "Eugenia Maria-Ohota")
        self.d2 = Disciplina(2, "Info", "Eugenia Maria Ohota")
        self.d3 = Disciplina(2, "Info", "Eugenia Maria")
        self.d4 = Disciplina(2, "Info", "Eugenia")
        self.d5 = Disciplina(2, "Info", "Eugenia-Maria")
        self.d1w = Disciplina(-1, "Informatica", "Eugenia Maria-Ohota")
        self.d2w = Disciplina(1, "", "Eugenia Maria-Ohota")
        self.d3w = Disciplina(1, "", "Eugenia MariaOhota")
        self.d4w = Disciplina(1, "", "Eugenia mariaOhota")
        self.d5w = Disciplina(1, "", "Eugenia Maria-ohota")
        self.d6w = Disciplina(1, "", "EugeniA")
        self.d7w = Disciplina(1, "", "Eugeni-A")
        self.d8w = Disciplina(1, "", "eugenia")
        self.d9w = Disciplina(1, "", "64")
        self.d10w = Disciplina(1, "", "")

        self.note1 = [10, 10, 10]
        self.note2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.note1w = [0]
        self.note2w = [-1, -2]
        self.note3w = []

        self.stat1 = Statistica(self.s1, self.d1, self.note1)
        self.stat2 = Statistica(self.s1, self.d1, self.note2)

        self.stat1w = Statistica(self.s1, self.d1, self.note1w)
        self.stat2w = Statistica(self.s1w, self.d1, self.note1)
        self.stat3w = Statistica(self.s1, self.d1w, self.note1)
        self.stat4w = Statistica(self.s1w, self.d1w, self.note1)
        self.stat5w = Statistica(self.s1, self.d1w, self.note1w)
        self.stat6w = Statistica(self.s1w, self.d1w, self.note1w)
        self.stat7w = Statistica(self.s1, self.d1, self.note2w)
        self.stat8w = Statistica(self.s1, self.d1, self.note3w)

    def tearDown(self):
        pass

    def test_createStudentgetStudentiPopulate(self):
        self.assertEqual(len(self.srv.getStudenti()), 0)
        self.srv.createStudent(11, "Matei")
        self.assertEqual(len(self.srv.getStudenti()), 1)
        self.srv.createStudent(12, "Andrei")
        self.assertEqual(len(self.srv.getStudenti()), 2)
        self.srv.populate()
        self.assertEqual(len(self.srv.getStudenti()), 12)

        with self.assertRaises(RepositoryException):
            self.srv.createStudent(1, "Baluta Iustinian-Lucian")
            self.srv.createStudent(11, "Matei")

        with self.assertRaises(ValidationException):
            self.srv.createStudent(13, "BalUta")
            self.srv.createStudent(-1, "EuG Eni-a")

    def test_createDisciplinagetDisciplinePopulate(self):
        self.assertEqual(len(self.srv.getDiscipline()), 0)
        self.srv.createDisciplina(11, "Informatica", "Runceanu")
        self.assertEqual(len(self.srv.getDiscipline()), 1)
        self.srv.createDisciplina(12, "Info", "Ghebe")
        self.assertEqual(len(self.srv.getDiscipline()), 2)
        self.srv.populate()
        self.assertEqual(len(self.srv.getDiscipline()), 12)

        with self.assertRaises(RepositoryException):
            self.srv.createDisciplina(12, "Info", "Raul")
            self.srv.createDisciplina(1, "Informatica", "Eugenia Maria-Ohota")

        with self.assertRaises(ValidationException):
            self.srv.createDisciplina(13, "", "Eugenia")
            self.srv.createDisciplina(-1, "Info", "Eugenia")
            self.srv.createDisciplina(13, "Info", "EugeniaMaria")

    def test_createStatisticagetCatalogPopulate(self):
        self.assertEqual(len(self.srv.getCatalog()), 0)
        self.srv.createStudent(11, "Matei")
        self.srv.createStudent(12, "Andrei")
        self.srv.createStudent(30, "Baluta")
        self.srv.createDisciplina(11, "Informatica", "Runceanu")
        self.srv.createDisciplina(12, "Info", "Ghebe")
        self.srv.createStatistica(11, "Matei", 12, "Info", "Ghebe", [10, 10])
        self.assertEqual(len(self.srv.getCatalog()), 1)
        self.srv.createStatistica(
            11, "Matei", 11, "Informatica", "Runceanu", [9, 9, 9])
        self.assertEqual(len(self.srv.getCatalog()), 2)
        self.srv.populate()
        self.assertEqual(len(self.srv.getCatalog()), 12)

        with self.assertRaises(RepositoryException):
            self.srv.createStatistica(0, "Ana", 4, "Info", "Eugenia", [2, 2])
            self.srv.createStatistica(
                11, "Matei", 0, "Info", "Maria", [10, 10])

        self.srv.createStatistica(
            30, "Baluta", 11, "Informatica", "Runceanu", [10, 10])
        self.assertEqual(len(self.srv.getCatalog()), 13)

        with self.assertRaises(ValidationException):
            self.srv.createStatistica(-1, "Baluta",
                                      11, "Informatica", "Runceanu", [10, 10])
            self.srv.createStatistica(
                30, "BalutaA", 11, "Informatica", "Runceanu", [10, 10])
            self.srv.createStatistica(
                30, "Baluta", -1, "Informatica", "Runceanu", [10, 10])
            self.srv.createStatistica(
                30, "Baluta", 11, "", "Runceanu", [10, 10])
            self.srv.createStatistica(
                30, "Baluta", 11, "Informatica", "RunceanuA", [10, 10])
            self.srv.createStatistica(
                30, "Baluta", 11, "Informatica", "Runceanu", [-1, 0])
            self.srv.createStatistica(
                30, "Baluta", 11, "Informatica", "Runceanu", [-1, 0])
            self.srv.createStatistica(
                30, "Baluta", 11, "Informatica", "Runceanu", [])

    def test_deleteStudent(self):
        self.assertEqual(len(self.srv.getStudenti()), 0)
        self.srv.populate()
        self.assertEqual(len(self.srv.getStudenti()), 10)
        self.assertEqual(self.srv.deleteStudent(
            1, "Baluta Iustinian-Lucian"), self.s1)
        self.assertEqual(len(self.srv.getStudenti()), 9)

        with self.assertRaises(RepositoryException):
            self.srv.deleteStudent(1, "Baluta Iustinian-Lucian")

    def test_deleteDisciplina(self):
        self.assertEqual(len(self.srv.getDiscipline()), 0)
        self.srv.populate()
        self.assertEqual(len(self.srv.getDiscipline()), 10)
        self.assertEqual(self.srv.deleteDisciplina(
            1, "Informatica", "Eugenia Maria-Ohota"), self.d1)
        self.assertEqual(len(self.srv.getDiscipline()), 9)

        with self.assertRaises(RepositoryException):
            self.srv.deleteDisciplina(1, "Informatica", "Eugenia Maria-Ohota")

    def test_setStudentFindStudent(self):
        self.assertEqual(len(self.srv.getStudenti()), 0)
        self.srv.populate()
        self.assertEqual(len(self.srv.getStudenti()), 10)
        self.srv.setStudent(1, "Baluta Iustinian-Lucian", 20, "Baluta")
        self.assertEqual(len(self.srv.getStudenti()), 10)
        self.assertEqual(self.srv.findStudent(
            20, "Baluta"), Student(20, "Baluta"))

        with self.assertRaises(RepositoryException):
            self.srv.setStudent(0, "Baluta", 20, "Baluta")
            self.srv.setStudent(20, "Baluta", 20, "Baluta")
            self.srv.setStudent(20, "Baluta", 20, "Baluta Iustinian-Lucian")

        with self.assertRaises(ValidationException):
            self.srv.setStudent(20, "Baluta", -1, "Baluta Iustinian-Lucian")
            self.srv.setStudent(20, "Baluta", 1, "BalutaA")

    def test_setDisciplina(self):
        self.assertEqual(len(self.srv.getDiscipline()), 0)
        self.srv.populate()
        self.assertEqual(len(self.srv.getDiscipline()), 10)
        self.srv.setDisciplina(
            1, "Informatica", "Eugenia Maria-Ohota", 20, "Info", "Eugenia")
        self.assertEqual(self.srv.findDisciplina(
            20, "Info", "Eugenia"), Disciplina(20, "Info", "Eugenia"))

        with self.assertRaises(RepositoryException):
            self.srv.setDisciplina(0, "Info", "Eugenia", 20, "Info", "Eugenia")
            self.srv.setDisciplina(20, "Info", "Eugenia",
                                   20, "Info", "Eugenia")
            self.srv.setDisciplina(20, "Info", "Eugenia",
                                   20, "Info", "Eugenia Maria")
            self.srv.setDisciplina(20, "Info", "Eugenia",
                                   20, "Informatica", "Eugenia")

        with self.assertRaises(ValidationException):
            self.srv.setDisciplina(
                20, "Info", "Eugenia", -1, "Informatica", "Eugenia Maria")
            self.srv.setDisciplina(20, "Info", "Eugenia",
                                   1, "", "Eugenia Maria")
            self.srv.setDisciplina(20, "Info", "Eugenia",
                                   1, "Informatica", "EugeniaMaria")
            self.srv.setDisciplina(20, "Info", "Eugenia",
                                   1, "Informatica", "EugeniaA Maria")
            self.srv.setDisciplina(20, "Info", "Eugenia", 1, "Informatica", "")

    def test_StatsStudentiNote(self):
        self.__repoS1.store(Student(1, "Baluta Iustinian-Lucian"))
        self.__repoS1.store(Student(2, "Raduletu Petre-Horia"))
        self.__repoS1.store(Student(3, "Tunseanu Sorin-Calin"))
        self.__repoS1.store(Student(4, "Schintee Mihai"))
        self.__repoS1.store(Student(5, "Pane Raul"))
        self.__repoS1.store(Student(6, "Hortopan Marius"))
        self.__repoS1.store(Student(7, "Dragulescu Ariana"))
        self.__repoS1.store(Student(8, "Ianc Andreea"))
        self.__repoS1.store(Student(9, "Papulete Daniela"))
        self.__repoS1.store(Student(10, "Clenciu Andreea"))
        # Adaugare Discipline
        self.__repoD1.store(Disciplina(
            1, "Informatica", "Eugenia Maria-Ohota"))
        self.__repoD1.store(Disciplina(2, "Matematica", "Nanu"))
        self.__repoD1.store(Disciplina(3, "Chimie", "Talaba Ioan"))
        self.__repoD1.store(Disciplina(4, "Biologie", "Neguleasa Carmen"))
        self.__repoD1.store(Disciplina(5, "Muzica", "Secara"))
        self.__repoD1.store(Disciplina(6, "Desen", "Plaveti"))
        self.__repoD1.store(Disciplina(7, "Fizica", "Sfantu Toma"))
        self.__repoD1.store(Disciplina(8, "Istorie", "Fosila"))
        self.__repoD1.store(Disciplina(9, "Romana", "Nisu"))
        self.__repoD1.store(Disciplina(10, "Engleza", "Sefter"))
        # Adaugare Stats
        s1 = Student(1, "Baluta Iustinian-Lucian")
        s2 = Student(2, "Raduletu Petre-Horia")
        s3 = Student(3, "Tunseanu Sorin-Calin")
        s4 = Student(4, "Schintee Mihai")
        s5 = Student(5, "Pane Raul")
        s6 = Student(6, "Hortopan Marius")
        s7 = Student(7, "Dragulescu Ariana")
        s8 = Student(8, "Ianc Andreea")
        s9 = Student(9, "Papulete Daniela")
        s10 = Student(10, "Clenciu Andreea")

        d1 = Disciplina(1, "Informatica", "Eugenia Maria-Ohota")
        d2 = Disciplina(2, "Matematica", "Nanu")
        d3 = Disciplina(3, "Chimie", "Talaba Ioan")
        d4 = Disciplina(4, "Biologie", "Neguleasa Carmen")
        d5 = Disciplina(5, "Muzica", "Secara")
        d6 = Disciplina(6, "Desen", "Plaveti")
        d7 = Disciplina(7, "Fizica", "Sfantu Toma")
        d8 = Disciplina(8, "Istorie", "Fosila")
        d9 = Disciplina(9, "Romana", "Nisu")
        d10 = Disciplina(10, "Engleza", "Sefter")

        note1 = [10, 10, 10]
        note2 = [10, 10, 9]
        note3 = [9, 8, 9]
        note4 = [8, 9, 8]
        note5 = [5, 7, 6]
        note6 = [5, 6, 5]
        note7 = [7, 7, 7]
        note8 = [8, 8, 10]
        note9 = [6, 10, 9]
        note10 = [4, 7, 7]

        stat1 = Statistica(s1, d1, note1)
        stat2 = Statistica(s2, d1, note2)
        stat3 = Statistica(s3, d1, note3)
        stat4 = Statistica(s4, d1, note4)
        stat5 = Statistica(s5, d1, note5)
        stat6 = Statistica(s6, d1, note6)
        stat7 = Statistica(s7, d1, note7)
        stat8 = Statistica(s8, d1, note8)
        stat9 = Statistica(s9, d1, note9)
        stat10 = Statistica(s10, d1, note10)

        self.__repoC1.store(stat1)
        self.__repoC1.store(stat2)
        self.__repoC1.store(stat3)
        self.__repoC1.store(stat4)
        self.__repoC1.store(stat5)
        self.__repoC1.store(stat6)
        self.__repoC1.store(stat7)
        self.__repoC1.store(stat8)
        self.__repoC1.store(stat9)
        self.__repoC1.store(stat10)

        with self.assertRaises(ValidationException):
            self.srv1.StatsStudentiNote(13, "", "Eugenia")
            self.srv1.StatsStudentiNote(-1, "Info", "Eugenia")
            self.srv1.StatsStudentiNote(13, "Info", "EugeniaMaria")
        listResult = self.srv1.StatsStudentiNote(
            1, "Informatica", "Eugenia Maria-Ohota")
        self.assertEqual(listResult[0].getS(), s6)
        self.assertEqual(listResult[1].getS(), s5)
        self.assertEqual(listResult[2].getS(), s10)
        self.assertEqual(listResult[3].getS(), s7)
        self.assertEqual(listResult[4].getS(), s4)
        self.assertEqual(listResult[5].getS(), s9)
        self.assertEqual(listResult[6].getS(), s3)
        self.assertEqual(listResult[7].getS(), s8)
        self.assertEqual(listResult[8].getS(), s2)
        self.assertEqual(listResult[9].getS(), s1)

    def test_StatsStudentiNume(self):
        self.__repoS1.store(Student(1, "Baluta Iustinian-Lucian"))
        self.__repoS1.store(Student(2, "Raduletu Petre-Horia"))
        self.__repoS1.store(Student(3, "Tunseanu Sorin-Calin"))
        self.__repoS1.store(Student(4, "Schintee Mihai"))
        self.__repoS1.store(Student(5, "Pane Raul"))
        self.__repoS1.store(Student(6, "Hortopan Marius"))
        self.__repoS1.store(Student(7, "Dragulescu Ariana"))
        self.__repoS1.store(Student(8, "Ianc Andreea"))
        self.__repoS1.store(Student(9, "Papulete Daniela"))
        self.__repoS1.store(Student(10, "Clenciu Andreea"))
        # Adaugare Discipline
        self.__repoD1.store(Disciplina(
            1, "Informatica", "Eugenia Maria-Ohota"))
        self.__repoD1.store(Disciplina(2, "Matematica", "Nanu"))
        self.__repoD1.store(Disciplina(3, "Chimie", "Talaba Ioan"))
        self.__repoD1.store(Disciplina(4, "Biologie", "Neguleasa Carmen"))
        self.__repoD1.store(Disciplina(5, "Muzica", "Secara"))
        self.__repoD1.store(Disciplina(6, "Desen", "Plaveti"))
        self.__repoD1.store(Disciplina(7, "Fizica", "Sfantu Toma"))
        self.__repoD1.store(Disciplina(8, "Istorie", "Fosila"))
        self.__repoD1.store(Disciplina(9, "Romana", "Nisu"))
        self.__repoD1.store(Disciplina(10, "Engleza", "Sefter"))
        # Adaugare Stats
        s1 = Student(1, "Baluta Iustinian-Lucian")
        s2 = Student(2, "Raduletu Petre-Horia")
        s3 = Student(3, "Tunseanu Sorin-Calin")
        s4 = Student(4, "Schintee Mihai")
        s5 = Student(5, "Pane Raul")
        s6 = Student(6, "Hortopan Marius")
        s7 = Student(7, "Dragulescu Ariana")
        s8 = Student(8, "Ianc Andreea")
        s9 = Student(9, "Papulete Daniela")
        s10 = Student(10, "Clenciu Andreea")

        d1 = Disciplina(1, "Informatica", "Eugenia Maria-Ohota")
        d2 = Disciplina(2, "Matematica", "Nanu")
        d3 = Disciplina(3, "Chimie", "Talaba Ioan")
        d4 = Disciplina(4, "Biologie", "Neguleasa Carmen")
        d5 = Disciplina(5, "Muzica", "Secara")
        d6 = Disciplina(6, "Desen", "Plaveti")
        d7 = Disciplina(7, "Fizica", "Sfantu Toma")
        d8 = Disciplina(8, "Istorie", "Fosila")
        d9 = Disciplina(9, "Romana", "Nisu")
        d10 = Disciplina(10, "Engleza", "Sefter")

        note1 = [10, 10, 10]
        note2 = [10, 10, 9]
        note3 = [9, 8, 9]
        note4 = [8, 9, 8]
        note5 = [5, 7, 6]
        note6 = [5, 6, 5]
        note7 = [7, 7, 7]
        note8 = [8, 8, 10]
        note9 = [6, 10, 9]
        note10 = [4, 7, 7]

        stat1 = Statistica(s1, d1, note1)
        stat2 = Statistica(s2, d1, note2)
        stat3 = Statistica(s3, d1, note3)
        stat4 = Statistica(s4, d1, note4)
        stat5 = Statistica(s5, d1, note5)
        stat6 = Statistica(s6, d1, note6)
        stat7 = Statistica(s7, d1, note7)
        stat8 = Statistica(s8, d1, note8)
        stat9 = Statistica(s9, d1, note9)
        stat10 = Statistica(s10, d1, note10)

        self.__repoC1.store(stat1)
        self.__repoC1.store(stat2)
        self.__repoC1.store(stat3)
        self.__repoC1.store(stat4)
        self.__repoC1.store(stat5)
        self.__repoC1.store(stat6)
        self.__repoC1.store(stat7)
        self.__repoC1.store(stat8)
        self.__repoC1.store(stat9)
        self.__repoC1.store(stat10)

        with self.assertRaises(ValidationException):
            self.srv1.StatsStudentiNote(13, "", "Eugenia")
            self.srv1.StatsStudentiNote(-1, "Info", "Eugenia")
            self.srv1.StatsStudentiNote(13, "Info", "EugeniaMaria")
        listResult = self.srv1.StatsStudentiNume(
            1, "Informatica", "Eugenia Maria-Ohota")
        self.assertEqual(listResult[0].getS(), s1)
        self.assertEqual(listResult[1].getS(), s10)
        self.assertEqual(listResult[2].getS(), s7)
        self.assertEqual(listResult[3].getS(), s6)
        self.assertEqual(listResult[4].getS(), s8)
        self.assertEqual(listResult[5].getS(), s5)
        self.assertEqual(listResult[6].getS(), s9)
        self.assertEqual(listResult[7].getS(), s2)
        self.assertEqual(listResult[8].getS(), s4)
        self.assertEqual(listResult[9].getS(), s3)

    def test_Stats20(self):
        self.assertEqual(len(self.srv.getCatalog()), 0)
        self.srv.populate()
        self.assertEqual(len(self.srv.getCatalog()), 10)
        self.assertEqual(len(self.srv.Stats20()), 2)

    def test_randomGenerator(self):
        self.assertEqual(len(self.srv.getStudenti()), 0)
        self.assertEqual(len(self.srv.getDiscipline()), 0)
        self.srv.randomGenerator(30)
        self.assertEqual(len(self.srv.getStudenti()), 30)
        self.assertEqual(len(self.srv.getDiscipline()), 30)
        self.srv.randomGenerator(20)
        self.assertEqual(len(self.srv.getStudenti()), 50)
        self.assertEqual(len(self.srv.getDiscipline()), 50)
