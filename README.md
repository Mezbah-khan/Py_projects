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


# Hey developers come i show you how to create a cars properly with basic functions #
# we are going to use the (class/def/init/staticmethods) and many more basic codes # 

class cars:
    def __init__(self,start,stop,run):
        self.start = start
        self.stop = stop
        self.run = run
        
    @staticmethod
    def start_car():
        print("car started")
        
    @staticmethod
    def stop_car():
        print("car stopped")
        
    @staticmethod
    def run_car():
        print("car is running")
        
class cars_blueprint(cars):
    def __init__(self,name,model,brand):
        self.name = name
        self.model = model
        self.brand = brand
        
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
        
car_stck = lamborgini("lamborgini",'RK15677XZ',1990)
print(car_stck.name)
print(car_stck.model)
print(car_stck.brand)

# frist lets stared the car #
car_stck.start_car()
car_stck.stop_car()
car_stck.run_car()




    

    
