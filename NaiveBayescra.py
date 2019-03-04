# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 18:52:56 2019

@author: Alivian
"""
import csv

#Function Write data(result) to CSV
def writeCSV(filename):
    with open(filename, "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerows(zip(result))

#Function Read data from CSV file
def readCSV(filename):
    with open(filename, newline='') as csvfile:
        datacsv = list(csv.reader(csvfile))
    return (datacsv)

#Function Classify data to two classes
def incomeSeparate(dataset):
    separated = {}
    for i in range(1, len(dataset)):
        vector = dataset[i]
        if (vector[-1] not in separated):
            separated[vector[-1]] = []
        separated[vector[-1]].append(vector)
    return separated

#Function to count attribut probability
def countAttribute(dataset, a):
    separated = {}
    for i in range(len(dataset)):
        vector = dataset[i]
        if (vector[a] not in separated):
            separated[vector[a]] = []
        separated[vector[a]].append(vector)
    return separated
    print()

#Read data Train,Count Data Train and assign it to separated variabel
dataTrain = readCSV('TrainsetTugas1ML.csv')
separated = incomeSeparate(dataTrain)

#assign dataTraino (All of attribut to attrib)
attrib = dataTrain[0]

#Make Empty List for data Probability
List2 = []

#Function Probability count and print Probability dataTest
def Probability(dataTrain, attrib, separated):
    for x in separated:
        List1 = []
        print(" P(Income", x, ") =", len(separated[x]), "/", len(dataTrain) - 1, ":",
              len(separated[x]) / (len(dataTrain) - 1))
        for i in [1, 2, 3, 4, 5, 6, 7]:
            attribute = countAttribute(separated[x], i)
            for a in attribute:
                print()
                print("\tP(", attrib[i].upper(), ":", a, ") =", len(attribute[a]), "/", len(separated[x]),
                      len(attribute[a]) / len(separated[x]))
                List1.append([a, len(attribute[a]) / len(separated[x])])
            print()
        List2.append([x, len(separated[x]) / (len(dataTrain) - 1), List1])
    return List2

List2 = Probability(dataTrain, attrib, separated)
print(List2)

#Print Probabiliy Every attribut in >50K and <=50K
for x in List2:
    print("P( Class :", x[0], ") =", x[1])
    for a in x[2]: print("P( Attribute :", a[0], ") =", a[1])
    print()

#Read TestseTugas1ML.csv with readCSV Function and assign to dataTes variable
#Create Result List
dataTest = readCSV('TestsetTugas1ML.csv')
result = []

#This looping to get Probability data (every data) with ID
for data in dataTest[1:]:
    print("====================================")
    print("ID Data :", data[0])
    prob = []
    for x in List2:
        print("P( Class :", x[0], ") =", x[1])
        prb = 1
        for att in data[1:]:
            for p in x[2]:
                if (att == p[0]):
                    prb = prb * p[1]
                    print("\t", att, p[1])
        print("Probabilitas\t= ", prb * x[1])
        prob.append([x[0], prb * x[1]])

    #Print prediction from >50K and <=50k
    print("\nPrediksi\t=", prob)
    #Print Result from Comparison probability >50K and <=50K
    print("Result\t\t= ", end="")
    if (prob[0][1] > prob[1][1]):
        print(prob[0][0]); result.append(prob[0][0])
    else:
        print(prob[1][0]); result.append(prob[1][0])
    print()

#Print all result data from DataTest (40 data)
for x in range(len(result)):
    print(result[x])
#Write result data to csv use writeCSV function
writeCSV('TebakanTugas1ML.csv')