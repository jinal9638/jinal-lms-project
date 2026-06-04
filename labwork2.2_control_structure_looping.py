'''Q.1

Write a Program in Python to find the maximum number from the given three numbers using a nested if statement.'''

a=1
b=2
c=3
d=4

if a>=b:
    if a>c:
        print(a,"is maximum number.")
    else:
        print(c,"is maximum number.")
else:
    if b>c:
        print(b,"is maximum number.")
    else:
        print(c,"is maximum number.")
    

'''Q.2

Write a Program in Python to find the minimum number from the given three numbers using a nested if statement.
'''

if a<=b:
    if a<c:
        print(a,"is minimum number.")
    else:
        print(c,"is minimum number.")
else:
    if b<a:
        print(b,"is minimum number.")
    else:
        print(c,"is minimum number.")
    

'''Q.3

Write a Program in Python to find the maximum number from the given four numbers using a nested if statement.
'''

if a>b:
    if a>c:
        if a>d:
            maximum=a
        else:
            maximum=d
    else:
        if c>d:
            maximum=c
        else:
            maximum=d
else:
    if b>c:
        if b>d:
            maximum=b
        else:
            maximum=d
    else:
        if c>d:
            maximum=c
        else:
            maximum=d
print("MAXIMUM NUMBER:",maximum)
            




'''Q.4 REPEAT LECTURE PRACTICE'''

#Q.5
'''
Write a Program in Python to create a menu-driven fast-food order system using the 'match case' feature.

For example:

Press 1 to order a Sandwich

Press 2 to order a Pizza

Press 3 to order a Burger

Extend this program by adding a nested match case for each menu item's subtype selection by the user.

For example:

Press 1 for Thin Crust Pizza

Press 2 for Cheese Burst Pizza

Press 3 for Fresh Dough Pizza
'''
while True:
    print("\nWelcome to the Fastfood court!")

    while True:
        print("\nPress 1 to order a Sandwich \nPress 2 to order a Pizza \nPress 3 to order a Burger \nPress 4 to Exit")
        order=int(input("\nenter your order 1,2,3 or 4:"))


        match order:
            case 1:
                print("\nWhich type of sandwich you want? \nPress 1 to order Grill Sandwich \nPress 2 to order Tandoori sandwich \nPress 3 to order Bombay sandwich")

                sandwich=int(input("\nenter your order 1,2 or 3:"))
                match sandwich:
                    case 1:
                        print("You ordered Grill Sandwich. ")
                    case 2:
                        print("You ordered Tandoori Sandwich.")
                    case 3:
                        print("You ordered Bombay Sandwich.")
                    case _:
                        print("Invalid input entered.")
                        continue
            case 2:
                 print("\nWhich type of pizza you want? \nPress 1 for Thin Crust Pizza \nPress 2 for Cheese Burst Pizza \nPress 3 for Fresh Dough Pizza")

                 pizza=int(input("\nenter your order 1,2 or 3:"))

                 
                 match pizza:
                     
                     case 1:
                         print("You ordered Thin Crust Pizza.")
                     case 2:
                         print("You ordered Cheese Burst Pizza.")
                     case 3:
                         print("You ordered Fresh Dough Pizza.")
                     case _:
                         print("Invalid input entered.")
                         

            case 3:
                print("\nWhich type of Burger you want? \nPress 1 for Veg cheese burger \nPress 2 for Tandoori cheese burger \nPress 3 for Peri Peri cheese burger")

                burger=int(input("\nenter your order 1,2 or 3:"))
                match burger:
                    case 1:
                        print("You ordered Veg cheese burger.")
                    case 2:
                        print("You ordered Tandoori cheese burger.")
                    case 3:
                        print("You ordered Peri Peri cheese burger.")
                    case _:
                        print("Invalid input entered.")
                        continue

            case 4:
                print("\nThank you for visiting!Have a Great Day!")
                break

            case _:
                print("Invalid input entered.")


    break



#Q.6

'''
Write a Program in Python to create a menu-driven telecom calling system using the 'match case' feature.

For example:

Press 1 for English

Press 2 for Hindi

Press 3 for Gujarati

Extend this program by adding a nested match case for each menu item's appropriate subtype selection by the user.
'''


while True:
    print("\nWelcome to Jio")

    while True:
        print("\nPlease select your language \nकृपया अपनी भाषा चुनें। \nકૃપા કરીને તમારી ભાષા પસંદ કરો. \n")
        print("Press 1 for English")
        print("हिंदी के लिए 2 दबाएँ।")
        print("ગુજરાતી માટે ૩ દબાવો")
        print("Press 4 for Exit (बाहर निकलने के लिए 4 दबाएँ।) (બહાર નીકળવા માટે 4 દબાવો)")

        language=int(input("choose your language 1,2,3 or 4:"))

        match language:
            case 1:
                print("\nPress 1 for Data Balance")
                print("Press 2 for explore new data plans")
                print("Press 3 for report network issue")
                print("Press 0 for Directly contact our customer support agent")

                sel_option=int(input("\nENTER YOUR CHOICE 1,2,3 OR 0:"))

                match sel_option:
                    case 1:
                        print("\nYour available data balance is 1.5 GB.")
                    case 2:
                        print("Available Data Plans: 1.5GB/Day, 2GB/Day,2.5GB/Day.")
                    case 3:
                        print("We have registered your complain,We will try to resolve it.")
                    case 0:
                        print("Connecting to our customer support agent...")
                    case _:
                        print("Invalid Input.")

            case 2:
                print("\nडेटा बैलेंस के लिए 1 दबाएँ।")
                print("नए डेटा प्लान देखने के लिए 2 दबाएँ।")
                print("नेटवर्क समस्या की रिपोर्ट करने के लिए 3 दबाएँ।")
                print("हमारे कस्टमर सपोर्ट एजेंट से सीधे संपर्क करने के लिए 0 दबाएँ।")

                sel_option1=int(input("\nअपनी पसंद दर्ज करें 1, 2, 3 या 0:"))

                match sel_option1:
                    case 1:
                        print("\nआपका उपलब्ध डेटा बैलेंस 1.5 GB है।")
                    case 2:
                        print("उपलब्ध डेटा प्लान: 1.5GB/दिन, 2GB/दिन, 2.5GB/दिन।")
                    case 3:
                        print("हमने आपकी शिकायत दर्ज कर ली है, हम इसे हल करने की कोशिश करेंगे।")
                    case 0:
                        print("हमारे कस्टमर सपोर्ट एजेंट से कनेक्ट किया जा रहा है...")
                    case _:
                        print("अमान्य निवेश।")

            case 3:
                print("\nડેટા બેલેન્સ માટે 1 દબાવો.")
                print("નવા ડેટા પ્લાન શોધવા માટે 2 દબાવો")
                print("નેટવર્ક સમસ્યાની જાણ કરવા માટે 3 દબાવો")
                print("અમારા ગ્રાહક સપોર્ટ એજન્ટનો સીધો સંપર્ક કરવા માટે 0 દબાવો")

                sel_option2=int(input("\nતમારી પસંદગી ૧,૨,૩ અથવા ૦ દાખલ કરો:"))

                match sel_option2:
                    case 1:
                        print("\nતમારું ઉપલબ્ધ ડેટા બેલેન્સ ૧.૫ જીબી છે.")
                    case 2:
                        print("ઉપલબ્ધ ડેટા પ્લાન: ૧.૫ જીબી/દિવસ, ૨ જીબી/દિવસ, ૨.૫ જીબી/દિવસ.")
                    case 3:
                        print("અમે તમારી ફરિયાદ નોંધી લીધી છે, અમે તેનો ઉકેલ લાવવાનો પ્રયાસ કરીશું.")
                    case 0:
                        print("અમારા ગ્રાહક સપોર્ટ એજન્ટ સાથે કનેક્ટ થઈ રહ્યું છે...")
                    case _:
                        print("અમાન્ય ઇનપુટ.")

            case 4:
                print("\nThank you for calling in Jio")
                print("Jio पर कॉल करने के लिए धन्यवाद।")
                print("Jio માં ફોન કરવા બદલ આભાર.")
                break

            case _:
                print("\nInvalid input")
                print("अमान्य निवेश।")
                print("અમાન્ય ઇનપુટ")

    break
                
                

            


                

