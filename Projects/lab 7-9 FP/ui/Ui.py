'''
Created on Nov 10, 2022

@author: balut
'''
from colorama import Fore
from errors.Exceptions import ValidationException, RepositoryException
from domain import Entities


class Console(object):
    '''
    classdocs
    '''

    def __init__(self, srv):
        '''
        Constructor
        '''
        self.__srv = srv

    def meniu(self):
        print(Fore.WHITE + "\nLista de functionalitati: ")
        print(Fore.GREEN + "1.Adaugare")
        print(Fore.GREEN + "2.Stergere")
        print(Fore.GREEN + "3.Modificare")
        print(Fore.GREEN + "4.Cautare")
        print(Fore.GREEN + "5.Catalog")
        print(Fore.GREEN + "6.Statistici")
        print(Fore.GREEN + "7.Afisare studenti")
        print(Fore.GREEN + "8.Afisare discipline")
        print(Fore.GREEN + "9.Afisare catalog")
        print(Fore.GREEN + "10.Genereaza entitati random")
        print(Fore.GREEN + "11.Populate")
        print(Fore.GREEN + "12.Cea mai putin frecventa nota")
        print(Fore.GREEN + "13.Sortari")
        print(Fore.GREEN + "0.Exit")


##########################################################################
    def AddMeniu(self):
        print(Fore.WHITE + "\nLista de functionalitati: ")
        print(Fore.GREEN + "1.Adauga student")
        print(Fore.GREEN + "2.Adauga disciplina")
        print(Fore.GREEN + "0.Exit")

    def add1(self):
        print(Fore.YELLOW + "Un student este format din ID/nume")
        id = int(input(Fore.LIGHTGREEN_EX + "Introduceti ID-ul: "))
        nume = input(Fore.LIGHTGREEN_EX + "Introduceti numele: ")
        try:
            self.__srv.createStudent(id, nume)
            print(Fore.LIGHTGREEN_EX + "\nStudent adaugat cu succes!\n")
        except ValidationException as ve:
            print(Fore.RED + str(ve))
        except RepositoryException as re:
            print(Fore.RED + str(re))

    def add2(self):
        print(Fore.YELLOW + "O disciplina este format din ID/nume/profesor")
        id = int(input(Fore.LIGHTGREEN_EX + "Introduceti ID-ul: "))
        nume = input(Fore.LIGHTGREEN_EX + "Introduceti numele: ")
        profesor = input(Fore.LIGHTGREEN_EX + "Introduceti profesorul: ")
        try:
            self.__srv.createDisciplina(id, nume, profesor)
            print(Fore.LIGHTGREEN_EX + "\nDisciplina adaugata cu succes!\n")
        except ValidationException as ve:
            print(Fore.RED + str(ve))
        except RepositoryException as re:
            print(Fore.RED + str(re))

    def AdaugaUI(self):
        while True:
            self.AddMeniu()
            cmd = input(Fore.LIGHTGREEN_EX +
                        "Introduceti functionalitatea: >>>")
            if cmd == '0':
                break
            elif cmd == '1':
                self.add1()
            elif cmd == '2':
                self.add2()
            else:
                print(Fore.RED + "\n!!!COMANDA INVALIDA!!!")


##########################################################################

    def StergeMeniu(self):
        print(Fore.WHITE + "\nLista de functionalitati: ")
        print(Fore.GREEN + "1.Sterge student")
        print(Fore.GREEN + "2.Sterge disciplina")
        print(Fore.GREEN + "0.Exit")

    def sterge1(self):
        print(Fore.YELLOW + "Introduceti datele studentului de sters ->")
        id = int(input(Fore.LIGHTGREEN_EX + "Introduceti ID-ul: "))
        nume = input(Fore.LIGHTGREEN_EX + "Introduceti numele: ")
        try:
            deleted = self.__srv.deleteStudent(id, nume)
            print(Fore.WHITE + "Student sters ->")
            print(Fore.LIGHTBLUE_EX + str(deleted))
        except RepositoryException as re:
            print(Fore.RED + str(re))

    def sterge2(self):
        print(Fore.YELLOW + "Introduceti datele disciplinei de sters ->")
        id = int(input(Fore.LIGHTGREEN_EX + "Introduceti ID-ul: "))
        nume = input(Fore.LIGHTGREEN_EX + "Introduceti numele: ")
        profesor = input(Fore.LIGHTGREEN_EX + "Introduceti profesorul: ")
        try:
            deleted = self.__srv.deleteDisciplina(id, nume, profesor)
            print(Fore.WHITE + "Disciplina stearsa ->")
            print(Fore.LIGHTBLUE_EX + str(deleted))
        except RepositoryException as re:
            print(Fore.RED + str(re))

    def StergeUI(self):
        while True:
            self.StergeMeniu()
            cmd = input(Fore.LIGHTGREEN_EX +
                        "Introduceti functionalitatea: >>>")

            if cmd == '0':
                break
            elif cmd == '1':
                self.sterge1()
            elif cmd == '2':
                self.sterge2()
            else:
                print(Fore.RED + "\n!!!COMANDA INVALIDA!!!")


##########################################################################

    def ModificaMeniu(self):
        print(Fore.WHITE + "\nLista de functionalitati: ")
        print(Fore.GREEN + "1.Modifica student")
        print(Fore.GREEN + "2.Modifica disciplina")
        print(Fore.GREEN + "0.Exit")

    def modifica1(self):
        print(Fore.YELLOW + "Introduceti datele studentului de modificat ->")
        id = int(input(Fore.LIGHTGREEN_EX + "Introduceti ID-ul: "))
        nume = input(Fore.LIGHTGREEN_EX + "Introduceti numele: ")
        print(Fore.YELLOW + "Introduceti noile date ale studentului->")
        idNew = int(input(Fore.LIGHTGREEN_EX + "Introduceti ID-ul: "))
        numeNew = input(Fore.LIGHTGREEN_EX + "Introduceti numele: ")
        try:
            self.__srv.setStudent(id, nume, idNew, numeNew)
            print(Fore.LIGHTBLUE_EX + "\nStudent modificat cu succes!")
        except ValidationException as ve:
            print(Fore.RED + str(ve))
        except RepositoryException as re:
            print(Fore.RED + str(re))

    def modifica2(self):
        print(Fore.YELLOW + "Introduceti datele disciplinei de modificat ->")
        id = int(input(Fore.LIGHTGREEN_EX + "Introduceti ID-ul: "))
        nume = input(Fore.LIGHTGREEN_EX + "Introduceti numele: ")
        profesor = input(Fore.LIGHTGREEN_EX + "Introduceti profesorul: ")
        print(Fore.YELLOW + "Introduceti noile date ale disciplinei ->")
        idNew = int(input(Fore.LIGHTGREEN_EX + "Introduceti ID-ul: "))
        numeNew = input(Fore.LIGHTGREEN_EX + "Introduceti numele: ")
        profesorNew = input(Fore.LIGHTGREEN_EX + "Introduceti profesorul: ")
        try:
            self.__srv.setDisciplina(
                id, nume, profesor, idNew, numeNew, profesorNew)
            print(Fore.LIGHTBLUE_EX + "\nDisciplina modificata cu succes!")
        except ValidationException as ve:
            print(Fore.RED + str(ve))
        except RepositoryException as re:
            print(Fore.RED + str(re))

    def ModificaUI(self):
        while True:
            self.ModificaMeniu()
            cmd = input(Fore.LIGHTGREEN_EX +
                        "Introduceti functionalitatea: >>>")
            if cmd == '0':
                break
            elif cmd == '1':
                self.modifica1()
            elif cmd == '2':
                self.modifica2()
            else:
                print(Fore.RED + "\n!!!COMANDA INVALIDA!!!")


##########################################################################

    def CautaMeniu(self):
        print(Fore.WHITE + "\nLista de functionalitati: ")
        print(Fore.GREEN + "1.Cauta student")
        print(Fore.GREEN + "2.Cauta disciplina")
        print(Fore.GREEN + "0.Exit")

    def cauta1(self):
        print(Fore.YELLOW + "Introduceti datele studentului de cautat ->")
        id = int(input(Fore.LIGHTGREEN_EX + "Introduceti ID-ul: "))
        nume = input(Fore.LIGHTGREEN_EX + "Introduceti numele: ")
        try:
            s = self.__srv.findStudent(id, nume)
            print(Fore.LIGHTBLUE_EX + "\nStudent gasit cu succes!")
            print(Fore.LIGHTGREEN_EX + str(s))
        except RepositoryException as re:
            print(Fore.RED + str(re))

    def cauta2(self):
        print(Fore.YELLOW + "Introduceti datele disciplinei de cautat ->")
        id = int(input(Fore.LIGHTGREEN_EX + "Introduceti ID-ul: "))
        nume = input(Fore.LIGHTGREEN_EX + "Introduceti numele: ")
        profesor = input(Fore.LIGHTGREEN_EX + "Introduceti profesorul: ")
        try:
            d = self.__srv.findDisciplina(id, nume, profesor)
            print(Fore.LIGHTBLUE_EX + "\nDisciplina gasita cu succes!")
            print(Fore.LIGHTGREEN_EX + str(d))
        except RepositoryException as re:
            print(Fore.RED + str(re))

    def CautaUI(self):
        while True:
            self.CautaMeniu()
            cmd = input(Fore.LIGHTGREEN_EX +
                        "Introduceti functionalitatea: >>>")
            if cmd == '0':
                break
            elif cmd == '1':
                self.cauta1()
            elif cmd == '2':
                self.cauta2()
            else:
                print(Fore.RED + "\n!!!COMANDA INVALIDA!!!")


##########################################################################

    def CatalogMeniu(self):
        print(Fore.WHITE + "\nLista de functionalitati: ")
        print(Fore.GREEN + "1.Asignare de note la un student si o disciplina")
        print(Fore.GREEN + "0.Exit")

    def catalog1(self):
        print(Fore.YELLOW + "Introduceti datele studentului ->")
        idS = int(input(Fore.LIGHTGREEN_EX + "Introduceti ID-ul: "))
        nume = input(Fore.LIGHTGREEN_EX + "Introduceti numele: ")
        print(Fore.YELLOW + "Introduceti datele disciplinei ->")
        idD = int(input(Fore.LIGHTGREEN_EX + "Introduceti ID-ul: "))
        denumire = input(Fore.LIGHTGREEN_EX + "Introduceti denumirea: ")
        profesor = input(Fore.LIGHTGREEN_EX + "Introduceti profesorul: ")
        print(Fore.YELLOW + "Introduceti notele Studentului(0->opreste): ")
        note = []
        cmd = -1
        while cmd != 0:
            cmd = int(input(Fore.GREEN + ">>>"))
            if cmd != 0:
                note.append(cmd)
        try:
            self.__srv.createStatistica(
                idS, nume, idD, denumire, profesor, note)
            print(Fore.LIGHTBLUE_EX + "\nStatistica adaugata cu succes!")
        except ValidationException as ve:
            print(Fore.RED + str(ve))
        except RepositoryException as re:
            print(Fore.RED + str(re))

    def CatalogUI(self):
        while True:
            self.CatalogMeniu()
            cmd = input(Fore.LIGHTGREEN_EX +
                        "Introduceti functionalitatea: >>>")
            if cmd == '0':
                break
            elif cmd == '1':
                self.catalog1()
            else:
                print(Fore.RED + "\n!!!COMANDA INVALIDA!!!")


##########################################################################
    def StatisticiMeniu(self):
        print(Fore.WHITE + "\nLista de functionalitati: ")
        print(
            Fore.GREEN + "1.Lista de studenti si notele lor la o materie ordonata dupa nume")
        print(
            Fore.GREEN + "2.Lista de studenti si notele lor la o materie ordonata dupa note")
        print(Fore.GREEN + "3.Primi 20% studenti")
        print(Fore.GREEN + "0.Exit")

    def statistici1(self):
        print(Fore.YELLOW + "Introduceti datele disciplinei ->")
        idD = int(input(Fore.LIGHTGREEN_EX + "Introduceti ID-ul: "))
        denumire = input(Fore.LIGHTGREEN_EX + "Introduceti denumirea: ")
        profesor = input(Fore.LIGHTGREEN_EX + "Introduceti profesorul: ")
        try:
            stats = self.__srv.StatsStudentiNume(idD, denumire, profesor)
            if len(stats) == 0:
                print(Fore.LIGHTBLUE_EX +
                      "\nStudentii nu au note la aceasta disciplina!")
            else:
                self.PrintAll(stats)
        except ValidationException as ve:
            print(Fore.RED + str(ve))

    def statistici2(self):
        print(Fore.YELLOW + "Introduceti datele disciplinei ->")
        idD = int(input(Fore.LIGHTGREEN_EX + "Introduceti ID-ul: "))
        denumire = input(Fore.LIGHTGREEN_EX + "Introduceti denumirea: ")
        profesor = input(Fore.LIGHTGREEN_EX + "Introduceti profesorul: ")
        try:
            stats = self.__srv.StatsStudentiNote(idD, denumire, profesor)
            if len(stats) == 0:
                print(Fore.LIGHTBLUE_EX +
                      "\nStudentii nu au note la aceasta disciplina!")
            else:
                self.PrintAll(stats)
        except ValidationException as ve:
            print(Fore.RED + str(ve))

    def statistici3(self):
        self.PrintAll(self.__srv.Stats20())

    def StatisticiUI(self):
        while True:
            self.StatisticiMeniu()
            cmd = input(Fore.LIGHTGREEN_EX +
                        "Introduceti functionalitatea: >>>")
            if cmd == '0':
                break
            elif cmd == '1':
                self.statistici1()
            elif cmd == '2':
                self.statistici2()
            elif cmd == '3':
                self.statistici3()
            else:
                print(Fore.RED + "\n!!!COMANDA INVALIDA!!!")

##########################################################################
    def RandomEntities(self):
        nr = int(input(Fore.LIGHTGREEN_EX + "Introduceti nr entitati: "))
        self.__srv.randomGenerator(nr)
##########################################################################

    def sortMeniu(self):
        print(Fore.WHITE + "\nLista de functionalitati: ")
        print(Fore.GREEN + "1.Merge sort")
        print(Fore.GREEN + "2.Bingo sort")
        print(Fore.GREEN + "0.Exit")

    def sortUI(self):
        while True:
            self.sortMeniu()
            cmd = input(Fore.LIGHTGREEN_EX +
                        "Introduceti functionalitatea: >>>")
            if cmd == '0':
                break
            elif cmd == '1':
                self.sort1()
            elif cmd == '2':
                self.sort2()
            else:
                print(Fore.RED + "\n!!!COMANDA INVALIDA!!!")

    def sort1(self):
        self.PrintAll(self.__srv.merge_sort_with_key(
            self.__srv.getStudenti(), lambda x: x.getNume(), lambda x: x.getID()))

    def sort2(self):
        self.PrintAll(self.__srv.bingoSort_with_key(
            self.__srv.getStudenti(), lambda x: x.getNume()))

##########################################################################

    def PrintAll(self, l):
        if len(l) == 0:
            print(Fore.LIGHTBLUE_EX + "\nLista este goala")
        else:
            for i in l:
                print(Fore.LIGHTBLUE_EX + str(i))

    def run(self):
        # self.__srv.populate()
        print("Legenda:")
        print(Fore.WHITE + "White -> list of functionalities")
        print(Fore.BLACK + "Black -> not yet implemented")
        print(Fore.GREEN + "Green -> implemented")
        print(Fore.RED + "Red -> warning")
        print(Fore.LIGHTGREEN_EX + "Light green -> user input")
        print(Fore.LIGHTBLUE_EX + "Light blue -> entity output\n")

        while True:
            self.meniu()
            cmd = input(Fore.LIGHTGREEN_EX +
                        "Introduceti functionalitatea: >>>")
            if cmd == '0':
                break
            elif cmd == '1':
                self.AdaugaUI()
            elif cmd == '2':
                self.StergeUI()
            elif cmd == '3':
                self.ModificaUI()
            elif cmd == '4':
                self.CautaUI()
            elif cmd == '5':
                self.CatalogUI()
            elif cmd == '6':
                self.StatisticiUI()
            elif cmd == '7':
                self.PrintAll(self.__srv.getStudenti())
            elif cmd == '8':
                self.PrintAll(self.__srv.getDiscipline())
            elif cmd == '9':
                self.PrintAll(self.__srv.getCatalog())
            elif cmd == '10':
                self.RandomEntities()
            elif cmd == "11":
                self.__srv.populate()
            elif cmd == "12":
                print(Fore.LIGHTBLUE_EX + "\nCea mai putin pupulara nota din catalog: " +
                      str(self.__srv.leastPopular()))
            elif cmd == "13":
                self.sortUI()
            else:
                print(Fore.RED + "\n!!!COMANDA INVALIDA!!!")


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
