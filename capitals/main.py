# This is a terminal game about capitals-now of the world

import csv
import random

def run():
    capitais = {}
    with open('../capitais.csv', newline='') as csvfile:
        capreader = csv.reader(csvfile)#, delimiter=' ', quotechar='"')
        for row in capreader:
            capitais[row[0]] = row[1]


    country, capital = random.choice(list(capitais.items()))
    print("What's the capital of {}?".format(country))
    answer = input().capitalize()
    if answer == capital.capitalize():
        print("That's correct!")
    else:
        print("You failed! It was {}".format(capital))
