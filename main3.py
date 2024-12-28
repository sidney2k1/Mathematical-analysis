def romantoint(number):
    resultnumber=0
    roman={"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
    for i in range(0,len(number)-1):
        if roman[number[i]]<roman[number[i+1]]:
            resultnumber-=roman[number[i]]
        else:
            resultnumber+=roman[number[i]]
        return resultnumber+roman[number[-1]]
roman=input("Input roman numeral:")
print("Integer equivalent is:",romantoint(roman))
