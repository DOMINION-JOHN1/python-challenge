def trian_calc (A,B,C):
    A=float(input("insert a number here; "))
    B=float(input("insert a number here; "))
    C=float(input("insert a number here; "))
    if  A+B > C and  A+C > B and B+C > A:
        print(True)
    else:
        print(False)

trian_calc("A","B","C")




