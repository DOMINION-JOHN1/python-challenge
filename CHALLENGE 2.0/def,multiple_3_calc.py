def mul_calc(num):
    num=float(input("enter value here; "))
    arrayA=range(3,100,5)
    for i in arrayA:
        print(i%num==0)


mul_calc('num')