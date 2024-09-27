print("Choose one of the following options")
print("    1. View chores")
print("    2. Marck chore as completed")
print("    3. View completed chores")
print("    4. Exit")

choice=int(input())
while (choice>4):
    print("**Error, invalid input**")
    choice=int(input())