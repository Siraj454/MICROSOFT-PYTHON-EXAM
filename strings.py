name=input("your name: ")
age=input("your age: ")
print("hello " +name +" "+age )
print(name.isalnum())
#more functions
adress="rawalpindi wedridge lalkurti"
i=adress.count('i')
print(f"i in adress appears {i} times ")
#replace
new_adress=adress.replace("wedridge","Saddar".upper())
print("new adress:",new_adress)
print("location of rawalpindi in adress is ",adress.find("rawalpindi"))
print("capitalize adress is ",adress.capitalize())
#more functions
message="Stay home it's vorona virus"
