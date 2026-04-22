password=input("Enter password")
if len(password)>10:
    print("Strong")
elif len(password)>6:
    print("Medium")
else:
    print("Weak")