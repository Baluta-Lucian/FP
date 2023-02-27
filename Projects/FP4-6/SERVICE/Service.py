'''
Created on Oct 26, 2022

@author: balut
'''
from DOMAIN.entities import ComplexNumber
from REPOSITORY.Repository import Repository
from VALIDATION.Validator import Validator
from Utility.Functions import Helpers
import numpy


class Service(object):
    '''
    classdocs
    '''

    def __init__(self, repo, validator, help):
        '''
        Constructor

        :param repo[Repository]: Reposity
        :param validator[Validator]: Validator
        :param help[Helpers]: Helper(Functions)
        '''
        self.repo = repo
        self.validator = validator
        self.help = help

    def createComplexNumber(self, real, imaginar):
        '''
        Functie care adauga un numar complex la lista de numere complexe
        :param real[int]: -> partea reala a unui numar complex
        :param imaginar[int]: -> partea reala a unui numar complex
            @post: Lungimea listei creste cu 1
        @return[ComplexNumber]: returneaza numarul complex adaugat
        @exception[ValueError]: Datele introduse nu sunt valide
        '''
        cn = ComplexNumber(real, imaginar)
        if self.validator != None:
            self.validator.validate(cn)
        self.repo.store(cn)
        return cn

    def createNumberOnIndex(self, real, imaginar, index):
        '''
        Functie care insereaza un număr complex pe o poziție dată.
        :param real[int]: -> partea reala a unui numar complex
        :param imaginar[int]: -> partea imaginara a unui numar complex
        :param index[int]: -> indexul unde se va insera in lista de numere complexe
            @Post: Lungimea listei creste cu 1
        @return[ComplexNumber]: returneaza numarul complex adaugat
        @exception[ValueError]:    *Validation: Datele introduse pentru numarul complex sunt invalide
                                   *Repository: Index out of range
        '''
        cn = ComplexNumber(real, imaginar)
        if self.validator != None:
            self.validator.validate(cn)
        self.repo.indexStore(cn, index)
        return cn

    def getList(self):
        '''
        Functie care returneaza o copie a listei de numere complexe
        :param self:
        @return[list[ComplexNumber]]: Copie a listei de numere complexe
        '''
        return self.repo.getAll()

    def getListRange(self, start_index, stop_index):
        '''
        Functie care returneaza o sublista a listei de numere complexe de la start_index pana la stop_index+1
        :param start_index[int]: -> Indexul de start al listei
        :param stop_index[int]: -> Indexul de stop al listei
        @return[list[ComplexNumber]: Lista cu cerinta functiei
        @exception[ValueError]: Index invalid
        '''
        if start_index < 0 or start_index >= len(self.repo.getAll()):
            if stop_index < start_index or stop_index >= len(self.repo.getAll()):
                raise ValueError("!!!Start and Stop index out of range!!!")
            raise ValueError("!!!Start index out of range!!!")
        if stop_index < start_index or stop_index >= len(self.repo.getAll()):
            raise ValueError("!!!Stop index out of range!!!")
        return self.repo.getAll()[start_index:(stop_index + 1)]

    def filterPrim(self):
        '''
        Functie care returneaza o lista de numere complexe din lista de numere complexe care au ca parte reala un numar prim
        :param self:
        @return[list[ComplexNumber]]: Lista de numere complexe ce respecta cerinta
        '''
        return [i for i in self.getList() if self.help.prim(i.getReal()) == True]

    def filterModul(self, semn, n):
        '''
        Functie care returneaza o lista de numere complexe din lista de numere complexe care au modulul diferit de n opus semnului(semn)
        :param semn[char]: -> semnul de comparat(>/=/<)
        :param n[int]: -> Numarul de comparat
        @return[list[ComplexNumber]]: lista de numere complexe ce respecta cerinta
        '''
        if semn == ">":
            return [i for i in self.getList() if self.help.module(i.getReal(), i.getImaginar()) <= n]
        if semn == "=":
            return [i for i in self.getList() if self.help.module(i.getReal(), i.getImaginar()) < n or self.help.module(i.getReal(), i.getImaginar()) > n]
        if semn == "<":
            return [i for i in self.getList() if self.help.module(i.getReal(), i.getImaginar()) >= n]

    def modifyIndex(self, index):
        '''
        Functie care elimina de la un anumit index un numar complex din lista de numere complexe
        :param index: -> indexul de unde dorim sa eliminam
            @post: Lungimea listei scade cu 1
        @return[ComplexNumber]: returneaza numarul complex eliminat
        @exception[ValueError]: Indexul este invalid
        '''
        return self.repo.indexDelete(index)

    def modifyRange(self, start_index, stop_index):
        '''
        Functie care elimina dintr-un anumit interval de pozitii numere complexe din lista de numere complexe
        :param start_index: -> indexul de inceput al intervalului
        :param stop_index: -> indexul de sfarsit al intervalului
            @post: Lungimea listei scade cu stop_index-start_index
        @return[list[ComplexNumber]]: returneaza o lista cu numerele complexe eliminate
        @exception[ValueError]: Interval invalid
        '''
        return self.repo.rangeDelete(start_index, stop_index)

    def modifyAllUnique(self, realExistent, imaginarExistent, realNew, imaginarNew):
        '''
        Functie care inlocuiește toate aparițiile unui număr complex cu un alt număr complex.
        :param realExistent[int]: -> partea reala a numarului complex din lista
        :param imaginarExistent[int]: -> partea imaginara a numarului complex din lista
        :param realNew[int]: -> noua parte reala
        :param imaginarNew[int]: -> noua parte imaginara
            @post: Toate elementele cn sunt schimbate cu elementele ot
        @return[int]: Numarul de modificari
        @exception[ValueError]: *Validation -> datele pentru numerele complexe sunt invalide
                                *Repository -> numarul complex ales de utilizator nu exista in lista
        '''
        cn = ComplexNumber(realExistent, imaginarExistent)
        ot = ComplexNumber(realNew, imaginarNew)
        if self.validator != None:
            self.validator.validate(cn)
            self.validator.validate(ot)
        return self.repo.setAllUnique(cn, ot)

    def searchRange(self, start_index, stop_index):
        '''
        Functie care Tipărește partea imaginara pentru numerele din listă dintr-un interval dat
        :param start_index[int]: -> Indexul de start al listei
        :param stop_index[int]: -> Indexul de stop al listei
        @return[list[ImaginaryPart]]: Lista cu partea imaginara a numerelor complexe dintr-un interval dat
        @exception[ValueError]: Index invalid
        '''
        local = self.getListRange(start_index, stop_index)
        imaginary = []
        for i in local:
            imaginary.append(i.getImaginar())
        return imaginary

    def searchModuleLess(self):
        '''
        Functie care returneaza o lista de numere complexe din lista de numere complexe care au modulul mai mic decat 10
        :param self:
        @return[list[ComplexNumber]]: lista de numere complexe a caror modul e mai mic decat 10
        '''
        return [i for i in self.getList() if self.help.module(i.getReal(), i.getImaginar()) < 10]

    def searchModuleEq(self):
        '''
        Functie care returneaza o lista de numere complexe din lista de numere complexe care au modulul egal cu 10
        :param self:
        @return[list[ComplexNumber]]: lista de numere complexe a caror modul este egal cu 10
        '''
        return [i for i in self.getList() if self.help.module(i.getReal(), i.getImaginar()) == 10]

    def opSum(self, start_index, stop_index):
        '''
        Functie care returneaza suma numerelor complexe dintr-un interval dat
        :param start_index[int]: -> indexul de start al intervalului
        :param stop_index[int]: -> indexul de stop al intervalului
        @return[ComplexNumber]: suma numerelor complexe
        @exception[ValueError]: index invalid
        '''
        local = self.getListRange(start_index, stop_index)
        real = 0
        imaginary = 0
        for i in local:
            real += i.getReal()
            imaginary += i.getImaginar()
        cn = ComplexNumber(real, imaginary)
        return cn

    def opMulti(self, start_index, stop_index):
        '''
        Functie care calculeaza produsul numerelor dintr-o subsecventă dată (se da poziția de început și sfârșit).
        :param start_index[int]: -> indexul de start al intervalului
        :param stop_index[int]: -> indexul de stop al intervalului
        @return[ComplexNumber]: produsul numerelor complexe
        @exception[ValueError]: index invalid
        '''
        local = self.getListRange(start_index, stop_index)
        real = 1
        imaginary = 1
        ok = 0
        for i in local:
            if ok == 0:
                real = i.getReal()
                imaginary = i.getImaginar()
                ok = 1
            else:
                x = real
                y = imaginary
                real = x * i.getReal() + y * i.getImaginar() * (-1)
                imaginary = i.getImaginar() * x + i.getReal() * y
            #(r + i)(r1+i1) = rr1 + r1i + i1r + i^2
        cn = ComplexNumber(real, imaginary)
        return cn

    def funcOpSort(self, e):
        '''
        Functie key pentru sortare
        :param e[ComplexNumber]: -> numarul complex
        @return[int]: partea imaginara a numarului complex
        '''
        return e.getImaginar()

    def opSort(self):
        '''
        Functie care returneaza lista sortată descrescător după partea imaginara
        @return[list[ComplexNumber]]: Lista de numere complexe sortata dupa partea imaginara
        '''
        local = self.getList()
        local.sort(reverse=True, key=self.funcOpSort)
        return local

    def undoList(self):
        '''
        Lista revine la forma anterioara 
        :param self:
        @return[str]: Mesaj de succes
        @exception[ValueError]: Lista este deja la forma originala
        '''
        self.repo.undo()
        return "Success UNDO!"

    def populateList(self):
        '''
        Functie care populeaza lista de numere complexe
        :param self:
            @post: Lungimea liste creste cu 16
        '''
        cn1 = ComplexNumber(30, 40)
        cn2 = ComplexNumber(-10, -20)
        cn3 = ComplexNumber(10, 20)
        cn4 = ComplexNumber(30, -40)
        cn5 = ComplexNumber(15, 17)
        cn6 = ComplexNumber(2, 3)
        cn7 = ComplexNumber(-4, -2)
        cn8 = ComplexNumber(4, 5)
        cn9 = ComplexNumber(6, 10)
        cn10 = ComplexNumber(10, 11)
        cn11 = ComplexNumber(213, 12314)
        cn12 = ComplexNumber(340, 123)
        cn13 = ComplexNumber(-123, -4214)
        cn14 = ComplexNumber(24, 25)
        cn15 = ComplexNumber(7, 2)
        cn16 = ComplexNumber(10, 1)
        self.repo.store(cn1)
        self.repo.store(cn2)
        self.repo.store(cn3)
        self.repo.store(cn4)
        self.repo.store(cn5)
        self.repo.store(cn6)
        self.repo.store(cn7)
        self.repo.store(cn8)
        self.repo.store(cn9)
        self.repo.store(cn10)
        self.repo.store(cn11)
        self.repo.store(cn12)
        self.repo.store(cn13)
        self.repo.store(cn14)
        self.repo.store(cn15)
        self.repo.store(cn16)
