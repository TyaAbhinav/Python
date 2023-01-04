"""
oo2.py
By: Abhinav Tyagi
Date: 02NOV22
"""
class MyTemplate():
	#Define a class object attribute, it will be the same for any instance of the class
	class_object_attribute1 = 6378137
	class_object_attribute2 = 6356752 
	#Constructor, called whenever an instance of the class is created.
	def __init__(self, attribute1: str, attribute2: bool) -> None:
		print("Constructor ran")
		#Take in an argument and assign it to a meaningful attribute name
		self.attr1 = attribute1
		self.attr2 = attribute2
#Instantiate the class
my_object = MyTemplate("Abhinav",True)
#Check the object and type
print(my_object.class_object_attribute1, my_object.class_object_attribute2)