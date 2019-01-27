import os
import csv
import random
from datetime import datetime


def EURandom():
    # now = datetime.now()
    countries = "eurovision2018.finalists"
    names = "names.txt"
    clist = []
    nlist = []

    cinput = input("Enter countries file (empty uses default): ")

    if cinput:
        countries = cinput

    with open(countries, newline='') as csvfile:
        creader = csv.reader(csvfile, delimiter=',')
        for row in creader:
            clist.append(row[0])

    cdict = dict(enumerate(clist))
    n_countries = len(cdict)
    print("Number of Countries: {0}".format(n_countries))

    ninput = input("Enter names file (empty uses default): ")

    if ninput:
        names = ninput

    with open(names, newline='') as csvfile:
        nreader = csv.reader(csvfile, delimiter=',')
        for row in nreader:
            nlist.append(row[0])

    n_people = len(nlist)
    print("Number of People: {0}".format(n_people))
    toomany = False

    if n_people > n_countries:
        print("Too many people. There will be duplicates...")
        print("(Number of duplicates counted in brackets)")
        toomany = True

    random.seed()
    outdict = {}
    nums = []
    attempt = 0
    for i in nlist:
        while True:
            num = random.randrange(1, len(cdict))
            if num not in nums:
                nums.append(num)
                outdict[cdict.get(num)] = i
                break
            elif toomany:
                attempt += 1
                key = cdict.get(num) + " (" + str(attempt) + ")"
                outdict[key] = i
                break
            else:
                pass

    out = ""
    n = 0
    for i, j in outdict.items():
        n += 1
        out += (str(n) + " " + j + ": " + i + "\n")

    if toomany:
        out += "Total Duplicates: {0}\n".format(attempt)
    print(out)

    # out = "Year: {0}\nNumber of Countries: {1}\nNumber of People: {2}\n\n"\
    out = "Number of Countries: {0}\nNumber of People: {1}\n\n"\
        .format(n_countries, n_people) + out
    # out += "Total: {0}\n".format(len(outdict))

    f = open("output.txt", 'w')
    f.write(out)
    f.close


EURandom()
