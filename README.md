# Hello wrold this is mezbah khan form backend developer # 
# In This reposotiry we are going to build our porjects with pyrhon language # 
# lets get started with our first project and that's a program that will print your grade's as result marks # 
nam1 = str (input("Enter your name : "))
marks = int(input('Enter your marks : '))

if (marks <= 100 and marks >= 80 ):
 print("Hey",nam1,"your grade is A+")

elif (marks < 80 and marks >= 70 ):
    print("Hey",nam1,"your grade is A")

if (marks < 70 and marks >= 60 ):
    print("Hey",nam1,"your grade is B")
    
elif (marks < 60 and marks >= 50 ):
    print("Hey",nam1,"your grade is C")
    
if (marks < 50 and marks >= 33 ):
    print("Hey",nam1,"your grade is D")

elif (marks < 32 and marks >= 0 ):
    print("hey",nam1,"you're failed ")   
else :
    print("Accoding your mark-sheet")






    
