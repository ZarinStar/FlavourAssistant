## FoodCompoundScript

import pandas as pd
import json
import csv

compoundFile = "Compound.json"
foodFile = "Food.json"
csvFile = "FoodMatrix.csv"

columnList = []
columnList.append("") #blank for first columm
compoundDict = []

#step 1: Create columns based on the "name" variable (or the "id" variable) from Compound.json in a new csv file.
for line in open(compoundFile, 'r'):
	compoundDict.append(json.loads(line)) #processes every json object as dict

for i in range(len(compoundDict)):
	key = compoundDict[i]
	value = key.get("id")
	validate = key.get("klass") #"klass":"Flavonoids"
	if validate == "Flavonoids":
		columnList.append(value) #we only care about compounds in the Flavonoids klass

# open the file in the write mode for the column headers (first row)
f = open(csvFile, 'w')
writer = csv.writer(f)
writer.writerow(columnList)
f.close()

#step 2: Create rows based on the "name" variable (or the "id" variable) from Food.json.