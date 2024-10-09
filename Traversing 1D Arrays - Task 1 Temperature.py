temperature = [12, 11, 15, 10, 11, 12, 13]
total = 0

for index in range(7):
    total = total + temperature[index]

print("The average temperature of the week is", total/7)