while True:
    print("Welcome to the Pattern Generator and Number Analyzer!\n\n\n")

    while True:
        print("Select an option: \n1.Generate a pattern \n2.Analyze a Range of Numbers \n3.Exit")
        choice=int(input("Enter your choice: "))
        
        if choice==1:
            rows=int(input("Enter the number of rows for the pattern : "))
            
            
            if rows<=0:
                print("Please enter value which is greater than 0.")
            else:
                print("\n\nPattern")
                for i in range(1,rows+1):
                    print("*" * i)
                    
            

            print("\n\n")
        elif choice==2:
            start=int(input("\n\nEnter the start of the range: "))
            end=int(input("Enter the end of the range: "))

            total=0
            print()
            if start>end:
                print("Error,Please enter the start value which is less than or equal to end value.\n")
                continue
            for num in range(start,end+1):
                if num%2==0:
                    print("Number",num,"is Even")
                else:
                    print("Number",num,"is Odd")

                total+=num

            print(f"Sum of all numbers from {start} to {end} is: {total}\n\n ")

        elif choice==3:
            print("Exiting the program.Goodbye!\n\n")
            break
            
        else:
            print("Error,Please enter valid number.\n\n")




            
    break
        
        
            
            
