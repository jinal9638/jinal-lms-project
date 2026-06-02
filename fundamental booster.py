from datetime import datetime
current_year=datetime.now().year

print("Welcome to the Interactive Personal Data Collector!")

name=input("\nPlease enter your name:")
age=int(input("Please enter your age:"))
height=float(input("Please enter your height in meters:"))
favourite_number=int(input("Please enter your favourite number:"))

print("\nThank you! Here is the information we collected:")



print(f"\nName: {name} (Type : {type(name)} Memory Address: {id(name)}")
print(f"Age: {age} (Type : {type(age)} Memory Address: {id(age)}")
print(f"Height: {height} (Type : {type(height)} Memory Address: {id(height)}")
print(f"Favourite Number: {favourite_number} (Type : {type(favourite_number)} Memory Address: {id(favourite_number)}")

print(f"\nYour birth year is approximately: {current_year-age} (based on your age of {age})" )

print("\nThank you for using the Personal Data Collector.Goodbye!")




    
