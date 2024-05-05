# Hello wrold this is mezbah khan form backend developer 
# In This reposotiry we are going to build our porjects with pyrhon language and data framework like tensorflow 
# lets get started with our first project and that is the simple program of printing grades by mark of results  
                                        project set --> 1 
                        
nam1 = str (input("Enter your name : ")) <br>
marks = int(input('Enter your marks : '))

if (marks <= 100 and marks >= 80 ):<br>
 print("Hey",nam1,"your grade is A+")

elif (marks < 80 and marks >= 70 ):<br>
    print("Hey",nam1,"your grade is A")

if (marks < 70 and marks >= 60 ):<br>
    print("Hey",nam1,"your grade is B")
    
elif (marks < 60 and marks >= 50 ):<br>
    print("Hey",nam1,"your grade is C")
    
if (marks < 50 and marks >= 33 ):<br>
    print("Hey",nam1,"your grade is D")<br>

elif (marks < 32 and marks >= 0 ):<br>
    print("hey",nam1,"you're failed ") 
   <br>                                        
else :
    print("Accoding your mark-sheet")

# lets create a simple system with bainary and floating mode # 
# we are going to use the besic fundamentals like if / elif statements #
                      project no --> 2 

mezbah_cxc=   int(input("Enter your Deciaml number as required in 1-00  :"))<br>
isitak_cxc=float(input("Enter your floating number as reqquired in 1-100 :"))

if (mezbah_cxc <=100 and mezbah_cxc >=80):<br>
    print("system is started in bainary mode")
    
elif (isitak_cxc <= 100.00 and isitak_cxc >= 80.00):<br>
    print("System is started in floating mode")
    
if (mezbah_cxc <= 79 and mezbah_cxc >= 60 ):<br>
    print("System is working properly in bainary mode")
    
elif (isitak_cxc <= 79.00 and  isitak_cxc >= 60.00):<br>
    print("System is working properly in floating mode")

if(mezbah_cxc <= 34 and mezbah_cxc >= 59):<br>
    print("System is not working slowly in bainary mode")
    
elif(isitak_cxc <= 34.00 and isitak_cxc>= 59.00):<br>
    print("System is not working slowly in floating mode")

if( mezbah_cxc<= 33 and mezbah_cxc>= 0):<br>
    print("System is stoped in bainary mode")

elif (isitak_cxc<=33.00 and isitak_cxc>=0.0 ):<br>
    print("System is stoped in floating mode")


# Hey developers come i show you how to create a car properly with basic function and fundamentals #
# we are going to use the (class/def/init/staticmethods) and many more basic modules # 
                            projects no --> 3
                  
class cars: <br>
    def __init__(self,start,stop,run):   <br>
        self.start = start  <br>
        self.stop = stop  <br>
        self.run = run  <br>
        
    @staticmethod
    def start_car():
        print("car started")
        
    @staticmethod
    def stop_car():
        print("car stopped")
        
    @staticmethod
    def run_car():
        print("car is running")
        
class cars_blueprint(cars):  <br>
    def __init__(self,name,model,brand):  <br>
        self.name = name <br>
        self.model = model  <br>
        self.brand = brand  <br>
        
    def name(self):
        return self.name
    
    def model(self):
        return self.model
    
    def brand(self):
        return self.brand
    
class lamborgini(cars_blueprint):
    
    @staticmethod
    def cars_moduls (self):
        print("cars moduls are 4 Milions")

  # lets open an identifiers and call then by printing  
car_stck = lamborgini("lamborgini",'RK15677XZ',1990)  <br>
print(car_stck.name)  <br>
print(car_stck.model)  <br>
print(car_stck.brand)  <br>

# lets recalls those function we have create 
car_stck.start_car()  <br>
car_stck.stop_car()  <br>
car_stck.run_car()  <br>

The projects was amazing .. So lets move forward --> 
# Imagine we've a school and yo're haired as a programmer 
# You have to create a program like student data 
# So create a program for this problem by using functions # 

class Identity:<br>
    def __init__(self, name, age, gender):<br>
        self.name = name <br>
        self.age = age <br>
        self.gender = gender <br>

class Info(Identity): <br>
    def __init__(self, name, age, gender, roll, parents): <br>
        super().__init__(name, age, gender) <br>
        self.roll = roll <br>
        self.parents = parents <br>

class School: <br>
    def __init__(self): <br>
        self.students = [] <br>

    def add_student(self, student):
        self.students.append(student)

    def welcome_students(self):
        for student in self.students:
            print("Hello Student", student.name, "Welcome to our school")
            
# lets print those statements and recalls those functions 
school = School () <br>
student1 = Info("Sara", 12, "Female", 1234567890, "Mr. and Mrs. Smith") <br>
student2 = Info("John", 13, "Male", 1234567891, "Mr. and Mrs. Johnson") <br>
school.add_student(student1) <br>
school.add_student(student2) <br>
school.welcome_students() <br>



    

    
