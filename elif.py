# This is how you can use elif in Python.

a = int(input("Enter your age."))
if a > 18:
    print("You are eligible for voting.")
elif a == 18:
    print("You are eligible for voting")
else:
    print("You are not eligible for voting.")
