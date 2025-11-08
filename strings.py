word = "Bangalore"

print(word[0])

print(word[-1])

print (word[2])

print(len(word))

print(word[3:])

for char in word:
    print(char)

search_char="B"

if search_char in word:
    print("found")
else:
    print("Not Found")

multi_line = "VISHAL MISHRA bolta hai " \
"JAI mahakal " \
"JAI SHRI RAM"

print(multi_line)

text = "Date is 8 11 2025"
print(text.split(" ", 2)) #2 signifies to split till the second delimiter

#If we want to fetch date only
#The split() method in Python is a string method used to divide a string into a list of substrings based on a specified delimiter. 

print("KK")
print(text.split(" ",2))

#Reverse of split is the join
lst=["Hi","Hello","How","Are","You"]
print(" ".join(lst))
new_str=" ".join(lst)

#The Join function is used to create a string by joining or combining 
# Every element in a list using delimiter

#strip used to remove white spaced char before and after the string

word = " Times Pro "
print(word.strip())
print(new_str)

#Find returns the index of first occurence
print(new_str.find('ll'))

date = "Today's Date is 8 11 2025"

print(date.split(" ",3)[3].replace(" ","-"))