# class A:
#     def a(self):
#         print("this is main/base/parent class.")

# class B(A):
#     def b(self):
#         print("this is child/derived class.")

# x=B()
# x.a()
# x.b()

# class Sampath:
#     def s(self):
#         print("owner of chat bandi")

# class Sampath_son(Sampath):
#     def s_s(self):
#         print("owner of gokul chat")

# x=Sampath_son()
# x.s_s()
# x.s()


# class Animal_parent:
#     def a(self):
#         print("four leg animal")

# class F(Animal_parent):
#     def s(self):
#          print("tiger,dog")

# x=F()
# x.a()
#x.s()


# class Math:
#     def addition(self,a,b):
#         return a+b
    
# class Multi(Math):
#     def Multi(self,a,b):
#         return a*b
    
# x=Multi()

# print("Addition= ",x.addition(6,7))
# print("multiplicatiob=",x.Multi(16,16))

# class Math:
#     def Addition(self,a,b):
#         return a+b
    
# class Multi(Math):
#     def multiplication(self,a,b):
#         return a*b
    
# class Division(Multi):
#     def division(self,a,b):
#         return a/b
    
# x=Division()

# num1=input("enter first number: ")
# num2=input("enter second number: ")

# print("Addition= ",x.Addition(num1,num2))
# print("multiplicatiob=",x.multiplication(num1,num2))
# print("division",x.division(num1,num2))

# class library:
#     def __init__(self,title,author,price):
#         self.title=title
#         self.author=author
#         self.price=price

#     def disp1(self):
#         print(f'Title:{self.title}')
#         print(f'Autor:{self.author}')
#         print(f'autor:{self.price}')


# class Book(library):
#     def __init__(self, title, author, price,year):
#         super().__init__(title, author, price)
#         self.year=year

#     def disp2(self):
#         super().disp1()


# x=Book("NSTI","CS",234,1923)
# x.year

