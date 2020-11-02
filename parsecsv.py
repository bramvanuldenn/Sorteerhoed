import csv
import os
from datetime import datetime


def write_csv(scores, naam):
    dateString = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    if os.stat("data/scores.csv").st_size == 0:
        with open('data/scores.csv', 'w', newline='') as csvfile:
            fieldnames = ['naam', 'datum', 'a', 'b', 'c', 'd']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

    with open('data/scores.csv', 'a', newline='') as csvfile:
        fieldnames = ['naam', 'datum', 'a', 'b', 'c', 'd']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writedict = {
            'naam': naam, 'datum': dateString, 'a': scores['bdm'], 'b': scores['fit'], 'c': scores['se'], 'd': scores['git']
        }
        writer.writerow(writedict)


def read_csv():
    returndict = {}
    with open("data/scores.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            returndict[row[0]] = row[1], row[2], row[3], row[4], row[5]
    csvfile.close()
    return returndict

def read_teksten():
    returndict = {}
    with open("data/teksten.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            returndict[row[0]] = row[1]
    return returndict

def read_vragen():
    vragen = {}
    with open("data/vragen.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            vragen[row[0]] = {
                "BDM": row[1],
                "FIT": row[2],
                "SE": row[3],
                "GIT": row[4]
            }
    return vragen

