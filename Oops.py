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
    
        


#---------------------------singal inheritance



# class parent1 :
#     def fun_1(self):
#         print("hello I am from fun_1 in parent1 class")
# class child(parent1):
#     def fun_2(self):
#         print("i am from child hello")
        
# object=child()
# object.fun_1()
# object.fun_2()
                             
                             
                             
# class parent1 :
#     def fun_1(self):
#         print("Bholenath")
# class child(parent1):
#     def fun_2(self):
#         print("sangamesh")
        
# object=child()
# object.fun_1()
# object.fun_2()



# class BankAccount:
#     def account_details(self):
#         print("Bank Account: Savings, Balance: $10,000")

# class SavingsAccount(BankAccount):
#     def interest_rate(self):
#         print("Interest Rate: 5% per year")

# # Creating an object of SavingsAccount class
# acc = SavingsAccount()
# acc.account_details()  # Inherited method
# acc.interest_rate()    # Child class method


# class calculator:
#     def input_number(self,a,b):
#         self.a=a
#         self.b=b
# class add(calculator):
#     def fun(self):
#         return self.a + self.b

# object=add()
# object.input_number(4,7)
# print(object.fun())



#---------multiple 



# class parent1:
#     def fun1(self):
#         print("hello from fun1 ")
# class parent2:
#     def fun2(self):
#         print("hello from fun 2")
# class parent3(parent1,parent2):
#     def fun3(self):
#         print("hello from fun3")
    
# obj=parent3()
# obj.fun1()
# obj.fun2()
# obj.fun3()


# class inputnumbers:
#     def input(self,a,b):
#         self.a=a
#         self.b=b
# class Add:
#     def add(self):
#         return self.a+self.b
    
# class calculator(inputnumbers,Add):
#     pass

# obj=calculator()
# obj.input(5,5)
# print(obj.add())




#----------multilevel 



# class grand_father:
#     def fun1(self,a,b):
#         self .a=a
#         self.b=b
        
# class parent(grand_father):
#     def fun2(self):
#         print(self.a+self.b)
    
# class child(parent):
#     def fun3(self):
#         print(self.a * self.b)
        
# obj=child()
# obj.fun1(10,2)
# obj.fun2()
# obj.fun3()



# #------------herachical 

# class parent:
#     def fun1(self,a,b):
#         self.a=a
#         self.b=b
# class child1(parent):
#     def fun2(self):
#         print(self.a+self.b)
# class child2(parent):
#     def fun3(self):
#         print(self.a*self.b)

# object1=child1()
# object1.fun1(5,4)
# object1.fun2()
        
# object=child2()
# object.fun1(5,5)
# object.fun3()


# Parent contains fun1(), which initializes a and b.
# Child1 inherits from Parent and has fun2() to perform addition.
# Child2 inherits from Parent and has fun3() to perform multiplication.
# We create separate instances of Child1 and Child2 to use their respective functions.


#-------------hybrid


# class Grand_parent:
#     def fun1(self,a,b):
#         self.a=a
#         self.b=b
# class parent1(Grand_parent):
#     def fun2(self):
#         print(self.a+self.b)
# class child1(parent1):
#     def fun3(self):
#         print(self.a*self.b)
# class parent2(Grand_parent):
#     def fun4(self):
#         print(self.a/self.b)
# class child2(parent2):
#     def fun5(self):
#         print(self.a-self.b)

# object=child1()
# object.fun1(10,5)
# object.fun2()
# object.fun3()


# object=child2()
# object.fun1(10,5)
# object.fun4()
# object.fun5()



#university ---> school ----> students



# class university():
#     def fun1(self):
#         print("ite form university")
# class school(university):
#     def fun2(self):
#         print("it is from school")
# class student1(school):
#     def fun3(self):
#         print("im student 1")
        
# class student2(school):
#     def fun4(self):
#         print("im student 2")
    


# class a:
#     def fun1(self):
#         print("fun1 ")
# class b(a):
#     def fun2(self):
#         print("fun2 ")
# class c(a):
#     def fun3(self):
#         print("fun3 ")
# class d(b,c):
#     def fun4(self):
#         print("from fun4")






# obj=d()
# obj.fun1()
# obj.fun2()
# obj.fun3()
# obj.fun4()





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