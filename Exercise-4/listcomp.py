"""
Script: listcomp.py
By: L00170982
Purpose: Working on List Comprehensions
Tested on Python v3.10.7; Windows 11
Alpha version: 5th October 2022
"""


newList=[]
newString="Good Day!"
 
#characters of string as elements in list
for letter in newString:
     newList.append(letter)
print(newList)

#collapsing code
newList=[letter for number in newString]
print(newList)

#range as element in list
newList=[number*10 for number in range(0,20)]
print(newList)

#if statement in list allocation
newList=[number*10 for number in range(0,20) if number<10]
print(newList)

#converting depth from feet into meters
conversion=0.3048
depthInFeet=[12.3,13.8,15.3,12.1,8.8]
depthInMeters=[depth*conversion for depth in depthInFeet]
print(depthInMeters)