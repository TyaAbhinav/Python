#slicing a string
a = "hello!"
print(a)

#printing first 3 letters
print("First 3 letters: "+ a[0:3:1])

#printing last 3 letters
print("Last 3 letters: "+ a[-1:-5:-1])

#printing 4 letter
print("4th letter: "+ a[3])

#reassembling a string
b= "NewString"
first_letters=b[0:4:1]
last_letters=b[-1:-4:-1]
insert_letter='Z'
new_name=first_letters+insert_letter+last_letters
print("Old String: "+ b +", inserted letter: "+ insert_letter)
print("New String: "+ new_name)

#String Interpolation
name="NewString"
print("Old String: "+ name)
name = name[0:5:1] + "Z"  + name[5:]
print("New String: "+name)