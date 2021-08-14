print("******************************")
print("Convert Number to Text Example")
print("******************************")

def convertNumtoText(inpText):
  resultOutput = ""
  if inpText == "1" :
    resultOutput = " One "
  elif inpText == "2" :
      resultOutput = " Two "
  elif inpText == "3" :
      resultOutput = " Three "
  elif inpText == "4" :
      resultOutput = " Four "
  elif inpText == "5" :
      resultOutput = " Five "
  elif inpText == "6" :
      resultOutput = " Six "
  elif inpText == "7" :
      resultOutput = " Seven "
  elif inpText == "8" :
      resultOutput = " Eight "
  elif inpText == "9" :
      resultOutput = " Nine "
  elif inpText == "0" :
      resultOutput = " Zero "
  return resultOutput

inpNumput =  input("Enter a Number you want to convert : ")
finalOutput = ""
textResult = ""
for numTemp in inpNumput : 
 finalOutput = convertNumtoText(str(numTemp))
 textResult = textResult + finalOutput
print(textResult)