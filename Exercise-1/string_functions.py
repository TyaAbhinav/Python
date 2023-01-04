#string functions
a="Its a sunny day"
print(a)

#length
print("String length = ", len(a))

#type
print(type(a),"\n")

#splitting string
print("splitting string:", a.split())

#join
print("Joining string:", ''.join([a.split()[0],a.split()[3]]))

#range
print(list(range(0,12,3)))

#lower
print("string in lowercase:", a.lower())

#islower
print("Is string in lowercase?\t", a.islower())
print(a.split()[3] + " - islower?\t", a.split()[3].islower())

#upper
print("string in uppercase:", a.upper())

#isupper
print("is string in uppercase?\t", a.isupper())

#index
print("Indexing: ", a.index("nny"))

#find
print("Is 'sunny' in string? ","sunny" in a)

#isalnum
print("Is string alphanumeric?\t", a.isalnum())

#isalpha
print("Is string alphabetic?\t", a.isalpha())

#title
print("Title case a string:\t", a.title())

#istitle
print("Is string titlecases?\t", a.istitle())

#swapcase
print("Swapping:\t", a.swapcase())

#removeprefix
print("Remove prefix 'Its a':", a.removeprefix('Its a'))

#removesuffix
print("Remove suffix 'sunny day':", a.removesuffix('sunny day'))
