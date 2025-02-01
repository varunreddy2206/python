# class AI:
#     def __init__(self):
#         self.name="varun"
        
#     def disp(self):
#         print(self.name)

# x=AI()
# # x.disp()
# print(x.name)

# class NSTI:
#     def __init__(self):
#         self._trade="AI"

# class CTS(NSTI):
#     def disp(self):
#         print(self._trade)
# x=NSTI
# x=CTS()
# x.disp()

###############################

#private

# class Trainer:
#     def __init__(self):
#         self.__salary="1000000"
#     def disp(self):
#         print(self.__salary)

#         return self.__salary

# x=Trainer
# print(x.disp())
     
# class Bank:
#     def __init__(self,account_number):
#         self._account_number = "2223565"

    
# class View(Bank):
#     def display(self):
#         print(f"acount:{self._account_number}")
#         return self._account_number
     
     
# x=View
# print(x.display)
# print(x._account_number)

# class Demo:
#     def __init__(self):
#         self.strt="hello"

#         def add_name(self):
#             self.name=input("enter your name:")
#             print(self.strt+self.name)

    
# class Protected:
#     def __init__(self,age):
#         self._age= "55"
# class My(Protected):
#     def display(self):
#         print(self._age)

# x=Protected
# x=My
# print(x.display)
######################################################3
# class Hospital:
#     def __init__(self):
#         self.__patients=[]

#     def add(self,patients):
#         self.__patients.append(patients)
#         print(f'patient {patients} is added')

#     def remove(self,patient):
#         if patient in self.__patients:
#             self.__patients.remove(patient)
#             print(f'patient {patient}removed from list.')
#         else:
#             print(f'{patient} not found')

#     def disp(self):
#         for patient in self.__patients:
#             print(patient)

# x=Hospital

# x.add("arun ")
# x.add('varun')
# x.add("venkati")
# x.remove('venkati')
# x.disp

# class NSTI:
#     def __init__(self):
#         self.__students=[]

#     def add(self,student):
#         self.__students.append(student)
#         print(f"student {student} added")

#     def remove(self,student):
#         if student in self.__students:
#             self.__students.remove(student)
#             print(f"students {student} is removed")
#         else:
#             print(f'{student} not found. ') 

#     def display(self):
#         for student in self.__students:
#             print(student)

# x=NSTI()

# x.add("varun")
# x.add("venkatesh")
# x.add("rammu")
# x.add("koushik")
# x.remove("venkatesh")
# x.remove("koushik")
# x.remove("dayakar")
# x.display
###################################################

# class Student:
#     def __init__(self,name,address,age):
#         self.name=name
#         self._address= address
#         self.__age=age
#     def __display(self):
#         print(f"i am {self.name} from {self._address} my age {self.__age} class AI")
# class Hod(Student):
#     pass


# a1=Student("varun","123 street",67)
# # a1.__display()
# # print(dir(a1))
# print(a1._Student__age)
# # print(a1.name)
# # print(a1._address)
# # print(a1.__age)





    

    
        
        