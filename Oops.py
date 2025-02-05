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



class car :
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.is_running=False
        
        
    def start(self):
        if not self.is_running:
            self.is_running=True
            print(f"{self.make} {self.model} started")
        else:
            print(f"{self.make} {self.model} started")
        
    def stop(self):
        if self.is_running:
            self.is_running=False
            print(f"{self.make} {self.model} stop")
        else:
            print(f"{self.make} {self.model} Already stopped")
            
    def accelerate(self):
        if self.is_running:
            print(f"{self.make} {self.model} is accelerating")
        else:
            print("Start the car before accrlerating .")
            
            
            
Car=car("Toyota","Fortuner",2025)
Car.start()
Car.accelerate()
Car.stop()
    
        

        