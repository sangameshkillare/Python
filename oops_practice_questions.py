# ----------------Create a class Student with attributes name and marks. Add methods to display details and calculate the grade.



# class Student:
    
#     def __init__(self,name,mark):
#         self.name=name
#         self.mark=mark
    
#     def display(self):
#         print(f"Your name is {self.name}")
#         print(f"You marks is {self.mark}")
        
#     def grade(self):
#          if self.mark < 35:
#              print("You are failed .")
            
#          elif self.mark <50:
#              print(" you have C grade .")
            
#          elif self.mark <80:
#              print("You have B grade .")

#          else:
#              print("you have A grade .")
    
    
    
# obj=Student("Sangamesh",20)
# obj.display()
# obj.grade()





#---------- Define a class Calculator with methods add, subtract, multiply, and divide. Handle edge cases in each.
    
    
    

# class Calaculator:
    
#     def __init__ (self):
#         self.num1=int(input("enter the num 1 :"))            
#         self.num2=int(input("enter the num 2 :"))   
#         self.operation=int(input("enter : "))  
                


# class display(Calaculator):
    
#     def now(self):
#         if self.operation ==1:
#                 print(self.num1+self.num2)
#         elif self.operation ==2:
#                  print(self.num1-self.num2)
#         elif self.operation ==3:
#                   print(self.num1//self.num2)
#         elif self.operation ==4:
#                  print(self.num1*self.num2)
#         else:
#             print("invalid")
                 
    

# obj2=display()
# obj2.now()
         
         
         
# --------Create a class Employee that stores name and salary. Use getter and setter methods with encapsulation.


# class Employee:
    
#     def set(self):
#         self._name=input("Enter the name :")
#         self._salary=int(input('enter the salary :'))
    
#     def get(self):
#         print(self._name)
#         print(self._salary)
        
# obj=Employee()
# obj.set()
# obj.get()




#---------------Create a base class Vehicle and derived classes Bike and Car. Add a method fuel_type to each.




# class Vehical:
#     print("this is the vehical.")

# class Bike(Vehical):
#     def fuel_type(self):
#         print("Fuel of bike is petrol.")
    
# class Car(Vehical):
#     def fuel_type(self):
#         print("Fuel of car is petrol also.")
    
    
# obj=Bike()
# obj.fuel_type()
# obj2=Car()
# obj2.fuel_type()  



#-----------5) Demonstrate the use of super() by creating a base class Person and a derived class Teacher.  
    
    
    
# class Person:
#     print("He/ she is the person")

# class Teacher(Person):
#     print("Maths teacher .")
    
# # obj=Person()
# obj2=Teacher()


# =--------------6) Build a class Animal, and create Bird and Fish subclasses that override a move() method.


# class Animal:
#     def move(self):
#         print('this is move from animal')
    
# class bird(Animal):
#     def move(self):
#         print('this is move from bird')

# class fish(Animal):
#     def move(self):
#         # super().move()
#         print('this is move from fish')


# obj=Animal()
# obj1=bird()
# obj2=fish()
# obj1.move()
# obj2.move()

# obj.move()
    
    
    
    
    
# 🔹 Polymorphism
# -----------Create classes Instagram, Twitter, and Facebook, each with a method post_content(). Write a function that takes any platform object and calls post_content.


# class Insta:
#     def post_content(self):
#         print("reals")
    
# class Facebook:
#     def post_content(self):
#         print("Videos")
# class Twitter:
#     def post_content(self):
#         print("Twitt's")

# obj=Insta()
# obj.post_content()
# obj1=Facebook()
# obj1.post_content()
# obj2=Twitter()
# obj2.post_content()





# Write a program where multiple classes define a method calculate_tax() differently. Use polymorphism to call the appropriate method based on the object.


