
#we can directly  access the  variables and methods , called as public modifier


# class industry:
#     def __init__(self):
#         self.course="DA"
#         self.tech="python"
#     def coursedetails(self):
#         return self.course + self.tech
    
# obj=industry()
# print(obj.course)
# print(obj.tech)
# print(obj.coursedetails) 



#--------------protected modifiers


# class first:
#     def __init__(self):
#         self._a=20
#         self._b=22
#     def num(self):
#         print(self._a,self._b)

# class second:   #class second(first):
#     def num2(self):
#         print(self._a)
        
        
# obj=second()
# obj.num()
# obj.num2()




# class name:
#     def __init__(self):
#         self._fn='sangamesh'
#         self._ln='killare'
#     def last(self):
#         print(self._fn,self._ln)

# class execute(name):
#     def new(self):
#         print(self._fn,self._ln)
        
        
# obj=execute()
# obj.last()
# obj.new()
    
    
# class alpha:
#     def num(self):
#         self.__fn = 'sangamesh' # Still mangled

#     def value(self): # Public getter method
#         return self.__fn

# class no(alpha):
#     def new(self):
#         print(self.value()) # Access via public method

# obj = no()
# obj.num()
# obj.new()



# Output: sangamesh  
    
# class alpha:
#     def num(self):
#         self.__fn='sangamesh'
    
# class no(alpha):
#     def new(self):
#         print(self.__fn)
        
# obj=no()
# obj.num()
# obj.new()









#------------ public,private,protected




class MyClass:
    def __init__(self):
        self.public_var = "I am public"
        self._protected_var = "I am protected"
        self.__private_var = "I am private"

    def public_method(self):
        print("Public method:", self.public_var)

    def _protected_method(self):
        print("Protected method:", self._protected_var)

    def __private_method(self):
        print("Private method:", self.__private_var)

    # Method to access private members within the class
    def access_private(self):
        self.__private_method()


# Create an object
obj = MyClass()

# Accessing public variable and method
print(obj.public_var)
obj.public_method()

# Accessing protected variable and method (still accessible, but convention says "internal use only")
print(obj._protected_var)
obj._protected_method()

# Trying to access private variable and method directly (will raise AttributeError)
# print(obj.__private_var)         # Uncommenting this will raise an error
# obj.__private_method()           # Uncommenting this will raise an error

# Accessing private variable and method indirectly
obj.access_private()

# Accessing private members using name mangling (not recommended but possible)
print(obj._MyClass__private_var)
obj._MyClass__private_method()




# write a programme to print  area ,perimeter of the rectangle -1) make all variables public .2) all variable private 3) all variables protected

