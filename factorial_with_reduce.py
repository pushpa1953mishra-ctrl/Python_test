from functools import reduce

n=8
lst = list(range(1,n+1))

out = reduce(lambda x,y: x*y,lst)

print(out)
        