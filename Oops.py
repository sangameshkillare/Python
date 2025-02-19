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
            