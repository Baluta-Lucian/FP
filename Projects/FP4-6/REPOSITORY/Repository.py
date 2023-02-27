'''
Created on Oct 26, 2022

@author: balut
'''


class Repository(object):
    '''
    classdocs
    REPREZENTARE PRIN DICTIONAR############################################################################3
    '''

    def __init__(self):
        '''
        Constructor

        :param self.numbers: lista de numere complexe
        '''
        self.numbers = {'0': []}
        self.dataList = {'0': []}

    def store(self, cn):
        '''
        Functie care adauga un numar complex la finalul listei de numere complexe
        :param cn: -> numar complex de adaugat
            @post: -> Lungimea listei creste cu 1
        '''
        self.dataList['0'].append(self.numbers['0'][:])
        self.numbers['0'].append(cn)

    def undo(self):
        '''
        Lista preia forma anterioara
        :param self:
        @exception[ValueError]: Lista e la forma originala
        '''
        if len(self.dataList['0']) == 0:
            raise ValueError("!!!List is at the original state!!!")
        self.numbers['0'] = self.dataList['0'].pop()

    def indexStore(self, cn, index):
        '''
        Functie care adauga un numar complex la un anume indice listei de numere complexe
        :param cn: -> numar complex de adaugat
        :param index: -> indexul unde dorim sa adaugam in lista
            @post: -> Lungimea listei creste cu 1
        @exception[ValueError] : Indexul este invalid
        '''

        if index < 0 or index > len(self.numbers['0']):
            raise ValueError("!!!Index out of range!!!")

        self.dataList['0'].append(self.numbers['0'][:])

        if index == len(self.numbers['0']):
            self.store(cn)

        else:
            self.numbers['0'].insert(index, cn)

#     #iteratia 2
#     • Șterge element de pe o poziție dată.
# • Șterge elementele de pe un interval de poziții.
# • Înlocuiește toate aparițiile unui număr complex cu un alt număr

    def indexDelete(self, index):
        '''
        Functie care elimina de la un anumit index un numar complex din lista de numere complexe
        :param index: -> indexul de unde dorim sa eliminam
            @post: Lungimea listei scade cu 1
        @return[ComplexNumber]: returneaza numarul complex eliminat
        @exception[ValueError]: Indexul este invalid
        '''
        if index < -1 or index >= len(self.numbers['0']):
            raise ValueError("!!!Index out of range!!!")

        self.dataList['0'].append(self.numbers['0'][:])
        deleted_item = self.numbers['0'].pop(index)
        return deleted_item

    def rangeDelete(self, start_index, stop_index):
        '''
        Functie care elimina dintr-un anumit interval de pozitii numere complexe din lista de numere complexe
        :param start_index: -> indexul de inceput al intervalului
        :param stop_index: -> indexul de sfarsit al intervalului
            @post: Lungimea listei scade cu stop_index-start_index
        @return[list[ComplexNumber]]: returneaza o lista cu numerele complexe eliminate
        @exception[ValueError]: Interval invalid
        '''
        # 0 1 2 3 4
        if start_index < 0 or start_index >= len(self.numbers['0']):
            # 1 2 3 4 5
            if stop_index < start_index or stop_index >= len(self.numbers['0']):
                raise ValueError("!!!Start and Stop index out of range!!!")
            raise ValueError("!!!Start index out of range!!!")
        if stop_index < start_index or stop_index >= len(self.numbers['0']):
            raise ValueError("!!!Stop index out of range!!!")
        # Future tests
        self.dataList['0'].append(self.numbers['0'][:])
        deleted_items = self.numbers['0'][start_index:(stop_index + 1)]
        del self.numbers['0'][start_index:(stop_index + 1)]
        return deleted_items

    #
    def find(self, cn):
        '''
        Functie care verifica daca un numar complex exista deja in lista
        :param cn[ComplexNumber]: -> numarul complex de verificat daca exista in lista
        @exception[ValueError]: Numarul nu exista in lista de numere complexe
        '''
        if len([i for i in self.numbers['0'] if i == cn]) == 0:
            raise ValueError("!!!Numarul complex ales nu exista in lista!!!")

    def setAllUnique(self, cn, ot):
        '''
        Functie care inlocuiește toate aparițiile unui număr complex cu un alt număr complex.
        :param cn[ComplexNumber]: -> Numarul complex pe care vrem sa-l inlocuim
        :param ot[ComplexNumber]: -> Numarul cu care vrem sa inlocuim
            @post: Elementele de tip cn iau valoarea ot
        @return[int]: Numarul de elemente schimbate
        @errors[ValueError]: cn nu exista 
        '''
        self.find(cn)
        self.dataList['0'].append(self.numbers['0'][:])
        changed = 0
        for i in self.numbers['0']:
            if i == cn:
                i.setReal(ot.getReal())
                i.setImaginar(ot.getImaginar())
                changed = changed + 1
        return changed

    def getAll(self):
        '''
        Functie care returneaza o copie a listei de numere complexe
        :param self.number[list[ComplexNumber]]: lista de numere complexe
        @return[list[ComplexNumber]]: Lista numerelor complexe
        '''
        return self.numbers['0']


'''REPREZENTARE PRIN LISTA'''
#     #iteratia 1
#     1. Adaugă număr în listă.
# • Adaugă număr complex la sfârșitul listei
# • Inserare număr complex pe o poziție dată.

#     def __init__(self):
#         '''
#         Constructor
#
#         :param self.numbers: lista de numere complexe
#         '''
#         self.numbers = []
#         self.dataList = []
#
#     def store(self, cn):
#         '''
#         Functie care adauga un numar complex la finalul listei de numere complexe
#         :param cn: -> numar complex de adaugat
#             @post: -> Lungimea listei creste cu 1
#         '''
#         self.dataList.append(self.numbers[:])
#         self.numbers.append(cn)
#
#     def undo(self):
#         '''
#         Lista preia forma anterioara
#         :param self:
#         @exception[ValueError]: Lista e la forma originala
#         '''
#         if len(self.dataList) == 0:
#             raise ValueError("!!!List is at the original state!!!")
#         self.numbers = self.dataList.pop()
#
#     def indexStore(self, cn, index):
#         '''
#         Functie care adauga un numar complex la un anume indice listei de numere complexe
#         :param cn: -> numar complex de adaugat
#         :param index: -> indexul unde dorim sa adaugam in lista
#             @post: -> Lungimea listei creste cu 1
#         @exception[ValueError] : Indexul este invalid
#         '''
#
#         if index < 0 or index > len(self.numbers):
#             raise ValueError("!!!Index out of range!!!")
#
#         self.dataList.append(self.numbers[:])
#
#         if index == len(self.numbers):
#             self.store(cn)
#
#         else:
#             self.numbers.insert(index, cn)
#
# #     #iteratia 2
# #     • Șterge element de pe o poziție dată.
# # • Șterge elementele de pe un interval de poziții.
# # • Înlocuiește toate aparițiile unui număr complex cu un alt număr
#
#     def indexDelete(self, index):
#         '''
#         Functie care elimina de la un anumit index un numar complex din lista de numere complexe
#         :param index: -> indexul de unde dorim sa eliminam
#             @post: Lungimea listei scade cu 1
#         @return[ComplexNumber]: returneaza numarul complex eliminat
#         @exception[ValueError]: Indexul este invalid
#         '''
#         if index < -1 or index >= len(self.numbers):
#             raise ValueError("!!!Index out of range!!!")
#
#         self.dataList.append(self.numbers[:])
#         deleted_item = self.numbers.pop(index)
#         return deleted_item
#
#     def rangeDelete(self, start_index, stop_index):
#         '''
#         Functie care elimina dintr-un anumit interval de pozitii numere complexe din lista de numere complexe
#         :param start_index: -> indexul de inceput al intervalului
#         :param stop_index: -> indexul de sfarsit al intervalului
#             @post: Lungimea listei scade cu stop_index-start_index
#         @return[list[ComplexNumber]]: returneaza o lista cu numerele complexe eliminate
#         @exception[ValueError]: Interval invalid
#         '''
#         # 0 1 2 3 4
#         if start_index < 0 or start_index >= len(self.numbers):
#             # 1 2 3 4 5
#             if stop_index < start_index or stop_index >= len(self.numbers):
#                 raise ValueError("!!!Start and Stop index out of range!!!")
#             raise ValueError("!!!Start index out of range!!!")
#         if stop_index < start_index or stop_index >= len(self.numbers):
#             raise ValueError("!!!Stop index out of range!!!")
#         # Future tests
#         self.dataList.append(self.numbers[:])
#         deleted_items = self.numbers[start_index:(stop_index + 1)]
#         del self.numbers[start_index:(stop_index + 1)]
#         return deleted_items
#
#     #
#     def find(self, cn):
#         '''
#         Functie care verifica daca un numar complex exista deja in lista
#         :param cn[ComplexNumber]: -> numarul complex de verificat daca exista in lista
#         @exception[ValueError]: Numarul nu exista in lista de numere complexe
#         '''
#         if len([i for i in self.numbers if i == cn]) == 0:
#             raise ValueError("!!!Numarul complex ales nu exista in lista!!!")
#
#     def setAllUnique(self, cn, ot):
#         '''
#         Functie care inlocuiește toate aparițiile unui număr complex cu un alt număr complex.
#         :param cn[ComplexNumber]: -> Numarul complex pe care vrem sa-l inlocuim
#         :param ot[ComplexNumber]: -> Numarul cu care vrem sa inlocuim
#             @post: Elementele de tip cn iau valoarea ot
#         @return[int]: Numarul de elemente schimbate
#         @errors[ValueError]: cn nu exista
#         '''
#         self.find(cn)
#         self.dataList.append(self.numbers[:])
#         changed = 0
#         for i in self.numbers:
#             if i == cn:
#                 i.setReal(ot.getReal())
#                 i.setImaginar(ot.getImaginar())
#                 changed = changed + 1
#         return changed
#
#     def getAll(self):
#         '''
#         Functie care returneaza o copie a listei de numere complexe
#         :param self.number[list[ComplexNumber]]: lista de numere complexe
#         @return[list[ComplexNumber]]: Lista numerelor complexe
#         '''
#         return self.numbers
