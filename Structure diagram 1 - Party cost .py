Child_buffet=2
cake=input("Do you need cake?y/n ")
if (cake=="y"):
    cake=15
else:
    cake=0
No_adults=int(input("How many adults will there be? "))
No_children=int(input("How many children will there be? "))
dietrequirements=[]
for index in range(No_children):
    requirements=input("Are there any dietary requirements for child ",index)
    dietrequirements.append(requirements)
if ((No_adults+No_children)>20):
    venue=50
else:
    venue=0
cost=(Child_buffet*No_children)+cake+venue
print(cost)