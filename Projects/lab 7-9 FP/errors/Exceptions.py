'''
Created on Nov 10, 2022

@author: balut
'''


class ValidationException(Exception):
    '''
    classdocs
    '''
    pass


class CatalogException(Exception):
    pass


class RepositoryException(Exception):
    pass
    # def __init__(self, msg):
    #     self.__msg= msg
    #
    # def getMessage(self):
    #     return self.__msg
    #
    # def __str__(self):
    #     return 'Repository Exception: ' + str(self.__msg)
    #


#
# class StudentNotFoundException(RepositoryException):
#     def __init__(self):
#         RepositoryException.__init__(self, "!!!Studentul nu a fost gasit!!!")
#
# class DisciplinaNotFoundException(RepositoryException):
#     def __init__(self):
#         RepositoryException.__init__(self, "!!!Disciplina nu a fost gasita!!!")
