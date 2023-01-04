def find_num(number_list: list, number: int)->bool:
    for iterate_number in number_list:
        if iterate_number == number:
            return True
        else:
            pass
result = find_num([1,2,3,4,5,6,7,8], 9)
print(result)

# number 9 is missing from the list
# after add 9 to the list
result = find_num([1,2,3,4,5,6,7,8,9], 9)
print(result)

"""after updating code to return False if value is not found"""
def find_num(number_list: list, number: int)->bool:
    for iterate_number in number_list:
        if iterate_number == number:
            return True
    return False
result = find_num([1,2,3,4,5,6,7,8], 9)
print(result)

"""This function has a list of even numbers which will result in true if found an even number otherwise false"""
def even_num(number_list: list)->bool:
    for iterate_number in number_list:
        if iterate_number % 2 ==0:
            return True
    return False
result = even_num([1,2,3,4,5,6,7,8])
print(result)

"""lambda function to find the volume of a cylinder, radius=r, height=h"""
cyl_vol = lambda r,h : 3.14*r*r*h
print(cyl_vol(4,6))