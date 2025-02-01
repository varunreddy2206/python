# class NSTI:
#     def __init__(self,Institute_name,Branch):
#         self.Institute_name=Institute_name
#         self.Branch=Branch


# class Trade(NSTI):
#     def __init__(self, Institute_name, Branch,Trade):
#         super().__init__(Institute_name, Branch)
#         self.Trade=Trade
        

# class Student(Trade):
#     def __init__(self, Institute_name, Branch, Trade,s_name):
#         super().__init__(Institute_name, Branch, Trade)
#         self.s_name=s_name

#     def disp(self):
#         print(f"institute name:{self.Institute_name}")
#         print(f"Branch:{self.Branch}")
#         print(f"Trade:{self.Trade}")
#         print(f"student name:{self.s_name}")

# x=Student(" nsti","ramanthapur","aipa","varun")

# x.disp()

############################################################

# class Employee:
#     def __init__(self,company_name,Branch):
#         self.company_name=company_name
#         self.Branch=Branch


# class Salary(Employee):
#     def __init__(self, company_name, Branch,salary):
#         super().__init__(company_name, Branch)
#         self.salary=salary

# class Work(Salary):
#     def __init__(self, company_name, Branch, salary,specific_work):
#         super().__init__(company_name, Branch, salary)
#         self.specific_work=specific_work


# class Experience(Work):
#     def __init__(self, company_name, Branch, salary, specific_work,work_experience):
#         super().__init__(company_name, Branch, salary, specific_work)
#         self.work_experience=work_experience

#     def disp(self):
#         print(f"Company name:{self.company_name}")
#         print(f"Branch:{self.Branch}")
#         print(f"salary:{self.salary}")
#         print(f"specific work:{self.specific_work}")
#         print(f"work experience:{self.work_experience}")

# x=Experience("tcs","it","250000","software tester","5years")

# y=Experience('hp',"non it","100000","hr","10years")
        
# x.disp()

# y.disp()


# class Animal:
#     def __init__(self,eat,species):
#         self.eat=eat
#         self.species=species

# class Mamal(Animal):
#     def __init__(self, eat, species,has_hair,walk):
#         super().__init__(eat, species)
#         self.has_hair=has_hair
#         self.walk=walk

# class Dog(Mamal):
#     def __init__(self, eat, species, has_hair, walk,bark):
#         super().__init__(eat, species, has_hair, walk)
#         self.bark=bark

#     def disp(self):
#         print(f"eat:{self.eat},which species:{self.species},walk:{self.walk},bark:{self.bark},hair colour:{self.has_hair}")


# x=Dog("non-veg","dog","hair colour is balck","walk with four legs","bow bow") 

# x.disp()
 ############################################################################

# class Vehicle:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model

# class Car(Vehicle):
#     def __init__(self, brand, model,number_of_doors,fuel_type):
#         super().__init__(brand, model)
#         self.number_of_doors=number_of_doors
#         self.fuel_type=fuel_type

# class Electriccar(Car):
#     def __init__(self, brand, model, number_of_doors, fuel_type,battery_capacity,range):
#         super().__init__(brand, model, number_of_doors, fuel_type)
#         self.battery_capacity=battery_capacity
#         self.range=range

#     def disp(self):
#         print(f"brand:{self.brand}")
#         print(f"model:{self.model}")
#         print(f"number of doors:{self.number_of_doors}")
#         print(f"fuel type:{self.fuel_type}")
#         print(f"battery capacity:{self.battery_capacity}")
#         print(f"range:{self.range}")

# x=Electriccar("TATA","TATA nexon ev","4","Electric","40.5 kwh","453 km")
# x.disp()

#########################################################################################

# class Library:
#     def __init__(self, library_name, location):
#         self.library_name = library_name
#         self.location = location

# class Book(Library):
#     def __init__(self, library_name, location, book_name, author, ISBN):
#         super().__init__(library_name, location)
#         self.book_name = book_name
#         self.author = author
#         self.ISBN = ISBN

# class Borrower(Book):
#     def __init__(self, library_name, location, book_name, author, ISBN, borrower_name, borrow_date):
#         super().__init__(library_name, location, book_name, author, ISBN)
#         self.borrower_name = borrower_name
#         self.borrow_date = borrow_date

#     def disp(self):
#         print(f"Library: {self.library_name}")
#         print(f"Location: {self.location}")
#         print(f"Book: {self.book_name}")
#         print(f"Author: {self.author}")
#         print(f"ISBN: {self.ISBN}")
#         print(f"Borrower: {self.borrower_name}")
#         print(f"Borrow Date: {self.borrow_date}")

# x = Borrower("Central Library", "Downtown", "1984", "venkat", "123-456-789", "varun reddy", "2024-01-15")
# x.disp()

       
        