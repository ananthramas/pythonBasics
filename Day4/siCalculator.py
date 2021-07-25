principle = float(input("Enter the starting cost principle: "))

rate = float(input("Enter the interest rate (Decimal): "))

time = float(input("For how many years do you want to calculate the interest for: "))
oftentime = float(input("How often, in years, will you charge/be charged interest (Decimal): "))

endCostSimple = (principle * (time/oftentime) * rate) + principle
print("The end cost will be " + str(endCostSimple))

