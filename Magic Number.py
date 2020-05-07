def Magic_number():
    print("Hello today this program will go over several calculations and it will come up the magic number.")
    reverse = 0
    reverse1 = 0
    validNumberChecker = 0
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ","!","@","#","$","%","^","&","*","(",")","_","-","+","=","`","~","?",",",".","<",">","/",";",":","]"]
    while(validNumberChecker == 0):
        x = (input("Please enter a number between 100 to 999: This number's first and third digits must differ from eachother by a value of 2 at minimum."))
        if str(x)[0:1] in alphabet:
            print("This is not a number.")
        else:
            x = int(x) 
            temp = x
            digit1 = str(x)[0:1]
            digit3 = str(x)[2:3]
            if x not in range (100,999):
                if (x < 100):
                    print("This number is too small!")
                if (x > 999):
                    print("This number is too big!")
                    
            else:
                differenceChecker = (abs(int(digit1)) - abs(int(digit3)))
                if (abs(int(differenceChecker)) < 2):
                    print("Your 1st and 3rd digits must have at minimum a 2 value difference.")
                else:
                    validNumberChecker = 1
    if(validNumberChecker == 1):
        print("Your number is "+str(x)+" correct? Okay, let's get on with the magic of math!")

        if x in range (100,999):
            while(x > 0):
                lastdigit = int(x) % 10
                reverse = int(reverse)*10 + int(lastdigit)
                x = int(x)//10
                step2 = int(reverse) - int (temp)
                step2 = abs(step2)
            
        print("Your number at Step 2: "+str(step2))
        step2Holder = step2
               
        if abs(step2) in range (-999,999):
             while(step2 > 0):
                lastdigit1 = int(step2) % 10
                reverse1 = int(reverse1)*10 + int(lastdigit1)
                step2 = int(step2)//10
                step3 = int(reverse1) - int (step2)
                step3 = abs(step3)
           
        step4 = int(step2Holder) + int(step3)
        print("Your number at Step 3: "+str(step3))
        print("Your Magic Number is: "+ str(step4))
        

        

