NumOfStud = int(input ("Pls enter number of students :- "))

count = 1

while (count <= NumOfStud):
    Maths_Marks = int(input ("Pls enter marks in maths :- "))
    Phy_Marks = int(input ("Pls enter marks in Physics :- "))
    Chem_Marks = int(input ("Pls enter marks in Chemistry :- "))

    Average_Marks = (Maths_Marks + Phy_Marks + Chem_Marks) / 3

    if (Average_Marks <= 75):
        print ("Student not qualified")
    else:
        print ("Student qualified")

    count = count + 1
