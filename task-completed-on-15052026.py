#store and print name age city & take user input and display formatted outputname=input( "type your name : ")
name=input("type your name:")
print("Hello",name,"!")
age=input("what is your age:")
print("Oh,WOW!",name," you are only ",age)
city=input("what is your city name :")
print(city ,"is a great city!")

#swap two variables

x=1
y=2
x,y=y,x
print(x)
print(y)

#find square and cube of a number

number=int(input("enter a no.:"))
print("Square:",number**2)
print("Cube:",number**3)

#convert temperature (celsius into farenheit)

C=int(input("what is the temperature right now in celsius:"))
print(((C*1.8)+32),"Farenheit")

#simple calculator(+,-,*,/)

x=int(input("enter a no.:"))
y=int(input("enter a no.:"))


print("Add:",x+y)
print("sub:",x-y)
print("multiply:",x*y)
print("divide:",x/y)

#find remainder using %

x=int(input("enter a no.:"))
y=int(input("enter a no.:"))

print("remainder:",x%y)

#calculate area of rectangle/circle

l=int(input("length of the rectangle:"))
b=int(input("breadth of the rectangle:"))
print("area of rectangle:",l*b)
Pi=22/7
r=int(input("radius of the circle:"))
print("area of circle:",Pi*r**2)

#calculate simple interest

P=int(input("enter the principle amount:"))
R=int(input("enter the rate of interest:"))
T=int(input("enter the time of period in years:"))
print("Simple interest:",(P*R*T)/100)

#print first five elements

a=input("type anything:")
print(a[0:5])

#check greater number between two inputs

a=int(input("enter a no.:"))
b=int(input("enter a no.:"))
if a>b:
 print( a, "is greater than", b)
else:
 print(b, "is greater than", a)


#check number is equal or not
a=int(input("enter a no.:"))
b=int(input("enter a no.:"))
if a == b:
    print( a, "is equal to", b)
else:
    print( a, "is not equal to", b)


#voting Eligibility (age=>18)
print("LET'S CHECK YOUR AGE FOR YOUR VOTING ELIGIBILITY")
age=int(input("TYPE YOUR AGE HERE :"))
if age>=18:
    print("You are eligible to give a vote.")
else:
    print("Sorry,You are not eligible to give a vote.")


#find largest of 3 numbers
F=int(input("enter a 1st number :"))
S=int(input("enter a 2nd number :"))
T=int(input("enter a 3rd number :"))
if F>S>T:
    print(F, "is a greatest number.")
if S>F>T:
    print(S, "is a greatest number.")
else:
    print(T, "is a greatest number.")
    
#check pass/fail based on marks
print("Let's check you are pass or fail.")
marks=int(input("Type your marks here : "))
if marks>=35:
    print("Congrulations!You are pass...")
else:
    print("Sorry,You are fail...")
    
#check if number is between 1-100
print("Let's check your number is between 1-100.")
number=int(input("type a no. :"))
if number>0 and number<=100:
    print(number, "is between 1-100.")
else:
    print(number, "is not between 1-100.")

#check leap year
print("Let's check entered year leap year or not...")
year=int(input("enter a year :"))
if year%4==0 and year%100!=0 and year%400==0:
    print(year, "is leap year.")
else:
    print(year, "is not leap year.")


#check if number is divisible by 3 and 5
print("Let's check entered number is divisible by 3 and 5")
n=float(input("enter a no.:"))
if n%3==0 and n%5==0:
    print(n, "is divisible by 3 and 5.")
else:
    print(n, "is not divisible by 3 and 5.")


#validate input(age>18 and city=='surat')
print("Tell your age and city")
age=int(input("enter your age:"))
city=input("In which city are you living right now?")
if age > 18 :
    print("Person is major.")
else:
    print("Person is minor.")
if city=='surat' or city=='Surat':
    print("person is belongs to surat city.")
else:
    print("person is not belongs to surat city.")


#validate input(age>18 and city=='surat')2nd method
print("Tell your age and city")
age=int(input("enter your age:"))
city=input("In which city are you living right now?")
if age > 18 and city=='surat' or city=='Surat':
    print("Person is major and belongs to surat city.")
else:
    print("Person is minor and not belongs to surat city.")

#increment and decrement a number
n=int(input("enter a number:"))
a=int(input("how much you want to add:"))
d=int(input("how much you want to decrease:"))
print("after increment:",n+a)
print("after decrement:",n-d)

