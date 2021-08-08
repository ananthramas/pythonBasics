# Arrays
studentNames = ["Advika","Akshaya","Adrin Joseph","Roshini","Sahith"]

longestName ="" 

#for loop .. looping over each element
for studentName in studentNames :
  if len(studentName) > len(longestName) :
    longestName = studentName
 
print("Longest namne : ",longestName)
