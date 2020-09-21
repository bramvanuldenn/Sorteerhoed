import datetime
from Sorteerhoed import parsecsv

# De class Afnemer is de persoon die op het moment de applicatie open heeft en de toets maakt.
# Alleen de naam is nodig voor het aanmaken van deze Class. De Class slaat ook de toetsscores
# in een dictionary op.

class Afnemer:
    def __init__(self, naam):
        self.naam = naam
        self.scoredict = {
            "a": 0,
            "b": 0,
            "c": 0,
            "d": 0,
        }

# Afnemer.addTo("a") - voegt een score van 1 toe aan de Afnemers algemene score.
# De argument is een String met als naam de dictionary key van een van de specialisaties.
    def addTo(self, dictKey):
        self.scoredict[dictKey] += 1

# Schrijft het huidige resultaat op in het CSV bestand.
    def schrijf_resultaat(self):
        parsecsv.write_csv(self.scoredict, self.naam)


# De "Toetsresultaat" class wordt gebruikt om oude toetsresultaten op te halen.
# Bij __init__ zijn nodig: de scoredict(format als Afnemer class), datum als String
# en de naam als string.

class Toetsresultaat:
    def __init__(self, scoredict, datum, naam):
        self.naam = naam
        self.datum = datetime.datetime.strptime(datum, "%d/%m/%Y %H:%M:%S")
        self.scoredict = scoredict


# Returnt de datum van afname in string formaat.
    def return_datum(self):
        return self.datum.strftime("%d/%m/%Y %H:%M:%S")


class Systeem():
    def __init__(self):
        self.vragen = parsecsv.read_vragen()
        self.resultaten = {}
        b = 0
        parsedData = parsecsv.read_csv()
        for i in parsedData:
            a = parsedData[i]
            scoredict = {
                "a": a[1],
                "b": a[2],
                "c": a[3],
                "d": a[4],
            }
            self.resultaten[b] = Toetsresultaat(scoredict, a[0], i)
            b += 1

    def return_vraag(self, nummer):
        return self.vragen[nummer]


