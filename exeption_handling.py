# exeption handling is the way to handle the expetion ,
# there two types of Exception complile and runtime Exception.

#-------compile time error - syntax error, runtime error .

#------indentation error
# for i in range(1,10):
# print(i)


#-----syntax error


# x=5
# print(x)
# y 5


#-----Name error

# Name="sangamesh"
# print(name)



#--------value error

# x=int(input("enter int :"))
# print(x)


#------type error

# name="akash"
# age=25
# print(name+age)


#-----------index error

# list=['python','js','rust','go']
# print(list[4])


#-------key error


# stdx={'name':'sangamesh','age':50,'collage':'rmc'}
# print(stdx['roll-no'])


#-------import error

# import numpy as np
# import addition as add




#--------- example without EH

# x=int(input('Enter 1 no :'))
# y=int(input('Enter 2 no :'))
# z=x/y
# print(z)
# print('done')


#----------with EH


# try :
#     x=int(input("enter number : "))
#     y=int(input("enter number : "))
#     result=x/y
#     print(result)
# except ZeroDivisionError:
#     print("cant divide by zero: ")
    
# else:
#     print("Execute successfully : ")
    
# finally:
#     print("Programe finished :")




#---------name error with EH


# try:
#     name='sangamesh'
#     print(Name)
# except NameError:
#     print("Paramerter is incorrect .")
# else:
#     print("Code succesfully exected.")
    




#-----------creating custome error



# class InvalidAgeError(Exception):
#     def __init__(self,age,message="Age is invalid"):
#         self.age=age
#         self.message=message
#         # super().__init__(self.message)



# try:
#     age=int(input("Enter your age : "))
#     if (0<= age <= 21):
#         raise InvalidAgeError(age)
#     else:
#         print("valid age ")

# except InvalidAgeError as e :
#     print(" not Eligible for vote")

# else:
#     print("Eligible for vote")
    
# finally:
#     print("vote now")



        
    
    



#----------------------fibo with execption handling


# try:
#     n=int(input("enter the number :"))
#     a=0
#     b=1
#     for i in range(1,n):
#         fibo=a+b
#         a=b
#         b=fibo
#         print(fibo)
        
# except:
#     print("Please enter valid Number :")
    
# else:
#     print("execute successfully.")
# finally:
#     print("End of programe.")









#------custom exception handling



# class invalidageerror(Exception):
#     def __init__(self,age,message="Age must be between 21 and 100 :"):
#         self.age=age
#         self.message=message
#         super().__init__(self.message)
        
    
    
# try:
#     age=int(input("enter the age :"))
#     if (21<=age and age>=100):
#         raise invalidageerror(age)
#     else:
#         print("valid age")
# except invalidageerror as e:
#     print(f"invalidageerror : {e.message} (age :{e.age})")
    
# else:
#     print('eligible for vote')
# finally:
#     print("rest of code ")        




#---------simple Indexerror example 


# try:
#     numbers =[1,2,3,4,5,6]
#     print(numbers[7])
# except IndexError as e:
#     print(f"IndexError:{e}")
# else:
#     print('No error')
# finally:
#     print("all set")
#--------------Atm



# class WithdrawalError(Exception):
#       pass

# class BankAccount:
#     # def __init__(self, balance):
#     #     self.balance = balance

#     def withdraw(self, amount,balance):
#         self.balance = balance
#         if amount > self.balance:
#             raise WithdrawalError(f"Cannot withdraw {amount}. Available balance: {self.balance}")
#         self.balance -= amount
#         print(self.balance)


# amount=int(input("enter the amount :"))
# balance=200
# try:
#     account = BankAccount()
#     account.withdraw(amount,balance)
#     print("Amount withdrawn successfully .")
# except WithdrawalError as e:
#     print(e)







# class Withdrawerror(Exception):
#     pass

# class Bank:
    
#     def withdraw(self,balance,amount):
#         self.amount=amount
#         self.balance=balance
        
#         if self.amount < self.balance:
#             raise Withdrawerror(f"Insufficient Funds , Please enter valid amount .")
#         else:
#             self.balance-= amount
#             print(f"Remaining balance : {self.balance}")
        
        
# amount=int(input("enter the amount to withdraw :"))       
# balance=1000
# try:
#      object=Bank()
#      object.withdraw(amount,balance)
#      print("amount withdrawn successfully .")
# except Withdrawerror as e:
#     print(e)




#---------------bank managment system


# class InvalidAmountError (Exception):
#     pass

# class InvalidNumber(Exception):
#     pass

# class Bank:
    
#     def deposit(self,balance,add):
#         self.balance=balance
#         self.add=add
#         print(f"Your {add} deposited sucssefully in your acount . Total balance-----> {balance}+{add}")
        
    
    
#     def withdraw(self,amount):
#         self.amount=amount
#         if amount <=0:
#             raise InvalidNumber ("please enter valid number :")
#         if amount>self.balance:
#             raise InvalidAmountError(f"Insufficient fund please check your Blance .")
#         else:
#             actual=self.balance-amount
#             print(f"Amount successfully withdrawn = {actual}")
            
        
# balance=0
# add=int(input("Enter the amount Deposit amount :-"))
# amount=int(input("Enter the amount withdaw amount :-"))

# try:
#     object=Bank()
#     print("1) deposit")
#     print("2) withdraw")
#     activity=int(input("enter number what you want to do :"))
#     object.deposit(balance,add)
#     object.withdraw(amount)
    
# except InvalidAmountError as e:
#     print(e)
    
    