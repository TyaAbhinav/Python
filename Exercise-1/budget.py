print("My Budget!")
# b= budget, f=food, e=electricity, r=rent, m=miscellaneous
# All Figures Monthly
# Semester will be 4 months long
# budget is per month
b = 1000*4
# € 4 per meal, 2 times a day, 7 days a week, 4 weeks monthly, 4 months
f = 4 * 2 * 7 * 4 * 4
# € 5 per week for Electricity. 4 weeks monthly, 4 months
e = 5 * 4 * 4
# € 70 per week for Rent, 4 weeeks monthly, 4 months
r = 70 * 4 * 4
# € 100 per month, 4 months
m = 100 * 4
print(f"My available budget per month is €{b}")
print(f"My expenditures this semester is €{f+e+r+m}")
print(f"This leaves me with €{b - (f+e+r+m)} to spend this semester")
