#Q.5

file=None

try:
    filename=input("Enter filename:")
    file=open(filename,"r")
    print("file content")
    print(file.read())

except FileNotFoundError:
    print("File Not Found")

except PermissionError:
    print("Error: You do not have permission to access this because it might be a folder or locked.")

finally:
    if file is not None:
        file.close()
        print("File has been safely closed.")
    else:
        print("No file was opened,so nothing to close.")

#Q.6

try:
    num1=int(input("Enter 1st no.:"))
    num2=int(input("Enter 2nd no.:"))
    print("Result:",num1/num2)

except ZeroDivisionError:
    print("Cannnot divide by Zero.")

except ValueError:
    print("Invalid Input")

finally:
    print("End of code execution.")

#Q.7

try:
    n=int(input("Enter a no.:"))

except ValueError:
    print("Error,entered value must be only number.")

else:
    if n<=0:
        print("Error,Value must be positive number.")
    else:
        print("Square root:",n**(1/2))

finally:
    print("Execution Complete.")


