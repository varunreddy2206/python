# class A:
#     def abc(self):
        
#         print("this a")

# class B(A):
#     def xyz(self):
#         print("this is b.")
    
# class C(A):
#     def www(self):
#         print("this is c.")

# class D(A):
#     def var(self):
#         print("this is D.")

# class E(B,C,D):
#     pass
# x=E()
# x.var()
# x.www()
# x.xyz()

# class Nsti:
#     def __init__(self,luch):
#         self.luch=luch

# class Ai(Nsti):
#     print("luch timeings 12:45")

# class Chnm(Nsti):
#     print("luch timings is 1:15")


# x=Nsti(luch=12)

# x.Ai
# x.Chnm
    

# class Nsti:
#     def __init__(self,luch):
#         self.lunch=luch

# class Lab:
#     def __init__(self,lab):
#         self.lab=lab

# class Ai(Nsti,Lab):
#     def __init__(self, luch,lab,computer):
#         Nsti.__init__(self,luch)
#         Lab.__init__(self,lab)
#         self.computer=computer

#     def disp(self):
#         print(f'luch:{self.lunch},lab:{self.lab},computer:{self.computer}')

# lunch=input("enter luch:")
# lab=input("enter lab:")
# computer=input("enter computer:")
        
# x=Ai(lunch,lab,computer)
# x.disp()
######################################################################################
# class Doctor:
#     def __init__(self, diagnosing):
#         self.diagnosing = diagnosing

# class Surgeon:
#     def __init__(self, surgery):
#         self.surgery = surgery

# class Specialist(Doctor, Surgeon):
#     def __init__(self, name, specialty, diagnosing, surgery):
#         Doctor.__init__(self, diagnosing)
#         Surgeon.__init__(self, surgery)
#         self.name = name
#         self.specialty = specialty

#     def disp(self):
#         print(f"Name: {self.name}, Specialty: {self.specialty}, Diagnosing: {self.diagnosing}, Surgery: {self.surgery}")


# name = input("Enter name: ")
# specialty = input("Enter specialty: ")
# diagnosing = input("Enter diagnosing type: ")
# surgery = input("Enter surgery type: ")

# specialist = Specialist(name, specialty, diagnosing, surgery)
# specialist.disp()

#####################################################################################

# class CourseContent:
#     def provide_materials(self):
#         print("providing course materials")

# class InteractiveTools:
#     def facilitate_interaction(self):
#         print("Facilitating student interactions with tools")

# class OnlineCourse(CourseContent,InteractiveTools):
#     def __init__(self,course_name):
#         self.course_name=course_name

#     def disp(self):
#         print("f'course name:{self.course_name}")

#     def start_course(self):
#         print("starting the course")

# course=OnlineCourse("introduction to ai")
# course.disp()
# course.provide_materials()
# course.facilitate_interaction()
# course.start_course()
#############################################################################

# class FlyingMechanism:
#     def fly(self):
#         print("drone is flying")

# class Camera:
#     def take_photo(self):
#         print("take photo")

# class Drone(FlyingMechanism,Camera):
#     def __init__(self,model):
#         self.model=model

#     def disp_info(self):
#         print(f"drone model:{self.model}")

#     def perform_action(self):
#         self.fly()
#         self.take_photo()

# drone=Drone("green high 2")
# drone.disp_info()
# drone.perform_action( )

#####################################################################




        
        





        
    
        