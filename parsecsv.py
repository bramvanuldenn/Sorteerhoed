import csv
import os
from datetime import datetime

scores = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
}
naam = "bram van ulden"

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
        writer.writerow({
            'naam': naam, 'datum': dateString, 'a': scores['a'], 'b': scores['b'], 'c': scores['c'], 'd': scores['d']
        })


def read_csv():
    returndict = {}
    with open("data/scores.csv", "r") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            returndict[row[0]] = row[1], row[2], row[3], row[4], row[5]
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
                "IT": row[4]
            }
    return vragen

