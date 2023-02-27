'''
Created on Oct 6, 2022

@author: balut
'''
from datetime import timedelta
from datetime import datetime
from datetime import date
import time


def meniu():
    print("1.Problema 3")
    print("2.Fibonacci(Problema 6)")
    print("0.Exit")


def Fibonacci(nr):
    l = [1, 1]
    n = 1
    if nr == 0:
        return 1
    else:
        while l[n] <= nr:
            l.append(l[n] + l[n - 1])
            n = n + 1
        return l[n]


if __name__ == '__main__':
    #    3. Determina o data calendaristica (sub forma an, luna, zi) pornind de
    # la doua numere întregi care reprezintă anul si numărul
    # de ordine al zilei in anul respectiv.
    while True:
        meniu()
        cmd = input("Introduceti functionalitatea: ")
        if cmd == '1':
            an = int(input("Introduceti anul: "))
            if an < 1:
                print("Anul introdus nu este corespunzator!!!\n\n")
                continue
            nr_ordine = int(input("Introduceti nr ordine al zilei din an: "))
            if nr_ordine <= 0 or nr_ordine > 365:
                print("!!!Numarul de ordine trebuie sa fie cuprins intre 1-365!!!\n\n")
                continue
            #seconds = timedelta(years=an, days=nr_ordine)
            date1 = date(an, 1, 1)
            date2 = date.fromordinal(nr_ordine)
            date2 = date2.replace(
                year=date1.year, month=date2.month, day=date2.day)
            print("\n", date2, "\n")
            #req_date = datetime.fromtimestamp()
            # rint(days)
        if cmd == '2':
            numar = int(input("Introduceti un numar natural: "))
            print("Numarul cerut este: ", Fibonacci(numar), "\n\n")
        if cmd == '0':
            break
        else:
            continue
    print("\nExit status 0")
