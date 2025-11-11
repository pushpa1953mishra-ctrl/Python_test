from functools import reduce

lst = [2,3,6,8,9]
       
       
total = reduce(lambda x,y:x+y,lst)

print(total)