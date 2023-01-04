"""
oo1.py
By: Abhinav Tyagi
Date: 02NOV22
"""
#Create a class
class MyfirstClass():

	#Constructor, called whenever an instance of the class is created.
	def __init__(self, my_greeting):
		print("Running constructor for MyfirstClass")
		#Create attributes and set initial values
		self.message = my_greeting
		
	def my_method(self):
		print(self.message)
my_class1 = MyfirstClass("Hello Fella")
my_class1.my_method()
print(type(my_class1))
my_class2 = MyfirstClass("It's a lovely day")
my_class2.my_method()
print(type(my_class2))