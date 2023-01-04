"""
program name: lists.py
Student no: L00170982
Aim: Working on Lists
Version Python v3.10.7; Windows 11
Tested on: 7th October 2022
"""

#to create a new list
List1=[2,4,6,"X","Y","Z"]
print("1st list=", List1)

#to find out the total length of list
print("total length=", len(List1))

#getting an element
print("4th charcater of the list=", List1[3])

#to concatenate a list
List2=[3,"P","Q",3,"word"]
print("2nd list=",List2)

#to concatenateboth list alltogether
print("Concate both list=", List1+List2)

#to create listoflist
print("Nested list=", [List1,List2])

#to change a specific element in the list
List2[4]="word 1"
print("changed second list=", List2)

#to append a list
List2.append(" extra word")
print("New appended list=", List2)

#insert
List1.insert(5,"A")
print("Insert to first list=", List1)

#extend
List1.extend([8,9,"B"])
print("Extend first list=", List1)

#remove
List1.remove("Y")
print("Removing 'Y'=", List1)

#pop
print("Pop =", List2.pop(),"second list=",List2)

#count
print("Repetition of '3'=", List2.count(3))

#reverse
List2.reverse()
print("Reversed second list=", List2)


