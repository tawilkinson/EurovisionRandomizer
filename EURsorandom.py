import os
import csv
import random
import copy
from collections import defaultdict
outdict = {}
duplicate_dict = defaultdict(lambda:1)

def randomizer(names, country_list):
    random.shuffle(country_list)
    num_processed = 0
    attempts = 0
    for name in names:
        try:
            key = country_list[-1]
            if key in outdict.keys():
                attempts += 1
                count = duplicate_dict[key] + 1
                duplicate_dict[key] = count
                key += " (" + str(count) + ")"
            country_list.pop()
            outdict[key] = name
            num_processed += 1
        except IndexError:
            pass
    return num_processed, attempts

def EURandom():
    countries = "eurovision2019.participants"
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

    n_countries = len(clist)
    print("Number of Countries: {0}".format(n_countries))

    ninput = input("Enter names file (empty uses default): ")

    if ninput:
        names = ninput

    with open(names, newline='') as csvfile:
        nreader = csv.reader(csvfile, delimiter=',')
        for row in nreader:
            nlist.append(row[0])

    # randomise people in case you are running this repeatedly
    random.shuffle(nlist)
    # check if there will be duplicates
    n_people = len(nlist)
    print("Number of People: {0}".format(n_people))

    if n_people > n_countries:
        print("Too many people. There will be duplicates...")
        print("(Number of duplicates counted in brackets)")

    random.seed()
    processed = 0
    total_attempts = 0
    while True:
        count, attempts = randomizer(nlist[:n_countries], clist.copy())
        processed += count
        total_attempts += attempts
        if processed >= n_people:
            break
        for i in range(count):
            nlist.pop(0)

    out = ""
    n = 0
    for i, j in outdict.items():
        n += 1
        out += (str(n) + " " + j + ": " + i + "\n")

    out += "Total Duplicates: {0}\n".format(total_attempts)
    print(out)

    # out = "Year: {0}\nNumber of Countries: {1}\nNumber of People: {2}\n\n"\
    out = "Number of Countries: {0}\nNumber of People: {1}\n\n"\
        .format(n_countries, n_people) + out
    # out += "Total: {0}\n".format(len(outdict))

    f = open("output.txt", 'w')
    f.write(out)
    f.close


EURandom()
