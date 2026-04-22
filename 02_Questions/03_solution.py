marks=int(input("Enter Your Marks:"))

if marks>100:
    print("Please verify your grade again")
    exit()

if marks>=90:
    print("A")
elif marks>=80:
    print("B")
elif marks>=70:
    print("C")
elif marks>=60:
    print("D")
else:
    print("F")