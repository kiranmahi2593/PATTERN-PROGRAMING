print("*****************welcome to pattern programing*****************\n")

print("below are the patterns available :\n")


while True:
    available_patterns = {"1":"CAPITAL LETTERS","2":"small letters","3":"Numbers"}
    for values,keys in available_patterns.items():
        print(values,keys)

    print("=================================")

    user_selection = int(input("select any of the above options :"))
    

    if user_selection == 1:

        AVAILABLE_OPTIONS = ("A- Z")
        while True:
            import capital
            print("availableoptions are :",AVAILABLE_OPTIONS)
            user_input = (input("enter any charatcter :"))

            if user_input == 'A':
                print(capital.A(A))
            if user_input == 'B':
                print(capital.B(B))
            
                
                  
                  
            
            
            


    


    
