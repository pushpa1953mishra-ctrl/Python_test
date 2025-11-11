numbers = [11,20,31,40,51,60,71,80,91,100]

def even(x):
    return x % 2 == 0

evens = list (filter(even,numbers))

print("Before Lambda :- ", evens)

print("********************************")

evens_lambda = list(filter(lambda x: x % 2 == 0 and x > 50,numbers))

print(evens_lambda)