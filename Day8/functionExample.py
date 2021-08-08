# function has identity , 
#    input and output  are optional

def compareNumbers(n1, n2):

  result = ""
  if n1 > n2 :
    result = " is greater than "
  elif n1 < n2 :
    result = " is lesser than "
  else :
    result = " is equal to "

  return str(n1)+result+str(n2)


print(compareNumbers(10,30))
print(compareNumbers(34,55))
print(compareNumbers(30,30))
print(compareNumbers(22,33))

