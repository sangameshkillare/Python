
##@ Can we modify or add tuple . The answer is no but using serval methodes  we can modify it 
# 1) change it into list 2) Modify it 3) change it into tuple

origle_tuple=(1,2,3,4,5)
print(origle_tuple)

new_list=list(origle_tuple)
print(new_list)
new_list.append(67)
#new_tuple=tuple(new_list)
print(tuple(new_list))