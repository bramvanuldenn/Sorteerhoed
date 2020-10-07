from classes import *
from PyQt5 import QtWidgets, uic

def naam():
    inputNaam = ui.invoernaam.text()
    return(inputNaam)

def main():
    s = Systeem()
    inputNaam = naam()
    print(f'Je naam is {inputNaam}')
    afnemer = Afnemer(inputNaam)
    print(afnemer.scoredict)
    for i in s.vragen:
        print(i)
        print(s.vragen[i])
        a = {
            "a": 0,
            "b": 1,
            "c": 2,
            "d": 3
        }
        inputAntwoord = str(input()).lower()
        iterdict = iter(s.vragen[i])

        if inputAntwoord in "abcd":
            val = a[inputAntwoord]
            print(val)
            for i in range(0, val):
                next(iterdict)
            a = (next(iterdict))
            print(a)
            afnemer.addto(a)
            print(afnemer.scoredict)
    afnemer.schrijf_resultaat()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication([])
    ui = uic.loadUi("Sorteerhoed.ui")
    ui.show()
    app.exec()
    ui.verzendnaam.clicked.connect(naam)
    main()