num=int(input("Enter the number factorial you need:"))
fact=1
while(num>1):
    fact*=num
    num-=1
print("The facorial is",fact)