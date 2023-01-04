"""
mytime.py
By: Abhinav Tyagi
Date: 02NOV22
"""
from datetime import datetime as dt
#Get the current time, returns a value like 2022-10-09 17:46:45.151666
today = dt.now().strftime("%d")
weekday = dt.now().strftime("%A")
month = dt.now().strftime("%B")
year = dt.now().strftime("%Y")
hours = dt.now().strftime("%I")
locate = dt.now().strftime("%p")
minute = dt.now().strftime("%M")
seconds= dt.now().strftime("%S")
print(f"Date : {year} {month} {today}, {weekday}")
print(f"Time : {hours}:{minute}:{seconds} {locate}")