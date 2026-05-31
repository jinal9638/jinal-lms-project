#question 1
'''
write a program to demonstrate different formatting options in print():
use sep to seprate values with a custom character
use end to customize what appears at the end of a print() statement
'''

a=[1,2,3,4,5]
print(*a,sep=" ")

print("hello","",end="everyone!")

#question2
"""
create a program that asks the user for their name,age and favorite hobby usinf the input()function then displays a formatted message like:
"hello,<name>!At<age>,enjoying<hobby>sounds"fun!"
"""

name=input("Type your name here:")
age=input("Tell me how old you are:")
hobby=input("Tell me about your hobby:")
print("Hello,",name, "At" ,age, "enjoying",hobby, 'sounds fun!"',"")

#question 3
"""
perform addition subtraction multiplication division floor division modulus and exponenitiation on two numbers input by user
"""

x=int(input("Enter 1st number:"))
y=int(input("Enter 2nd number:"))

print("addition:",x+y)
print("subtraction:",x-y)
print("multiplication:",x*y)
print("division:",x/y)
print("floor division:",x//y)
print("Remainder:",x%y)
print(x,"^",y,':',x**y)

#question 4
'''
write a
python program that:
declares variables of different datatypes
print their values and types using the type() function
'''

student="jinal"
born_date=13
time=11.30
s=True
print(student,type(student))
print(born_date,type(born_date))
print(time,type(time))
print(s,type(s))

#question 5
'''
create a program where the user inputs their height and weight
store the, in approprately named variables and print a formatted message displaying their values
'''

height=float(input("Tell me your height in feet:"))
weight=float(input("Tell me your weight in kg:"))
print(f"Your height is {height} cm and your weight is {weight} kg.")

#question 6
'''
implement a program to demonstrate logical operators(and,or,not)by asking the user for boolean inputs
'''
value1=input("enter a value True or False:").lower()
value2=input("enter a value True or False:").lower()

if value1=="true":
    value1=True
elif value1=="false":
    value1=False
else:
    print("Invalid input for value1.")
    exit()

if value2=="true":
    value2=True
elif value2=="false":
    value2=False
else:
    print("Invalid input for value2.")
    exit()

print('AND:',value1 and value2)
print('OR:',value1 or value2)
print('NOT VALUE1:',not value1)
print('NOT VALUE2:',not value2)


#QUESTION 7
'''
WRITE A PROGRAM TO DEMONSTRATE ASSIGNMENT OPERATORS (=,+=,-=,*=,/=,)USING A SINGLE VARIABLE
'''
N=5
print("N is",N)
N+=10
print("N+=10 is",N)
N-=5
print("N-=5 is",N)
N*=2
print("N*=2 is",N)
N/=2
print("N/=2 is",N)
