print("-------------------------------------")
inpValue = (input("Enter a Number or Word :"))
print("-------------------------------------")
print(inpValue)

for singleChar in inpValue :
  print(singleChar)

intInputVal = int(inpValue)

while intInputVal > 0 :
  # mod operator to give the reminder when divided  
  print(intInputVal%10)
  intInputVal = int(intInputVal/10)

