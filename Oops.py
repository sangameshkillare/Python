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