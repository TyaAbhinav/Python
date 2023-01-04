"""
Script: tuples.py
By: L00170982
Purpose: Working on Tuples
Tested on Python v3.10.7; Windows 11
Alpha version: 5th October 2022
"""

newTuple = ("one", "diff", "example", "one")
print(newTuple)

#type
print(type(newTuple), "\n")

#count
print("Count of 'one'\t\t:", newTuple.count("one"))

#index
print("Position of 'diff'\t", newTuple.index("diff"))

#getting specific element
print(newTuple[2])