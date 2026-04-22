age=int(input("Enter Your Age:"))
day=input("Enter Day(Monday/Tuesday/Wednesday/Thursday/Friday/Saturday/Sunday):")

price=12 if age>=18 else 8

if day=="Wednesday":
    price=price-2

print("Ticket Price for you is $",price)
