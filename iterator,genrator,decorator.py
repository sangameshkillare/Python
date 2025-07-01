# def gen():
#     i=1
#     n=200
#     while i<=n:
#         yield i
#         i+=1
    
    

# print(gen())
# i=gen()
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))


# def decorator(x):
#     print('starting ......')
#     hello()
#     print('ending ......')

# def hello():
#     print('executed successfully .....')
    
    
# decorator(hello)




#----------------iterator



# a=[1,2,3,4,5,6]

# it=iter(a)

# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))



# my_list = ['a', 'b', 'c']
# it = iter(my_list)

# for item in it:
#     if item!='c':
#         print(item)
#     else:
#         raise StopIteration




class count:
    def __init__(self,low,high):
        self.current=low
        self.high=high
    def __iter__(self):
        return self
    def __next__(self):
        if self.current<=self.high:
            num=self.current
            self.current+=1
            return num
        else:
            raise StopIteration

counter=count(1,10)
for num in counter:
    print(num)
        
        



