def sss(num1,num2):
    if num1>5:
        return 1
    else:
        num1 += 1
        num2 += 1
        result=num1+num2
        print(result)
        return sss(num1,num2)
a=sss(5,2)
print(a)

