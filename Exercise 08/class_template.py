"""
Class_template.py
By: Abhinav Tyagi
Date: 02NOV22
"""
class Myfirsttemplate():
	My_attribute1= "This is my first template"
	My_attribute2= "Adding attributes"
	My_attribute3= "this is the last attribute"
	def __init__(self, attribute1: str, attribute2: bool, attribute3: int) -> None:
		print("Constructor working")
		self.attr1 = attribute1
		self.attr2 = attribute2
		self.attr3 = attribute3
object = Myfirsttemplate("Abhinav Tyagi", True, 13)
print(object.attr1, object.attr2, object.attr3)
print(object.My_attribute1, object.My_attribute2, object.My_attribute3)
