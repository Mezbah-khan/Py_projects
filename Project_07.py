# hello wrold this is mezbah khan from backend developer 
# Lets create project with python laibaries and dict keys
# lets build this project with proper codes 

class dictonary : 
    hello = "This is a minni project: "
    
    # lets create the instructor 
    def __init__(self , Data ):
        self. Data = Data
        
    # lets create the warning notice 
    @staticmethod
    def warning ():
        print('Only int , str, bolean value is required : ')
        
    def val_dict(self, Data):
        if type(self.Data) == str:
            print(self.Data)
            
        elif type(self.Data) == int:
            print(self.Data)
            
        elif type(self.Data) == bool:
            print(self.Data)
            
        elif type(self.Data) == float:
            print(self.Data)
        else:
            dictonary.warning()
            
    # Let's create the input function for user data
    
input_data = {} 
input_data['Name'] = str(input('Enter your name: '))
input_data['Age'] = int(input('Enter your age: '))
input_data['Gender'] = str(input('Enter your gender: '))
input_data['Married'] = bool(input('Enter your marital status: '))
input_data['section'] = float(input('Enter your barth section: '))


    # Lets recall those function with identifiers 
System_check = dictonary(input_data)
print(System_check.hello) 
print('This is your store data : ',System_check.Data)
