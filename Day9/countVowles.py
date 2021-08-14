# For examples
#for examples 

inputText = input("Enter a word : ")

vowelCounter = 0
for singleChar in inputText :
  if singleChar in "aeiou":
    vowelCounter +=  1
    

print("Number of vowels : ",vowelCounter )