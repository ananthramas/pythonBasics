import random

MAX_ATTEMPTS = 5


print("------------------------------------")
print("    Guess Number in ",MAX_ATTEMPTS,"attempts")
print("-----------------------------------")

randomNumber = random.randint(0,20);


attemptCounter = 1

while attemptCounter <= 5 :
  print("Life - ",MAX_ATTEMPTS-attemptCounter+1)
  userNumber = int(input("Guess the number :"))
  if   userNumber == randomNumber :
    print("You have won. Guessed it right!")
    break
  elif userNumber > randomNumber :
    print("Better luck next time...Guess a smaller number")
  else :
    print("Better luck next time...Guess a bigger number")
  attemptCounter = attemptCounter+1

if(attemptCounter==6) :
  print(" You have lost number to be guessed was : ",randomNumber)
    



    

