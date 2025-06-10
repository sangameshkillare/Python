
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