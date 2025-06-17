#single thing can  have a multiple forms  depends upon the situation
#similar function act differently depends on the situation 
# what is polymorphism ?
# what is method overloading , overriding ?

# diff between overloading and overriding ?
#  what is supermethod ? == with the help of the super method we can handel thhe overloading and overriding .


# def add(*arg):
#     return sum(arg)

# print(add(1,8))
# print(add(8,5,7,5))




# print(len("sangamesh"))
# print(len(["sangamesh ", "killare "]))
# print(len(['''sangamesh
#           killare ''']))



#--------------polymorphism in user define functions


# def word(element):
#     return len(element)

# print(word([1,5,6,8,6]))
# print(word('sangamesh'))
    




#-------------build in polimorphisam

# print(len("sangamesh"))
# print(len(["sangamesh","killare"]))


# def add(a,b,c=0):
#     return a+b+c
# print(add(2,5))
# print(add(2,4,6))

#----------arbetri argument

# def add(*arg):
#     return sum(arg)
# print(add(5,6))
# print(add(5,5,6))


#---------returns absulate values in diff data types 


# print(abs(-10))     
# print(abs(-4.5))      
# print(abs(3 + 5j))    



# ----------------max return the values for diff data type



# print(max("python"))      
# print(max([10, 20, 30]))  
# print(max((5, 15, 25)))   



#-------------------min



# print(min("python"))      
# print(min([10, 20, 30]))  
# print(min((5, 15, 25)))   



#----------------type


# print(type("python"))      
# print(type([10, 20, 30]))  
# print(type((5, 15, 25)))  



#------------sum

      
# print(sum([10, 20, 30]))  
# print(sum((5, 15, 25)))  



#-----------reversed


# print(list(reversed("python")))      
# print(list(reversed([10, 20, 30])))  
# print(tuple(reversed((5, 15, 25))))  




#----------method ooverloading

# Overloading is a concept in programming where multiple functions or methods have the same name but different parameters. It allows for improved code readability and flexibility. Overloading can occur in methods (method overloading) or operators (operator overloading), depending on the programming language.
#-method overloading occer  in the same  class and same function 


# class calculator:
#     def add(self,a,b=0,c=0,d=0):
#         return a+b+c+d

# calc=calculator()
# print(calc.add(1))
# print(calc.add(1,4))
# print(calc.add(1,3,4))
# print(calc.add(1,3,4,5))



#--------------------------------------overriding-----------------------------------------


#same class , same method but having diff parameters 
# #overriding occur in inheritance 
# if child class , parent class having  same functions ,name
#child class overrieds the func of parent class and disply it own property




class father:
    def home(self):
        print("This is sangamesh fathers Home .")
        
class sangamesh(father):
    def home(self):
        super().home()
        print("This is sangamesh's home.")
        
whos=sangamesh()
whos.home()





# class Animal:
#     def speak(self):
#         print("this is the  speak method from animal class")
#     def move(self):
#         print("this is the move method from the animal class")
        
# class Dog(Animal):
#     def speak(self):
#         print("this is the speak method from dog ")

# class Bird(Animal):
#     def speak(self):
#         print("this is the speak method from Bird ")


# obj=Dog()
# obj.speak()

# obj=Bird()
# obj.speak()






# class Employee:
#     company_name='Fujitsu'
    
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
        
# obj=Employee('sangamesh',100000)
# obj2=Employee('Harsha',500000)
# print(f"{obj.name}'s salary :{obj.salary}")
# print(f"{obj2.name}'s salary :{obj2.salary}")

# print(f"{obj.name}'s is working in {obj.company_name}")





#_________Create a BankAccount class with a private balance attribute and provide public getter and setter methods to interact with it (encapsulation).

# class BankAccount:
#     def __init__(self,initial=0):
#         self.__balance=initial
        
#     def get_balance(self):
#         return self.__balance
    
#     def set_balance(self,amount):
#         if amount <0 and abs(amount) < self.__balance:
#             print("Insufficient amount in bank account .")
#         else:
#             self.__balance+=amount
    
    
# account=BankAccount(1000)

# print(account.get_balance())
# account.set_balance(-2000)
# print(account.get_balance())




# class Person:
#     print("He/she is a person")

# class employee1(Person):
#     print("thiis is Emp 1 .")
    
# class employee2(Person):
#     print("thiis is Emp 2 .")
    
# obj=Person()
# # obj.employee()



# 5. Demonstrate multiple inheritance with a Person class and an Employee class, where Employee inherits from Person.




# class Person:
#     def __init__(self,name):
#         self.name=name
#         print(f'{self.name} is a person')
        
# class worker:
#     def __init__(self,job_title):
#         self.job_title=job_title
#         print(f"The job title of {self.job_title}")

# class emp(Person,worker):
#     def __init__(self,name,salary,job_title):
#         Person.__init__(self,name)
#         worker.__init__(self,job_title)
#         self.salary=salary
#         print(f'{self.name} s salary is {self.salary}')
        
# obj=emp('sangamesh',100000,"Full_stack_dev")



# Demonstrate Method Resolution Order (MRO) with multiple inheritance. Create classes ClassA, ClassB, and ClassC and display the method calling order.





# class ClassA:
#     def show(self):
#         print("classA")
    
# class ClassB(ClassA):
#     def show(self):
#         print("classB")
#         super().show()

# class ClassC(ClassB,ClassA):
#     def show(self):
#         print("classC")
#         super().show()


# obj=ClassC()

# obj.show()

# print(ClassC.__mro__)



#Note super method calls next Mro . ckassc->classb->classA





#  Write a class MathOperations that has both static methods and instance methods. Show the difference by calling methods using the instance and class name.?
 
 
# class Mathoperation:
#     def Multi(self,a,b):
#         return a*b
    
#     @staticmethod
#     def add(a,b):
#         return a+b
# obj=Mathoperation()

# print(obj.add(5,4))
# print(obj.Multi(4,4))




#Create an abstract class Shape with an abstract method area(). Derive Circle and Rectangle classes and implement the area() method.



# from abc import ABC, abstractmethod
# import math

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return math.pi * self.radius ** 2

# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

# c = Circle(3)
# r = Rectangle(4, 5)

# print("Circle area:", c.area())
# print("Rectangle area:", r.area())





#  Define a ComplexNumber class with attributes real and imaginary. Overload the + operator to add two complex numbers and the str() method for string representation.






# class Com:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img
        
#     def __add__(self,other):
#         return Com(self.real + other.real , self.img + other.img)
    
#     def __str__(self):
#         return f"{self.real} +{self.img}i"


# obj=Com(5,5)
# obj1=Com(4,7)


# obj3=obj+obj1

# print(obj3)




# Create a class Reverse that implements the iterator protocol to iterate over a list in reverse order using the __iter__() and __next__() methods.







# class Reverse:
#     def __init__(self, data):
#         self.data = data
#         self.index = len(data)

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration
#         self.index -= 1
#         return self.data[self.index]

# r = Reverse([10, 20, 30])
# for i in r:
#     print(i)












