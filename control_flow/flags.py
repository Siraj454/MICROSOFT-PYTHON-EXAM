#setting flags
free_food=False
order=float(input("Enter amount of order:"))
if float(order) >150:
    free_food=True
if free_food:
    print("Enjoy Your discount!")