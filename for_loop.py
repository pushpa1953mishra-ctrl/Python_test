numList = [10,100,190,180,120,176,189,190]
sum = 0
count = 0

for ele in numList:
    sum = sum + ele
    count = count + 1

print ("Sum is :-",sum)
print ("Count is :-",count)

Mean = round(sum/count,2)

print (Mean)