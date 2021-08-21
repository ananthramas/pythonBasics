print("-------------------------------------")
inpValue = (input("Enter a Number or Word :"))
print("-------------------------------------")
print(inpValue)
print("reverse : ", inpValue[::-1])
# revese string
revValue = inpValue[::-1]
if inpValue == revValue :
  print(" It is a palindrome ")
else :
  print("It is not a palindrome  ")