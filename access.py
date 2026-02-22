lastname="abbas" 
#THIS IS THE GLOBAL VARIABLE(LAST NAME) WHICH CAN BE ACCESSED ANYWHERE IN THE CODE
from main import access
def greet_employee(name):
     print("Welcome to the company, " + name + " " + lastname)
   
for attempt in range(1,4):
    password = input("Enter password:")
    if password =="musa989B":
        print("Access granted")
        #NAME IS THE LOCAL VARIABLE
        greet_employee("Musa")
        access("musa")
        break
    elif attempt>=3:
         print("Locked")
         break
    else:
         print("try again")