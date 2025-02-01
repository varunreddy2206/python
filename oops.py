# class Computer:

#     def config(self):
#         print("i5,16gb,1tb")
#         print('i3,8gb,1tb')
# com1=Computer()
# com2=Computer()

# com1.config()


# class AI:
#     institute="NSTI"

#     def __init__(self,name,age,address):
#         self.name=name
#         self.age=age
#         self.address=address

# students=AI("varun","77","hyd")
# print(f'{students.name},{students.age},{students.address}')

# class AI:
#     institute="NSTI"
    
#     def __init__(self):
#         print("varun",22,"hyd")
#         print("venkat",87,"hyd")
# student=AI()
# student=AI()

# class NSTI:
#     trades="NSTI"

#     def __init__(self,trade,student,pc):
#         self.trades=trade
#         self.students=student
#         self.pc=pc

# trade1=NSTI("ai",21,16)
# trade2=NSTI("csa",40,40)
# trade3=NSTI("chnm",30,27)

# print({trade1.trades},{trade1.students},{trade1.pc})
# print({trade2.trades},{trade2.students},{trade2.pc})
# print({trade3.trades},{trade3.students},{trade3.pc})

# class Student():

#     def __init__(self,name,roll_number):
#         self.name=name
#         self.roll_number=roll_number
# student1=Student("varun",45)
# student2=Student("divakar",5)

# print(student1.name,student1.roll_number)
# print(student2.name,student2.roll_number)

# class Rectangle:
#     def __init__(self,length,width):
#         self.length=length
#         self.width=width
#     def area(self):
#         return self.length * self.width

# rectangle=Rectangle(5,3)
# print("the area of the rectangle is:", rectangle.area())

# class Cricle:
#     def __init__(self,radius):
#         self.radius=radius
#     def circumference(self):
#          return 2* 3.14*self.radius
#     def area(self):
#         return 3.14 *(self.radius**2)

# circle = Cricle(5)

# print("circumference of the circle:",circle.circumference())
# print("area of the circle:", circle.area())


# class Wallet:
#     def __init__(self, name, balance=0):
#         self.name = name
#         self.balance = balance

#     def add_money(self, money):
#         if money > 0:
#             self.balance += money
#             print(f"Money added: {money}. New balance: {self.balance}")
#         else:
#             print("Please enter a valid amount.")

#     def spend(self, money):
#         if money > self.balance:
#             print("Insufficient balance.")
#         else:
#             self.balance -= money
#             print(f"Spent amount: {money}. Remaining balance: {self.balance}")

#     def check_balance(self):
#         print(f"{self.name}'s balance is {self.balance}")



# x = Wallet("Venkaty")
# y = Wallet("Divakar")

# x.add_money(50)
# x.spend(10)      
# x.check_balance() 


# class Flipkart():
#     def __init__(self):
#         self.cart={}
        
#     def adding_iteam(self,name,price):
#         if name in self.cart:
#             self.cart[name]+=price
#         else:
#             self.cart[name]=price
       
#         print(f'iteam added :{name} price for iteam:{price}')

#     def display_iteam(self):

#         if not self.cart:
#             print("the cart is empty.")
#         else:
#             print('iteams  in the cart:')
#             for name,price in self.cart.items():
#                 print(f'iteams in cart:{name}     price of iteam: {price}')

#     def removing_iteam(self,name):
#         if name in self.cart:
#             del self.cart[name]
#             print(f'iteam removed:{name}')
#         else:
#             print(f'iteam{name} not found  in cart.')
# x=Flipkart()

# x.adding_iteam('laptop',65000)
# x.adding_iteam('mobile',20000)

# # x.display_iteam()
# x.removing_iteam('laptop')
# x.display_iteam()

# class Flipkart:
#     def __init__(self,name):
#         self.name=name
#         self.item=[]

#     def add_item(self,i_name,price):
#         self.item.append({'name':i_name,"price":price})
#         print(f'Added{i_name} to list with price {price} ')

#     def remove(self,i_name):
#         for item in self.item:
#             if item['name']==i_name:
#                 self.item.remove(item)
#                 print(f'removed{i_name}')
#                 return
#         print(f'{i_name} not found')

#     def display(self):
#         if self.item:
#             print(f"cart for {self.name}")
#             for item in self.item:
#               print(f'{item["name"]}:{item["price"]}')
#         else:
#             print("cart is empty:")

# x=Flipkart("varun")#object

# x.add_item("maccbook",100000)
# x.add_item("watch",2000)

# x.display()

# class shoopingfilpkart(Flipkart)

      
# class Student:
#     def __init__(self,name,id_num,address):
#         self.name=name
#         self._id_num=id_num
#         self.__address= address

# student1=Student("varun",23,"23-34")
# student2=Student("divana",65,"9459-33")

# print(student1.name,student1._id_num)
# print(student1.__address())

# class Student:
#     def __init__(self, name, id_num, address):
#         self.name = name
#         self._id_num = id_num 
#         self.__address = address  

#     def display(self):
#         print(f"name:{self.name}id_number:{self._id_num},address:{self.__address}") 

#     def set_address(self):
#         self.__address= new__address

# class Person:
#     def __init__(self, name, age, address):
#         self.name = name
#         self._age = age
#         self.__address = address

#     def display_details(self):
#         print(f"Name: {self.name},Age : {self._age},Address: {self.__address}")
    
   
# person=Person("varun",88,"1st street")
# person.display_details()
# # print("name: {person.name},age:{person._age},address:{person.__address}")

# try:
#     print(person.__address)
# except AttributeError:
#     print("cannot access private attribute directly")
        
# class Person:
#     def __init__(self, name, age, address):
#         self.name = name
#         self._age = age
#         self.__address = address

#     def display_details(self):
#         print(f"Name: {self.name}, Age: {self._age}, Address: {self.__address}")


# person = Person("varun", 30, "123 Main St")


# person.display_details()


# try:
#     print(person.__address)
# except AttributeError:
#     print("Cannot access private attribute directly.")

# print("Accessing private attribute using name mangling:", person._Person__address)

# x1 =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(x1)
# print(type(x1))