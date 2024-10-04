total = 0

for index in range(12):
    thismonthsavings = float(input("Enter this months savings: "))
    total += thismonthsavings
    print ("Your overall savings so far is ", round(total,2))