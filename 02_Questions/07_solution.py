size=input("Enter Size(Small/Medium/Large)")
shot=input("Extra Shot Needed(Y/N):")

if shot=='Y':
    print("The Coffee with extra shot in",size,"ready")
elif shot=='N':
    print("The Coffee in",size,"ready")
else:
    print("Enter Y or N")
