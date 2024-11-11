# This is a terminal game about capitals of the world

import csv
import random
import os
from importlib import resources
print(os.getcwd())
from capitals import data

file = resources.files(data) / 'capitais.csv'

def run():
    capitais = {}

    with open(file, newline='') as csvfile:
        capreader = csv.reader(csvfile)
        for row in capreader:
            capitais[row[0]] = row[1]

    capitais.pop("Country")
    country, capital = random.choice(list(capitais.items()))
    print("What's the capital of {}?".format(country))
    answer = input().capitalize()
    if answer == capital.capitalize():
        print("That's correct!")
    else:
        print("You failed! It was {}".format(capital))
