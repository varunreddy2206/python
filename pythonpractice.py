# my_string="varun reddy"
# print("original string:",my_string)
# print("first character:",my_string[-1])

##################################################
#concatenation
# string1="varun"
# string2="reddy"
# concat_str= string1+" "+string2
# repeat_str=concat_str *2
# print("concatination str:", concat_str)
# print("repeating str:", repeat_str)

########################################################
# #string searching
# my_string="varun reddy"
# substring="vankat"
# found_index=my_string.find(substring)
# if found_index != -1:
#     print(f"substring:{substring} found at index :{found_index}")
# else:
#     print(f"substring:{substring} not found")

#####################################################################

#replacing substring

# my_string="varun reddy"
# new_string= my_string.replace("practice", "python")
# print("string afer replacement:",new_string)

######################################################################

# file=open("varun.txt",'r')
# # file.write("hello varun\nthis is file handling")
# # file.close()
# # print("reading all lines once:")
# lines=file.readlines()
# for line in lines:
#     print(line,end='')
# file.close()
###################################

# file=open("varun.txt",'r')
# content=file.read()
# print("full content")
# print(content)
# file.close()
#####################################

# file=open("varun.txt",'r')
# print("reading all lines at once:")
# lines=file.readlines()
# for line in lines:
#     print(line,end='')
# file.close()

#####################################

# file=open("varun.txt",'a')
# file.write("\n appending a new line to the file")
# file.close()

########################################

# with open('varun.txt','r') as file:
#     content=file.read()
#     print("content using with statement")
#     print(content)
############################################################

# def add(a,b):
#     result =a+b
#     return result

# def subtract(a,b):
#     result = a-b
#     return result

# def multiply(a,b):
#     result = a*b
#     return result

# def divide(a,b):
#     if b!=0:
#         result = a/b

#     else:
#         result="cannot divide by zero"
#     return result


# num1=10
# num2=23

# print("addition:",add(num1,num2))
# print("substraction:", subtract(num1,num2))
# print("multiplication:",multiply(num1,num2))
# print("division:",divide(num1,num2))

#########################################################

# import os 
# def divide_numbers(x,y):
#     try:
#         return x/y
#     except ZeroDivisionError:
#         return "error: Division by zero is not allowed."

# def access_list_element(lst,index):
#     try:
#         return lst[index]
#     except IndexError:
#         return "error: index is out of range."

# def get_dict_value(dct,key):
#     try:
#         return dct[key]
#     except KeyError:
#         return "error: key not found in dictionary."

# def convert_to_integer(value):
#     try:
#         return int(value)
#     except ValueError:
#         return "error: cannot convert value to integer."

#     except TypeError:
#         return "error: invalid type for conversion."

# print("division example:")
# print(divide_numbers(10,0))

# print("\n list accsess example:")
# my_list=[1,2,3]
# print(access_list_element(my_list,5))

# print("\ndictionary access examle:")
# my_dict={'a':1,"b":2}
# print(get_dict_value(my_dict,'c'))

# print("\n integer conversation example:")
# print(convert_to_integer('123abc'))
# print(convert_to_integer(123.45))

###########################################

# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.__age=age

    
#     def get_age(self):
#         return self.__age

#     def set_age(self,age):
#         if age>0:
#             self.__age=age

# s1=student("varun",23)
# print(s1.get_age())
# s1.set_age(21)
# print("updated age:",s1.get_age())
#################################################

# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.__age=age
    
#     def get_age(self):
#         return self.__age

#     def set_age(self,age):
#         if age>0:
#             self.__age=age
#             print("age is updated succesfully")
#         else:
#             print("entered age is invalid give positive number")

    
# name=input(f'enter name:')
# age=int(input(f"current student age:"))

# s1=Student(name,age)

# new_age=int(input("enter new age to updated:"))
# s1.set_age(new_age)
# print(f'\nupdated age of {s1.name}:{s1.get_age()}')

# class Student:
#     def __init__(self,age,name):
#         self.age=age
#         self.name=name

# s1=Student("varun",88)
# print(f'student name',s1.name)
# print("student age ",s1.age)
##########################################


        
    