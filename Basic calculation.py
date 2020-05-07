def project1():
   answer= input("PLAYER 1, please pick a number: ")
   x= input("Player 2, please pick a number: ")
   
   factor= int(99) - int(answer)
   b= int(x) + int(factor)
   c=1+(int(b) - 100)
   d=int(x) - int (c)

   print("I said the answer was " + str(answer) + " and the calculation result is " + str(d))
   
