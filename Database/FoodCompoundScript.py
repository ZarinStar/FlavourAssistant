## FoodCompoundScript

import pandas as pd
import json

compoundFile = "Compound.json"
foodFile = "Food.json"

columnList = []
compoundData = []
#for line in open('tweets.json', 'r'):
#    tweets.append(json.loads(line))

#step 1:
#Create columns based on the "name" variable (or the "id" variable) from Compound.json in a new csv file.
for line in open(compoundFile, 'r'):
	#data = json.load(f)
	compoundData.append(json.loads(line)) #processes every json object as string, not ideal
	#for i in compoundData['id']:
	#	columnList.append(i)

print(compoundData[0])#test
#print(columnList[0]) #test

#step 2: 
#Create rows based on the "name" variable (or the "id" variable) from Food.json.