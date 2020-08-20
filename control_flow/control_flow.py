while True:
    try:
        deposit=int(input("Enter deposit amount"))
        
        if deposit<100:
            print("amount too low")    
            break      
        else:
            print("Deposited")  
            break
    except ValueError:
        print("Enter Numbers only")            

