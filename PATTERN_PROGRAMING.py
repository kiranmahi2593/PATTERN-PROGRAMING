print("*****************welcome to pattern programing*****************\n")

print("Below are the available patterns  :\n")


while True:
    available_patterns = {1:"CAPITAL LETTERS",2:"small letters",3:"Numbers"}
    for values,keys in available_patterns.items():
        print(values,keys)
        
    print("=================================")

    user_selection = int(input("Select any of the above options :"))

######################## CAPITAL LETTERS ######################            

    if user_selection == 1:

        AvailableOptions = ("A to Z")
        while True:
            print("Available Options are :",AvailableOptions)

            import capital
            user_input = input("enter any charatcter :")

            if user_input == 'A':
                print(capital.A())
            elif user_input == 'B':
                print(capital.B())
            else:
                print("invalid input : Exitings")
                break
######################## SMALL LETTERS ###################### 
            
    elif user_selection == 2:
        AvailableOptions = ("a to b")
        while True:
            print("Available Options are :",AvailableOptions)

            import small
            user_input = input("enter any charatcter :")

            if user_input == "a":
                print(small.a())
            elif user_input == 'b':
                print(capital.b())
            else:
            
                print("invalid input : Exitings")
                break


    
                

        
    
                



                
                  
                  
            
            
            


    


    
