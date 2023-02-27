'''
Created on Oct 26, 2022

@author: balut
'''
"""
Fiecare student primește o problemă din lista de mai jos.
Cerințe generale:
• Folosiți procesul de dezvoltare: Incrementală bazată pe funcționalități (vezi
curs 1) și Dezvoltare dirijată de teste (curs 2)
• Planificați iterații pentru 3 laboratoare succesive. În fiecare săptămână primiți
o notă pentru ce s-a realizat pentru iterația din săptămâna curentă.
• Prima iterație trebuie sa conțină cel puțin 3 cerințe (din funcționalitățile 3-5)
• Documentația trebuie să conțină: enunțul, lista de funcționalități, planul de
iterații, scenarii de rulare, lista de taskuri (activități)
• Toate funcțiile trebuie să includă specificații, toate funcțiile trebuie sa fie
testate (funcții de test cu assert) în afară de partea cu interacțiunea utilizator.
• Separați partea de interfață utilizator de restul aplicației (sa nu aveți funcții
care fac 2 lucruri: un calcul + tipărire/citire)
• La prima iterație se cere o soluție procedurală (mai multe funcții toate în
același modul), varianta finală trebuie să fie modulară (curs 3)
utilizator.
• Datele de intrare trebuie validate, programul semnalează erorile către
"""

from SERVICE.Service import Service
#from DOMAIN.entities import ComplexNumber
from REPOSITORY.Repository import Repository
from VALIDATION.Validator import Validator
from UI.UI import Console
from Utility.Functions import Helpers
from TEST.Tester import GodTester

if __name__ == '__main__':
    repo = Repository()
    val = Validator()
    help = Helpers()
    serv = Service(repo, val, help)
    ui = Console(serv)
    tester = GodTester()
    tester.TestAll()
    ui.startUI()

    print("\nReturned 0")
