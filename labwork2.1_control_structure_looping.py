#Q.1 repeat

#Q.2
'''
CREATE A PROGRAM THAT:
ACCEPT A USER'S AGE AS INPUT
USES NESTED IF ELSE STATEMENTS TO CATEGORIZE THE USER INTO AGE GROUPS:
-CHILD(0-12)
-TEENAGER(13-19)
-ADULT(20-59)
-SENIOR(60+)
'''

age=int(input("Enter your age:"))

if  age>=0:
    if age<=12:
        print("YOU ARE IN CHILD AGE GROUP")
    else:
        if age<=19:
            print("YOU ARE IN TEENAGER AGE GROUP")
        else:
            if age<=59:
                print("YOU ARE IN ADULT AGE GROUP")
            else:
                print("YOU ARE IN SENIOR AGE GROUP")
else:
    print("INVALID AGE ENTER")

#Q.3 REPEAT

#Q.4
'''    
WRITE PYTHON PROGRAM TO:
TAKE A NUMBER AS INPUT FROM THE USER AND CHECK WHETER IT IS NEUTRAL NUMBER OR NOT USING A LADDER IF STATEMENT
'''
n=int(input("enter a no:"))
if n==0:
    print(n,"is neutral number. ")
if n<0:
    print(n, "is negative number.")
if n>0:
    print(n, "is positive number.")

