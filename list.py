lst = [2,4,7,9.7,'a','r','tata']

print (len(lst))

print (lst[2:5])

if (9.72 in lst):
    print ("Present Sir")

else:
    print ("Absent Sir")

# Use of Append
lst.append("Jai Shri Ram")

print(lst)

# Use of extend

#lst.extend()

another_list = [4, 5, 6,12,19,3,7]
lst.extend(another_list)

# Use of insert

lst.insert(3,"JAI MAHAKAL")
print(lst)

# Use of sort

another_list.sort()
print("After sorting:- ",another_list)

# Use of remove
lst.remove(4)

print(lst)

#Use of pop to pop element at index
ele=lst.pop(2)
print("VM",ele)
print(lst)

#Use of del
del lst[2]

print(lst)

del lst[3:5]

print(lst)

#Clear the list
lst.clear()

print(lst)