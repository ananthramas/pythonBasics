
counter = 0


while counter <10 :
  counter = counter +1
  # mod operator gives reminder.
  if counter%2 == 0 :
    print("Hello I am a even number : ",counter )
    continue
  print("This is next to hello statement", counter)
  if counter == 7 :
   break   
  
print("End of program")  
  