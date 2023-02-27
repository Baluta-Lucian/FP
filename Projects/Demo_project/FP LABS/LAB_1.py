'''
Created on Aug 2, 2022

@author: balut
'''
from _ast import If

if __name__ == '__main__':
    # LAB 1
    # 1:Calculati suma a n numere naturale
    # 2:Verificati daca un numar citit de la tastatura este prim
    # 3:Calculati cel mai mare divizor comun a doua numere

    # 1:
    s = 0
    i = int(input("citeste un numar:"))
    while i > 0:
        n = int(input())
        s = s + n
        i = i - 1
    print("suma numerelor naturale este: ", s)
