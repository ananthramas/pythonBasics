inputText = input("Enter a word : ")

#vaiable to hold vowel counter
# initialized to zero
aVowelCounter = 0
eVowelCounter = 0
iVowelCounter = 0
oVowelCounter = 0
uVowelCounter = 0

for singleChar in inputText :
  if singleChar == "a" :
     aVowelCounter += 1
  elif singleChar == "e" :
     eVowelCounter += 1
  elif singleChar == "i" :
     iVowelCounter += 1
  elif singleChar == "o" :
     oVowelCounter += 1
  elif singleChar == "u" :
     uVowelCounter += 1

print("Number of a's : ", aVowelCounter)
print("Number of e's : ", eVowelCounter)
print("Number of i's : ", iVowelCounter)
print("Number of o's : ", oVowelCounter)
print("Number of u's : ", uVowelCounter)
