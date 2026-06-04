#Q.1
'''
Write a program using a `while loop to:

- Take numbers as input from the user until they enter 0.
'''
while True:
    n=int(input("TYPE ANY NO.:"))

    if n == 0:
        print("We get the zero")
        break
            
print("\n")
#Q.2
'''
Create a program using a `for loop to:

Iterate over a given range(1 to 10).

- Print each digit's square, one per line.
'''
for i in range(1,11):
    print(i,"^2 =",i**2)
print("\n")
#Q.3
'''
Write a program to:

- Use a while loop to print all even numbers between 1 and 50.
'''
for i in range(1,51):
    if i%2 == 0:
        print(i,"is Even number.")
        
print("\n")

#Q.4
'''
Write a program to:

- Use the `range() function to generate a sequence of numbers from 1 to 20.

- Print only the odd numbers using a `for loop.
'''

for i in range(1,21):
    if i%2!=0:
        print(i,"is Odd number.")

print("\n")

#Q.5
'''
Implement a program that:
* Uses the `range() function with three arguments
(start, stop, step) to print multiples of 5 from 5 to 50.
'''

count=0

for i in range(5,51,5):
    count+=1
    print("5*",count,"=",i)

print("\n")

#Q.6
'''
Create a program using a for loop and range() to:

  - Print a reverse countdown from 10 to 1.
'''
print("Here coundown begins...")

for i in range(10,0,-1):
    print(i)

print("\n")

#Q.7
'''
Write a program that:

  - Uses a for loop and range() to iterate through numbers from 1 to 50.

  - Checks if each number is divisible by 2, 3, or both using nested if-elif-else.

  - Prints messages for each case (e.g., "Divisible by 2", "Divisible by 3", "Divisible by both").
'''

for i in range(1,51):
    if i%2==0 and i%3==0:
        print(i,"Divisible by both")
    elif i%2==0:
        print(i,"Divisible by 2")
    elif i%3==0:
        print(i,"Divisible by 3")
    else:
        print(i,"is not divisble 2 or 3.")
    

    
