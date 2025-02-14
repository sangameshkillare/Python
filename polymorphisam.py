#single thing can  have a multiple forms  depends upon the situation

#-------------build in polimorphisam

# print(len("sangamesh"))
# print(len(["sangamesh","killare"]))


# def add(a,b,c=0):
#     return a+b+c
# print(add(2,5))
# print(add(2,4,6))

#----------arbetri argument

# def add(*arg):
#     return sum(arg)
# print(add(5,6))
# print(add(5,5,6))


#---------returns absulate values in diff data types 


# print(abs(-10))     
# print(abs(-4.5))      
# print(abs(3 + 4j))    



# ----------------max return the values for diff data type



# print(max("python"))      
# print(max([10, 20, 30]))  
# print(max((5, 15, 25)))   



#-------------------min



# print(min("python"))      
# print(min([10, 20, 30]))  
# print(min((5, 15, 25)))   



#----------------type


# print(type("python"))      
# print(type([10, 20, 30]))  
# print(type((5, 15, 25)))  



#------------sum

      
# print(sum([10, 20, 30]))  
# print(sum((5, 15, 25)))  



#-----------reversed


# print(list(reversed("python")))      
# print(list(reversed([10, 20, 30])))  
# print(tuple(reversed((5, 15, 25))))  




#----------method ooverloading

# Overloading is a concept in programming where multiple functions or methods have the same name but different parameters. It allows for improved code readability and flexibility. Overloading can occur in methods (method overloading) or operators (operator overloading), depending on the programming language.



# class calculator:
#     def add(self,a,b=0,c=0,d=0):
#         return a+b+c+d

# calc=calculator()
# print(calc.add(1))
# print(calc.add(1,4))
# print(calc.add(1,3,4))
# print(calc.add(1,3,4,5))



#--------------------------------------overriding-----------------------------------------

#-method overloading occer  in the same  class and same function 
#same class , same method but having diff parameters 
# 
# #overriding occur in in heritance 
# if child class , parent class having  same functions ,name
#child class overrieds the func of parent class and disply it own property




class father:
    def home(self):
        print("This is sangamesh fathers Home .")
        
class sangamesh(father):
    def home(self):
        # super().home()
        print("This is sangamesh's home.")
        
whos=sangamesh()
whos.home()



#-----------------exeption handling 


