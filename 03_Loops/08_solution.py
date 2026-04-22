num=int(input("Enter Number To Check If Prime or Not: "))
for i in range(2,int(num**0.5)+1):
    if num%i==0:
        print("Not Prime")
        break
else:
    print("Prime")