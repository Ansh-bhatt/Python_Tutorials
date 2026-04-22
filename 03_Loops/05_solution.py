input_str=input("Enter The String To Check: ")


for char in input_str:
    if input_str.count(char)==1:
        print(char ,"is Not Repatable")
        break
