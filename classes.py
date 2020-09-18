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

# Geeft de score dictionary.
    def return_scores(self):
        return self.scoredict

# Returnt naam String.
    def return_naam(self):
        return self.naam

# Schrijft het huidige resultaat op in het CSV bestand.
    def schrijf_resultaat(self):
        parsecsv.write_csv(self.scoredict, self.naam)

# De "Vraag" class wordt aangemaakt met een dictionary met antwoorden.
# De format van de dictionary is: { "specialisatie": "vraag" }

class Vraag:
    def __init__(self, antwoorddict):
        self.antwoorddict = {}
        for a in antwoorddict:
            self.antwoorddict[a] = a[0]

# Returnt de antwoord dictionary.
    def return_dict(self):
        return self.antwoorddict

# De "Toetsresultaat" class wordt gebruikt om oude toetsresultaten op te halen.
# Bij __init__ zijn nodig: de scoredict(format als Afnemer class), datum als String
# en de naam als string.

class Toetsresultaat:
    def __init__(self, scoredict, datum, naam):
        self.naam = naam
        self.datum = datetime.datetime.strptime(datum, "%d/%m/%Y %H:%M:%S")
        self.scoredict = scoredict

# Returnt de score dictionary.
    def return_scoredict(self):
        return self.scoredict

# Returnt de datum van afname in datetime formaat.
    def return_datum(self):
        return self.datum

# Returnt de naam van de afnemer als String.
    def return_naam(self):
        return self.naam

class Systeem():
    def __init__(self):
        self.resultaten = parsecsv.read_csv()



Afnemer = Afnemer("bitch")
Afnemer.schrijf_resultaat()
