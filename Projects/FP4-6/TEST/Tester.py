'''
Created on Oct 27, 2022

@author: balut
'''

from SERVICE.Service import Service
from DOMAIN.entities import ComplexNumber
from REPOSITORY.Repository import Repository
from VALIDATION.Validator import Validator
from UI.UI import Console
from Utility.Functions import Helpers
from pickle import TRUE, FALSE


class GodTester(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''

    def allPrint(self, l):
        '''
        Functie care printeaza o lista de numere complexe
        :param l:
        '''
        if len(l) == 0:
            print("List is empty!")
        else:
            print("\nStart of list: ")
            for i in l:
                print(i)
            print("End of list!")

##########################################################################
    def TestAll(self):
        self.TestEntities()
        self.TestRepository()
        self.TestValidator()
        self.TestHelpers()
        self.TestService()


##########################################################################
    def TestService(self):
        '''
        searchRange

        '''
        testRepo = Repository()
        testHelper = Helpers()
        testVal = Validator()
        testServ = Service(testRepo, testVal, testHelper)
        ######AddServiceTests######
        try:
            cn1 = testServ.createComplexNumber(30, 20)
            assert(cn1 == ComplexNumber(30, 20))
        except ValueError:
            raise ValueError

        try:
            cn2 = testServ.createComplexNumber(30.10, 20)
            assert(True)
        except ValueError as ve:
            assert(str(ve) == "!!!The real part can only be integer!!!\n")

        try:
            cn3 = testServ.createComplexNumber(30.10, 20.14)
            assert(True)
        except ValueError as ve:
            assert(str(
                ve) == "!!!The real part can only be integer!!!\n!!!The imaginary part can only be integer!!!")
        #######GetListTests########
        assert(len(testServ.getList()) == 1)
        #######FilterPrim##########
        assert(len(testServ.filterPrim()) == 0)
        testServ.createComplexNumber(11, 20)
        assert(len(testServ.filterPrim()) == 1)
        #######FilterModule##########
        assert(len(testServ.filterModul("=", 10)) == 2)
        assert(len(testServ.filterModul(">", 30)) == 1)
        assert(len(testServ.filterModul("<", 30)) == 1)
        assert(len(testServ.filterModul("<", 1000)) == 0)
        #######searchModuleLess######
        assert(len(testServ.searchModuleLess()) == 0)
        testServ.createComplexNumber(2, 3)
        assert(len(testServ.searchModuleLess()) == 1)
        #######searchModuleEq########
        assert(len(testServ.searchModuleEq()) == 0)
        testServ.createComplexNumber(10, 1)
        assert(len(testServ.searchModuleEq()) == 1)
        #######populateList##########
        assert(len(testServ.getList()) == 4)
        testServ.populateList()
        assert(len(testServ.getList()) == 20)
        #######modifyIndex###########
        assert(ComplexNumber(30, 40) == testServ.modifyIndex(4))
        assert(len(testServ.getList()) == 19)
        try:
            testServ.modifyIndex(200)
            assert(False)
        except ValueError as ve:
            assert(str(ve) == "!!!Index out of range!!!")
        #########AddIndex############
        testServ.createNumberOnIndex(30, 40, 19)
        assert(len(testServ.getList()) == 20)
        try:
            testServ.createNumberOnIndex(40, 50, 3214)
            assert(False)
        except ValueError as ve:
            assert(str(ve) == "!!!Index out of range!!!")
        #########ModifyRange##########
        assert(len(testServ.modifyRange(0, 2)) == 3)
        try:
            testServ.modifyRange(200, 300)
            assert(False)
        except ValueError as ve:
            assert(str(ve) == "!!!Start and Stop index out of range!!!")
        try:
            testServ.modifyRange(0, 300)
            assert(False)
        except ValueError as ve:
            assert(str(ve) == "!!!Stop index out of range!!!")
        try:
            testServ.modifyRange(-200, 3)
            assert(False)
        except ValueError as ve:
            assert(str(ve) == "!!!Start index out of range!!!")
        ###########MoifyAllUnique#####
        # self.allPrint(testServ.getList())
        cn = ComplexNumber(10, 1)
        ot = ComplexNumber(11, 1)
        assert(testServ.modifyAllUnique(10, 1, 11, 1) == 2)
        try:
            testRepo.setAllUnique(cn, ot)
            assert(False)
        except ValueError as ve:
            assert(str(ve) == "!!!Numarul complex ales nu exista in lista!!!")
        ############GetListRange######
        assert(len(testServ.getListRange(0, 0)) == 1)
        try:
            testServ.getListRange(200, 300)
            assert(False)
        except ValueError as ve:
            assert(str(ve) == "!!!Start and Stop index out of range!!!")
        try:
            testServ.getListRange(0, 300)
            assert(False)
        except ValueError as ve:
            assert(str(ve) == "!!!Stop index out of range!!!")
        try:
            testServ.getListRange(-200, 3)
            assert(False)
        except ValueError as ve:
            assert(str(ve) == "!!!Start index out of range!!!")
        ############searchRange########
        assert(len(testServ.searchRange(0, 0)) == 1)
        try:
            testServ.searchRange(200, 300)
            assert(False)
        except ValueError as ve:
            assert(str(ve) == "!!!Start and Stop index out of range!!!")
        try:
            testServ.searchRange(0, 300)
            assert(False)
        except ValueError as ve:
            assert(str(ve) == "!!!Stop index out of range!!!")
        try:
            testServ.searchRange(-200, 3)
            assert(False)
        except ValueError as ve:
            assert(str(ve) == "!!!Start index out of range!!!")
        ##########opSum#################
        cn = testServ.opSum(0, 0)
        assert(cn.getReal() == 11)
        assert(cn.getImaginar() == 1)
        cn = testServ.opSum(0, 4)
        assert(cn.getReal() == 56)
        assert(cn.getImaginar() == -22)
        ##########opMulty###############
        cn = testServ.opMulti(0, 0)
        assert(cn.getReal() == 11)
        assert(cn.getImaginar() == 1)
        cn = testServ.opMulti(0, 1)
        assert(cn.getReal() == -90)
        assert(cn.getImaginar() == -230)
        #(11 + 1i)(-10 - 20i) = -110 - 10i -220i +20 = -90 -230i
        ###########opSort###############
        nr = len(testServ.getList())
        nr = nr - 1
        testServ.modifyRange(0, nr)
        testServ.createComplexNumber(-10, -20)
        testServ.createComplexNumber(11, 1)
        testServ.createComplexNumber(10, 20)
        local = testServ.opSort()
        cn1 = local[0]
        cn2 = local[1]
        cn3 = local[2]
        assert(cn1 == ComplexNumber(10, 20))
        assert(cn2 == ComplexNumber(11, 1))
        assert(cn3 == ComplexNumber(-10, -20))


##########################################################################

    def TestEntities(self):
        cn1 = ComplexNumber(30, -20)
        cn2 = ComplexNumber(-10, 20)
        cn3 = ComplexNumber(-10, 20)
        #######GetRealTests########
        assert(cn1.getReal() == 30)
        assert(cn2.getReal() == -10)
        assert(cn3.getReal() == -10)
        #######GetImaginarTests####
        assert(cn1.getImaginar() == -20)
        assert(cn2.getImaginar() == 20)
        assert(cn3.getImaginar() == 20)
        #######SetRealTests########
        cn1.setReal(40)
        cn2.setReal(-15)
        cn3.setReal(-15)
        assert(cn1.getReal() == 40)
        assert(cn2.getReal() == -15)
        assert(cn3.getReal() == -15)
        #######SetImaginarTests####
        cn1.setImaginar(-30)
        cn2.setImaginar(11)
        cn3.setImaginar(11)
        assert(cn1.getImaginar() == -30)
        assert(cn2.getImaginar() == 11)
        assert(cn3.getImaginar() == 11)
        #######EqTests#############
        assert((cn1 == cn2) == False)
        assert((cn2 == cn3) == True)
        #######StrTests############
        assert(str(cn1) == "40 - 30i")
        assert(str(cn3) == "-15 + 11i")


##########################################################################
    def TestRepository(self):
        ########INITIALIZE#########
        testRepo = Repository()
        cn1 = ComplexNumber(30, -20)
        cn2 = ComplexNumber(-10, 20)
        cn3 = ComplexNumber(-10, 20)
        ########AddTests###########
        assert(len(testRepo.getAll()) == 0)
        testRepo.store(cn1)
        assert(len(testRepo.getAll()) == 1)
        testRepo.store(cn2)
        testRepo.store(cn3)
        assert(len(testRepo.getAll()) == 3)
        #########indexAdd##########
        testRepo.indexStore(ComplexNumber(10, 20), 2)
        assert(len(testRepo.getAll()) == 4)
        Lcopy = testRepo.getAll()
        assert(Lcopy[2] == ComplexNumber(10, 20))
        try:
            testRepo.indexStore(ComplexNumber(10, 20), 70)
            assert(True)
        except ValueError as ve:
            assert(str(ve) == "!!!Index out of range!!!")
        #########indexDelete########
        cn = Lcopy[2]
        assert(cn == testRepo.indexDelete(2))
        assert(len(testRepo.getAll()) == 3)
        try:
            testRepo.indexDelete(70)
            assert(False)
        except ValueError as ve:
            assert(str(ve) == "!!!Index out of range!!!")
        ########rangeDelete#########
        assert(len(testRepo.rangeDelete(0, 0)) == 1)
        assert(len(testRepo.getAll()) == 2)
        try:
            testRepo.rangeDelete(4, 7)
            assert(False)
        except ValueError as ve:
            assert(str(ve) == "!!!Start and Stop index out of range!!!")
        try:
            testRepo.rangeDelete(0, 5)
            assert(False)
        except ValueError as ve:
            assert(str(ve) == "!!!Stop index out of range!!!")
        try:
            testRepo.rangeDelete(-1, 1)
            assert(False)
        except ValueError as ve:
            assert(str(ve) == "!!!Start index out of range!!!")
        #########allUniqueModify#####
        cn = ComplexNumber(-10, 20)
        ot = ComplexNumber(11, 11)
        assert(testRepo.setAllUnique(cn, ot) == 2)
        try:
            testRepo.setAllUnique(cn, ot)
            assert(False)
        except ValueError as ve:
            assert(str(ve) == "!!!Numarul complex ales nu exista in lista!!!")
        ##########UNDO################
        testUndo = Repository()
        testUndo.store(ComplexNumber(20, 30))
        assert(len(testUndo.getAll()) == 1)
        testUndo.store(ComplexNumber(10, 20))
        assert(len(testUndo.getAll()) == 2)
        testUndo.undo()
        assert(len(testUndo.getAll()) == 1)
        testUndo.undo()
        assert(len(testUndo.getAll()) == 0)
        try:
            testUndo.undo()
            assert(False)
        except ValueError as ve:
            assert(str(ve) == "!!!List is at the original state!!!")
##########################################################################

    def TestValidator(self):
        testVal = Validator()
        cn1 = ComplexNumber(30.20, -20)
        cn2 = ComplexNumber(-10.10, 20.10)
        cn3 = ComplexNumber(-10, 20)
        try:
            testVal.validate(cn1)
        except ValueError as ve:
            assert(str(ve) == "!!!The real part can only be integer!!!\n")
        try:
            testVal.validate(cn2)
        except ValueError as ve:
            assert(str(
                ve) == "!!!The real part can only be integer!!!\n!!!The imaginary part can only be integer!!!")
        try:
            testVal.validate(cn3)
            assert(True)
        except ValueError:
            raise ValueError

##########################################################################
    def TestHelpers(self):
        testHelp = Helpers()
        assert(testHelp.module(10, 1) == 10)
        assert(testHelp.prim(11) == True)
        assert(testHelp.prim(-1) == False)
        assert(testHelp.prim(10) == False)
        assert(testHelp.prim(2) == True)
