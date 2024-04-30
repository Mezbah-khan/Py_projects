# Hello wrold, this is mezbah khan form backend developer # 
# We are gonna create some python projects in this Reposotiry and will push our gits value # 
#lets started our frist projects with basic fundamentals like mark counting with (if/elif) statements #

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
    print("Accoding your mark-sheet)
# This is a basic programming for mark counting and published results # 

                        # project no --> 2  
#This is our secend project and we are using the def function with simpale example # 
class mezbah :
    def __init__ (self,name,age):
        self.name = name
        self.age = age    
# lets create the body structure for this function # 
s1= mezbah("mezbah khan",18)
print(s1.name)
print(s1.age) 
                      # project no --> 3
# we're going create a loop using the function #                       
class mezbah :
    def __init__(self) :
        Loop_1= 0 
        for x in range (0,5):
            x += 1
            print(x)
s1= mezbah()
s2=mezbah() 
                  # project no --> 3
# lets create cars blue-print and make a wokeable code # 
class car:
     @staticmethod
     def start():
          print("car started")
          
     @staticmethod
     def stop():
          print("car stopped")
          
     @staticmethod
     def running ():
          print("car is runing")

class koyota (car):
     def __init__(self,name,price ):
          self.name = name
          self.price = price
          
car1 =koyota("Rokey",1000)
print(car1.name)
print(car1.price)
car1.start()
car1.running()
car1.stop()

           # project no --> 4
 # lets talk about inheritance model in python # 
class age :
    @staticmethod
    def age ():
     print("can voted")
     
class age1 (age):
    @staticmethod
    def age1():
        print("cant voted")
        
class check(age1):
    def __init__(self,name):
        self.name= name
        
voting = check("mezbah khan")
print(voting.name)
voting.age()
voting.age1()

             # project no --> 5
 # lets change the class attributes my methods -
class Person:
    name = "isitak"  # Class attribute
    
    def changename(self, name):
        self.name = name  # Assigning the new name to the instance attribute
        
p1 = Person()
p1.changename("mezbah khan")
print(p1.name)  # Output: "mezbah khan"













    
