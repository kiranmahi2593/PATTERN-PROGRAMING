

def A():
    for row in range(7):
        for col in range(5):
            if (row==0)and (col in {1,2,3}):
                print("*",end=" ")
            elif (row in {1,2,4,5,6}) and (col in {0,4}):
                print("*",end=" ")
            elif (row in {3}):
                print("*",end=" ")
            
            else:
                print(' ',end=" ")
        print()
#A()

print()
print()

def B():
    for row in range(7):
        for col in range(5):
            if row==0 and col in {0,1,2}:
                print("*",end=" ")
            elif row in {1,2,4,5} and col in {0,3}:
                print("*",end=" ")
            elif row in {3,6} and col in {0,1,2}:
                print("*",end=" ")
            else:
                print(' ',end=" ")
        print()
#B()
        

                
