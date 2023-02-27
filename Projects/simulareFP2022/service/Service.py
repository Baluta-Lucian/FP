'''
Created on Dec 14, 2022

@author: balut
'''


class ServiceClasament(object):
    '''
    classdocs
    '''

    def __init__(self, repoE, repoM):
        '''
        Constructor
        '''
        self.__repoE = repoE
        self.__repoM = repoM

    def cautareEcipe(self, sponsor):
        '''
        Functie care cauta toate echipele cu un anumit sponsor dat de utilizator
        :param sponsor[str]: sponsorul dat de utilizator
        @return[list[Echipa]]: lista de echipe care au sponsorul cerut
        '''
        cerinta = []
        echipe = self.__repoE.get_all()
        for e in echipe:
            if e.getSponsor() == sponsor:
                cerinta.append(e)
        return cerinta

    def __getGolaveraj(self, e):
        '''
        Functie care calculeaza golaverajul unei echipe(nr de goluri marcare in cazul nostru)
        :param e[str]: Denumirea echipei de calculat golaverajul
        @return[int]: golaverajul echipei
        '''
        golaveraj = 0
        for m in self.__repoM.get_all():
            if m.getE1() == e:
                golaveraj += m.getG1()
            elif m.getE2() == e:
                golaveraj += m.getG2()
        return golaveraj

    def __meciuriCastigate(self, e):
        '''
        Functie care calculeaza cate meciuri a castigat o echipa
        :param e[str]: denumirea echipei de calculat meciurile castigate
        @return[int]: numarul de meciuri castigate
        '''
        meciuriCastigate = 0
        for m in self.__repoM.get_all():
            if m.getE1() == e:
                if m.getG1() > m.getG2():
                    meciuriCastigate += 1
            elif m.getE2() == e:
                if m.getG2() > m.getG1():
                    meciuriCastigate += 1
        return meciuriCastigate

    def clasamentEchipe(self):
        '''
        Functie care afiseaza clasamentul(ordine descrescatoare a meciurilor castigate, altfel->
        ->dupa golaveraj, altfel -> alfabetic dupa numele echipei)
        :param self:
        @return[list[Echipa]]: lista sortata dupa cerinta
        '''
        echipe = self.__repoE.get_all()
        for x in range(0, len(echipe)):
            for y in range(x + 1, len(echipe)):
                if self.__meciuriCastigate(echipe[x].getEchipa()) < self.__meciuriCastigate(echipe[y].getEchipa()):
                    t = echipe[x]
                    echipe[x] = echipe[y]
                    echipe[y] = t
                elif self.__meciuriCastigate(echipe[x].getEchipa()) == self.__meciuriCastigate(echipe[y].getEchipa()):
                    if self.__getGolaveraj(echipe[x].getEchipa()) < self.__getGolaveraj(echipe[y].getEchipa()):
                        t = echipe[x]
                        echipe[x] = echipe[y]
                        echipe[y] = t
                    elif self.__getGolaveraj(echipe[x].getEchipa()) == self.__getGolaveraj(echipe[y].getEchipa()):
                        if echipe[x].getEchipa() > echipe[y].getEchipa():
                            t = echipe[x]
                            echipe[x] = echipe[y]
                            echipe[y] = t
        return echipe

    def getAllEchipe(self):
        '''
        Functie care returneaza lista de echipe
        :param self:
        @return[list[Echipa]]: lista de echipe
        '''
        return self.__repoE.get_all()

    def getAllMeciuri(self):
        '''
        Functie care returneaza lista de meciuri
        :param self:
        @return: [list[Meci]]: lista de meciuri
        '''
        return self.__repoM.get_all()
