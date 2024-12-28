numbers=int(input("Input your number:"))
digits=len(str(numbers))
resultnumber=0
temp=numbers
while temp>0:
    digit=temp%10
    resultnumber+=digit**digits
    temp=temp//10
if numbers==resultnumber:
    print("This number is an armstrong number")
else:
    print("This number is not an armstrong number")