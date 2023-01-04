"""
Script: functions.py
By: L00170982
Purpose: Working on Functions, passing and returning values
Tested on Python v3.10.7; Windows 11
Alpha version: 5th October 2022
"""

#function to calculate circumference of circle
def circumference(radius=1)->float:
	"""
		Calcilate the circumferenceof circleby taking its radius
		Default radius=1 if no valuse is provided
		Return float value
    """
	return 2*3.142*radius
	
#getting radius as input as string
r=input("Provide a value for radius of circle: ")

#convert radius from string to float
rf=float(r)

#circumference function call
cir=circumference(rf)

print(f"Radius ={r}, Circumference = {cir:1.3f}")

#passing unknown no of arguments to function
def adder(*numbers: int)->int:
	"""
	    Calculation of the sum all provided as arguments
		integer type values is passed in argument
		Return integer value
	"""
	final=0
	for number in numbers:
		final+=number
	return final
	
print(f"Adding numbers: 12,45,42,6,78 = {adder(12,45,42,6,78)}")
#tuple unpacking, p=price, mP=maximumprice,I=item
def expensive(p):
	#valiable set up
	mP=0
	mPI=""
	
    #iterating and unpacking tuple
	for description,price in p:
	    #if p is maximum then record it in variable
		if price>mP:
			mP=price
			mPI=description
		#if price is not maximum then do nothing
		else:
			pass
	#return maximumprice and I
	return mP, mPI
p=[("Notebboks",2.0),("Pen",1.3),("Pencil",0.90)]
#calling function
mprice,product = expensive(p)
print(f"List of Is : {p}")
print(f"Maximum price I : {product}, and it's price : {mprice}")

