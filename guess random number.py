import random
target=random.randint(1,100)


while True:
    userChoice=int(input("Enter a value"))
    if(userChoice==target):
        print("true guess")
        break
    elif(userChoice<target):
        print("the target is larger")
    else:
        print("the target is smaller")
        
        
        
        
print("--game is over--")
        
        

            
        
        
    
