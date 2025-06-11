#Abstraction in programming is the concept of hiding complex implementation details and showing only the essential features of an object or system to the user.

# It helps in:

# Reducing complexity

# Increasing code reusability

# Focusing on what an object does instead of how it does it



# what is abstraction ?
# what is abstract class ?
# what is abstract method ?
# what is encapsulation , explain with live example ?
# what are the aaccess specifiers in python ?
# what is the difference between private ,public and protected ?
# write a programe to check the given str in palindrome or not  with the help of abstrction ?

# we use decorator for implementing abstraction .

# from abc import ABC , abstractmethod
# class Baseclass(ABC):
#     @abstractmethod 
#     def method_1(self):
#         print("hello")
    
# obj=Baseclass()
# obj.method_1()




#----------ex1
from abc import ABC , abstractmethod
class Shape(ABC): #abstract class
    @abstractmethod   #decorator of abstract method 
    def area(self): #abstract method
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
    

class Rectangle (Shape):   #concrete class
    def __init__(self,width,height):   #initialized method
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height
    
    def perimeter(self):
        return 2*(self.width+self.height)
    
obj=Rectangle(5,8)  #creates the obj
print(f"Area:{obj.area()}")  # calling the function 
print(f"perimeter:{obj.perimeter()}")






