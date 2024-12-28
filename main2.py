def primefactors(number):
    print("The prime factors of the number are given below:")
    for i in range(1,number+1):
        if number%i==0:
            print(i)
number=int(input("Enter a number"))
primefactors(number)