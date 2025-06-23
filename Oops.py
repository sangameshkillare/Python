# class is blueprint of the object .
#the real time implementation of the class is caled as the object . or it is a instance of the class .
#bottom to up 
#popl divide the code in differet functions ,top to bottom approch 
#oops divids in obj and class , bottom to top approch , inheritanc n polymorphism ,abstraction and encaptulation

# what is object and what is class , explain with examaple ?
# what is the diff between oops ans pop?
# what is function what are different types of functions , explain all types of functions in detail ?
# what is the difference between buildin funtion and user defined function?
# what is the difference between user defined function and lambda function ?
# what is difference between print and  return ?
#what are the diffrent class methods in python ?
#what is the diffreence between class , static and dynamic method ?
#what is the diffreence between static variable and static method ?
#explain dynamic/ststic/class method in detail with example ?


# static methods  dynamic methods 




  #-----------creating and calling the class and object 
  
# class num:
#     a=2
#     b=3
# object1=num()
# print(object1.a)


# class add:
#     a=2
#     b=4
#     print(a+b)
# obj2=add()
# print(obj2.a)


# class sub:
#     a,b=5,4
#     print(a-b)
# obj1=sub()







# class car:
#     price=100
#     gst=18/100
#     total=price*gst
    
# obj=car()
# print(obj.price)

# print(obj.gst)
# print(f"total={obj.total}")



# class full_name:
#     name="sangamesh"
#     last_name="killare"
#     age=21
# s=full_name()
# print(s.name)
# print(s.last_name)
# print(s.age)



#----------------dynamic method 


# class num:
#   def div(self,a,b):
#     print(a//b)
  
# obj1=num()
# obj1.div(5,4)bject1




# class calculator:
#   @classmethod
#   def add(self,a,b):
#     return f"the addition is  : {a+b}"
#   @classmethod
#   def div(cls,a,b):
#     return f"the division is  : {a/b}"
#   @classmethod
#   def sub(cls,a,b):
#     return f"the substraction is  : {a-b}"
#   @classmethod
#   def mult(cls,a,b):
#     # return f"the multition is  : {a*b}"
#     print(f"the multition is  : {a*b}")

# object1=calculator()
# object1.add(5,5)
# object1.sub(5,5)
# object1.div(5,5)
# object1.mult(5,5)




#--------------combine two strings witj the help of object and classes

# class concate:
#   def strings(self,a,b):
#     str3=a+b
#     print(str3)
    
    
# object=concate()
# object.strings("sangamesh"," $ killare")



#----------class method


# class num:
#   @classmethod
#   def sub(cls):
#     print('hii from class method')
    
# obj1=num()
# obj1.sub()





#----------static method 



# class one:
#   @staticmethod
#   def add():
#     print("adion")
  
# obj1=one()
# obj1.add()
  

  
# class demo:
#   def d1(self):
#     print('this is a dynamic method .')
#   @classmethod
#   def d2(cls):   
#     print('this is a class method .')
#   @staticmethod
#   def d3():
#     print('this is a static method .')
  
# object=demo()
# object.d1()
# object.d2()
# object.d3()



# class car:
#     def __init__(self):
#         self.year=2004
#         self.model="bmw"
#         self.color="black"
# mycar=car()
# print(mycar.color)


# class person:
#     def __init__(self,Name,age):
#         self.name=Name
#         self.age=age
        
#     def fun1(self):
#         print( f"{self.name}{self.age}")
    
# p1=person("sangamesh",21)

# p1.fun1()



# class operation:
#     def __init__(self,x,y):
#         self.x=5
#         self.y=10
    
#     def add(self):
#         print(self.x+self.y)
# num= operation()
# num.add()


# class operation:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
    
#     def add(self):
#         print(self.x+self.y)
# num= operation(5,10)
# num.add()


# class operation:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
    
#     def add(self):
#         print(self.x+self.y)
#     def sub(self):
#         print(self.x-self.y)
#     def mult(self):
#         print(self.x*self.y)
#     def div(self):
#         print(self.x/self.y)
# num= operation(5,10)
# num.add()
# num.sub()
# num.mult()
# num.div()



# class car :
#     def __init__(self,make,model,year):
#         self.make=make
#         self.model=model
#         self.year=year
#         self.is_running=False
        
        
#     def start(self):
#         if not self.is_running:
#             self.is_running=True
#             print(f"{self.make} {self.model} started")
#         else:
#             print(f"{self.make} {self.model} started")
        
#     def stop(self):
#         if self.is_running:
#             self.is_running=False
#             print(f"{self.make} {self.model} stop")
#         else:
#             print(f"{self.make} {self.model} Already stopped")
            
#     def accelerate(self):
#         if self.is_running:
#             print(f"{self.make} {self.model} is accelerating")
#         else:
#             print("Start the car before accrlerating .")
            
            
            
# Car=car("Toyota","Fortuner",2025)
# Car.start()
# Car.accelerate()
# Car.stop()
    
        






#--------------- __ init__ is a spacial method  which called automatically , no need to call while ceating an object .


# class computer:
    
#     def cofig(self,name,bob):
#         self.name=name
#         self.bob=bob
#         print(f"From config : ",bob,name )
        
        
        
#     def cofig2(self):
#         print(f"From config-2 : ",self.bob,self.name )
        
        
# object=computer()
# object.cofig("sangamesh",2007)
# object.cofig2()




#-----------------


# class a:
#     def __init__(self):
#         print("This is init from A")
        
#     def feature1(self):
#         print("this is feature 1")
        
#     def feature2(self):
#         print("this is fratuer 2")

# class b (a):
#     def __init__(self):
#         super().__init__()                    #--------------------super keyword 
#         print("This is init from b")
        
#     def feature3(self):
#         print("this is feature 3")
        
#     def feature(self):
#         print("this is fratuer ")
        

# # obj=a()
# obj=b()     #--------it will print init from b not from a beacase if class have  init method then it dont go to the parent class and if we want init from  parent ther we want to use super() keyword .






#-------------
# # When you create an instance of class c, the __init__ method of class c is called. Inside this __init__ method, you have a call to super().__init__(). In Python, super() follows the method resolution order (MRO) to determine which class's __init__ method to call.

# In your case, class c inherits from both class a and class b. The MRO for class c is [c, a, b, object]. This means that super().__init__() in class c will call the __init__ method of class a first, and not class b.



# class a:
#     def __init__(self):
#         print("This is init from A")
        
#     def feature1(self):
#         print("this is feature 1")
        
#     def feature2(self):
#         print("this is fratuer 2")

# class b :
#     def __init__(self):
#         print("This is init from b")
        
        
#     def feature3(self):
#         print("this is feature 3")
        
#     def feature4(self):
#         print("this is fratuer ")
        
        
# class c(a,b) :
#     def __init__(self):
#         super().__init__()
       
#         print("This is init from c")
        
#     def feature5(self):
#         print("this is feature 3")
        
#     def feature6(self):
#         print("this is fratuer ")


# obj=c() 







#------------look to this code here we have create a  class computer and inside it we have two function. In first one there is special method called init and passing it value using self keyword (self is compulsory argument to access the variables in other function , increaces code simplacity , it is buildin keyword/function  or in another words using self we are binding data to every function or method  and they are working together .) . after we have created object named a object1 and passing it value , it will inisilize the values to the init function with the help of self keyword .


# class computer:
    
#     def __init__(self,name,bob):
#         self.name=name
#         self.bob=bob
#         print(f"From config : ",bob,name )
        
        
        
#     def cofig2(self):
#         print(f"From config-2 : ",self.bob,self.name )
        
        
# object1=computer("sangamesh",2007)
# object1.cofig2()





#----------instance variable and class variable in oops 


# class car ():
    
#     wheels=4                                   #--------------class variable beacuse of class namespace 
    
#     def __init__(self):
#         self.brand="bmw "                      #--------------instance variable because instance namespaces 
#         self.millage=10
        
    
    
# obj1=car()
# obj2=car()
# obj2.brand="tata"
# obj2.millage=6


# print(obj1.brand,obj1.millage,obj1.wheels)
# print(obj2.brand,obj2.millage,obj1.wheels)




#---------------inner class and outer class 


# class student():
    
#     def __init__(self,name,rollno):
#         self.name=name
#         self.rollno=rollno
#         self.lap=self.laptop()         #-------------object of laptop( ) class should inside of outer class normalli i __init__
        
#     class laptop():
        
#         def __init__(self):
#             self.brand="hp"
#             self.ram=8
            
#         def show(self):
#             print(self.brand,self.ram)
            
#     def show(self):
#         print(self.name,self.rollno)
    
            
            
# object=student('sangamesh',15)
# # print(object.name,object.rollno)
# object.show()
# object.lap.show()

# print(object.lap.brand,object.lap.ram)
            
            
     
     
     
#------------------ Student Class
# Create a class Student with:

# Attributes: name, roll_no, marks

# Method display() that prints the student's details.

# ✅ Try creating two students and calling the method for both
            
            
            
            
# class std:
  
#   def __init__(self,name,roll,mark):
#     self.name=name
#     self.roll=roll
#     self.mark=mark
    
#   def display(self):
#     print(self.name,self.roll,self.mark)
    
# obj=std('sangamesh',3,90)
# obj.display()