'''
Created on Dec 14, 2022

@author: balut
'''


class ServiceCafenea(object):
    '''
    classdocs
    '''

    def __init__(self, repo):
        '''
        Constructor
        '''
        self.__repo = repo

    def filter(self, tara, pret):
        cafenele = self.__repo.get_all()
        required = []
        for c in cafenele:
            if c.getTara() == tara:
                if c.getPret() < pret:
                    required.append(c)
        return required

    def getAll(self):
        return self.__repo.get_all()

    def sortByTara(self):
        cafenele = self.__repo.get_all()
        cafenele.sort(key=lambda x: x.getTara())
        return cafenele

    def sortByPret(self, tara):
        tara.sort(key=lambda x: x.getPret(), reverse=True)
        return tara
