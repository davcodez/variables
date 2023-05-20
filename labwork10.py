first_name= input("Enter First Name: ")
last_name = input("Enter Last Name: ")
age = int(input("Enter Age: "))
curent_year = int(input("Enter Current Year: "))

earthly_appearance = curent_year -age
# print (first_name+" "+last_name+" "+"you are " +str(age)+ " years old and you came to earth in the year"+str(earthly_appearance))
print (f"{first_name} {last_name}, you are {age}years old and you came to earth in the year{earthly_appearance}")