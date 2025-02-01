# first we'll have to import module from abstract base class library

# from abc import ABC,abstractmethod


# class Vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass
    
#     @abstractmethod
#     def stop(self):
#         pass

# class Bike(Vehicle):
#     def start(self):
#         print("hello KTM koushik")

#     def stop(self):
#         print("good bye ktm")


# class Flight(Vehicle):

#     def start(self):
#         print("flight is ready to take off")

#     def stop(self):
#         print("flight is landed")

# x=Bike()
# x.start()
# x.stop()

# y=Flight()

# y.start()

# y.stop()



# from abc import ABC ,abstractmethod

# class Math(ABC):
#     @abstractmethod
#     def area(self):
#         pass
    
#     @abstractmethod
#     def perimeter(self):
#         pass
# class Square(Math):
#     def __init__(self,side):
#         self.side=side

#     def area(self):
#         return self.side*self.side
    
#     def perimeter(self):
#         return 4 * self.side
    
# class Rectangle(Math):
#     def __init__(self,l,b):
#         self.l=l
#         self.b=b

#     def area(self):
#         return self.l * self.b
    
#     def perimeter(self):
#         return 2*(self.l * self.b)

# x=Square(8)
# y=Rectangle(10,8)

# print(f'square area :{x.area()}')
# print(f'perimeter of square:{x.perimeter()}')

# print(f'Area of rectangle:{y.area}')
# # print(f'perimeter of rectangle: {y.perimeter}')

# from abc import ABC, abstractmethod

# class Bank(ABC):
#     @abstractmethod
#     def deposite(self):
#         pass

#     @abstractmethod
#     def saving(self):
#         pass

#     @abstractmethod
#     def credit(self):
#         pass

# class Details(Bank):
#     def __init__(self):
#         self.balance=0
#         self.saving_balance=0
#         self.current_balance=0
    
#     def deposite(self,amount):
#         self.balance += amount
#         print(f"deposite rs {amount}.total balance: rs{self.balance}")
        

#     def saving(self):
#         self.saving_balance = self.balance * 0.8
#         print(f"saving account balance :rs {self.saving_balance}")

#     def current(self):
#         self.current_balance = self.balance *0.2
#         print(f"current account balance rs {self.current_balance}")

#     def credit(self,amount):
#         if amount <= self.balance:
#             self.balance -=amount
#             print(f"credit rs {amount}  remaining balance {self.balance}")
#         else:
#             print("insufficient balance to credit.")

# x=Details()
# x.deposite(10000000000000)
# x.saving()
# x.current()
# x.credit(2000)

# class Movie:
#     def __init__(self,id,title,price):
#         self.id=id
#         self.__title=title
#         self.__price=price

#     def s_title(self,title):
#         self.__title=title

#     def t_price(self, price):
#         if price>0:
#             self.__price=price
#         else:
#             print("enter price more than 0.")

#     def g_title(self):
#         return  self.__title
    
#     def g_ticket(self):
#         return self.__price
    
#     def disp(self):
#         print(f'id: {self.id}')
#         print(f'name : {self.__title}')
#         print(f'price:{self.__price}')

# def movie():
#     id=input("enter id:")
#     title=input("enter Movie name:")
#     while True:
#         price=float(input("enter the price :"))
#         if price>0:
#           break
#         else:
#             print("price must more than rs 0.")

#     return Movie(id,title,price)

# x=movie()

# x.disp()


# class Book:
#     def __init__(self,title,author,price):
#         self.__title=title
#         self.__author=author
#         self.__price=price

#     def s_title(self,title):
#         self.__title=title

#     def b_author(self,author):
#         self.__author=author

#     def t_price(self, price):
#         if price>0:
#             self.__price=price
#         else:
#             print("enter price more than 0.")

#     def g_title(self):
#         return  self.__title
    
#     def g_book(self):
#         return self.__price
    
#     def disp(self):
#         print(f'title: {self.__title}')
#         print(f'author : {self.__author}')
#         print(f'price:{self.__price}')

# def creat_book():
#     title=input("enter title:")
#     author=input("enter  name:")
#     while True:
#         price=float(input("enter the price :"))
#         if price>0:
#           break
#         else:
#             print("price must more than rs 0.")

#     return Book(title,author,price)

# x=creat_book()

# x.disp()
        

# from abc import ABC, abstractmethod

# class Employe(ABC):
    
#     @abstractmethod
#     def get_details(self):
#         pass

# class CreateEmploye(Employe):
#     def __init__(self, name, position, salary):
#         self.__name = name
#         self.__position = position
#         self.__salary = salary

#     def get_name(self):
#         return self.__name
    
#     def get_position(self):
#         return self.__position
    
#     def get_salary(self):
#         return self.__salary
    
#     def set_name(self, name):
#         self.__name = name 

#     def set_position(self, position):
#         self.__position = position

#     def set_salary(self, salary):
#         if salary > 0:
#             self.__salary = salary
#         else:
#             print("Salary must be positive")
    
#     def get_details(self):
#         return f"Name: {self.__name}, Position: {self.__position}, Salary: {self.__salary}"

# def create_employe():
#     name = input("Enter employee name: ")
#     position = input("Enter position of employee: ")
#     while True:
#         try:
#             salary = float(input("Enter the employee's salary: "))
#             break
#         except ValueError:
#             print("Please enter a valid number for salary")
    
#     return CreateEmploye(name, position, salary)

# x = create_employe()
# print(x.get_details())


# from abc import ABC, abstractmethod

# class Employee(ABC):
#     @abstractmethod
#     def calculate_salary(self):
#         pass
    
#     @abstractmethod
#     def get_details(self):
#         pass

# class FullTimeEmployee(Employee):
#     def __init__(self, name, monthly_salary):
#         self.name = name
#         self.monthly_salary = monthly_salary

#     def calculate_salary(self):
#         return self.monthly_salary

#     def get_details(self):
#         return f"Full-Time Employee: {self.name}, Monthly Salary: {self.monthly_salary}"

# class PartTimeEmployee(Employee):
#     def __init__(self, name, hourly_rate, hours_worked):
#         self.name = name
#         self.hourly_rate = hourly_rate
#         self.hours_worked = hours_worked

#     def calculate_salary(self):
#         return self.hourly_rate * self.hours_worked

#     def get_details(self):
#         return f"Part-Time Employee: {self.name}, Hourly Rate: {self.hourly_rate}, Hours Worked: {self.hours_worked}"


# full_time_emp = FullTimeEmployee("Alice", 5000)
# part_time_emp = PartTimeEmployee("Bob", 20, 120)

# print(full_time_emp.get_details())
# print(f"Calculated Salary: {full_time_emp.calculate_salary()}")
# print()
# print(part_time_emp.get_details())
# print(f"Calculated Salary: {part_time_emp.calculate_salary()}")


# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass

    
#     @abstractmethod
#     def move(self):
#         pass

# class Dog(Animal):
#     def sound(self):
#         return "bark"
    
#     def move(self):
#         return "walk"

# class Bird(Animal):
#     def sound(self):
#         return "chirp"
    
#     def move(self):
#         return "fly"

# dog = Dog()
# bird = Bird()

# print(f"Dog sound: {dog.sound()}, Dog move: {dog.move()}")
# print(f"Bird sound: {bird.sound()}, Bird move: {bird.move()}")

# from abc import ABC, abstractmethod

# class Appliance(ABC):
#     @abstractmethod
#     def turn_on(self):
#         pass
    
#     @abstractmethod
#     def turn_off(self):
#         pass

# class Fan(Appliance):
#     def turn_on(self):
#         print("Fan is turned on")
    
#     def turn_off(self):
#         print("Fan is turned off")

# class Light(Appliance):
#     def turn_on(self):
#         print("Light is turned on")
    
#     def turn_off(self):
#         print("Light is turned off")

# fan = Fan()
# light = Light()

# fan.turn_on()
# fan.turn_off()

# light.turn_on()
# light.turn_off()
