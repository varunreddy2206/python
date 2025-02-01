#calling 
# class A:
#     def x(self):
#         return "varun"
    
# class B:
#     def x(self):
#         return "reddy"
    
# def z(q):
#     return q.x()
    

# r=A()
# t=B()

# print(z(r))
# print(z(t))


# class Maths:
#     def area(self):
#         pass

#     def Perimeter(self):
#         pass

#     # def Volume(self):
#     #     pass
    
# class Rectangle(Maths):
#     def __init__(self,l,b):
#         self.l=l
#         self.b=b

#     def area(self):
#         return self.l* self.b
    
#     def Perimeter(self):
#         return 2*(self.l +self.b)
    
#     def Volume(self):
#         return 
    
# class Square(Maths):
#     def __init__(self,a):
#         self.a=a

#     def area(self):
#         return self.a * self.a

# x=[Rectangle(5,6),Square(4)]

# for result in x:
#     print(result.area())

# for result in x:
#     print(result.Perimeter())
####################################################
# from abc import ABC,abstractmethod
# class NSTI(ABC):
#     @abstractmethod
#     def xyz(self):
#         pass

# class AI(NSTI):
#     def xyz(self):
#         return "Artificial intelligence"
    
# class CHNM(NSTI):
#     def xyz(self):
#         return "computer hardware,networking and maitanace"
    
# x=[AI(),CHNM()]

# for result in x:
#     print(result.xyz())

#####################################################

# from abc import ABC,abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def calculate_area(self):
#         pass

# class Rectangle(Shape):
#     def __init__(self,l,b):
#         self.l=l
#         self.b=b

#     def calculate_area(self):
#         return self.l*self.b

# class Triangle(Shape):
#     def __init__(self,base,h):
#         self.base=base
#         self.h=h

#     def calculate_area(self):
#         return 0.5*self.base*self.h
    
# class Circle(Shape):
#     def __init__(self,r):
#         self.r=r

#     def calculate_area(self):
#         return  3.14*self.r*self.r
    
# x=[Rectangle(2,3),Triangle(4,5),Circle(4)]

# for result in x:
#     print(result.calculate_area())
           
##############################################

# from abc import ABC,abstractmethod

# class Restaurant(ABC):
#     @abstractmethod
#     def preparation_time(self):
#         pass
#     def pricing(self):
#         pass

# class Main_course(Restaurant):
#     def __init__(self,menu_iteams,base_price,cooking_time):
#         self.menu_iteams=menu_iteams
#         self.base_price=base_price
#         self.cooking_time=cooking_time

#     def preparation_time(self):
#         return self.cooking_time
        
#     def pricing(self):
#         return self.base_price

# class Beverages(Restaurant):
#     def __init__(self,manchuria,manchuria_price):
#         self.manchuria=manchuria
#         self.manchuria_price=manchuria_price
    

#     def preparation_time(self):
#         return self.manchuria

#     def pricing(self):
#         return self.manchuria_price

# class Desserts(Restaurant):
#     def __init__(self,desert_name,desert_pricing):
#         self.desert_name=desert_name
#         self.desert_pricing=desert_pricing

#     def preparation_time(self):
#         return self.desert_name

#     def pricing(self):
#         return self.desert_pricing

# x=[Main_course("chicken biryani: ","1 hour","130"),Beverages("chicken manchuria","65"),Desserts("apricot","200")]

# for result in x:
#     print(result.preparation_time())
#     print(result.pricing())



####################################################################

# from abc import ABC, abstractmethod

# class Game_of_throns(ABC):
#     @abstractmethod
#     def Kingdoms(self):
#         pass

#     @abstractmethod
#     def House_name(self):
#         pass

#     @abstractmethod
#     def Leader(self):
#         pass

#     @abstractmethod
#     def Family_members(self):
#         pass


# class Starks(Game_of_throns):
#     def __init__(self, father_name="Eddard Ned Stark", mother_name="Catelyn Stark", 
#                  son1_name="Robb Stark", daughter1_name="Sansa Stark", 
#                  son2_name="Bran Stark", daughter2_name="Arya Stark", 
#                  son3_name="Rickon Stark", son4_name="Jon Snow"):
#         self.father_name = father_name
#         self.mother_name = mother_name
#         self.son1_name = son1_name
#         self.daughter1_name = daughter1_name
#         self.son2_name = son2_name
#         self.daughter2_name = daughter2_name
#         self.son3_name = son3_name
#         self.son4_name = son4_name

#     def Kingdoms(self):
#         return "Winterfell"

#     def House_name(self):
#         return "House Stark"

#     def Leader(self):
#         return self.father_name

#     def Family_members(self):
#         return [self.mother_name, self.son1_name, self.daughter1_name, 
#                 self.son2_name, self.daughter2_name, self.son3_name, self.son4_name]


# class Lanisters(Game_of_throns):
#     def __init__(self, father_name="Tywin Lannister", mother_name="Joanna Lannister", 
#                  son1_name="Jaime Lannister", daughter1_name="Cersei Lannister", 
#                  son2_name="Tyrion Lannister"):
#         self.father_name = father_name
#         self.mother_name = mother_name
#         self.son1_name = son1_name
#         self.daughter1_name = daughter1_name
#         self.son2_name = son2_name

#     def Kingdoms(self):
#         return "Kings landing"

#     def House_name(self):
#         return "House Lannister"

#     def Leader(self):
#         return self.father_name

#     def Family_members(self):
#         return [self.father_name, self.mother_name, self.son1_name, self.daughter1_name, self.son2_name]

# class Targaryens(Game_of_throns):
#     def __init__(self, father_name="Aerys II Targaryen", mother_name="Rhaella Targaryen", 
#                  son1_name="Viserys Targaryen", daughter1_name="Daenerys Targaryen", 
#                  son2_name="Aegon Targaryen"):
#         self.father_name = father_name
#         self.mother_name = mother_name
#         self.son1_name = son1_name
#         self.daughter1_name = daughter1_name
#         self.son2_name = son2_name

#     def Kingdoms(self):
#         return "King's Landing"  

#     def House_name(self):
#         return "House Targaryen"

#     def Leader(self):
#         return self.father_name  

#     def Family_members(self):
#         return [self.father_name, self.mother_name, self.son1_name, self.daughter1_name, self.son2_name]


# starks = Starks()

# print(f"Kingdom: {starks.Kingdoms()}")
# print(f"House Name: {starks.House_name()}")
# print(f"Leader: {starks.Leader()}")
# print("Family Members:", ', '.join(starks.Family_members()))

# lanisters = Lanisters()


# print(f"\nKingdom: {lanisters.Kingdoms()}")
# print(f"House Name: {lanisters.House_name()}")
# print(f"Leader: {lanisters.Leader()}")
# print("Family Members:", ', '.join(lanisters.Family_members()))

# targaryens = Targaryens()

# print(f"\nKingdom: {targaryens.Kingdoms()}")
# print(f"House Name: {targaryens.House_name()}")
# print(f"Leader: {targaryens.Leader()}")
# print("Family Members:", ', '.join(targaryens.Family_members()))

############################################################################

