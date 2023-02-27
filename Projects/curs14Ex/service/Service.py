'''
Created on Feb 23, 2023

@author: balut
'''


class Service(object):
    '''
    classdocs
    '''

    def __init__(self, repoStuds, repoLabs, val):
        '''
        Constructor
        '''
        self.__repoStuds = repoStuds
        self.__repoLabs = repoLabs
        self.__val = val

    def getAllStudenti(self):
        return self.__repoStuds.getAll()

    def getAllLaboratoare(self):
        return self.__repoLabs.getAll()
