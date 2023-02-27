'''
Created on Nov 10, 2022

@author: balut
'''
from domain.Entities import Student, Disciplina, Statistica, Situatie
import names
import random
import string


class ServiceCatalog(object):
    '''
    classdocs
    '''

    def __init__(self, repoS, repoD, repoC, val):
        '''
        Constructor
        '''
        self.__repoS = repoS
        self.__repoD = repoD
        self.__repoC = repoC
        self.__val = val

        self.__randomD = ["Accounting",
                          "Art History",
                          "Arts and Humanities",
                          "Biology",
                          "Business and Management",
                          "Chemistry",
                          "Classical Studies",
                          "Combined Studies",
                          "Computing and IT",
                          "Counselling",
                          "Creative Writing",
                          "Criminology",
                          "Design",
                          "Early Years",
                          "Economics",
                          "Education",
                          "Electronic Engineering",
                          "Engineering",
                          "English",
                          "Environment",
                          "Film and Media",
                          "Geography",
                          "Health and Social Care",
                          "Health and Wellbeing",
                          "Health Sciences",
                          "History",
                          "International Studies",
                          "Languages",
                          "Law",
                          "Marketing",
                          "Mathematics",
                          "Mental Health",
                          "Music",
                          "Nursing and Healthcare",
                          "Philosophy",
                          "Physics",
                          "Politics",
                          "Psychology",
                          "Religious Studies",
                          "Science",
                          "Social Sciences",
                          "Social Work",
                          "Sociology",
                          "Software Engineering",
                          "Sport & Fitness",
                          "Statistics"]

    def createStudent(self, id, nume):
        '''
        Functie care creeaza si adauga un student in lista de studenti
        :param id[int]: id-ul studentului
        :param nume[string]: numele studentului
        @raises[ValidationException]: Student invalid
        @raises[RepositoryException]: Student existent in lista de studenti
        '''
        s = Student(id, nume)
        self.__val.validateS(s)
        self.__repoS.store(s)

    def createDisciplina(self, id, denumire, profesor):
        '''
        Functie care creeaza si adauga o disciplina in lista de discipline
        :param id[int]:id-ul disciplinei
        :param denumire[string]: denumirea disciplinei
        :param profesor[string]: profesorul disciplinei
        @raises[ValidationException]: Disciplina invalida
        @raises[RepositoryException]: Disciplina existent in lista de discipline
        '''
        d = Disciplina(id, denumire, profesor)
        self.__val.validateD(d)
        self.__repoD.store(d)

    def createStatistica(self, idS, nume, idD, denumire, profesor, note):
        '''
        Functie care adauga o statistica in catalog
        :param idS[int]: id-ul studentului
        :param nume[string]: numele studentului
        :param idD[int]: id-ul disciplinei
        :param denumire[string]: denumirea disciplinei
        :param profesor[string]: profesorul disciplinei
        :param note[list[int]]: notele studentului la disciplina aleasa
        @raises[ValidationException]: Student/Disciplina/Statistica invalida
        @raises[RepositoryException]: Student/Disciplina nu existenta in lista de stundeti/discipline
        @raises[RepositoryException]: Statistica existenta in lista de statistici
        '''
        s = Student(idS, nume)
        d = Disciplina(idD, denumire, profesor)
        self.__val.validateS(s)
        self.__val.validateD(d)
        self.__repoS.findOne(s)
        self.__repoD.findOne(d)
        stat = Statistica(s, d, note)
        self.__val.validateStat(stat)
        self.__repoC.store(stat)

    def deleteStudent(self, id, nume):
        '''
        Functie care sterge un student din lista de studenti
        :param id[int]: id-ul studentului
        :param nume[string]: numele studentului
        @return[Student]: Studentul sters din lista de studenti
        @raises[RepositoryException]: Studentul nu exista in lista de studenti
        '''
        s = Student(id, nume)
        self.__repoC.deleteByStudent(s)
        return self.__repoS.delete(s)

    def deleteDisciplina(self, id, denumire, profesor):
        '''
        Functie care sterge o disciplina din lista de discipline
        :param id[int]: id-ul disciplinei
        :param denumire[string]: denumirea disciplinei
        :param profesor[string]: profesorul disciplinei
        @return[Disciplina]: Disciplina stearsa din lista de discipline
        @raises[RepositoryException]: Disciplina nu exista in lista de discipline
        '''
        d = Disciplina(id, denumire, profesor)
        self.__repoC.deleteByDisciplina(d)
        return self.__repoD.delete(d)

    def setStudent(self, id, nume, idNew, numeNew):
        '''
        Functie care modifica un student din lista de studenti
        :param id[int]: id-ul studentului de modificat
        :param nume[string]: numele studentului de modificat
        :param idNew[int]: noul id al studentului
        :param numeNew[string]: noul nume al studentului
        @raises[ValidationException]: Noul student este invalid
        @raises[RepositoryException]: Studentul nou existent in lista de studenti/ Studentul de modificat nu exista in lista
        '''
        s = Student(id, nume)
        sNew = Student(idNew, numeNew)
        self.__val.validateS(sNew)
        self.__repoS.modify(s, sNew)

    def setDisciplina(self, id, denumire, profesor, idNew, denumireNew, profesorNew):
        '''
        Functie care modifica o disciplina din lista de discipline
        :param id[int]: id-ul disciplinei de modificat
        :param denumire[string]: denumirea disciplinei de modificat
        :param profesor[string]: profesorul disciplinei de modificat
        :param idNew[int]: noul id al disciplinei
        :param denumireNew[string]: noua denumire a disciplinei
        :param profesorNew[string]: noul profesor al disciplinei
        @raises[ValidationException]: Noua disciplina este invalida
        @raises[RepositoryException]: Disciplina noua exista in lista de discipline/Disciplina de modificat nu exista in lista
        '''
        d = Disciplina(id, denumire, profesor)
        dNew = Disciplina(idNew, denumireNew, profesorNew)
        self.__val.validateD(dNew)
        self.__repoD.modify(d, dNew)

    def getStudenti(self):
        '''
        Functie care returneaza lista de studenti
        :param self:
        @return[list[Student]]: Lista de studenti
        '''
        return self.__repoS.getAll()

    def getDiscipline(self):
        '''
        Functie care returneaza lista de discipline
        :param self:
        @return[list[Disciplina]]: Lista de discipline
        '''
        return self.__repoD.getAll()

    def getCatalog(self):
        '''
        Functie care returneaza catalogul
        :param self:
        @return[list[Statistica]]: Catalogul
        '''
        return self.__repoC.getAll()

    def findStudent(self, id, nume):
        '''
        Functie care cauta un student in lista de studenti
        :param id[int]: id-ul studentului de cautat
        :param nume[string]: numele studentului de cautat
        @return[Student]: Studentul gasit in lista de studenti
        @raises[RepositoryException]: Studentul nu exista in lista de studenti
        '''
        return self.__repoS.findOne(Student(id, nume))

    def findDisciplina(self, id, denumire, profesor):
        '''
        Functie care cauta o disciplina in lista de discipline
        :param id[int]: id-ul disciplinei de cautat
        :param denumire[string]: denumirea disciplinei de cautat
        :param profesor[string]: profesorul disciplinei de cautat
        @return[Disciplina]: Disciplina gasita in lista de discipline
        @raises[RepositoryException]: Disciplina nu exista in lista de discipline
        '''
        return self.__repoD.findOne(Disciplina(id, denumire, profesor))

    def StatsStudentiNume(self, idD, denumire, profesor):
        '''
        Functie care afiseaza lista de studenti cu notele lor la o materie din catalog ordonata dupa nume
        :param idD[int]: id-ul disciplinei
        :param denumire[string]: denumirea disciplinei
        :param profesor[string]: profesorul disciplinei
        @return[list[Statistica]]: Lista ordonata dupa nume
        @raises[ValidationException]: Disciplina este invalida
        '''
        disciplina = Disciplina(idD, denumire, profesor)
        self.__val.validateD(disciplina)
        catalog = self.__repoC.getAll()
        noteDisciplina = []
        for c in catalog:
            if c.getD() == disciplina:
                noteDisciplina.append(c)
        noteDisciplina.sort(key=lambda x: x.getS().getNume())
        return noteDisciplina

    def StatsStudentiNote(self, idD, denumire, profesor):
        '''
        Functie care afiseaza lista de studenti cu notele lor la o materie din catalog ordonata dupa media notelor
        :param idD[int]: id-ul disciplinei
        :param denumire[string]: denumirea disciplinei
        :param profesor[string]: profesorul disciplinei
        @return[list[Statistica]]: Lista ordonata dupa media notelor
        @raises[ValidationException]: Disciplina este invalida
        '''
        disciplina = Disciplina(idD, denumire, profesor)
        self.__val.validateD(disciplina)
        catalog = self.__repoC.getAll()
        noteDisciplina = []
        for c in catalog:
            if c.getD() == disciplina:
                noteDisciplina.append(c)
        noteDisciplina.sort(key=lambda x: x.getMedie())
        return noteDisciplina

    def Stats20(self):
        '''
        Functie care returneaza o lista cu primii 20% din studenti cu media generala cea mai mare
        :param self:
        @return[list[Situatie]]: Lista cu primii 20% studenti ordonata dupa media generala in ordine descrescatoare
        '''
        studenti = self.__repoS.getAll()
        catalog = self.__repoC.getAll()
        stat100 = []

        for s in studenti:
            n = 0
            medie = 0
            for c in catalog:
                if c.getS() == s:
                    medie += int(c.getMedie())
                    n += 1
            stat100.append(Situatie(s, medie // n))
        stat20 = []
        n = (len(stat100) * 20) // 100
        stat100.sort(key=lambda x: x.getMedieGenerala(), reverse=True)
        for i in range(0, n):
            stat20.append(stat100[i])
        return stat20

    def leastPopular(self):
        catalog = self.__repoC.getAll()
        frecv = []
        for x in range(0, 11):
            frecv.append(0)
        for c in catalog:
            for nota in c.getNote():
                frecv[nota] += 1
        minn = 999999
        poz = -1
        for n in range(1, 11):
            if frecv[n] != 0:
                if frecv[n] < minn:
                    minn = frecv[n]
                    poz = n
        return poz

    def randomGenerator(self, nr):
        '''
        Functie care creeaza nr entitati de tip studenti/discipline
        :param nr[int]: numarul de entitati de generat
            @post: Lista de studenti si de discipline creste cu nr(daca nr>0)
        '''
        for _ in range(0, nr):
            idS = int(''.join(random.choice(string.digits) for _ in range(7)))
            numeS = names.get_full_name()
            s = Student(idS, numeS)
            self.__val.validateS(s)
            self.__repoS.store(s)
            idD = int(''.join(random.choice(string.digits) for _ in range(7)))
            denumire = random.choice(self.__randomD)
            profesor = names.get_full_name()
            d = Disciplina(idD, denumire, profesor)
            self.__val.validateD(d)
            self.__repoD.store(d)

    def __merge(self, list1, list2, key, key2):
        result = []

        i = 0
        j = 0

        while i < len(list1) and j < len(list2):
            if key(list1[i]) < key(list2[j]):
                result.append(list1[i])
                i += 1

            elif key(list1[i]) == key(list2[j]):
                if key2(list1[i]) < key2(list2[j]):
                    result.append(list1[i])
                    i += 1

                else:
                    result.append(list2[j])
                    j += 1

            else:
                result.append(list2[j])
                j += 1

        result.extend(list1[i:])
        result.extend(list2[j:])

        return result

    def merge_sort_with_key(self, l, key=lambda x: x, key2=lambda x: x):
        list_len = len(l)

        if list_len <= 1:
            return l

        middle = list_len // 2
        left = l[:middle]
        right = l[middle:]

        sorted_left = self.merge_sort_with_key(left, key, key2)
        sorted_right = self.merge_sort_with_key(right, key, key2)
        return self.__merge(sorted_left, sorted_right, key, key2)

    def __maxMin(self, l, bingoList, key):
        for i in range(1, len(l)):
            if key(bingoList[0]) > key(l[i]):
                bingoList[0] = l[i]
            if key(bingoList[1]) < key(l[i]):
                bingoList[1] = l[i]

        return bingoList

    def bingoSort_with_key(self, l, key=lambda x: x):
        bingo = l[0]
        nextBingo = l[0]
        bingoList = [bingo, nextBingo]
        bingoList = self.__maxMin(l, bingoList, key)
        largestEle = bingoList[1]
        nextElePos = 0

        while(key(bingoList[0]) < key(bingoList[1])):
            startPos = nextElePos
            for i in range(startPos, len(l)):
                if key(l[i]) == key(bingoList[0]):
                    l[i], l[nextElePos] = l[nextElePos], l[i]
                    nextElePos = nextElePos + 1

                elif key(l[i]) < key(bingoList[1]):
                    bingoList[1] = l[i]

            bingoList[0] = bingoList[1]
            bingoList[1] = largestEle

        return l

    def populate(self):
        '''
        Functie care populeaza lista de studenti/discipline si catalogul
        :param self:
        @post: Lista de studenti/discipline si catalogul creste cu 10
        '''
        # Adaugare Studenti:
        self.__repoS.store(Student(1, "Baluta Iustinian-Lucian"))
        self.__repoS.store(Student(2, "Raduletu Petre-Horia"))
        self.__repoS.store(Student(3, "Tunseanu Sorin-Calin"))
        self.__repoS.store(Student(4, "Schintee Mihai"))
        self.__repoS.store(Student(5, "Pane Raul"))
        self.__repoS.store(Student(6, "Hortopan Marius"))
        self.__repoS.store(Student(7, "Dragulescu Ariana"))
        self.__repoS.store(Student(8, "Ianc Andreea"))
        self.__repoS.store(Student(9, "Papulete Daniela"))
        self.__repoS.store(Student(10, "Clenciu Andreea"))
        # Adaugare Discipline
        self.__repoD.store(Disciplina(1, "Informatica", "Eugenia Maria-Ohota"))
        self.__repoD.store(Disciplina(2, "Matematica", "Nanu"))
        self.__repoD.store(Disciplina(3, "Chimie", "Talaba Ioan"))
        self.__repoD.store(Disciplina(4, "Biologie", "Neguleasa Carmen"))
        self.__repoD.store(Disciplina(5, "Muzica", "Secara"))
        self.__repoD.store(Disciplina(6, "Desen", "Plaveti"))
        self.__repoD.store(Disciplina(7, "Fizica", "Sfantu Toma"))
        self.__repoD.store(Disciplina(8, "Istorie", "Fosila"))
        self.__repoD.store(Disciplina(9, "Romana", "Nisu"))
        self.__repoD.store(Disciplina(10, "Engleza", "Sefter"))
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

        self.__repoC.store(stat1)
        self.__repoC.store(stat2)
        self.__repoC.store(stat3)
        self.__repoC.store(stat4)
        self.__repoC.store(stat5)
        self.__repoC.store(stat6)
        self.__repoC.store(stat7)
        self.__repoC.store(stat8)
        self.__repoC.store(stat9)
        self.__repoC.store(stat10)
