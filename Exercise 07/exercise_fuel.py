"""
exercise_fuel.py
By: Abhinav Tyagi
Date: 02NOV22
"""
def calculating_endurance():
	while True:
		try:
			user_input = float(input("Enter the fuel in litres:"))
			user_input1 = float(input("Enter the consumption rate of fuel in litres per minute:"))
			print(f"Remaining endurance: = {user_input/user_input1} minutes")
		except ZeroDivisionError:
			print("Wrong Input")
			continue
		except:
			print("Error!, please enter numerical values only")
		else:
			break
		finally:
			print("")
			break

calculating_endurance()