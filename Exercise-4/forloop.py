"""
Script: forloop.py
By: L00170982
Purpose: Working on For loops
Tested on Python v3.10.7; Windows 11
Alpha version: 5th October 2022
"""

iterable_variable=[5,3,7,3,8,9]

#for loop
for item in iterable_variable:
	print(item, end=" ")
print("\n")

#arithmetic operation inside for loop
total=0
for item in iterable_variable:
	total+=item
print(total)

#if statement as condition in for loop
for item in iterable_variable:
	if item %2!=0:
		print(item)
print("\n")

for letter in "Abhinav Tyagi":
	if letter == "i":
		print(f"Found letter {letter}")
		break
	else:
		print(f"Don't want {letter}")
#pass, continue, break
newList=[1,2,3,0]
for number in newList:
	if number==1:
		pass
	if number==2:
		continue
	if number==3:
		print(f"Found number {number}")
	if number==0:
		break

#tuples
tuples=[(1,2),(3,4),("A","B")]
for items in tuples:
	print(items)

#tuple unpacking
for a,b in tuples:
	print(a,"\n",b)

#range
for index in range(5,30,6):
	print(index, end=",")
		 
