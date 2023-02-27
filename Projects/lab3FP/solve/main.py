'''
Created on Oct 19, 2022

@author: balut
'''
from enum import unique

if __name__ == '__main__':
    #     Se predă în săptămâna 3
    # Scrieti o aplicatie care are interfata utilizator tip consolă cu un meniu:
    # 1 Citirea unei liste de numere intregi
    # 2,3 Gasirea secventelor de lungime maxima care respectă o proprietatea dată. Fiecare student primeste 2 proprietati din lista
    # de mai jos.
    # 4 Iesire din aplicatie.
    # Documentatia să contină:
    #  Scenarii de rulare pentru cele două cerinte primite (vezi curs 1 – scenarii de rulare)
    # Cazuri de testare pentru cele doua cerinte în format tabelar (vezi curs
    #     # 1 – cazuri de testare)
    #     3. Oricare doua elemente consecutive sunt relativ prime intre ele
    # (a, b relativ prime daca si numai daca cmmdc(a,b) = 1).
    # 6. sunt toate distincte intre ele
    def meniu():
        print("1.Citire lista ")
        print("2.Functionalitate 2 ")
        print("3.Functionalitate 3 ")
        print("4.Functionalitate 4 ")
        print("0.Exit!")

    def cmmdc(a, b):
        if a == b:
            return a
        if a > b:
            return cmmdc(a - b, b)
        else:
            return cmmdc(a, b - a)

    def distincte(l):
        max = -999999
        indice_start = 0
        indice_stop = 0
        start_max = 0
        stop_max = -1
        k = 1
        for x in range(0, len(l) - 1):
            y = x + 1
            if l[x] == l[y]:
                k = 1
                indice_start = y
                indice_stop = y
            else:
                k = k + 1
                indice_stop = indice_stop + 1
                if k > max:
                    max = k
                    start_max = indice_start
                    stop_max = indice_stop

        aux = [start_max, stop_max, max]
        return aux

    def unique_items(l):
        output = []
        for x in l:
            if x not in output:
                output.append(x)
        return output

    def distincte_list(l):
        aux = []
        result = []
        k = 0
        max = -1
        for x in range(0, len(l)):
            aux.append(l[x])
            k = k + 1
            aux_list = unique_items(aux)
            if len(aux_list) != len(aux):
                k = k - 1
                if k > max:
                    max = k
                    k = 1
                    result = []
                    for y in aux_list:
                        result.append(y)
                    aux = [l[x]]
                else:
                    k = 1
                    aux = [l[x]]
        if k > max:
            max = k
            k = 0
            result = []
            for y in aux_list:
                result.append(y)
        return result

    def crescatoare_list(l):
        aux = []
        result = []
        max = -1
        for x in range(0, len(l)):
            aux.append(l[x])
            if sorted(aux) != aux:
                if len(aux) - 1 > max:
                    max = len(aux) - 1
                    result = []
                    aux.pop()
                    for y in aux:
                        result.append(y)
                    aux = [l[x]]
                else:
                    aux = [l[x]]
        if len(aux) > max:
            max = len(aux)
            result = []
            for y in aux:
                result.append(y)
        return result

    def print_distincte(l):
        print("Lungimea maxima a secventei: ", len(l))
        print("Secventa: ")
        for i in range(0, len(l)):
            print(l[i], " ")
        print("!!!Sfarsitul secventei!!!\n")

    def relativ_prime(l):
        max = -1
        indice_start = 0
        indice_stop = 0
        start_max = 0
        stop_max = -1
        k = 1
        for x in range(0, len(l) - 1):
            y = x + 1
            if cmmdc(l[x], l[y]) != 1:
                k = 1
                indice_start = y
                indice_stop = y
            else:
                k = k + 1
                indice_stop = indice_stop + 1
                if k > max:
                    max = k
                    start_max = indice_start
                    stop_max = indice_stop

        aux = [start_max, stop_max, max]
        return aux

    def print_secventa(x_start, y_stop, z_len, l):
        print("Lungimea maxima a secventei: ", z_len)
        print("Secventa: ")
        for i in range(x_start, y_stop + 1):
            print(l[i], " ")
        print("!!!Sfarsitul secventei!!!\n")

    def citire_lista(l):
        # l=[]
        x = input("Introduceti numerele din lista separate prin spatiu: ")
        x = x.split(' ')
        for i in x:
            # print(i, " ")
            l.append(int(i))

    def printare_lista(l):
        print("Afisare lista:")
        for i in l:
            print(i, " ")
        print("!!!Sfarsitul afisarii!!!\n")

    def test_f2():
        test_list = [10, 11, 13]
        aux = relativ_prime(test_list)
        assert(aux[0] == 0)
        assert(aux[1] == 2)
        assert(aux[2] == 3)
        test_list = [10, 10, 11]
        aux = relativ_prime(test_list)
        assert(aux[0] == 1)
        assert(aux[1] == 2)
        assert(aux[2] == 2)
        test_list = [10, 20, 30]
        aux = relativ_prime(test_list)
        assert(aux[0] == 0)
        assert(aux[1] == -1)
        assert(aux[2] == -1)

    def test_f3():
        test_list = [10, 11, 13]
        aux = distincte_list(test_list)
        assert(aux == test_list)
        test_list = [10, 10, 220]
        aux = distincte_list(test_list)
        assert(aux == [10, 220])
        test_list = [10, 10, 10]
        aux = distincte_list(test_list)
        assert(aux == [10])

    def run():
        l = []
        test_ist = [10]
        assert(sorted(test_ist) == test_ist)
        test_f2()
        test_f3()
        while True:
            meniu()
            cmd = input("Introduceti functionalitatea: ")
            if cmd == "1":
                l = []
                citire_lista(l)
                printare_lista(l)
            elif cmd == "2":
                aux = relativ_prime(l)
                print_secventa(aux[0], aux[1], aux[2], l)
            elif cmd == "3":
                print_distincte(distincte_list(l))
            elif cmd == "4":
                aux = crescatoare_list(l)
                print_distincte(aux)
            elif cmd == "0":
                print("\n!!!Am iesit din aplicatie!!!\n")
                break
            else:
                print("!!!COMANDA INVALIDA!!!\n\n")

    run()
    print("Returned 0")
    exit()
