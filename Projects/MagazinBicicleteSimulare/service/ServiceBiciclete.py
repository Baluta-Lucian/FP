'''
Created on Dec 13, 2022

@author: balut
'''


class ServiceProduse(object):
    '''
    classdocs
    '''

    def __init__(self, repo, val):
        '''
        Constructor
        '''
        self.__repo = repo
        self.__val = val

    def stergeTip(self, tip):
        self.__repo.deleteByTip(tip)

    def stergeMax(self):
        maxx = self.__max()
        self.__repo.deleteByMax(maxx)

    def __max(self):
        maxx = -9999999
        produse = self.getAll()
        for b in produse:
            if b.getPret() > maxx:
                maxx = b.getPret()
        return maxx

    def getAll(self):
        return self.__repo.get_all()
