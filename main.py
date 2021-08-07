import random

MAX_ATTEMPTS = 5

print("Guess the Number", MAX_ATTEMPTS, "attempts")

randomNumber = random.randit(0,20);
print("Random", randomNumber)
attempt_counter = 0

while attempt_counter < 5 :
  print("Life - ", MAX_ATTEMPTS - attempt_counter+1)

  userNumber = int(input("Guess the number : "))
  if userNumber == randomNumber :
   print("You did it!")
   break
  elif userNumber > randomNumber :
   print("Guess a smaller number")
  else :
   print("Guess a bigger number")
  attempt_counter = attempt_counter+1
if (attempt_counter == 6)
 print("You have lost, number to be guessed was : ", randomNumber)
