'''
Created on Oct 26, 2022

@author: balut
'''

from SERVICE.Service import Service

##########################################################################


class Console(object):
    '''
    classdocs
    '''

    def __init__(self, serv):
        '''
        Constructor

        :param serv[Service]: GaspController-ul
        '''
        self.serv = serv

    def meniu(self):
        '''
        Functie care afiseaza meniul principal
        :param self:
        '''
        print("\n1. Adaugă număr în listă.")
        print("2. Modifică elemente din listă.")
        print("3. Căutare numere.")
        print("4. Operații cu numerele din listă")
        print("5. Filtrare")
        print("6. Undo")
        print("7. Lista de numere complexe")
        print("0. Exit!")

#########################################################ADD##############

    def addMeniu(self):
        '''
        Functie care afiseaza meniul pentru functionalitatea de adaugare
        :param self:
        '''
        print("\n1. Adaugă număr complex la sfârșitul listei")
        print("2. Inserare număr complex pe o poziție dată.")
        print("0. Inapoi la meniul principal")

    def getCmdAdd(self):
        '''
        Functie care preia cererea utilizatorului pentru functia de adaugare
        :param self:
        @return[char]: cererea utilizatorului pentru functia de adaugare
        '''
        self.addMeniu()
        cmd = input("Introduceti functionalitatea: ")
        return cmd

    def add1(self):
        '''
        Functie care adauga numarul complex dorit de utilizator
        :param self:
            @post: Lungimea listei de numere complexe creste cu 1
        @exception[ValueError]: Numarul complex este invalid
        '''
        try:
            real = int(input("Introduceti partea reala: "))
            imaginar = int(input("Introduceti partea imaginara: "))
            self.serv.createComplexNumber(real, imaginar)
            print("Numar complex adaugat cu succes!\n")
        except ValueError as ve:
            print(ve)

    def add1String(self, cmd):
        if len(cmd) != 2:
            print("!!!INVALID ARGUMENTS!!!")
        else:
            try:
                self.serv.createComplexNumber(int(cmd[0]), int(cmd[1]))
                print("Numar complex adaugat cu succes!\n")
            except ValueError as ve:
                print(ve)

    def add2String(self, cmd):
        if len(cmd) != 3:
            print("!!!INVALID ARGUMENTS!!!")
        else:
            try:
                cn = self.serv.createNumberOnIndex(
                    int(cmd[0]), int(cmd[1]), int(cmd[2]))
                print(str(cn) + "-> Adaugat cu succes!!!\n")
            except ValueError as ve:
                print(ve)

    def add(self, cmd):
        if len(cmd) == 0:
            print("!!!Numar argumente invalid!!!")
        else:
            if cmd[0] == "final":
                self.add1String(cmd[1:])
            elif cmd[0] == "index":
                self.add2String(cmd[1:])
            else:
                print("!!!FUNCTIONALITATE INVALIDA!!!")

    def add2(self):
        try:
            real = int(input("Introduceti partea reala: "))
            imaginar = int(input("Introduceti partea imaginara: "))
            index = int(input("Introduceti indexul: "))
            cn = self.serv.createNumberOnIndex(real, imaginar, index)
            print(str(cn) + "-> Adaugat cu succes!!!\n")
        except ValueError as ve:
            print(ve)

    def addUI(self):
        '''
        Functie pentru controlul cererii a utilizatorului pentru functionalitatea de adaugare
        :param self:
        '''
        while True:
            cmd = self.getCmdAdd()
            if cmd == "0":
                break
            elif cmd == "1":
                self.add1()
            elif cmd == "2":
                self.add2()
            else:
                print("\n!!!FUNCTIONALITATE INVALIDA!!!\n")


##########################################################################

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

    def modifyMeniu(self):
        '''
        Functie care afiseaza meniul pentru functionalitatea de modificare
        :param self:
        '''
        print("\n1. Șterge element de pe o poziție dată")
        print("2. Șterge elementele de pe un interval de poziții")
        print("3. Înlocuiește toate aparițiile unui număr complex cu un alt număr complex.")
        print("0. Inapoi la meniul principal")

    def modify1(self):
        try:
            index = int(input("Introduceti index-ul: "))
            cn = self.serv.modifyIndex(index)
            print("Numarul sters este: ")
            print(str(cn))
            print("\n")
        except ValueError as ve:
            print(str(ve))

    def modify1String(self, cmd):
        if len(cmd) != 1:
            print("!!!INVALID ARGUMENTS!!!")
        else:
            try:
                cn = self.serv.modifyIndex(int(cmd[0]))
                print("Numarul sters este: ")
                print(str(cn))
                print("\n")
            except ValueError as ve:
                print(str(ve))

    def modify2(self):
        try:
            index_start = int(input("Introduceti index-ul de start: "))
            index_stop = int(input("Introduceti index-ul de stop: "))
            self.allPrint(self.serv.modifyRange(index_start, index_stop))
        except ValueError as ve:
            print(str(ve))

    def modify2String(self, cmd):
        if len(cmd) != 2:
            print("!!!INVALID ARGUMENTS!!!")
        else:
            try:
                self.allPrint(self.serv.modifyRange(int(cmd[0]), int(cmd[1])))
            except ValueError as ve:
                print(str(ve))

    def modify3(self):
        try:
            realEx = int(
                input("Introduceti partea reala a numarului existent: "))
            imaginarEx = int(
                input("Introduceti partea imaginara a numarului existent: "))
            realNew = int(input("Introduceti partea reala a numarului nou: "))
            imaginarNew = int(
                input("Introduceti partea imaginara a numarului nou: "))
            nr = self.serv.modifyAllUnique(
                realEx, imaginarEx, realNew, imaginarNew)
            print("Numere modificate: " + str(nr))
        except ValueError as ve:
            print(str(ve))

    def modify3String(self, cmd):
        if len(cmd) != 4:
            print("!!!INVALID ARGUMENTS!!!")
        else:
            try:
                nr = self.serv.modifyAllUnique(
                    int(cmd[0]), int(cmd[1]), int(cmd[2]), int(cmd[3]))
                print("Numere modificate: " + str(nr))
            except ValueError as ve:
                print(str(ve))

    def getCmdModify(self):
        '''
        Functie care preia cererea utilizatorului pentru functia de modificare
        :param self:
        @return[char]: cererea utilizatorului pentru functia de modificare
        '''
        self.modifyMeniu()
        cmd = input("Introduceti functionalitatea: ")
        return cmd

    def modifyUI(self):
        '''
        Functie pentru controlul cererii a utilizatorului pentru functionalitatea de modificare
        :param self:
        '''
        while True:
            cmd = self.getCmdModify()
            if cmd == "0":
                break
            elif cmd == "1":
                self.modify1()
            elif cmd == "2":
                self.modify2()
            elif cmd == "3":
                self.modify3()
            else:
                print("\n!!!FUNCTIONALITATE INVALIDA!!!\n")

    def modify(self, cmd):
        if len(cmd) == 0:
            print("!!!FUNCTIONALITATE INVALIDA!!!")
        else:
            if cmd[0] == "pozitie":
                self.modify1String(cmd[1:])
            elif cmd[0] == "interval":
                self.modify2String(cmd[1:])
            elif cmd[0] == "inlocuieste":
                self.modify3String(cmd[1:])


##########################################################################

    def searchMeniu(self):
        '''
        Functie care afiseaza meniul pentru functionalitatea de cautare
        :param self:
        '''
        print("\n1. Tipărește partea imaginara pentru numerele din listă. Se dă intervalul de poziții (sub secvența)")
        print("2. Tipărește toate numerele complexe care au modulul mai mic decât 10")
        print("3. Tipărește toate numerele complexe care au modulul egal cu 10.")
        print("0. Inapoi la meniul principal")

    def getCmdSearch(self):
        '''
        Functie care preia cererea utilizatorului pentru functia de cautare
        :param self:
        @return[char]: cererea utilizatorului pentru functia de cautare
        '''
        self.searchMeniu()
        cmd = input("Introduceti functionalitatea: ")
        return cmd

    def search1(self):
        try:
            index_start = int(input("Introduceti index-ul de start: "))
            index_stop = int(input("Introduceti index-ul de stop: "))
            self.allPrint(self.serv.searchRange(index_start, index_stop))
        except ValueError as ve:
            print(str(ve))

    def search1String(self, cmd):
        if len(cmd) != 2:
            print("!!!INVALID ARGUMENTS!!!")
        else:
            try:
                self.allPrint(self.serv.searchRange(int(cmd[0]), int(cmd[1])))
            except ValueError as ve:
                print(str(ve))

    def search2String(self, cmd):
        self.allPrint(self.serv.searchModuleLess())

    def search2(self):
        '''
        Functie care printeaza utilizatorului numerele complexe care au modulul mai mic decat 10
        :param self:
        @return[list[ComplexNumber]]: Lista de numere complexe care au modulul mai mic decat 10
        '''
        self.allPrint(self.serv.searchModuleLess())

    def search3(self):
        '''
        Functie care printeaza utilizatorului numerele complexe care au modulul egal cu 10
        :param self:
        @return[list[ComplexNumber]]: Lista de numere complexe care au modulul egal cu 10
        '''
        self.allPrint(self.serv.searchModuleEq())

    def search3String(self, cmd):
        self.allPrint(self.serv.searchModuleEq())

    def search(self, cmd):
        if len(cmd) == 0:
            print("!!!INVALID ARGUMENTS!!!")

        else:
            if cmd[0] == "interval":
                self.search1String(cmd[1:])
            elif cmd[0] == "<10":
                self.search2String(cmd[1:])
            if cmd[0] == "=10":
                self.search3String(cmd[1:])

    def searchUI(self):
        '''
        Functie pentru controlul cererii a utilizatorului pentru functionalitatea de cautare
        :param self:
        '''
        while True:
            cmd = self.getCmdSearch()
            if cmd == "0":
                break
            elif cmd == "1":
                self.search1()
            elif cmd == "2":
                self.search2()
            elif cmd == "3":
                self.search3()
            else:
                print("\n!!!FUNCTIONALITATE INVALIDA!!!\n")

##########################################################################

    def actionsMeniu(self):
        '''
        Functie care afiseaza meniul pentru functionalitatea de operatii
        :param self:
        '''
        print("\n1. suma numerelor dintr-o subsecventă dată (se da poziția de început și sfârșit)")
        print("2. Produsul numerelor dintr-o subsecventă dată (se da poziția de început și sfârșit)")
        print("3. Tipărește lista sortată descrescător după partea imaginara")
        print("0. Inapoi la meniul principal")

    def getCmdActions(self):
        '''
        Functie care preia cererea utilizatorului pentru functia de operatii
        :param self:
        @return[char]: cererea utilizatorului pentru functia de operatii
        '''
        self.actionsMeniu()
        cmd = input("Introduceti functionalitatea: ")
        return cmd

    def actions1(self):
        try:
            index_start = int(input("Introduceti index-ul de start: "))
            index_stop = int(input("Introduceti index-ul de stop: "))
            cn = self.serv.opSum(index_start, index_stop)
            print("Suma intervalului este: " + str(cn))
        except ValueError as ve:
            print(str(ve))

    def actions1String(self, cmd):
        if len(cmd) != 2:
            print("!!!INVALID ARGUMENTS!!!")

        else:
            try:
                cn = self.serv.opSum(int(cmd[0]), int(cmd[1]))
                print("Suma intervalului este: " + str(cn))
            except ValueError as ve:
                print(str(ve))

    def actions2(self):
        try:
            index_start = int(input("Introduceti index-ul de start: "))
            index_stop = int(input("Introduceti index-ul de stop: "))
            cn = self.serv.opMulti(index_start, index_stop)
            print("Produsul intervalului este: " + str(cn))
        except ValueError as ve:
            print(str(ve))

    def actions2String(self, cmd):
        if len(cmd) != 2:
            print("!!!INVALID ARGUMENTS!!!")

        else:
            try:
                cn = self.serv.opMulti(int(cmd[0]), int(cmd[1]))
                print("Suma intervalului este: " + str(cn))
            except ValueError as ve:
                print(str(ve))

    def actions3String(self, cmd):
        self.allPrint(self.serv.opSort())

    def actions3(self):
        self.allPrint(self.serv.opSort())

    def actions(self, cmd):
        if len(cmd) == 0:
            print("!!!FUNCTIONALITATE INVALIDA!!!")
        else:
            if cmd[0] == "suma":
                self.actions1String(cmd[1:])
            elif cmd[0] == "produs":
                self.actions2String(cmd[1:])
            elif cmd[0] == "sort":
                self.actions3String(cmd[1:])
            else:
                print("!!!FUNCTIONALITATE INVALIDA!!!")

    def actionsUI(self):
        '''-
        Functie pentru controlul cererii a utilizatorului pentru functionalitatea de cautare
        :param self:
        '''
        while True:
            cmd = self.getCmdActions()
            if cmd == "0":
                break
            elif cmd == "1":
                self.actions1()
            elif cmd == "2":
                self.actions2()
            elif cmd == "3":
                self.actions3()
            else:
                print("\n!!!FUNCTIONALITATE INVALIDA!!!\n")
##########################################################################


########################################################FILTER############

    def filterMeniu(self):
        '''
        Functie care afiseaza meniul pentru functionalitatea de filtrare
        :param self:
        '''
        print("\n1. Filtrare parte reala prim – elimină din listă numerele complexe la care partea reala este prim.")
        print("2. Filtrare modul – elimina din lista numerele complexe la care modulul este <,= sau > decât un număr dat.")
        print("0. Inapoi la meniul principal")

    def getCmdFilter(self):
        '''
        Functie care preia cererea utilizatorului pentru functia de filtrare
        :param self:
        @return[char]: cererea utilizatorului pentru functia de filtrare
        '''
        self.filterMeniu()
        cmd = input("Introduceti functionalitatea: ")
        return cmd

    def filter1(self):
        '''
        Functie care afiseaza numerele complexe care au partea reala un numar prim
        :param self:
        @return[list[ComplexNumber]]: Lista de numere complexe care au partea reala numar prim
        '''
        self.allPrint(self.serv.filterPrim())

    def filter2(self):
        '''
        Functie care afiseaza numerele complexe care au modulul contrar semnului ales de utilizator fata de numarul ales de utilizator
        :param self:
        @return[list[ComplexNumber]]: Lista de numere complexe care au modulul contrar semnului ales de utilizator fata de numarul ales de utilizator
        '''
        semn = input("Introduceti semnul (</=/>): ")
        n = int(input("Introduceti numarul de comparat: "))
        self.allPrint(self.serv.filterModul(semn, n))

    def filter2String(self, cmd):
        if len(cmd) != 2:
            print("!!!INVALID ARGUMENTS!!!")
        else:
            semn = cmd[0]
            n = int(cmd[1])
            self.allPrint(self.serv.filterModul(semn, n))

    def filterUI(self):
        '''
        Functie pentru controlul cererii a utilizatorului pentru functionalitatea de filtrare
        :param self:
        '''
        while True:
            cmd = self.getCmdFilter()
            if cmd == "0":
                break
            elif cmd == "1":
                self.filter1()
            elif cmd == "2":
                self.filter2()
            else:
                print("\n!!!FUNCTIONALITATE INVALIDA!!!\n")

    def filter(self, cmd):
        if len(cmd) == 0:
            print("!!!FUNCTIONALITATE INVALIDA!!!")
        else:
            if cmd[0] == "prim":
                self.filter1()
            elif cmd[0] == "semn":
                self.filter2String(cmd[1:])
            else:
                print("!!!FUNCTIONALITATE INVALIDA!!!")
##########################################################################

    def undoOperation(self):
        try:
            msg = self.serv.undoList()
            print(msg)
        except ValueError as ve:
            print(str(ve))

#######################################################UI#################

    def getCmdStart(self):
        '''
        Functie care afiseaza meniul pentru meniul principal
        :param self:
        '''
        self.meniu()
        cmd = input("Introduceti functionalitatea: ")
        return cmd

    def getCmdString(self):
        self.meniu()
        cmd = input(">>>")
        cmd.strip()
        cmd_list = cmd.split(";")
        return cmd_list

    def startUI(self):
        # print("\n1. Adaugă număr în listă.")
        # print("2. Modifică elemente din listă.")
        # print("3. Căutare numere.")
        # print("4. Operații cu numerele din listă")
        # print("5. Filtrare")
        # print("6. Undo")
        # print("7. Lista de numere complexe")
        # print("0. Exit!")
        '''
        Functie pentru controlul cererii a utilizatorului pentru meniul principal
        :param self:
        '''
        print("Introduceti modul de consola:(Optiuni/Comanda):")
        uiSelect = input(">>>")
        if uiSelect == "Comanda":
            self.serv.populateList()
            while True:
                cmd = self.getCmdString()
                if len(cmd) > 0:
                    if cmd[0] == "Exit":
                        break
                    elif cmd[0] == "Adauga":
                        self.add(cmd[1:])
                    elif cmd[0] == "Modifica":
                        self.modify(cmd[1:])
                    elif cmd[0] == "Cautare":
                        self.search(cmd[1:])
                    elif cmd[0] == "Operatii":
                        self.actions(cmd[1:])
                    elif cmd[0] == "Filtrare":
                        self.filter(cmd[1:])
                    elif cmd[0] == "Undo":
                        self.undoOperation()
                    elif cmd[0] == "Afisare":
                        self.allPrint(self.serv.getList())
                    else:
                        print("\n!!!FUNCTIONALITATE INCORECTA!!!\n")
                else:
                    print("\n!!!FUNCTIONALITATI INSUFICIENTE!!!\n")
        else:
            self.serv.populateList()
            while True:
                cmd = self.getCmdStart()
                if cmd == "0":
                    break
                elif cmd == "1":
                    self.addUI()
                elif cmd == "2":
                    self.modifyUI()
                elif cmd == "3":
                    self.searchUI()
                elif cmd == "4":
                    self.actionsUI()
                elif cmd == "5":
                    self.filterUI()
                elif cmd == "6":
                    self.undoOperation()
                elif cmd == "7":
                    self.allPrint(self.serv.getList())
                else:
                    print("\n!!!FUNCTIONALITATE INCORECTA!!!\n")
##########################################################################
