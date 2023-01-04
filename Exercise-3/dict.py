"""
Script: dict.py
By: L00170982
Purpose: Working on Dictionaries
Tested on Python v3.10.7; Windows 11
Alpha version: 5th October 2022
"""

newDictionary = {"FName":"Abhinav", "SName":"Tyagi", "Lnumber":"L00170982", "Course":"MSc in Computing in Cloud Technologies"}
print(newDictionary)

#Extracting specific information
#print(newDictionary["Lnumber"],"\t",newDictionary{"Course"])

#adding top dcitionary
#newDictionary["module"]="Infrastructure as Code"
#print(newDictionary)

#changing value of specific key
newDictionary["module"]="IAC"
#print(newDictionary)

#getting all values
print(newDictionary.values())

#getting all items
print(newDictionary.items())