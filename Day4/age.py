# Logic : based on age decide Child >0 <16, Adult >16  <60, Senior >60

age = int(input("Enter your age :"))


if age > 0  and age < 16 : 
 print(" You are an CHILD")
elif age >= 16  and age < 60 :
 print(" You are not ADULT")
else :
  print(" You are not Senior citizen")

