#child class can acess the properties of parent class
# # singal - 1 parent and child class
# Multiple-multiple parent nad 1 child
#multilevel in heritance - 3 levels  super class- parent class- child class
#heirachical - 1 paren multiple childs
#hybrid - combination of any inheritance types like multi and singal





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