#QUESTION 1 IS SAME AS LAB WORK 1.2

#QUESTION 2
'''
WRITE A PROGRAM WHERE THE USER INPUTS FLOATING-POINT NUMBER.
CONVERT THIS NUMBER INTO AN INTEGER USING INT()  AND PRINT BOTH VALUES WITH A MESSAGE EXPLAINING THE DIFFERANCE
'''
float_value=float(input("Enter a decimal a value:"))
int_value=int(float_value)

print("\nOriginal Decimal value:",float_value)
print("Converted into an Integer value:",int_value)
print("int() removes the decimal part and keep only whole number.")
#QUESTION 3
'''
CREATE A PROGRAM THAT:
TAKES A BOOLEAN VALUE(TRUE OR FALSE)AS INPUT
CONVERTS THE BOOLEAN TO AN INTEGER AND A STRING AND PRINTS ALL THREE VALUES
'''
data=input("Enter True or False:").capitalize()
if data =="True":
    bool_value=True
elif data =="False":
    bool_value=False
else:
    print("Invalid data entered...")
    
bool_string=str(data)
bool_integer=int(bool(data))
print("STRING BOOLEAN VALUE:",bool_string,"\nINTEGER BOOLEAN VALUE:",bool_integer,"\nBOOLEAN  VALUE:",bool_value)

#q.4 repeat of fundamental booster

#q.5  repeat of lecture practice

